listFruits = ["apple", "banana", "orange", "grape", "mango"]
newline = ["Guava" , "watermelon"]

print(listFruits)
print('first value :- ' + listFruits[0])
print('last value :- ' + listFruits[-1])

print()
print('value \'4 is exluded\'s from 0-3 :- ')
print(listFruits[:4])


#add a new list inside the list
listFruits.append(newline)
print(listFruits)


#removes items
listFruits.remove(newline)
print(listFruits)


#destructure all the items and then add ll the intem of both list in the listFruits
listFruits.extend(newline)
print(listFruits)