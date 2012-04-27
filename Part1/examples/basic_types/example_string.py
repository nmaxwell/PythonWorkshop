#strings

print 'Spam' #print some spam
spam = 'Spam Spam Spam' #assign some spam

spam2 = spam + ' ' + spam #concatenate some spam
print spam2 

print spam[0] #first character of spam
print spam[:2] #first two characters of spam
print spam[-2:] #last two characteres of spam
print spam[::-1] #spam in reverse
print spam[::2] #every other character

whitespace = "  foo"
print whitespace
print whitespace.strip() #removed leading and trailing whitespace

print len("i am a string") # returns the length of the string