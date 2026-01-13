from user import User #читается: из файла user импортируй сущность User
from card import Card #читается: из файла card импортируй сущность Card

alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()


card = Card("4353 1234 5678 8765", "11/28", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)

