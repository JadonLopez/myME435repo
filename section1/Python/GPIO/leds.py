import gpiozero as gz
from gpiozero import LEDBoard
import time
import signal

def led_board():
    print("LED Board")
    leds = LEDBoard(14,15,18,PWM=True)
    leds.on()
    time.sleep(1)
    
    leds.off()
    time.sleep(1)
    
    leds.value = (1, 0, 1)
    time.sleep(1)
    
    leds.value = (0.2, 0.2, 0.2)
    time.sleep(1)
    
    leds.blink()
    signal.pause()

def led_pwm():
    print("LED PWM")
    red_led = gz.PWMLED(14)
    yellow_led = gz.PWMLED(15)
    green_led = gz.PWMLED(18)

    red_led.value = 0.25
    time.sleep(1)
    red_led.value = 0.5
    time.sleep(1)
    red_led.value = 0.75
    time.sleep(1)
    red_led.value = 1
    time.sleep(1)

    red_led.pulse(fade_in_time=3, fade_out_time=0.5)
    yellow_led.pulse(fade_in_time=3, fade_out_time=0.5)
    green_led.pulse(fade_in_time=3, fade_out_time=0.5)
    signal.pause()

def fancy_blink():
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    red_led.blink(on_time=0.5, off_time=0.5)
    yellow_led.blink(on_time=0.5, off_time=0.5)
    green_led.blink(on_time=0.5, off_time=0.5)
    signal.pause()

def traffic_light():
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    while(1):
        green_led.on()
        time.sleep(4)
        green_led.off()
        yellow_led.on()
        time.sleep(1)
        yellow_led.off()
        red_led.on()
        time.sleep(3)
        red_led.off()

def basic_on_off():
    print("Basic On/Off")
    red_led = gz.DigitalOutputDevice(14)
    yellow_led = gz.DigitalOutputDevice(15)
    green_led = gz.DigitalOutputDevice(18)
    red_led.on()
    yellow_led.on()
    green_led.on()
    
    time.sleep(3)
    red_led.off()
    yellow_led.off()
    green_led.off()

def main():
    print("LEDs")

main()