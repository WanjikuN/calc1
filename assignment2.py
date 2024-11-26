# An empty list
my_list = []

# Append 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert 15 at index 2
my_list.insert(2,15)

#extend  with another list :[50,60,70]
my_list.extend([50,60,70]) 

#Remove last element
my_list.pop()

#Sort in ascending order
my_list.sort()

#Find and Print the index of the value 30
print(my_list.index(30))
