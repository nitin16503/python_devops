#                                                         🙌 𝕃𝕚𝕤𝕥𝕤 🙌 
# List are mutable.
friends = ["daksh", 'pankaj', 'mohit', 'chuha', 'bua']
print (friends)

# 1st index number
print(friends[0])

#last index number
print(friends[4])

#adding element to list 
friends.append("raj")
print(friends)

#removing element from list 
#1 -> "remove" by name
friends.remove("raj")
print(friends)
#2 -> "remove" by index
friends.remove(friends[4])
print(friends)
#3 -> "pop" by index
friends.pop(3) 
print(friends)
friends.pop() #pop(nothing) -> it removes and returns the last element by default.
print(friends)
#4 -> "del" by index/slice
del friends[0:2]
print(friends)

# adding element to list
friends.insert(0,"myself")
print(friends)

#                                                        🙌 𝕋𝕦𝕡𝕝𝕖𝕤 🙌
# Tuples are immutable.
friends = ("me", "anime", "workout")