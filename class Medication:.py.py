class Medication:
    def __init__(self, name, dosage):
        self.name = name
        self.dosage = dosage

    def consume(self):
        print(f"Принято лекарство - {self.name}. Доза - {self.dosage}")


class Tablet(Medication):
    def __init__(self, name, dosage, colour):
        Medication.__init__(self, name, dosage)# напиши конструктор, вызови в нём конструктор суперкласса и добавь новый атрибут colour
        self.colour = colour

    def print_colour(self):
        print(f"Цвет таблетки - {self.colour}")


tablet = Tablet("Наследин", "2", "Белый")
tablet.consume()       # Принято лекарство - Наследин. Доза - 2
tablet.print_colour()  # Цвет таблетки - Белый