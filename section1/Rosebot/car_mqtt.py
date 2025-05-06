from rosebot import RoseBot
from mqtt_helper import MqttClient
import time

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

        if type_name == "set_speeds":
            self.robot.drive_system.set_speeds(payload[0], payload[1], payload[2], payload[3])

        if type_name == "stop":
            self.robot.drive_system.stop()

        if type_name == "pan":
            self.robot.servo_head.set_pan_position(payload)

        if type_name == "tilt":
            self.robot.servo_head.set_tilt_position(payload)

def main():
    print("GPIO MQTT Test")
    app = App()
    
    try:
        while True:
            time.sleep(0.1)
            app.mqtt_client.send_message("pan",90)
            app.mqtt_client.send_message("tilt",90)
            time.sleep(1)
            app.mqtt_client.send_message("pan",20)
            time.sleep(1)
            app.mqtt_client.send_message("tilt",50)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Exiting...")
        app.robot.drive_system.stop()
        app.robot.drive_system.close()
        app.mqtt_client.close()  
          
main()