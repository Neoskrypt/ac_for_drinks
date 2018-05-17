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


class Adder:
    def __init__(self,name,amount):
        super().__init__(name,amount)

    @staticmethod
    def add(obj: DictDrink ):
        db = shelve.open("db", "c")
        if obj.name in db:
            raise ex.DrinkAlreadyExists("")
        elif obj.amount <= 0 or obj.amount > 10:
            raise ex.InvalidVol("")
        elif obj.name is "":
            raise ex.PassArgs("")
        else:
            db[obj.name] = DictDrink.to_dict(obj)
            print("Drink successfully added!!!\n name = {} litres = {}".
            format(obj.name, obj.amount))

    @staticmethod
    def list(obj_type):
        """print list of drinks"""
        db = shelve.open("db", flag='c', protocol=None, writeback=False)

        if obj_type == 'drinks':
            for name in db.keys():
                print(name)
        elif obj_type == 'reserves':
            for key in db.keys():
                print("{} ({} litres)".format(key, db[key]['amount']))
        else:
            raise ex.PassArgs("Incorrect object type: '{}'".format(obj_type))


###############################################################################


###############################################################################
if __name__ == "__main__":

    arg_command = sys.argv[0]

    if len(sys.argv) > 1:
        arg_command = sys.argv[1]
    else:
        sys.exit(1)

    if arg_command == "add" and len(sys.argv) > 2:

        b = DictDrink(sys.argv[2], 10)
        c = Adder.add(b)
    elif arg_command == "list" and len(sys.argv) > 2:
        obj_type = sys.argv[2]
        Adder.list(obj_type)
    else:
        raise ex.PassArgs("Incorrect arguments passed.")
