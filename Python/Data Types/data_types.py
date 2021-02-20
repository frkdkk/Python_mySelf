#Data Types

"""
Text(Yazı) : str
Numeric(Nümerik) : int, float, complex
Sequance(Sıralı) : list, tuple, range
Mapping(Eşli) : dict
Set : set, frozenset
Boolean : bool
Binary : bytes, bytearray, memoryview

"""



#"type()" değişkenin türünü bulmak için kullanılır.
x = 5
print(type(x))


#Örnek
x = "Hello World"
y = 20
z = 20.5
t = 1j 
a = ["elma", "muz", "çilek"]
b = ("elma", "muz", "çilek")
c = range(6)
d = {"name" : "John", "age" : 36}
e = {"elma", "muz", "çilek"}
f = frozenset({"elma", "muz", "çilek"})
g = True
h = b"Selam"
i = bytearray(5)
k = memoryview(bytes(5))


x = str("Selam")
x = int(20)
x = float(20.5)
x= complex(1j)
x = list(("apple", "banana"))
x = tuple(("apple", "banana")) #TUPLE
x = range(6)
x = dict(name="John",age = 36 )
x = set(("apple","banana"))  #SET
x = frozenset(("apple", "banana"))
x = bool(5)  #0 dışındaki tüm değerlerde TRUE
print(x)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

