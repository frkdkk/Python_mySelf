#Change Item Value


myList = ["apple", "banana", "cherry"]
myList[1] = "orange"
print(myList)


#Change a Range of Item Value
myList = ["apple", "banana", "cherry", "orange", "kiwi"]
myList[1:3]=["apple","kiwi"]
print(myList)


#Tek indexe iki değer gönderme
myList = ["apple", "banana", "cherry", "orange", "kiwi"]
myList[1:2]=["apple","kiwi"]
print(myList)


#İki indexe tek değer gönderme
myList = ["apple", "banana", "cherry"]
myList[0:2] = ["orange"]
print(myList)


#Insert Items (istenen indexe değer gönderme)
myList = ["apple", "banana", "cherry"]
myList.insert(2, "watermelon")
print(myList)