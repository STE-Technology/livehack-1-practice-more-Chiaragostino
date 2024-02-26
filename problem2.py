"""
problem2.py
Chiara A
02/26/2024
"""
#User inputs the age of the children
first_child=int(input("What is the age of the first child?: "))
second_child=int(input("What is the age of the second child?: "))

#calculates the age of the third child
third_child= second_child - first_child + second_child 

#outputs the third childs age
print("The age of the third child is", third_child)


