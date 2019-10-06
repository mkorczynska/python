class Robot:	
	def up(self, dist):
		self.x -= dist

	def down(self, dist):
		self.x += dist

	def left(self, dist):
		self.y -= dist

	def right(self, dist):
		self.y += dist

	def __init__(self, name, num):
		self.n=name
		self.nu=num
		
class Board:
	def drawBoard(self, size, arr):
		arr=[[0 for col in range(size)] for row in range(size)]
		return arr
			
	def printBoard(self, arr):
		for i in arr:
			print(" ".join(map(str,i)))

	def change(self, arr, x, y):
		arr[x][y]=0

class Figth:
	def rand(self, pl):
		items=['scissors', 'paper', 'rock']
		attrib=random.choice(items)


				
ex=False
tab=[]
board=Board()

while ex==False:
	try:
		num_pl=int(input("Podaj ilość graczy: "))
		maks=4
		if num_pl>maks:
			print("Maksymalna ilość graczy wynosi 4.")
		elif num_pl<=1:
			print("Liczba graczy musi być większa od 1.")
		else:
			break
	except ValueError:
		print("Podana wartość musi być liczbą. Spróbuj jeszcze raz.")
	
if num_pl==2:
	name1=input("Podaj imię pierwszego robota: ")
	name2=input("Podaj imię drugiego robota: ")
	r1=Robot(name1, 1)
	r2=Robot(name2, 2)
	pl_arr=[r1, r2]
	print("Witajcie w grze ",r1.n," i ",r2.n,"!")
	print("Oto plansza dla Waszej gry:")
	tab=board.drawBoard(10, tab)
	r1.x=0
	r1.y=0
	tab[r1.x][r1.y]=1
	r2.x=9
	r2.y=9
	tab[r2.x][r2.y]=2
	board.printBoard(tab)
elif num_pl==3:
	name1=input("Podaj imię pierwszego robota: ")
	name2=input("Podaj imię drugiego robota: ")
	name3=input("Podaj imię trzeciego robota: ")
	r1=Robot(name1, 1)
	r2=Robot(name2, 2)
	r3=Robot(name3, 3)
	pl_arr=[r1, r2, r3]
	print("Witajcie w grze ",name1,", ",name2," i ",name3,"!")
	print("Oto plansza dla Waszej gry:")
	tab=board.drawBoard(15, tab)
	r1.x=0
	r1.y=0
	tab[r1.x][r1.y]=1
	r2.x=14
	r2.y=14
	tab[r2.x][r2.y]=2
	r3.x=14
	r3.y=0
	tab[r3.x][r3.y]=3
	board.printBoard(tab)
else:
	name1=input("Podaj imię pierwszego robota: ")
	name2=input("Podaj imię drugiego robota: ")
	name3=input("Podaj imię trzeciego robota: ")
	name4=input("Podaj imię czwartego robota: ")
	r1=Robot(name1, 1)
	r2=Robot(name2, 2)
	r3=Robot(name3, 3)
	r4=Robot(name4, 4)
	pl_arr=[r1, r2, r3, r4]
	print("Witajcie w grze ",name1,", ",name2,", ",name3," i ",name4,"!")
	print("Oto plansza dla Waszej gry:")
	tab=board.drawBoard(20, tab)
	r1.x=0
	r1.y=0
	tab[r1.x][r1.y]=1
	r2.x=19
	r2.y=19
	tab[r2.x][r2.y]=2
	r3.x=19
	r3.y=0
	tab[r3.x][r3.y]=3
	r4.x=0
	r4.y=19
	tab[r4.x][r4.y]=4
	board.printBoard(tab)

i=0
while i<=1:
	for pl in pl_arr:
		print("Kolej gracza nr: ",pl.nu,"-",pl.n)
		move=input("Podaj kierunek poruszania się robota [u/d/l/r]:")
		dist=int(input("Podaj dystans do przejscia: "))
		if move=="u":
			board.change(tab, pl.x,pl.y)
			pl.up(dist)
			tab[pl.x][pl.y]=pl.nu
		elif move=="d":
			board.change(tab, pl.x,pl.y)
			pl.down(dist)
			tab[pl.x][pl.y]=pl.nu
		elif move=="l":
			board.change(tab, pl.x,pl.y)
			pl.left(dist)
			tab[pl.x][pl.y]=pl.nu
		elif move=="r":
			board.change(tab, pl.x,pl.y)
			pl.right(dist)
			tab[pl.x][pl.y]=pl.nu
	board.printBoard(tab)
	i=i+1
