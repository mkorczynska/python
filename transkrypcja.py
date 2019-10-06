import codecs, re, csv, locale


def words_from_line(line):
	words=re.split('[\W\d]+',line)
	return [w.lower() for w in words if w]


file=open("tekst.txt",'r')
dict={'a':'a',
'б':'b',
'в':'w',
'г':'g',
'д':'d',
'е':'je',
'ё':'jo',
'ж':'ż',
'з':'z',
'и':'i',
'й':'j',
'к':'k',
'л':'l',
'м':'m',
'н':'n',
'о':'o',
'п':'p',
'р':'r',
'с':'s',
'т':'t',
'у':'u',
'ф':'f',
'х':'ch',
'ц':'c',
'ч':'cz',
'ш':'sz',
'щ':'szcz',
'ъ':'',
'ы':'y',
'ь':'',
'э':'e',
'ю':'ju',
'я':'ja',
'!':'',
',':'',
'.':'',
'-':''}


tekstn=''
for line in file:
	words=words_from_line(line)
	linen=''
	for word in words:
		wn=''
		for l in word:
			ln=''
			if l in dict:
				ln+=dict[l]
			else:
				ln+=l
			wn+=ln
		linen+=wn+' '
	tekstn+=linen+'\n'
print(tekstn)
