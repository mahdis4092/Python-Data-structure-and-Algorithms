List=[2,3,4,5,6,7,8]
#Add or Append item in the Last Position
List.append(12)
print(List)
#Insert item in arbitary position
List.insert(3,20)
print(List)
#The remove() method removes the first matching value from the list.
#The pop() method like del deletes value at a particular index. But pop() method returns deleted value from the list
List2=[2,3,2,5,6,7,8]
List2.remove(2)
print(List2)#output [3, 2, 5, 6, 7, 8]

List3=[12,10,8,14,15,18]
List3.pop(2)
print(List3)#output [12, 10, 14, 15, 18]