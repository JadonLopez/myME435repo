import gpiozero as gz
import time, signal

def helper_function(leds,state):
    if state == "on":
        leds.on()
        time.sleep(1)
        leds.off()
    elif state == "off":
        leds.off()

def passing_stuff_to_lambda():
    print("Passing stuff to lambda")
    button = gz.Button(25)
    leds = gz.LEDBoard(14,15,18)
    button.when_pressed = lambda: helper_function(leds,"on")
    button.when_released = lambda: helper_function(leds,"off")
    signal.pause()

def function_using_def():
    print("def makes a function")
    print("def can have many lines of code")

functoin_using_lambda = lambda: print("lambda makes a function too, but 1 line only")

def buttons_with_events():
    print("Using callback function")
    button = gz.Button(25)
    button.when_pressed = lambda: print("Button pressed")
    button.when_released = lambda: print("Button released")
    button.when_held = lambda: print("Button held")
    signal.pause()

def read_button_state():
    button = gz.Button(25)
    while True:
        if button.is_pressed:
            print("Button is pressed")
        else:
            print("Button is not pressed")
        time.sleep(0.5)

def main():
    print("Pushbuttons")
    read_button_state()

main()