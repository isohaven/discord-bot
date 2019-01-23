import imp
import nltk
from nltk.corpus import cmudict
import nltk

is_digit = lambda s: s.replace('.','',1).isdigit()

d = cmudict.dict()
# input should not have puntuation etc
# s.translate(None, string.punctuation)
def nsyl(word):
	num = 0
	try:
		num = [len(list(y for y in x if is_digit(y[-1]))) for x in d[word.lower()]]
	except Exception as e:
		print('fail')
		# word not in dict
	return num
print(nsyl('Zoe'))