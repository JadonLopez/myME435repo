from rosebot_drive_system import DriveSystem
from sensors import UltraSonic, LineSensors
from rosebot_servo_head import ServoHead

class RoseBot:

    def __init__(self):
        self.drive_system = DriveSystem()
        self.ultrasonic = UltraSonic()
        self.line_sensors = LineSensors()
        self.servo_head = ServoHead()