from random import randint as r
x=set()
y=set()
z=set()
#Multimea ce contine numere de la 0 pana la 200
w=set()
for i in range(0,6):
    x.add(r(0,200))
    y.add(r(0,200))
    z.add(r(0,200))
for i in range(0,201):
    w.add(i)
print("X:",x)
print("Y:",y)
print("Z:",z)
c1=w-(x|y|z)
c2=(w-x)&(w-y)&(w-z)
print("a)Primul rezultat este c1 si al doilea rezultat este c2")
if(c1==c2):
    print("Valorile sunt egale, legea lui Morgan este ADEVARATA")
else:
    print("Legea lui Morgan este FALSA")

c3=w-(x&y&z)
c4=(w-x)|(w-y)|(w-z)
print("b)Primul rezultat este c3 si al doilea rezultat este c4")
if(c3==c4):
    print("Valorile sunt egale, legea lui Morgan este ADEVARATA")
else:
    print("Legea lui Morgan este FALSA")
