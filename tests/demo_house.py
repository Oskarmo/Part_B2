import uuid

from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse("OskarSmartHus")

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
# TODO: continue registering the remaining floor, rooms and devices
upper_floor = DEMO_HOUSE.register_floor(2)
#Etasje 1
bathroom1 = DEMO_HOUSE.register_room(ground_floor, 6.3, "Bathroom 1")
guest_room1 = DEMO_HOUSE.register_room(ground_floor, 8, "Guest Room 1" )
living_room_kitchen = DEMO_HOUSE.register_room(ground_floor, 39.75, "Living Room/Kitchen")
Garage = DEMO_HOUSE.register_room(ground_floor, 19, "Garage")

#Device in garage
Automatic_garage_door = DEMO_HOUSE.register_device(Garage, "Automatic Garage Door","9a54c1ec-0cb5-45a7-b20d-2a7349f1b132", "MythicalTech", "Guardian Lock 9000" , is_actuator=True)

#Devices Bathroom 1

humidity_sensor = DEMO_HOUSE.register_device(bathroom1, "Humidity Sensor", "3d87e5c0-8716-4b0b-9c67-087eaaed7b45", "AetherCorp", "Aqua Alert 800", is_sensor=True, unit = '%')
#Måling fra humidity_sensor
measurement = humidity_sensor.measure(unit = '%')
last_measurement = humidity_sensor.last_measurement()

#Devices guest room 1

smart_oven_guest1 = DEMO_HOUSE.register_device(guest_room1, "Smart Oven", "8d4e4c98-21a9-4d1e-bf18-523285ad90f6","AetherCorp", "Pheonix HEAT 333", is_actuator= True)

#Devices in Entrance

smart_lock_entrance = DEMO_HOUSE.register_device(entrance, "Smart Lock", "4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1" ,"MythicalTech", "Guardian Lock 7000", is_actuator=True)
electricity_meter = DEMO_HOUSE.register_device(entrance, "Electricity Meter", "a2f8690f-2b3a-43cd-90b8-9deea98b42a7", "MysticEnergy Innovations", "Volt Watch Elite", is_sensor=True, unit = 'Kwh')
#Måling fra electricity_meter
measurement = electricity_meter.measure(unit = 'Kwh')
last_measurement = electricity_meter.last_measurement()

#devices in LivingRoom/kitchen

Motion_sensor = DEMO_HOUSE.register_device(living_room_kitchen, "Motion Sensor", "cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5", "NebulaGuard Innovations", "MoveZ Detect 69", is_sensor=True, unit = 'BIP')
#Måling fra Moion_sensor
measurement = Motion_sensor.measure(unit = 'BIP')
last_measurement = Motion_sensor.last_measurement()

Co2_sensor = DEMO_HOUSE.register_device(living_room_kitchen, "CO2 sensor" ,"8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e", "ElysianTech", "Smoke Warden 1000", is_sensor=True, unit = 'ppm')
#Måling fra Co2_sensor
measurement = Co2_sensor.measure(unit = 'ppm')
last_measurement = Co2_sensor.last_measurement()

heat_pump = DEMO_HOUSE.register_device(living_room_kitchen, "Heat Pump", "5e13cabc-5c58-4bb3-82a2-3039e4480a6d", "ElysianTech", "Thermo Smart 6000", is_actuator=True)

#Etasje 2

office = DEMO_HOUSE.register_room(upper_floor,11.75, "Office")
Hallway = DEMO_HOUSE.register_room(upper_floor, 10, "Hallway")
Bathroom2 = DEMO_HOUSE.register_room(upper_floor, 9.25, "Bathroom 2")
Guest_room2 = DEMO_HOUSE.register_room(upper_floor, 8, "Guest room 2")
Guest_room3 = DEMO_HOUSE.register_room(upper_floor, 10, "Guest room 3")
Dressing_room = DEMO_HOUSE.register_room(upper_floor, 4, "Dressing room")
Master_bedroom = DEMO_HOUSE.register_room(upper_floor, 17, "Master bedroom")

#Device in office
smart_plug = DEMO_HOUSE.register_device(office, "Smart Plug" , "1a66c3d6-22b2-446e-bf5c-eb5b9d1a8c79" ,"MysticEnergy Innovations", "FlowState X", is_actuator=True)

#Device in Bathroom 2
dehumidifier = DEMO_HOUSE.register_device(Bathroom2, "Dehumidifier", "9e5b8274-4e77-4e4e-80d2-b40d648ea02a" ,"ArcaneTech Solutions" , "Hydra Dry 8000", is_actuator=True)

#Device in Guest room 2
light_bulp = DEMO_HOUSE.register_device(Guest_room2, "Light Bulp", "6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28", "Elysian Tech", "Lumina Glow 4000", is_actuator=True,)

#Device in Guest room 3
air_quality_sensor = DEMO_HOUSE.register_device(Guest_room3, "Air Quality Sensor", "7c6e35e1-2d8b-4d81-a586-5d01a03bb02c", "CelestialSense Technologies", "AeroGuard Pro", is_sensor=True, unit = '%')
#Måling fra sensor
measurement = air_quality_sensor.measure(unit = '%')
last_measurement = air_quality_sensor.last_measurement()

#Devices in Master bedroom
temperature_sensor = DEMO_HOUSE.register_device(Master_bedroom, "Temperature Sensor", "4d8b1d62-7921-4917-9b70-bbd31f6e2e8e" ,"AetherCorp", "SmartTemp 42", is_sensor=True,unit = '°C')
#Måling fra sensor
measurement = temperature_sensor.measure(unit = '°C')
last_measurement = temperature_sensor.last_measurement()

smart_oven = DEMO_HOUSE.register_device(Master_bedroom, "Smart Oven", "c1e8fa9c-4b8d-487a-a1a5-2b148ee9d2d1" ,"IgnisTech Solutions", "Ember Heat 3000", is_actuator=True)
#Device in dressing room
