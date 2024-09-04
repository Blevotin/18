class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor <= 0 or new_floor > self.number_of_floors:
            return print("Такого этажа нет")
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                    print(i)
        else:
            print("Такого этажа не существует")

a = House("Жк", 23)
a.go_to(23)
