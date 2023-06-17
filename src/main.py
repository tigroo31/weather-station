from time import sleep

from machine import Pin


def print_hi(name):
    print(f"Plan venguda dins la station meteo {name}")


if __name__ == '__main__':
    print_hi("FabDuLys")

led = Pin(2, Pin.OUT)
while True:
    led.value(not led.value())
    sleep(0.5)
