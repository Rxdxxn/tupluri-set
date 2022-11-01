p1=(18,182,72,'masculin','necasatorit')
p2=(15,165,48,'feminin','necasatorit') 
p3=(35,162,61,'feminin','casatorit')
p4=(28,205,90,'masculin','necasatorit')
p5=(49,170,75,'masculin','casatorit')
p6=(21,169,65,'feminin','necasatorit')

def sub20(a,b,c,d,e,f):
    procent=0
    if a[0]<20:
        procent+=1
    if b[0]<20:
        procent+=1
    if c[0]<20:
        procent+=1
    if d[0]<20:
        procent+=1
    if e[0]<20:
        procent+=1
    if f[0]<20:
        procent+=1
    proc=round((procent/6)*100)
    return proc

def mare170(a,b,c,d,e,f):
    procent=0
    if a[1]>170:
        procent+=1
    if b[1]>170:
        procent+=1
    if c[1]>170:
        procent+=1
    if d[1]>170:
        procent+=1
    if e[1]>170:
        procent+=1
    if f[1]>170:
        procent+=1
    proc=round((procent/6)*100)
    return proc

def medium(a,b,c,d,e,f):
    masa=0
    num=0
    if a[0]>18:
        masa+=a[2]
        num+=1
    if b[0]>18:
        masa+=b[2]
        num+=1
    if c[0]>18:
        masa+=c[2]
        num+=1
    if d[0]>18:
        masa+=d[2]
        num+=1
    if e[0]>18:
        masa+=e[2]
        num+=1
    if f[0]>18:
        masa+=f[2]
        num+=1
    mass=(masa/num)
    return mass

def women(a,b,c,d,e,f):
    num=0
    femei=0
    if a[3]=='feminin':  
        femei+=1
        if a[0]>20 and a[4]=='necasatorit' and a[3]=='feminin':
            num+=1
    if b[3]=='feminin':
        femei+=1
        if b[0]>20 and b[4]=='necasatorit' and b[3]=='feminin':  
            num+=1
    if c[3]=='feminin':  
        femei+=1
        if c[0]>20 and c[4]=='necasatorit' and c[3]=='feminin':
            num+=1
    if d[3]=='feminin': 
        femei+=1
        if d[0]>20 and d[4]=='necasatorit' and d[3]=='feminin':
            num+=1
    if e[3]=='feminin':  
        femei+=1
        if e[0]>20 and e[4]=='necasatorit' and e[3]=='feminin':
            num+=1
    if f[3]=='feminin':  
        femei+=1
        if f[0]>20 and f[4]=='necasatorit' and f[3]=='feminin':
            num+=1
    procent=round((num/femei)*100)
    return procent

def greutate(a,b,c,d,e,f):
    num=0
    gmm=0
    if  a[0]>20 and a[0]<50:
        num+=1
        if a[2]>medium(a,b,c,d,e,f):
            gmm+=1
    if  b[0]>20 and b[0]<50:
        num+=1
        if b[2]>medium(a,b,c,d,e,f):
            gmm+=1
    if  c[0]>20 and c[0]<50:
        num+=1
        if c[2]>medium(a,b,c,d,e,f):
            gmm+=1
    if  d[0]>20 and d[0]<50:
        num+=1
        if d[2]>medium(a,b,c,d,e,f):
            gmm+=1
    if  e[0]>20 and e[0]<50:
        num+=1
        if e[2]>medium(a,b,c,d,e,f):
            gmm+=1
    if  f[0]>20 and f[0]<50:
        num+=1
        if f[2]>medium(a,b,c,d,e,f):
            gmm+=1
    procent=round((gmm/num)*100)
    return procent

print("Procentul persoanelor sub 20 de ani este in jur de:",sub20(p1,p2,p3,p4,p5,p6),"%")
print("Procentul persoanelor cu înălțimea mai mare de 170 cm este in jur de:",mare170(p1,p2,p3,p4,p5,p6),"%") 
print("Masa medie a unei persoane de peste 18 ani este de:",medium(p1,p2,p3,p4,p5,p6),"kg")  
print("Procent din numărul persoanelor de sex feminin,peste 20 de ani și nu sunt căsătorite in jur de:",women(p1,p2,p3,p4,p5,p6),"%")
print("Procent din numărul persoanelor între 20 și 50 ani,greutatea mai mare decât greutatea medie, este in jur de:",greutate(p1,p2,p3,p4,p5,p6),"%")