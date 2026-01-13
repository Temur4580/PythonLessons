class User:
    

    def __init__(self, name):
        print("я создался")
        self.username = name
        self.age = 0


    def sayName(self):
        print("меня зовут", self.username)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card
        