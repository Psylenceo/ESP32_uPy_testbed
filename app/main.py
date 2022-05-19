from machine import Pin, PWM

print()
print("Hello this is v0.6")
print()

led_pwm = PWM(Pin(2))
led_pwm.freq(10)
led_pwm.duty_u16(32758)
