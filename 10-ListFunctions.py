friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]
lucky_numbers = [4, 8, 9, 23, 42]

#extend funtion:
friends.extend(lucky_numbers)

#add individual items to a list
friends.append("Creed")

#Add a value at index vaule 1, Kelly
friends.insert(1, "Kelly")
friends.remove("Jim")


print(friends)
print(friends.index("Karen"))




#remove the last element in the list
friends.pop()
print(friends)

friends.sort()
print(friends)


lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)


#clear the list
friends.clear()
