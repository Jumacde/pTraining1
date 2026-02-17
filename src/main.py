class Member:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def prof(self):
        print(f"{self.name} is {self.age} years old")
    
    def drinkAge(self):
        adult = Member(self.name, self.age, self.sex)

        if adult.age >= 20:
            print(f"{self.name} can drink alcohole")
        else:
            print(f"{self.name} cannot drink alcohole")

def main():
    p1 = Member("Alice", 17, "female")
    p2 = Member("Bob", 45, "male")
    
    p1.prof()
    p1.drinkAge()
    p2.prof()
    p2.drinkAge()

if __name__ == "__main__":
    main()