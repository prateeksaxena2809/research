from extract_meaning_from_shabdasagar import extract_meaning
from Levenshtein import distance
from nltk.tokenize import word_tokenize


def extract_suffix(word,meaning):
	tokens=word_tokenize(meaning)
	close_words=[token for token in tokens if (distance(word,token)/len(word))<=0.5]
	return close_words



if __name__ == '__main__':
	suffix_list=[]
	words=[word.strip() for word in open('hindi_word_list.txt').readlines()]
	for word in words:
		meanings=extract_meaning(word)
		for meaning in meanings:
			candidates=extract_suffix(word,meaning)
			print(word,candidates)
