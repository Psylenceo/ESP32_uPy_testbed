from machine import Pin, PWM, UART
from micropyGPS import MicropyGPS

led_pwm = PWM(Pin(2))
raw_gps = UART(2, baudrate=9600)
gps = MicropyGPS()

print()
print("Hello this is v0.7.2a")
print()

led_pwm.freq(5)
led_pwm.duty_u16(32758)

print()
print("Is it flashing yet?")
print()

for x in raw_gps
    gps.update(x)
