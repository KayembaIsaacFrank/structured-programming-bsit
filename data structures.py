# list data structure; uses these brackest[]
'''
boys = ['Jones', 'james', 'peter']
#print(boys)

# example 2
print(boys[0]) #picking the first person; index = 0

# adding elements to the list
method 1
girls = [] #initialize the empty list
girls.append('Joan')
girls.append('Fridah')
girls.append('Benitah')
print(girls)

# method 2 using loops
girls = []
girls.append('Fridah')
number = int(input("enter the number of girls you want to record"))
i = 0; 
while i <= number:
    girl = input("enter the name")
    girls.append(girl)
    i += 1
print(girls)
'''
## list operations(editing)
girl = ['Joan', 'Jane', 'Hope', 'Benitah']
'''
## list modification
girl[0] = "Joanitah" #calling the person at index 0(Joan)(editing the name)
girl.insert(1, "Juliet")# adding someone to the list from index 1
girl.pop()## deleting the last item...note that pop only deletes the last value
girl.remove("Juliet")# deletes any item selected
print(girl)

#returning the list using for loop
for g in girl:
    print(g)

##list slicing
# we are using the above list
print(girl[1:4])# prints from 1 to the less number to 4


#PYTHON DICTIONARY

#represented with {} brackets



#example
credentials = {
    'username': "b33348@ucu.ac.ug",
    'password': "12345"
}
#extracting data from the dict
print(credentials['username'])#call the dict name(credentials) then the key(username)


print("log in system")
username = input("Enter your username:")
password = input("Enter your password:")
 
##checking the authentification
if username == credentials['username'] and password == credentials['password']:
    print("Login successful")
else:
    print("Invalid credentials, please try again!")

##Dict operators
#changing a value in the dictionary
credentials = {
    'username': "b33348@ucu.ac.ug",
    'password': "12345"
}
#eg
credentials['username'] = "isaac" #assign the key

##adding an item to the dict
credentials["personal_email"] = "isaackayemba669@gmail.com" 

print(f"updated dictionary: {credentials}")
'''
##combination of lists and dictionaries
#storing data for multiple people
students = [{'username': "b33348@ucu.ac.ug",'password': "12345"},
            {'username': "b33348@ucu.ac.ug",'password': "12345"}, 
            {'username': "b33348@ucu.ac.ug",'password': "12345"},
            {'username': "b33348@ucu.ac.ug",'password': "12345"},
            {'username': "b33348@ucu.ac.ug",'password': "12345"}
            ]
print(students)
'''
##adding to the dictionary
student = {'username':"b33347@ucu.ac.ug", 'password': "b43356@ucu.ac.ug"}
students.append(student)
print(students)
'''