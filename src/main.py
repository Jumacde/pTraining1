class Member:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        # initialize the function to use the results of them to other functions 
        self.setPronomen() 

    # function: check Sex and show it.
    def checkSex(self):
        if self.sex == "male":
            return"man"
        elif self.sex == "female":
            return "woman"
        else:
            return "unknown"
        
    # function: set the personal pronomen via the function checkSex()
    def setPronomen(self):
        if self.checkSex() == "man":
            self.pronomen = "he"
        elif self.checkSex() == "woman":
            self.pronomen = "she"
        else:
            self.pronomen = "they"

    # function: show pfofile of 3 persons(name, age and sex).
    def prof(self):
        print(f"{self.name} is {self.age} years old and a {self.checkSex():}")
    
    # function: check age and show whether the parson can drink alcohole or not.
    def drinkAge(self):
        if self.age >= 20:
            print(f"{self.pronomen} can drink alcohole")
        else:
            print(f"{self.pronomen} cannot drink alcohole")

# set the profile-date of 3 persoons.
def main():
    p1 = Member("Alice", 17, "female")
    p1.setPronomen()
    p2 = Member("Bob", 45, "male")
    p2.setPronomen()
    p3 = Member("Num1", 33, "none")
    p3.setPronomen()
    
    # to execute all functions for 3 persons.
    for p in [p1, p2, p3]:
        p.setPronomen()
        p.prof()
        p.drinkAge()

if __name__ == "__main__":
    main()