import sqlite3
from typing import Optional
from smarthouse.domain import SmartHouse
from smarthouse.domain import Device
from smarthouse.domain import Measurement
from smarthouse.domain import Room
from datetime import datetime
from smarthouse.domain import Sensor
from smarthouse.domain import Actuator
import logging


class SmartHouseRepository:
    """
    Provides the functionality to persist and load a _SmartHouse_ object
    in a SQLite database.
    """

    def __init__(self, file: str) -> None:
        self.file = file
        self.conn = sqlite3.connect(file)

    def __del__(self):
        self.conn.close()

    def cursor(self) -> sqlite3.Cursor:
        """
        Provides a _raw_ SQLite cursor to interact with the database.
        When calling this method to obtain a cursors, you have to
        rememeber calling `commit/rollback` and `close` yourself when
        you are done with issuing SQL commands.
        """
        return self.conn.cursor()

    def reconnect(self):
        self.conn.close()
        self.conn = sqlite3.connect(self.file)


    def load_smarthouse_deep(self):
        """
        This method retrives the complete single instance of the _SmartHouse_
        object stored in this database. The retrieval yields a _deep_ copy, i.e.
        all referenced objects within the object structure (e.g. floors, rooms, devices)
        are retrieved as well.
        """
        # TODO: START here! remove the following stub implementation and implement this function
        #       by retrieving the data from the database via SQL `SELECT` statements.
        # Oppretter et tomt smarthus
        smart_house = SmartHouse()

        cursor = self.cursor()

        cursor.execute("SELECT id, name, area, floor FROM rooms")
        rooms_data = cursor.fetchall()

        for room_id, room_name, room_size, floor_id in rooms_data:
            floor = smart_house.register_floor(floor_id)
            room = smart_house.register_room(floor, room_size, room_name)

        cursor.execute("SELECT id, room, kind, category, supplier FROM devices")
        device_data = cursor.fetchall()

        for device_id, room_id, model_name,device_type, supplier in device_data:
            if device_type == "actuator":
                device = Actuator(device_id, model_name, device_type, supplier)
            else:
                device = Device(device_id, model_name, device_type, supplier)
            smart_house.register_device(room, device)

        cursor.close()
        return smart_house

    def get_latest_reading(self, sensor) -> Optional[Measurement]:
        """
        Retrieves the most recent sensor reading for the given sensor if available.
        Returns None if the given object has no sensor readings.
        """
        # TODO: After loading the smarthouse, continue here
        # Kobler til database
        cursor = self.cursor()

        # Henter siste måling
        cursor.execute("SELECT value, unit, ts FROM measurements WHERE device = ? ORDER BY ts DESC LIMIT 1", (sensor.id,))
        latest_reading = cursor.fetchone()

        # Lukker cursor
        cursor.close()

        # finner måling og returnerer målingen
        if latest_reading:
            value, unit, timestamp = latest_reading
            return Measurement(timestamp, float(value), unit)

        return None

    def update_actuator_state(self, actuator):
        """
        Saves the state of the given actuator in the database. 
        """
        # TODO: Implement this method. You will probably need to extend the existing database structure: e.g.
        #       by creating a new table (`CREATE`), adding some data to it (`INSERT`) first, and then issue
        #       and SQL `UPDATE` statement. Remember also that you will have to call `commit()` on the `Connection`
        #       stored in the `self.conn` instance variable.
        if isinstance(actuator, Actuator):
            cursor = self.conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS actuators (
                                                        id TEXT PRIMARY KEY,
                                                        room TEXT,
                                                        kind TEXT,
                                                        category TEXT,
                                                        supplier TEXT,
                                                        state BOOLEAN
                                                    )''')

            # Here we use room.room_name as a unique identifier for the room
            cursor.execute('''INSERT OR REPLACE INTO actuators (id, room, kind, category, supplier, state)
                                                        VALUES (?, ?, ?, ?, ?, ?)''',
                           (actuator.id, actuator.room.room_name, actuator.model_name, actuator.get_device_type(),
                            actuator.supplier,
                            actuator.is_active()))

            # Commit the changes to the database
            self.conn.commit()  # Move commit here to persist changes before reconnecting

            cursor.close()
        else:
            print("Error: The given device is not an actuator.")

    def reconnect(self):
        # Remove the line that closes the connection
        self.conn.close()
        self.conn = sqlite3.connect(self.file)
        # Don't open a new connection here, let the subsequent method calls create new connections

    def calc_avg_temperatures_in_room(self, room, from_date: Optional[str] = None, until_date: Optional[str] = None) -> dict:
        """Calculates the average temperatures in the given room for the given time range by
        fetching all available temperature sensor data (either from a dedicated temperature sensor 
        or from an actuator, which includes a temperature sensor like a heat pump) from the devices 
        located in that room, filtering the measurement by given time range.
        The latter is provided by two strings, each containing a date in the ISO 8601 format.
        If one argument is empty, it means that the upper and/or lower bound of the time range are unbounded.
        The result should be a dictionary where the keys are strings representing dates (iso format) and 
        the values are floating point numbers containing the average temperature that day.
        """
        # TODO: This and the following statistic method are a bit more challenging. Try to design the respective 
        #       SQL statements first in a SQL editor like Dbeaver and then copy it over here.  
        return NotImplemented

    
    def calc_hours_with_humidity_above(self, room, date: str) -> list:
        """
        This function determines during which hours of the given day
        there were more than three measurements in that hour having a humidity measurement that is above
        the average recorded humidity in that room at that particular time.
        The result is a (possibly empty) list of number representing hours [0-23].
        """
        # TODO: implement
        return NotImplemented

