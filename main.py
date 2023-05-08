from MyLinkedList import Lista

myLinkedList = Lista()

for i in range(0, 7):
    myLinkedList.append(i)

print(myLinkedList)

myLinkedList.delete(5)

print(myLinkedList)

myLinkedList.append(18)
myLinkedList.append(21)
myLinkedList.append(37)
print(myLinkedList)
print(myLinkedList.get(37))
myLinkedList.append(51, lambda a, b: a < b)
print(myLinkedList)
