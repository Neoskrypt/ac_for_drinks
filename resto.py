import shelve
import exeptions_new as ex
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
    def add(self):
        db = shelve.open("db","c")
        name = input("Enter name of dataDase->")
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
    def display():
        db = shelve.open("db","w")
        for i in db:
            print(i,db[i])
        db.close()

def main():
    print("What do you want to do ?-> ")
    print("Add the drinks - 1\n List of drinks - 2")
    choice = input()

    if choice == "1":
        b = DictDrink("Beer light",10)
        b1 = DictDrink("Martini",8)
        c = Adder.add(b1)
    elif choice == "2":
        Adder.display()


#######################################################################
if __name__ == "__main__":
    resto.py
    main()
