# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30


# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0]=15
# print(x)

# students[0]['last_name']='Bryant'
# print(students[0]["last_name"])

# sports_directory[[1][0]] = 'Andres'
# print(sports_directory[[1][0]])

# z[0]['y'] = 30
# print(z[0]['y'])

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(myDict):
#     for item in myDict:
#         for key in item:
#             print(item[key])

# def iterateDictionary(myDict):
#     for people in myDict:
#         print(people)

# iterateDictionary(students)

# print(students[0][0])
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterateDictionary2(key_name, some_list):
#         for i, names in enumerate(some_list):
#             print(some_list[i][key_name])

# iterateDictionary2("first_name",students)
# iterateDictionary2("last_name",students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictionary):
    for keys in dictionary:
        print(f"\n{len(dictionary[keys])} {keys}")
        for i in range (0,len(dictionary[keys]),1):
            print(dictionary[keys][i])

printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon