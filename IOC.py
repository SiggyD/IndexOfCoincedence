#! /usr/bin/python
'''
Finds the IOC of plaintext and individual streams
'''
import sys, getopt, string, os

def getIOC( str,keyint ): # function that will write IOC of a string to line in file
	length = len(str)
	freqMult = 0.0
	for i in range (0,26):
		ccount = str.count(string.ascii_lowercase[i])
		freq = (ccount/float(length))
		freq2 = ((ccount - 1)/float(length - 1))
		freqMult += freq * freq2
	iocOut.write("%.4f, Keylength %d \n" %(freqMult,keyint)) 
	return

def getIOCDef( str ): #returns the IOC as a number
	length = len(str)
	freqMult = 0.0
	for i in range (0,26):
		ccount = str.count(string.ascii_lowercase[i])
		freq = (ccount/float(length))
		freq2 = ((ccount - 1)/float(length - 1))
		freqMult += freq * freq2
	#iocOut.write("%.4f\n" %freqMult) 
	return freqMult

print "*** Index of Coincidence *** "
if (len(sys.argv) < 2): # check args
	print "Usage: IOC.py <file>"
	exit()
inputFile = open(sys.argv[1],"r")
iocOut = open(sys.argv[1]+'_IOC.txt','w')

cipherText = inputFile.read()
cipherText = cipherText.lower()
inputFile.close()
cleanText = ""

print "Results show the IOC and the supposed keylength respectively"
print "############################################"
for i in range(0,len(cipherText)): #clean the ciphertext for processing
	if ((ord(cipherText[i]) > 96) & (ord(cipherText[i]) < 123)):
		cleanText += cipherText[i]
print "Clen len", len(cleanText)
print "Original IOC: ", getIOCDef(cleanText)
for i in range(1,51): # try different stream lengths
	getIOC(cleanText[0::i],i)
iocOut.close() 
os.system("cat "+sys.argv[1]+'_IOC.txt'+" | sort -nr")
