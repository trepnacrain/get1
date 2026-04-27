import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    
    def set_number(self, number):
        v = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, v)
        return v
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f'Напряжение выходит за динамический диапазон ЦАП (0.0 - {self.dynamic_range:.2f} В)')
            print('устанавливаем 0.0 В')
            GPIO.output(self.gpio_bits, 0)
            return 0

        else:
            n = int(voltage / self.dynamic_range* 255)
            self.set_number(n)
        return n
    

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()


if __name__ == '__main__':
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = int(input('Введите напряжение в Вольтах:'))
                dac.set_voltage(voltage)

            except ValueError:
                print('Вы ввели не число. Попробуйте еще раз\n')

    finally:
        dac.deinit()



