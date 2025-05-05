from spi_ledpixel import Freenove_SPI_LedPixel
import time

class CarLeds:

    def __init__(self):
        self.neopixel_strip = Freenove_SPI_LedPixel(count=8, bright=128)

    def set_all_leds(self, red, green, blue):
        self.neopixel_strip.set_all_led_color_data(red, green, blue)
        self.neopixel_strip.show()

    def set_led(self, led_index, red, green, blue):
        self.neopixel_strip.set_led_color_data(led_index, red, green, blue)
        self.neopixel_strip.show()

if __name__ == "__main__":
    car_leds = CarLeds()
    car_leds.set_all_leds(255,0,0)
    time.sleep(1)
    car_leds.set_led(1, 0, 255, 0)
    time.sleep(1)
    car_leds.set_led(2, 0, 0, 255)
    time.sleep(1)
    print("Done")