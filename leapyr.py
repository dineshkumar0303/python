def leap(y):
    if y%400==0:
        print("leap year!!!!!")
    elif y%100!=0 and y%4==0:
        print("leap year")
    else:
        print("NOOOOOOO")
y=int(input())
leap(y)
