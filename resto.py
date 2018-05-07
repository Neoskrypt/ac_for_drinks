import shelve
#https://code.activestate.com/recipes/576642/
#https://pymotw.com/2/shelve/
#https://pythoner.name/shelve-objects
#https://www.quora.com/How-do-I-put-dictionary-to-the-shelve-in-Python
class Drink:

    def __init__(self,name = None,amount = None,**data):
        self._data = data
        self.name = name
        self.amount = amount
    def get(self,key): #метод для возврата значения
        return self._data[key]
    def set(self,key,value)->None: #метод присваивания нового значения
        self._data[key] = value
    def add(self,x):
        self._data.update(x)
    def _dict(self)->dict:
        return self._data
    def __str__(self)->str:
        return (";\n".join("%s=>%s" % i for i in self._data.items()))

################################################################################
d = shelve.open("db_file")  # open -- file may get suffix added by low-level
print(d)
"""                           # library
data = {"name":"Vodka","amount":4.5}
d[key] = data              # store data at key (overwrites old data if
                           # using an existing key)
data = d[key]              # retrieve a COPY of data at key (raise KeyError
                           # if no such key)
del d[key]                 # delete data stored at key (raises KeyError
                           # if no such key)

flag = key in d            # true if the key exists
klist = list(d.keys())     # a list of all existing keys (slow!)

# as d was opened WITHOUT writeback=True, beware:
d['xx'] = [0, 1, 2]        # this works as expected, but...
d['xx'].append(3)          # *this doesn't!* -- d['xx'] is STILL [0, 1, 2]!

# having opened d without writeback=True, you need to code carefully:
temp = d['xx']             # extracts the copy
temp.append(5)             # mutates the copy
d['xx'] = temp             # stores the copy right back, to persist it

# or, d=shelve.open(filename,writeback=True) would let you just code
# d['xx'].append(5) and have it work as expected, BUT it would also
# consume more memory and make the d.close() operation slower.

d.close()                  # close it
"""
