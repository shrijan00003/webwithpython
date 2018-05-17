# HERE WE ARE GOING TO DISCUSS ABOUT SOME DATATYPE RATHER THAN THE BASIC ONE 


# list with heterogeneous value
# but it is good to have the same type of list 
l=[26,"alice","bob"]
# print(l[0])

# SET
#set is the collection of item here the order of the value in the set is not important 
# what we care about is whether perticular value is in the set or not 
#  the item in the set should be unique so , if we are going to add same element again then 
# there will be no effect in the set 
s=set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
# prindatat(s)

# DICTIONARIES IN PYTHON
# Its seems like javascript object of name value pair 
# we call it here key and value 
ages={"Alice":22,"BOb":27}
ages["Charlie"]=30 #adding new vaule
ages["Alice"] +=1 #changing or modifying vaule of dictionaries

print(ages)