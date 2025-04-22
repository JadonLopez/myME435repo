from motor import OrdinaryCar

class DriveSystem:

    def __init__(self):
        self.car = OrdinaryCar()

    def scale_speed(self, speed):
        return int(speed / 100 * 4095)

    def go(self, left_speed, right_speed):
        left_duty = self.scale_speed(left_speed)
        right_duty = self.scale_speed(right_speed)
        self.car.set_motor_model(left_duty, left_duty, right_duty, right_duty)

    def stop(self):
        self.car.set_motor_model(0, 0, 0, 0)

    def close(self):
        self.car.close()