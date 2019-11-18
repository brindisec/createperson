#ChaseBrindise

class Person():
    def __init__(self, age, name, height, occupation):
        self.name = name
        self.age = age
        self.height = height
        self.occupation = occupation

    def description(self):
        print(f"I am {self.name}. "
              f"I am a {self.occupation} who is {self.height}"
              f" and I am {self.age}")
