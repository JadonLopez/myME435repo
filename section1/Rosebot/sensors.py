import gpiozero as gz
import time, warnings

class UltraSonic:
    
    def __init__(self):
        warnings.filterwarnings("ignore",category=gz.PWMSoftwareFallback) # Ignores PWM software fallback warnings
        self.ultrasonic = gz.DistanceSensor(echo=22, trigger=27)
        
    def get_cm(self):
        return self.ultrasonic.distance * 100

class LineSensors:
    pass

if __name__ == "__main__":
    ultrasonic = UltraSonic()
    try:
        while True:
            distance = ultrasonic.get_cm()
            print(f"Distance: {distance:.2f} cm")
            time.sleep(2)
    except KeyboardInterrupt:
        print("End of test")