from machine import Pin, PWM, UART

print()
print("Hello this is v0.7.1a")
print()

led_pwm = PWM(Pin(2))
led_pwm.freq(5)
led_pwm.duty_u16(32758)

print()
print("Is it flashing yet?")
print()

gps = UART(2, baudrate=115200)
print(gps.read(72))
print(gps.read(72))
print(gps.read(72))
print(gps.read(72))
print(gps.read(72))
