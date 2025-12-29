# # def greet_student(Sohan):
# #     print(type(name))
# #     print(f"hellow,{sohan}!Welcome to python class.")
# #     return f"good day, {name}!"

# #     greet_student()
# #     print(result)

# # classwork related positional argument and key arguments

# # task 1
# # create a small function to calculate the volume of a cuboid

#  def cuboid_volum(length,width,height):

#     return Length * width * height

# # length=12
# # width=112
# # height=12



# def vol(l,b,h):
#     return l*b*h
# print(vol(10,12,12))


# repeat same message multiple times using function

# def message():
#     for i in range(9):
#         print("hellow")

# print(message())        

## recursive function

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci (n-1) + fibonacci(n-2)

# print(fibonacci(5))

## sum of natural number using resursive function 

# def sum(n):
#     if n==1:
#         return n
#     else:
#         return n + sum(n-1)

# print(sum(5))

# ## from the list find the smallest number using rsesurcive function

# def smallest_number(n):
#     if len(n) == 1:
#         return s[1]
#     else:
#         return smallest_number (n)
#         n = [1,2,3,4,5]

# print(smallest_number(1))


# def smallest_number(list):
#     # Base case: if the list has only one element
#     if len(list) == 1:
#         return list[0]
    
#     # Recursive case
#     min_of_rest = smallest_number(list[1:])
    
#     if list[0] < min_of_rest:
#         return list[0]
#     else:
#         return min_of_rest

