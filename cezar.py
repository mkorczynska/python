t="Ala ma kota"
t=t.lower()
t=t.replace(" ","")
p=3
def cezar(txt, prz):
	k=""
	for l in txt:
		#print(l,chr(ord(l)+prz))
		s=ord(l)+prz
		if s>ord("z"):
			s-=26
		elif s<ord("a"):
			s+=26
		o=chr(s)
		k+=o
	return(k)
		
kod=cezar(t,p)
print("Zakodowany tekst: ", kod)
dekod=cezar(kod,p*(-1))
print("Odkodowany tekst: ", dekod)
print("brute force")
i=1
while i<=26:
	dekod=cezar(kod,i*(-1))
	print(dekod)
	i+=1
	
	
