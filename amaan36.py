items = {
    'rice' : { 'price': 80, 'a': '0.5', 'b': '1', 'c': '1.5', 'd': '2'},
    'sugar' : { 'price': 100, 'a': '0.5', 'b': '1', 'c': '1.5', 'd': '2'},
    'wheat' : { 'price': 120, 'a': '0.5', 'b': '1', 'c': '1.5', 'd': '2'},
    'pulse' : { 'price': 60, 'a': '0.5', 'b': '1', 'c': '1.5', 'd': '2'}
}

count = 1
total = 0
for (name,p) in items.items():
    print(f"{count}.{name}")
    for (k,v) in p.items():
        if k != "price":
            print(k, v)

    price = p["price"]        
    x = input("enter the quantity a,b,c,d:")
    if x in "abcd":
        w = float(p[x])
        total = total + price*w
    count = count + 1
print(total)        
