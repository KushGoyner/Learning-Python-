def printf(**arg):
    for i,j in arg.items():
        print("key:",i,"value:",j)

printf(a=1,b=2,c=3)