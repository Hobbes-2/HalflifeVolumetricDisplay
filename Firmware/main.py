from machine import Pin
import neopixel
import time

LED_COUNT = 64
DATA_PIN = 0       # Pico GP0; change to your actual data GPIO - 0 in this case
FRAME_TIME = 0.1   # seconds per frame

pixels = neopixel.NeoPixel(Pin(DATA_PIN), LED_COUNT)

def light_half(first_row, last_row):
    pixels.fill(0, 0, 0)

    # Assumes row-major order: index = row * 8 + column
    for row in range(first_row, last_row):
        for col in range(8):
            pixels[row * 8 + col] = (20, 20, 20)  # dim light

    pixels.write()

while True:
    for _ in range(5):
        light_half(0, 4)
        time.sleep(FRAME_TIME)

    for _ in range(5):
        light_half(4, 8)
        time.sleep(FRAME_TIME)
