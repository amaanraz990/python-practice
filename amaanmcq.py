questions = [ 
              ['Colors are defined in HTML using?','Rgb', '.hex', 'rgba', 'all the above','d']  ,                                        
              ['What is the smallest heading in HTML by default?', 'h1','h5','h6','h2',"c"],
              ['What are the types of lists available in HTML?', 'orderlist,','unorderlist','a and b both', 'non','c'],
              ['How to create an ordered list in HTML?', '<href>', '<ol>','<ul>', '<a>','c'],
              ['HTML files are saved by default with the extension?','.ht','.ml','.html', 'none of the above','c'],
              ['We enclose HTML tags within?', '<>', '[]', '!!','none','a'],
              ['What is the effect of the <b> tag?', 'bold','brake', 'balance','none','a'],
              ['Which of the following is correct about HTML?',' Hyper text laungage', 'hyper text markup language',' a and b both', 'none','b'],
              ['How to display preformatted text in HTML?',' <p>',' <hr>', '<pre>', '<div>','c'],
              ['Which of the following tags doesnt require a closing tag?','<hr>',' <a>','<href>', '<img>','a'],
]

total_score = 0
count = 1
for q in questions:
    print  (f"{count}.{q[0]}")
    print (f"a.{q[1]}")
    print (f"b.{q[2]}")
    print (f"c.{q[3]}")
    print (f"d.{q[4]}")

    ra = q[5]
    ans = input("Enter answer: ")
    if ra == ans:
        q.append(1)
    else:
        q.append(0)
    q.append(ans)
    count += 1 

total_score = 0     
count = 1 
for q in questions:

    print(f"{count}.{q[0]}")
    print(f"write answer is {q[5]} and you enter {q[7]}")
    if q[6] == 1:

        print("write answer")
    else:

        print("wrong answer")
    total_score = total_score + q[6]
    count = count + 1
print(f"total score is {total_score} out of 10")            

