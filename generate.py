from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/processForm')
def collect():
	minLen = int(request.args.get('minLen'))
	maxLen = int(request.args.get('maxLen'))
	minWord = int(request.args.get('minWord'))
	maxWord = int(request.args.get('maxWord'))
	numSub = bool(request.args.get('numSub'))
	alternate = bool(request.args.get('alternate'))

	password = createPass(minLen, maxLen, minWord, maxWord, numSub, alternate)

	return render_template('passwords.html', password=password)

# #################################################

def getWords():
	wordfile = open('words.dat', 'r')
	wordlist = wordfile.readlines()
	for item in wordlist:
		index = wordlist.index(item)
		wordlist[index] = item.strip('\n')
	return wordlist

def getNewWord():
	wordlist = getWords()
	word = ""
	for i in range(4):
		word += random.choice(wordlist)
	return word

def createPass(minLen, maxLen, minWord, maxWord, numSub, alternate):
	word = getNewWord()
	if len(word) >= minLen and len(word) <= maxLen:
		print(len(word))
		return word
	else:
		getNewWord()

	return word
	# count how long each word is, make sure totalLen <= maxLen and totalLen >= minLen
	# make sure to use between specified number of words
	# concatenate this all together to generate a password


	#then do number replacement and alternate handss


if __name__ == '__main__':
	app.run(debug=True)