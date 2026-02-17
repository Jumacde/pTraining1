class Member:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.setPronomen()

    def checkSex(self):
        if self.sex == "male":
            return"man"
        elif self.sex == "female":
            return "woman"
        else:
            return "unknown"
        
    def setPronomen(self):
        if self.checkSex() == "man":
            self.pronomen = "he"
        elif self.checkSex() == "woman":
            self.pronomen = "she"
        else:
            self.pronomen = "they"

    def prof(self):
        print(f"{self.name} is {self.age} years old and a {self.checkSex():}")
    
    def drinkAge(self):
        if self.age >= 20:
            print(f"{self.pronomen} can drink alcohole")
        else:
            print(f"{self.pronomen} cannot drink alcohole")

def main():
    p1 = Member("Alice", 17, "female")
    p1.setPronomen()
    p2 = Member("Bob", 45, "male")
    p2.setPronomen()
    p3 = Member("Num1", 33, "none")
    p3.setPronomen()
    
    for p in [p1, p2, p3]:
        p.setPronomen()
        p.prof()
        p.drinkAge()

if __name__ == "__main__":
    main()