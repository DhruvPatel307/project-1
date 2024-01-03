import random

def game(comp,your):
    if(comp==your):
        return None
    elif(comp=='r' and your=='s'):
        return False
    elif(comp=='r' and your=='p'):
        return True
    elif(comp=='p' and your=='r'):
        return False
    elif(comp=='p' and your=='s'):
        return True
    elif(comp=='s' and your=='p'):
        return False
    elif(comp=='s' and your=='r'):
        return True


print("comuter turns : select rock(r),Scessior(s),paper(p)") 
comp=random.randint(1,3)
if(comp==1):
    comp='s'
elif(comp==2):
    comp='r'
else:
    comp='p'


your=input("your turns : select rock(r),Scessior(s),paper(p) : ")


print("computer select : "+comp)
print("you select : "+your)

a=game(comp,your)

if(a==None):
    print("Game tie.")
elif(a):
    print("You Win.")
else:
    print("You Lose try again.")