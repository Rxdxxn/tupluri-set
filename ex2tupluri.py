from datetime import date
#tuplul declarat conform datelor din problema
data=(19,10,'miercuri')
#data curenta
data2=date(2022,data[1],data[0])
#data de la inceputul anului
data1=date(2022,1,1)
miercuri = 1
for i in range(data1.toordinal(), data2.toordinal()):
    d = date.fromordinal(i)
    if (d.weekday() == 2):
        miercuri += 1
print("Numarul de zile de",data[2],"de la inceputul anului este:",miercuri)