#https://github.com/mafm/ledger.py/blob/master/test_ledger.py
#https://pymotw.com/2/shelve/
import resto

################################################################################
drinks ={"Name":"Pivo","amount":8}
dr = resto.Drinks(drinks)
print(dr)

d = {"Name": "Vodka","amount":5}
dr.add(d)
print(dr)
d = {"Name": "Vodka","amount":5}
dr.add(d)
print(dr)
print(dr._dict())
dr.set("Martini",15)
print(dr)


dr.loadBinary()
