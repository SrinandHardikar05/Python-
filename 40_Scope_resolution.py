# variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# We cannot print a with the help of func2() because it is a different vatiable inside a different function 

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)