from machine import Pin, PWM

print()
print("Hello this is v0.3")
print()

led_pwm = PWM(Pin(2))
led_pwm.freq(5)
led_pwm.duty_u16(32768)
