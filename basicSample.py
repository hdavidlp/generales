def x(a, *param):
    print (a)
    for  p in param:
        print(f"{p}")


x("Uno","Dos:2","Tres:3")