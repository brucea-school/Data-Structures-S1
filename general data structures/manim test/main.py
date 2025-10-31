def go(x,y):
    if x>y:
        return go(x-1,y+2)+3
    elif x<y:
        return 2*go(x+1,y-1)-5
    else:
        return x*x+y

print(go(12,7))
