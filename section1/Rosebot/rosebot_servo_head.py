from servo import Servo
import time

class ServoHead:

    def __init__(self):
        self.servos = Servo()

    def set_pan_position(self, degrees):
        self.servos.set_servo_pwm('0',degrees)

    def set_tilt_position(self, degrees):
        self.servos.set_servo_pwm('1', degrees)

    def reset(self):
        self.set_pan_position(90)
        self.set_tilt_position(90)

if __name__ == '__main__':
    servo_head = ServoHead()
    try:
        while True:
            servo_head.set_pan_position(90)
            servo_head.set_tilt_position(90)
            time.sleep(1)

            servo_head.set_pan_position(40)
            time.sleep(1)
            servo_head.set_pan_position(140)
            time.sleep(1)

            servo_head.set_tilt_position(90)
            time.sleep(1)
            servo_head.set_tilt_position(160)
            time.sleep(1)

            servo_head.reset()
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nEnd of program")