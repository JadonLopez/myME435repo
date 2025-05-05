from motor import OrdinaryCar
import time

class DriveSystem:

    def __init__(self):
        self.car = OrdinaryCar()

    def scale_speed(self, speed):
        return int(speed / 100 * 4095)
    
    def set_speeds(self, lf, lr, rf, rr):
        self.car.set_motor_model(self.scale_speed(lf), self.scale_speed(lr), self.scale_speed(rf), self.scale_speed(rr))

    def go(self, left_speed, right_speed):
        self.set_speeds(left_speed, left_speed, right_speed, right_speed)

    def stop(self):
        self.set_speeds(0, 0, 0, 0)

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