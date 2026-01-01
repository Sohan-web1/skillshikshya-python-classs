# dictionary is a mutable data
# type which is built and stores pairs

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

first_dictianory = {"name":"sohan","age":20}
print(first_dictianory.values())
print(first_dictianory.keys())

second_dictianory = {"name":"sohan","age":20}
print(second_dictianory)

first_hash = hash('age')
second_hash = hash('age')

print(first_hash)
print(second_hash)

print(second_dictianory)

print(second_dictianory.items())

for key,value in second_dictianory.items():
    print(key)
    print(value)

    # accessing elements from dictonary
    name = second_dictianory['name']
    print(name)

    # accessing using get() method
    name = second_dictianory.get('name')
    print(name)

dict_1 = {'name':"abcd",'age':26}
dict_2 = {'age':26,'name':"efgh"}
print(dict_1==dict_2)
print(dict_1 is dict_2)
print(id(dict_1))

# merging the dictionaries 

result_dict = dict_2 | dict_1
print(result_dict)
print(id(result_dict))

# update merge
dict_1.update(dict_2)
print(dict_1)
print(id(dict_1))

# intersection merge 
dict_1 = {'name':"abcd",'age':26}
dict_2 = {'age':26,'name':"efgh"}
result_dict = dict_2 and dict_1
print(result_dict)

key argument merge
result_dict = {**dict_2,**dict_1}
print(result_dict)

remove key value pair
dict_3 ={'name':"sohan","age":26}
value = dict_3.pop('name')
print(value)
print(dict_3)

value = dict_3.popitem()
print(value)
print(dict_3)

aryithmatic opeartion
additon 
a = 10
b = 20
c = a+b
print (c)

# substract
a = 10
b = 20
c = a-b
print (c)

# multiplication
a = 10
b = 20
c = a*b
print (c)

# division
a = 20
b = 50
c = a/b
print (c)

# modulus operation
a = 10
b = 20
c = a%b
print (c)

# floor division oerators
a = 10
b = 20
c = a//b
print (c)

# expontial operation
a = 10
b = 20
c = a**b
print (c)

# comparison (relational) operators
a = 10
b = 20
c = a == b
print (c)

# not equal too
a = 10
b = 20
c = a!=b
print (c)

# greater then
a = 10
b = 20
c = a>b
print (c)

# less then
a = 10
b = 20
c = a<b
print (c)

# greater then equal too
a = 10
b = 20
c = a>=b
print (c)

# lesser then equal too
a = 10
b = 20
c = a<=b
print (c)

logical operator
a = True
b = False
c = a and b
print(c)

a = True
b = False
c = a or b
print(c)

a = True
b = False
c = not a
print(c)

# task 1

listing =[]
seting ={}

if listing and seting:
    print("True")
else:
    print("False")

listing =[1,2,3,4]
seting ={5,6,7,8}

if listing and seting:
    print("True")
else:
    print("False")

task 
listing = [1,2,3,4]
seting ={5,6,7,8}
if not listing:
    print("True") 
else:
    print("False")

if not listing and not seting:
    print("True")
else:
    print("False")

if not listing or not seting:
    print("True")
else:
    print("False")

# assignment operators
# addition
a = 10
a += 20
print(a)

# subraction
a = 10
a -= 20
print(a)

# multiplication
a = 10
a *= 20
print(a)

# division
a = 10
a /= 20
print(a)

a = 10
a **= 20
print(a)

a = 10
a //= 20
print(a)

a = 10
a %= 20
print(a)

# expontial assignment operators
# 
a = 10
a **= 2
print(a)

# modulus
a = 10
a %= 2
print(a)

a = 10
a //= 2
print(a)

membership operator
a = 10
b = 20
c = a in b
print(c)

a = 10
b = 20
c = a not in b
print(c)

dict = [1,2,3,4]
if 1 is dict:
    print("True")
else:
    print("False")

use in opeartion in dictianory
keys and values to check membershhip
dict_1= {"nam":"sohan","age":'20'}
if 'sohan'in dict_1:
    print("True")
else:
    print("False")

dict_1= {"name":"sohan","age":'20'}
if 'sohan'is dict_1:
    print("True")
else:
    print("False")


bitewise operators 
a = 2
b = 3

print(a & b)
print(a | b)
print(a ^ b)

for i in range(10):
    print(i)
    if i % 2 == 0:
        continue
    print(f"odd number: {i}") 

a = [1,2,3,"dog",4,5,6,'ORANGE',7,8,9,10,"forest",11,1,23,None,15,56,345]
for i in a:   
    if i ==None:
        break
print(i)

find smallest loop from the random intizer

a = [324,2423,352,35,45,35,253253,3252,5,32,354235,5,223,5225,23326,232,36]
b = a[17]

for i in range(1, len(a)):
    if a[i]<b:   
        a = b[i]  
    print(smallest)    

