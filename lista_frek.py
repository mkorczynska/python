import codecs, re, csv


def words_from_line(line):
	words=re.split('[\W\d]+',line)
	return [w.lower() for w in words if w]


file="txt.txt"
dictionary={}

with open(file, 'r', encoding="utf-8") as txtfile:
	for line in txtfile:
		words=words_from_line(line)
		for word in words:
			try:
				dictionary[word]
			except:
				dictionary[word]=0
			finally:
				dictionary[word]+=1


for word in sorted(dictionary, key=dictionary.get, reverse=True):
	print('%s %d'%(word, dictionary[word]))


with open("output.csv", 'w') as csvfile:
	fieldnames=["word", "num"]
	writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for word in sorted(dictionary, key=dictionary.get, reverse=True):
		writer.writerow({"word":word, "num":dictionary[word]})
