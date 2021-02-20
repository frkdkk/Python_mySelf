#Boolean Values

# True-False (1-0)
print(9<10)
print(9>10)


print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#İçinde bir şey olan string int vs. her zaman True döndürür.
#İçi boş olmayan tuple,set,list True döndürür.
#0 haricinde her sayı True döndürür.

#False döndüren durumlar.
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


def myFunc():
    return True

print(myFunc())



x = 200
print(isinstance(x,int))