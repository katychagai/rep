class ElectronicDevice:
    def power_on(self):
        print("Устройство включено")
        
    def power_off(self):
        print("Устройство выключено")
        
class Television(ElectronicDevice):
    def change_channel(self):
        print("Канал был изменен")
        
class Computer(ElectronicDevice):
    def open_application(self):
        print("Приложение было открыто")

# создаём объекты классов
electronic_device = ElectronicDevice()
computer = Computer()
tv = Television()

# вызываем методы
electronic_device.power_on()
electronic_device.power_off()

computer.power_on()
computer.power_off()    # Я ем...
computer.open_application()  # Я сплю...

tv.power_on()
tv.power_off()     # Я ем...
tv.change_channel()   # Я сплю...
