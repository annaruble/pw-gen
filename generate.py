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

	password = createPass(minLen, maxLen, minWord, maxWord, numSub)

	return render_template('passwords.html', password=password)

# #################################################

def getWords():
	wordfile = open('words.dat', 'r')
	wordlist = wordfile.readlines()

	for item in wordlist:
		index = wordlist.index(item)
		wordlist[index] = item.strip('\n')

	lenDict = {}
	for word in wordlist:
		lenDict.setdefault(len(word), []).append(word)

	return lenDict

def createPass(minLen, maxLen, minWord, maxWord, numSub):
	lenDict = getWords()

	minWordList = lenDict[minWord]
	midWordList = lenDict[minWord+1]
	maxWordList = lenDict[maxWord]

	longword = ""
	longword += random.choice(minWordList)
	longword += random.choice(maxWordList)
	longword += random.choice(midWordList)
	longword += random.choice(minWordList)

	if numSub is True:
		password = numberSubstitution(longword)
	else: 
		password=longword

	if len(password) > maxLen:
		return("Refresh the page to get a password more suited to your requirements.")
	else:
		return password

def numberSubstitution(password):
	switch = {'e':'3', 'i':'1', 'a':'4', 'b':'8', 'q':'9', 'o':'0'}
	print(password)
	newpass = ""
	for ch in password:
		if ch in switch.keys():
			ch = ch.replace(ch, switch[ch])
		newpass += ch
	return newpass


if __name__ == '__main__':
	app.run(debug=True)
