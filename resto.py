import shelve
import exeptions as ex
# import json
import sys
from sys import argv

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
        name = "Drink"
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
    @staticmethod
    def _list():
        """print list of drinks"""
        db = shelve.open("db", flag='c', protocol=None, writeback=False)
        names_only = input("Names only [Y/n] ->")

        if names_only == "Y":
            for name in db.keys():
                print(name)
        elif names_only == "n":
            for key in db.items():
                print(key, sep=' ', end='\n', file=sys.stdout, flush=False)
            #print((";\n".join("%s=>%s" % i for i in db.items())))


###############################################################################


###############################################################################
if __name__ == "__main__":

    arg_command = sys.argv[0]

    if len(sys.argv) > 1:
        arg_command = sys.argv[1]
        print("list", sep=' ', end='\n', file=sys.stdout, flush=False) # for to check
        print("add", sep=' ', end='\n', file=sys.stdout, flush=False) # for to check
        #command = input()
    else:
        sys.exit(1)

    if arg_command == "add":

        b = DictDrink("Borjomi",1.5)
        c = Adder.add(b)
    elif arg_command == "list":
        c = Adder._list()
    else:
        sys.exit(1)
