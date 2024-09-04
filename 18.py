class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor <= 0:
            return print("Такого этажа нет")
        if new_floor <= self.number_of_floors:
            for i in range(new_floor):
                if i < self.number_of_floors:
                    print(i+1)
        else:
            print("Такого этажа не существует")

a = House("Жк", 23)
a.go_to(23)
