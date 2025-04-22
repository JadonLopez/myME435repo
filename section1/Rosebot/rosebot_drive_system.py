from motor import OrdinaryCar
import time

class DriveSystem:

    def __init__(self):
        self.car = OrdinaryCar()

    def scale_speed(self, speed):
        return int(speed / 100 * 4095)

    def go(self, left_speed, right_speed):
        left_duty = self.scale_speed(left_speed)
        right_duty = self.scale_speed(right_speed)
        self.car.set_motor_model(left_duty, left_duty, right_duty, right_duty)

    def strafe_left(self, speed):
        duty = self.scale_speed(speed)
        self.car.set_motor_model(-duty, duty, duty, -duty)

    def go_straight_for_seconds(self, seconds, speed):
        self.go(speed,speed)
        time.sleep(seconds)
        self.stop()
    
    def go_straight_for_inches(self, inches, speed):
        m = 1 # TODO change value
        b = 0 # TODO change value
        in_per_sec = m * speed + b
        seconds = inches/in_per_sec
        self.go_straight_for_seconds(seconds,speed)

    def spin_in_place_for_seconds(self, seconds, speed, isLeftSpin=True):
        duty = self.scale_speed(speed)
        if isLeftSpin:
            self.car.set_motor_model(-duty, -duty, duty, duty)
        else:
            self.car.set_motor_model(duty, duty, -duty, -duty)
        time.sleep(seconds)
        self.stop()

    def stop(self):
        self.car.set_motor_model(0, 0, 0, 0)

    def close(self):
        self.car.close()