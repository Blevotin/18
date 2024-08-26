class house():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number = number_of_floors
    def go_to(self, new_floor):
        if new_floor <= self.number:
            for i in range(new_floor):
                if i < self.number:
                    print(i+1)
        else:
            print("Такого этажа не существует")

a = house("Жк", 23)
a.go_to(23)
