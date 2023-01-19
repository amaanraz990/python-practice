#DSA
# Que 
# it is based on pop means first first item removed then second one and one by one
"""
items = []
while True:
    option = int(input("please enter 1 to add \n 2 to pop \n and 0 to exit "))
    if option == 0:
        break
    elif option == 1:
        txt = input("input item to add: ")
        items.append(txt)
    elif option == 2:
        if len(items) > 0:
            t = items[0]
            print(f"pop item is {t}")
            del items[0]
        else:
            print("empty list")    
    else:
        print("invalid input")

    print("New list is: ")
    print(items)
    """
# stack
# pop item last then second last so on     
items = []
while True:
    option = int(input("please enter 1 to add \n 2 to pop \n and 0 to exit "))
    if option == 0:
        break
    elif option == 1:
        txt = input("input item to add: ")
        items.append(txt)
    elif option == 2:
        if len(items) > 0:
            t = items.pop()
            print(f"your item is {t}")
        else:
            print("empty list")    
    else:
        print("invalid input")

    print("New list is: ")
    print(items)





    
