#Q.   If languages of two friends are same; what will happen to the program in previous problem?
#Ans: It will print all the keys and values(There is nothing wrong if values are duplicate).

#Q.   If languages of two friends are same; what will happen to the program in previous problem?
#Ans: It will override the new values on the privious one since only unique 'keys' are allowed.

#Q.   Can you change Contained in the values inside a Set S1's list which S1= {8, 7, 12, "Harry", [1,2]}
#ans: We cannot have a list, like [1, 2], as an element in a set because sets in Python only allow immutable (hashable) objects as their elements.
#     A list is mutable and thus cannot be included in a set.If you attempt to create a set like S1 = {8, 7, 12, "Harry", [1, 2]}, Python will raise
#     a TypeError.
