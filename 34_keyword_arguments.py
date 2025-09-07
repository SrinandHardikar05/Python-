# keyword arguments = an argument preceded by an identifier helps with 
# readability order of arguments doesn't matter 
# 1. positional 2. default 3. KEYWORD 4 arbitrary

def hello(greetings, title, first, last):
    print(f"{greetings} {title}{first} {last}")

hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")