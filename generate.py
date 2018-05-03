from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)
Bootstrap(app)

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
	sentence = bool(request.args.get('sentence'))

	password1 = createPass(minLen, maxLen, minWord, maxWord, numSub, sentence)
	password2 = createPass(minLen, maxLen, minWord, maxWord, numSub, sentence)	
	password3 = createPass(minLen, maxLen, minWord, maxWord, numSub, sentence)

	return render_template('passwords.html', password1=password1, password2=password2, password3=password3)

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

def getAdj():
	adjFile = open('adjectives.txt', 'r')
	adjList = adjFile.readlines()
	
	for item in adjList:
		index = adjList.index(item)
		adjList[index] = item.strip('\n')	
	
	adjDict = {}
	for word in adjList:
		adjDict.setdefault(len(word), []).append(word)
	return adjDict
	
def getNoun():
	nounFile = open('nouns.txt', 'r')
	nounList = nounFile.readlines()
	
	for item in nounList:
		index = nounList.index(item)
		nounList[index] = item.strip('\n')	
	
	nounDict = {}
	for word in nounList:
		nounDict.setdefault(len(word), []).append(word)	
	return nounDict
	
def getVerb():	
	verbFile = open('verbs.txt', 'r')
	verbList = verbFile.readlines()
	
	for item in verbList:
		index = verbList.index(item)
		verbList[index] = item.strip('\n')	
	
	verbDict = {}
	for word in verbList:
		verbDict.setdefault(len(word), []).append(word)
	return verbDict

def getAdverb():	
	adverbFile = open('adverbs.txt', 'r')
	adverbList = adverbFile.readlines()
	
	for item in adverbList:
		index = adverbList.index(item)
		adverbList[index] = item.strip('\n')	
	
	adverbDict = {}
	for word in adverbList:
		adverbDict.setdefault(len(word), []).append(word)
	return adverbDict

def createPass(minLen, maxLen, minWord, maxWord, numSub, sentence):
	password = ""

	if sentence is True:
		adjDict = getAdj()
		nounDict = getNoun()
		verbDict = getVerb()
		adverbDict = getAdverb()
		
		password += random.choice(adjDict[minWord+1])
		password += random.choice(nounDict[minWord])
		password += random.choice(verbDict[minWord+1])
		password += random.choice(adverbDict[maxWord])

	else:
		lenDict = getWords()
		
		minWordList = lenDict[minWord]
		midWordList = lenDict[minWord+1]
		maxWordList = lenDict[maxWord]
		
		password += random.choice(minWordList)
		password += random.choice(maxWordList)
		password += random.choice(midWordList)
		password += random.choice(minWordList)

	if numSub is True:
		password = numberSubstitution(password)

	if len(password) > maxLen or len(password) < minLen:
		return("Alter your word length values to get your specified password length.")
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
