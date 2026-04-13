import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_number(self, number):
        v = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.PWM(self.gpio_pin, v)

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f'Напряжение выходит за динамический диапазон ЦАП (0.0 - {self.dynamic_range:.2f} В)')
            print('устанавливаем 0.0 В')
            return 0

        vo = int(voltage / self.dynamic_range * 255)
        GPIO.PWM(self.gpio_pin, vo)


if __name__ == '__main__':
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input('Введите напряжение в Вольтах:'))
                dac.set_voltage(voltage)

            except ValueError:
                print('Вы ввели не число. Попробуйте еще раз\n')

    finally:
        dac.deinit()

    


