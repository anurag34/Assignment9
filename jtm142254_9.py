#!/usr/bin/python

import re
def main():
	a = []
	b = []
	lst = []
	count = 0
	Happy = 0
   	Sad = 0
        Sarcastic = 0
        Surprised = 0
        Crook = 0
        Neutral = 0
        Angry = 0
	i = 0
	emotions = {}
	dic = {}
	f = open("content.txt", "r")
	for line in f:
		words1 = line.split()
		a.append(words1)
		count = count + 1
		match = re.findall(r'[:;][)DPp]' ,line)
		match1 = re.findall(r"[:Bx=>O]['-_][<(/)oO]", line)
		lst = b + match
		print lst
	dic[':)'] = 'HAPPY'
	dic[':D'] = 'HAPPY'
	dic[':('] = 'SAD'
	dic[':\'('] = 'SAD'
	dic[':P'] = 'SARCASTIC'
	dic[';)'] = 'SARCASTIC'
	dic[':-o'] = 'SURPRISED'
	dic['O_O'] = 'SURPRISED'
	dic['B-)'] = 'CROOK'
	dic[';)'] = 'CROOK'
	dic[':-/'] = 'NEUTRAL'
	dic['=_='] = 'NEUTRAL'
	dic['x-('] = 'ANGRY'
	dic['>_<'] = 'ANGRY'
	
	f1 = open("content.txt", "r")
	for line in f1:
		words = line.split()
		if ":)" in words or ":D" in words:
         	 	  Happy = Happy + 1
       	        elif ":(" in words or ":'(" in words:
           		 Sad = Sad + 1
        	elif ":P" in words or ";)" in words:
          		  Sarcastic = Sarcastic + 1
      	        elif ":-o" in words or "O_O " in words:
            		Surprised = Surprised + 1
       	        elif "B-)" in words or ";)" in words:
           		 Crook = Crook + 1
                elif ":-/" in words or "=_=" in words:
           		 Neutral = Neutral + 1
                elif ">_<" in words or "x-(" in words:
           		 Angry = Angry + 1
       	        else:
                      print ""


	print " Number of time Happy emotions occur is :",Happy# print number of time emotions occurs
    	print " Number of time Sad emotions occur  is: ",Sad
    	print " Number of time Sarcastic emotions occur is: ",Sarcastic
    	print " Number of time Surprised emotions occuris: ",Surprised
    	print " Number of time Crook emotions occuris: ",Crook
    	print " Number of time Neutral emotions occur is: ",Neutral
    	print " Number of time Angry emotions occuris: ",Angry 
	total_emotions = Happy+Sad+Sarcastic+Surprised+Crook+Neutral+Angry#definetotal varaiavle which has total number of emotions
    	print "Total emotions is:",total_emotions
    	print " Happy_%  :",(Happy*100/total_emotions)# print % of time emotions occurs
    	print " Sad_% : ",(Sad*100/total_emotions)
    	print " Sarcastic_% : ",(Sarcastic*100/total_emotions)
    	print " Surprised_% : ",(Surprised*100/total_emotions)
    	print " Crook_% : ",(Crook*100/total_emotions)
    	print " Neutral_% : ",(Neutral*100/total_emotions)
    	print " Angry_% : ",(Angry*100/total_emotions)
	

	f.close()
	f1.close()
#	for x in a:
#		if (x not in emotions):
#			emotions[x] = " "
#	for k in dic.keys():
#		for x in range(0,16):
#			if lst[x] == k:
#				emotions[a[x]] = dic[x]
		







if __name__ == '__main__':
	main()

