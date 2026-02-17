class member:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def prof(self):
        print(f"i am {self.name} and {self.age} years old")

def main():
    p1 = member("jene", 17, "female")
    p1.prof()

if __name__ == "__main__":
    main()