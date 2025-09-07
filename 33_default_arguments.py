# Default arguments = A deafult value for certain parameters default is 
# used when that argument is omitted make your functions, reduces no of arguments
# 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary


# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500, 0, 0.05))


import time 

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")

count(0,10)