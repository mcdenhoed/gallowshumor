# coding: utf-8
import re, sys, readline, string
from collections import Counter
class Guesser():
	guessString = ""
	guessed = set()
	DICTIONARY = "/etc/dictionaries-common/words"
	length = 0
	result = set()
	def __init__(self):
		pass
		
	def search(self):
		result = set()
		dictionary_file = open(self.DICTIONARY, "r")
		for line in dictionary_file:
			if re.search(self.guessString, line):
				result.add(line.lower().strip()	)
		print "{0} words matching".format(len(result))
		self.result = result

	def alphabetSearch(self):
		megastring = ''.join(self.result)
		c = Counter(megastring)
		for l in self.guessed:
			del c[l]
		print c.most_common()

	def updateSet(self, wordinfo):
		self.guessString = ""
		nope = False
		guessed = set()
		for i in list(wordinfo):
			if i == '*':
				pass
			elif re.search("[a-z]", i) != None:
				guessed.add(i)
			else:
				print "Nice try"
				nope = True
				break
		if nope == False:
			self.guessed.update(guessed)

	def makeSearchString(self, wordinfo):
		guessString = "^"
		nope = False
		for i in list(wordinfo):
			if i == '*':
				guessString += "[^"
				for a in self.guessed:
					guessString += a
				guessString += "]"
			elif re.search("[a-z]", i) != None:
				guessString += i
			else:
				print "blah"
				nope = True
				break
		guessString += "$"
		print guessString
		if not nope:
			self.guessString = guessString

	def newGuess(self):
		newguess = raw_input("Your next guess: ").lower().strip()
		if newguess in string.lowercase:
			self.guessed.add(newguess)

	def run(self):
		while True:
			wordinfo = raw_input("Word please (* is wildcard): ").lower()
			self.updateSet(wordinfo)
			self.makeSearchString(wordinfo)
			self.search()
			self.alphabetSearch()
			self.newGuess()

if __name__ == "__main__":
	g = Guesser()
	g.run()