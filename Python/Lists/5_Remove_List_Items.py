#Remove List Items


# "remove()" seçilen item'i siler.
myList = ["apple", "banana", "cherry"]
myList.remove("banana")
print(myList)


# "pop()" seçilen index'i siler.
myList = ["apple", "banana", "cherry"]
myList.pop(0)
myList.pop() #İndex belirtilmezse sondaki index'i siler.
print(myList)


# "del" ile istenilen index silinebilir ya da liste tamamen silinebilir.
myList = ["apple", "banana", "cherry"]
del myList[1]
print(myList)
del myList #Liste tamamen silindi.


# "clear()" listeyi tamamen boşaltır
myList = ["apple", "banana", "cherry"]
myList.clear()
print(myList)

