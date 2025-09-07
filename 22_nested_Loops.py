# nested loop = A loop within another loop (outer, inner)
            # outer loop:
                # inner loop:


rows = int(input("Enter the number of rows: "))
colunms = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")



for x in range(rows):
    for c in range(colunms):
        print(symbol, end=" ") # end keyword is used for printing the item on same line
    print() # it'll print in a new line 