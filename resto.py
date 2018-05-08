#import shelve


import exeptions as ex
class Drink:

    def __init__(self,data=None):
        self._data = data
    def get(self,drinks): #метод для возврата значения
        return self._data[drinks]
    def set(self,drinks,reserves)->None: #метод присваивания нового значения
        self._data[drinks] = reserves
    def add(self,x):
        self._data.update(x)
    def _dict(self)->dict:
        return self._data
    def __str__(self)->str:
        return (";\n".join("%s=>%s" % drinks for drinks in self._data.items()))

################################################################################
class Drinks(Drink):
    def __init__(self,data):
        super().__init__(data)

    def allex(self):
        for k in self._data:
            try:
                if i in self._data:
                    raise ex.AlExists()
            except ex.AlExists() as Al:
                print(Al)

    def not_found(self):
        for i in self._data:
            try:
                if i not in self._data.keys():
                    raise ex.NotFound()
            except ex.NotFound() as nt:
                print(nt)

    def invVol(self):
        for i in self._data:
            try:
                if reserves >= 0.5:
                    raise ex.InvalidVol()
            except ex.InvalidVol() as inv:
                print(inv)
