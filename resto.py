
import shelve
import exeptions as ex
# import json

class Drink:

    def __init__(self, name, amount = 0):
        self.name,self.amount = name, amount

    def to_dict(self)-> dict:
         return {"name":self.name,
                "amount":self.amount}
    @classmethod
    def from_dict(cls, value: dict):
        return cls(**value)

    def __str__(self)->str:
        return "Drink {} ({} litres)".format(self.name,self.amount)

def addDrink(drink:Drink):
    """Adds drink to the db"""
    db = shelve.open("db_file1","c") # открываем файл
    name = input("Enter name of dataDase->")
    db[name] = drink.to_dict()
    db[name].update({"name":drink.name,"amount":drink.amount}) # добавляет номенкл позиции в базу данных


    if drink.name in db:
        raise ex.DrinkAlreadyExists("")
    elif drink.amount <= 0 or drink.amount > 10:
        raise ex.InvalidVol("")
    elif drink.name.isdigit() and drink.amount.isalpha():
        raise ex.PassArgs("")
    elif drink.name is "":
        raise ex.PassArgs("")
    else:
        print("Drink successfully added!!!\n name = {} litres = {}".
        format(drink.name,drink.amount))

def display():
    db = shelve.open("db_file1")
    print (":\n".join("%s=%s" % i for i in db.items()))

###############################################################################
def choice():
    ans = {"1":Drink,"2":display}
    print("What do you want to do ?-> ")
    print("Add the drinks - 1\n List of drinks - 2")
    choice = input()
    #ans[choice]()
    if choice == "1":
        d1 = Drink("Beer light",10)
        d2 = Drink("Martini",8)
        addDrink(d1)
        addDrink(d2)
    elif choice == "2":
        display()
###############################################################################
def main():
    choice()
main()
