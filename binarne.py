import re
w=input("Wprowadz liczby 0 i 1 oddzielone przecinkami:")
w=w.replace(",","")
w=w[::-1]
print(w)
l=[]
for z in w:
	z=int(z)
	l.append(z)

print(l)
d=0
i=0
for c in l:
	d+=c*(2**i)
	print(d)
	i+=1
def podzielnosc(liczba, dzielnik):	
	if liczba%dzielnik==0:
		return True
	else:
		return False
		
print(podzielnosc(d,5))
