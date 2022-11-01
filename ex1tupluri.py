e1=("Mihai","Ionescu","masculin",10,10,9)
e2=("Eugenia","Florescu","feminin",8,9,10)
e3=("Andrei","Aron","masculin",3,7,5)
e4=("Maria","Ocna","feminin",8,3,7)
e5=("Ion","Popescu","masculin",9,9,9)
def notamed(a):
    a=sum(a[3:])/3
    return a
def restanta(a):
    for i in range(1,4):
        while i in a[3:]:
            print("Elevul/a",a[0],a[1],"este restantier")
            break
    return 
def eminent(a):
    while notamed(a)>=9.0 and a[3]>=9 and a[4]>=9 and a[5]>=9:
        print("Elevul/a",a[0],a[1],"este eminent")
        break
    return 


print("Nota medie este de:",notamed(e1),"la primul elev,",notamed(e2),"la al 2 elev,",notamed(e3),"la al 3 elev,",notamed(e4),"la al 4 elev,",notamed(e5),"la al 5 elev.")
restanta(e1),restanta(e2),restanta(e3),restanta(e4),restanta(e5)
eminent(e1),eminent(e2),eminent(e3),eminent(e4),eminent(e5)