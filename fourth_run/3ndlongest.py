from unittest import TestCase


class L:

    def lengthOfLongest(self,s:str)->int:
        #lets use a string to store a repetition free substring
        #use a for loop, iterating throught the characters of the input string
        #"abcabcbb"
        max=0
        window= ""
        for character in s:
            #keep the window repetition free
            #check whether a repetition would occur, before adding the character, keeping the window repetition free
            if(self.hasRepetition(window+character)):
                #our goal is to let the execution proceed to the else statement
                #the window will grow to "abc" the current character to be added is "a"
                # shrink the window to "bc" before appending "a"
                window=window[window.index(character)+1:]
            else:
                window+=character
                #everytime a character gets added try and replace max
                max= max(len(window),max)
        return max
    
    def hasRepetition(self,s:str)->bool:
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    return True
        return False

class TestStuff(TestCase):

    def testIt(self):
        s = "abcabcbb"
        res = L().lengthOfLongest(s)