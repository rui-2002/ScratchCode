from __future__ import division

print(5/2)
print(5//2)


# functions

def double(x):
    return x**2

def apply_to_one(f):
    return f(1)

my_double=double
x=apply_to_one(my_double)
print(x)


y=apply_to_one(lambda x:x+4)

another_double=lambda x:2*x
def another_double(x): return 2*x

def my_print(message="my default msg"):
    print(message)

my_print("hello")
my_print()

def subtract(a=0,b=0):
    return a-b

print(subtract(1,2))
print(subtract(b=5))


# Strings 

tab_string="\t"
print((tab_string))


# want to use \
not_tab_string=r"\t"
print(len(not_tab_string))

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

print(multi_line_string)

# Exceptions 

try :
    print(0/0)
except ZeroDivisionError:
    print("Cannot divide by zero")


# List :

integer_list=[1,2,3]
heterogeneours_list=["string",0.1,True]
list_of_lists=[integer_list,heterogeneours_list,[]]


list_length=len(integer_list)
list_sum=sum(integer_list)


print(list_length)
print(list_sum)
print(list_of_lists)

x=list(range(10))
print(x)
zero=x[0]
nine=x[-1]
eigth=x[-2]
x[0]=-1

print(x)

last_three = x[-3:] # [7, 8, 9]
without_first_and_last = x[1:-1]
copy_of_x = x[:] 

x.append(0)

print(x)


# Tuples :immutable cannot be modified list


my_tuple=(1,2)
try:
    my_tuple[1]=2
except TypeError:
    print("Cannot modify a tuple")


# print index of tuple data
print(my_tuple.index(2))

# Dictonaries : key value pair

empty_dict={}
empty_dict2=dict()

grades={"sumit":1 , "amit":2}

grades["sumit"]=2
print(grades)

try:
    kates_grade = grades["Kate"]
except KeyError:
    print ("no grade for Kate!")
