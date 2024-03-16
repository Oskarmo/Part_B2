class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit



# TODO: Add your own classes here!
import uuid
from datetime import datetime
import random
class Actuator:
    def __init__(self, device_id, serial_number, device_type, supplier, model_name):
        self.device_id = device_id
        self.serial_number = serial_number
        self.device_type = device_type
        self.supplier = supplier
        self.model_name = model_name
        self.status = False
        self.target_value = None

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def is_active(self):
        return self.status

    def set_target_value(self, value):
        self.target_value = value

    def get_device_type(self):
        return self.device_type

    def is_actuator(self):
        return True

    def is_sensor(self):
        return False


class Sensor:
    def __init__(self, device_id, serial_number, device_type, supplier, model_name):
        self.device_id = device_id
        self.serial_number = serial_number
        self.device_type = device_type
        self.supplier = supplier
        self.model_name = model_name
        self.measurements = []

    def last_measurement(self):
        if self.measurements:
            return self.measurements[-1]
        else:
            return None

    def measure(self):
        timestamp = datetime.now().isoformat()  # tid og dato i iso format
        value = random.uniform(0, 100)  # tilfeldig verdi mellom 0 og 100
        measurement = Measurement(timestamp, value, unit="")
        self.measurements.append(measurement)
        return measurement

    def get_device_type(self):
        return self.device_type

    def is_actuator(self):
        return False

    def is_sensor(self):
        return True


class Floor:
    def __init__(self, level):
        self.level = level
        self.rooms = []

    def register_room(self, room):
        self.rooms.append(room)

    def get_rooms(self):
        return self.rooms


class Room:
    def __init__(self, room_size, room_name=None):
        self.room_size = room_size
        self.room_name = room_name
        self.devices = []

    def get_area(self):
        return self.room_size

    def register_device(self, device):
        self.devices.append(device)

    def measure_device(self, device_id, timestamp, value, unit):
        device = self.get_device_by_id(device_id)
        if device and device.is_sensor:
            measurement = device.measure(unit)
            return measurement
        return None

    def get_devices(self):
        return self.devices.copy()

    def get_device_by_id(self, device_id):  # Henter enhet etter serienummer
        for device in self.devices:
            if device.device_id == device_id:
                return device

class SmartDevice:
    def __init__(self, device_type, supplier=None, model_name=None, unit = None , device_id = None):
        self.device_type = device_type
        self.supplier = supplier
        self.model_name = model_name
        self.device_id = device_id
        self.room = None
        self.measurements = []
        self.unit = unit
        self._is_actuator = False
        self._is_sensor = False
        self._is_active =  False
        self.extra_information = None


    def set_device_class(self, device_class):
        self.device_class = device_class

    def get_device_type(self):
        return self.device_type

    @property
    def is_actuator(self):
        return self._is_actuator
    @is_actuator.setter
    def is_actuator(self, value):
        self._is_actuator = value

    @property
    def is_sensor(self):
        return self._is_sensor
    @is_sensor.setter
    def is_sensor(self, value):
        self._is_sensor = value

    def measure(self, unit = None):
        if self.is_sensor:
            timestamp = datetime.now().isoformat() #Dagens dato/tid i iso format
            value = random.uniform (0,100) #tilfeldig verdi for sensor fra 0-100
            if unit is not None:
                unit = str(unit)
            measurement = Measurement(timestamp, value, unit=unit)
            self.measurements.append(measurement)
            return measurement
        else:
            raise ValueError("device is not a sensor")

    def last_measurement(self):
        if self.is_sensor and self.measurements:
            latest_measurement = self.measurements[-1]
            return latest_measurement
        else:
            return None

    def turn_on(self, *args):
        if self.is_actuator:
            self._is_active = True

            if args:
                self.extra_information = args[0]
        else:
            raise ValueError("Device is not Actuator")

    def turn_off(self):
        if self.is_actuator:
            self._is_active = False
            self.extra_information = None
        else:
            raise ValueError("Device is not Actuator")

    def is_active(self):
        return self._is_active
class SmartHouse:
    def __init__(self, name):
        self.name = name
        self.floors = []
        self.devices = []

    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def register_floor(self, level):  # Registrerer ny etasje etter gitt etasje nummer
        new_floor = Floor(level)
        self.floors.append(new_floor)
        return new_floor
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """

    def register_room(self, floor, room_size, room_name=None):
        room = Room(room_size, room_name)
        floor.register_room(room)
        return room
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """

    def get_floors(self):
        return sorted(self.floors, key=lambda x: x.level)
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """

    def get_rooms(self):
        return [room for floor in self.floors for room in floor.get_rooms()]
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """

    def get_area(self):
        return sum(room.get_area() for room in self.get_rooms())
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """


    def register_device(self, room, device_type, device_id=None, supplier=None, model_name=None, is_actuator=False,
                        is_sensor=False, unit=None):
        existing_device = next((device for device in self.devices if device.device_id == device_id), None)

        if existing_device:  # Oppdaterer rommet om device allerede er registrert
            if existing_device.room != room:
                existing_device.room.devices.remove(existing_device)
                existing_device.room = room
                room.devices.append(existing_device)

                source_room = next((r for r in self.get_rooms() if existing_device in r.devices), None)
                if source_room:
                    source_room.devices.remove(existing_device)

            existing_device.unit = unit
            return existing_device

        else:  # Device er ikke registrert, oppretter ny
            if isinstance(device_type, SmartDevice):
                device = device_type
            else:
                device = SmartDevice(device_type, supplier, model_name, unit)

            device.device_id = device_id
            device.is_actuator = is_actuator
            device.is_sensor = is_sensor
            device.unit = unit

            if device.room is not None and device in device.room.devices:
                device.room.devices.remove(device)
            device.room = room
            room.devices.append(device)

            self.devices.append(device)
            return device

    def get_devices(self):
        return self.devices

    def get_device_by_id(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                return device
        return None









