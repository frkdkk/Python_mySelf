#Add List Items

# "append()" metodu sona ekler.
myList = ["apple", "banana", "cherry"]
myList.append("orange")
print(myList)


# "insert()" metodu istenilen index'e ekler.
myList = ["apple", "banana", "cherry"]
myList.insert(1,"orange")
print(myList)


# "extend()" metodu var olan listeye başka listenin değerlerini ekler.
myList1 = ["apple", "banana", "cherry"]
myList2 = ["mango", "pineapple", "papaya"]
myList1.extend(myList2)
print(myList1)


# "extend()" metodu sadece listeyi listeye eklemez,tuple'ı listeye de ekleyebilir.
myList1 = ["apple", "banana", "cherry"]
myTuple1 = ("mango", "pineapple", "papaya")
myList1.extend(myTuple1)
print(myList1)