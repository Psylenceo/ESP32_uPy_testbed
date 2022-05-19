from machine import Pin, PWM

print("Hello")

led_pwm = PWM(Pin(2))
led_pwm.freq(2)
led_pwm.duty_u16(32768)
