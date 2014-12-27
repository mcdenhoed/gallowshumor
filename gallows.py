# coding: utf-8
import re, sys, readline

class Guesser():
	guessString = ""
	guessed = set()
	DICTIONARY = "/etc/dictionaries-common/words"
	length = 0
	def __init__(self):
		pass

	def search(self):
		dictionary_file = open(DICTIONARY, "r")
		for line in file:
			if re.search(sys.argv[1], line):
				result += line.lower()

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
		if not nope:
			self.guessString = guessString

	def run(self):
		while True:
			wordinfo = raw_input("Word please (* is wildcard): ").lower()
			self.updateSet(wordinfo)
			self.makeSearchString(wordinfo)
			self.search

if __name__ == "__main__":
	g = Guesser()
	g.run()