import shelve
import exeptions as ex
# import json

class DictDrink:

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
class Adder(DictDrink):
    def __init__(self,name,amount):
        super().__init__(name,amount)
    def add(self,name):
        db = shelve.open("db","c")
        db[name] = DictDrink.to_dict(self)
        if self.name in db:
            raise ex.DrinkAlreadyExists("")
        elif self.amount <= 0 or self.amount > 10:
            raise ex.InvalidVol("")
        elif self.name.isdigit() and self.amount.isalpha():
            raise ex.PassArgs("")
        elif self.name is "":
            raise ex.PassArgs("")
        else:
            print("Drink successfully added!!!\n name = {} litres = {}".
            format(self.name,self.amount))
        return db[name]
    def display(self,name):
        """ вывод на экран обьектов заданного типа"""
        db = shelve.open("db")
        if self.name not in db:
            """ если напитка нет в БД"""
            raise ex.NotFound("")
        else:
            db = db.get(name,"Undefined")

            #print(db) # print as dict
            print((";\n".join("%s=>%s" % i for i in db.items())))



###############################################################################
def main():
    print("What do you want to do ?-> ")
    print("Add the drinks - 1\n List of drinks - 2")
    choice = input()

    if choice == "1":
        name = input("Enter kind of drink->")
        brand = input("Enter mark of drink-> ")
        lts = float(input("Enter litres-> "))
        b = DictDrink(brand,lts)
        c = Adder.add(b,name)
    elif choice == "2":
        brand = input("Enter mark of drink->") # for example Beer
        b = DictDrink(brand)
        c = Adder.display(b,brand)


###############################################################################
if __name__ == "__main__":

    main()
