# this is is our 3rd class
'''
multi-line comment 3 ' above and below
'''

# Review
# Assignment 

# write 4 assignment statements for int, float, boolean, string; print; print type

x = 10+2
y = 7.9
q = True
msg = "Hi i am a new CPRG student"

print("the value of the variable x is: ",x,"and the type is ",type(x))
print("the value of the variable y is: ",y,"and the type is ",type(y))
print("the value of the variable q is: ",q,"and the type is ",type(q))
print("the value of the variable msg is: ",msg,"and the type is ",type(msg))


# casting - changing from one type to another; from int to float is promoting(increasing the size); from float to int is demoting(decreasing in size)

#some function call: print, input, int, float, str, bool
num_as_text = "43"
num_as_num = int(num_as_text) #converting string (text) to num

print(num_as_text) #will print as text
print(num_as_num) # will it print?
print(str(num_as_num)) # equivalent

num = 3