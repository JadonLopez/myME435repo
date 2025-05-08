from rosebot import RoseBot
from mqtt_helper import MqttClient
import time, threading

distance = 0

class App:
    def __init__(self):
        self.robot = RoseBot()
        
        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/lopezjj/#",
                                 publish_topic_name="me435/lopezjj/to_computer",
                                 mqtt_broker_ip_address="broker.hivemq.com",
                                 use_off_campus_broker=True)

    def mqtt_callback(self, type_name, payload):
        print(f"My Callback: {type_name} - {payload}")

        if type_name == "leftForward":
            self.robot.drive_system.go(payload[2], 0)
            time.sleep(payload[1])
            self.robot.drive_system.stop()

        if type_name == "leftReverse":
            self.robot.drive_system.go(-payload[2], 0)
            time.sleep(payload[1])
            self.robot.drive_system.stop()

        if type_name == "rightForward":
            self.robot.drive_system.go(0, payload[2])
            time.sleep(payload[1])
            self.robot.drive_system.stop()

        if type_name == "rightReverse":
            self.robot.drive_system.go(0, -payload[2])
            time.sleep(payload[1])
            self.robot.drive_system.stop()
            
        if type_name == "bothForward":
            self.robot.drive_system.go(payload[2], payload[3])
            time.sleep(payload[1])
            self.robot.drive_system.stop()

        if type_name == "bothReverse":
            self.robot.drive_system.go(-payload[2], -payload[3])
            time.sleep(payload[1])
            self.robot.drive_system.stop()

def read_ultrasonic(app):
    global distance
    while True:
        distance = app.robot.ultrasonic.get_cm()
        # print(f"Distance: {distance} cm")
        time.sleep(0.1)

def send_distance_loop(client):
    while True:
        client.send_message("ultra", [distance])  # Send latest distance
        print(f"Published distance: {distance} cm")
        time.sleep(2)  # Send every 2 seconds

def main():
    print("Program start...")
    app = App()
    sensor_thread = threading.Thread(target=read_ultrasonic, args=(app,), daemon=True)
    sensor_thread.start()

    send_thread = threading.Thread(target=send_distance_loop, args=(app.mqtt_client,), daemon=True)
    send_thread.start()
   
    try:
        while True:
            time.sleep(0.1)            
            
    except KeyboardInterrupt:
        print("Exiting...")
        app.robot.drive_system.stop()
        app.robot.drive_system.close()
        app.mqtt_client.close()  
          
main()