import codecs, re, csv, locale


def words_from_line(line):
        words=re.split('[\W\d]+',line)
        return [w.lower() for w in words if w]


file="wiki.txt"
dictionary={}

with open(file, 'r', encoding="utf-8") as txtfile:
        for line in txtfile:
                words=words_from_line(line)
                for word in words:
                       revword=word[::-1]
                       if word not in dictionary:
                              dictionary[revword]=word

for word in sorted(dictionary, key=locale.strxfrm):# key=dictionary.get):
        print('%35s %s'%(dictionary[word], word))


