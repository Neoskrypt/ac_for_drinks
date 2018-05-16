import shelve
import exeptions as ex
# import json
import sys

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
    @staticmethod
    def _list():
        """print list of drinks"""
        db = shelve.open("db", flag='c', protocol=None, writeback=False)
        #names_only = ""
        #names_only == False
        #if names_only == True:
        for name in db.keys():
            print(name, sep=' ', end='\n', file=sys.stdout, flush=False)
        #else:
            #print((";\n".join("%s=>%s" % i for i in db.items())))


###############################################################################


###############################################################################
if __name__ == "__main__":
        try:
            arg_command = sys.argv[1]
        except IndexError:
            arg_command = ""
        if arg_command == "":
            print("list", sep=' ', end='\n', file=sys.stdout, flush=False)
            print("add", sep=' ', end='\n', file=sys.stdout, flush=False)
            command = input("Enter command->")
        else:
            command = arg_command
        if command == "add":
            name = input("Enter kind of drink->")
            b = DictDrink("Borjomi",1.5)
            c = Adder.add(b,name)
        elif command == "list":
            c = Adder._list()
