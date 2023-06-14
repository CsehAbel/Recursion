class LongestSubstringWithoutRepetition:
    def __init__(self, string):
        self.string = string
        self.longest = 0
        self.longest_substring = ''
        self.current = ''
        self.current_longest = 0

    #LeetCode #3
    #Given a string, find the length of the longest substring without repeating characters.
    #Example 1:
    #Input: "abcabcbb"
    #Output: 3
    #Explanation: The answer is "abc", with the length of 3.
    #Example 2:
    #Input: "bbbbb"
    #Output: 1
    #Explanation: The answer is "b", with the length of 1.
    #Example 3:
    #Input: "pwwkew"
    #Output: 3
    #Explanation: The answer is "wke", with the length of 3.
    #             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    def longest_substring_without_repetition(self):
        for char in self.string:
            if char not in self.current:
                self.current += char
                self.current_longest += 1
                if self.current_longest > self.longest:
                    self.longest = self.current_longest
                    self.longest_substring = self.current
            else:
                self.current = self.current[self.current.index(char) + 1:] + char
                self.current_longest = len(self.current)
        return self.longest_substring

class LongestSubstringWithoutRepetition:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge case
        if len(s) == 1:
            return 1

        # Initialize variables
        longest = 0
        current = 0
        seen = {}

        # Iterate through the string
        for index, char in enumerate(s):
            # If we haven't seen the character, add it to the dict
            if char not in seen:
                seen[char] = index
                current += 1
            # If we have seen the character, update the longest and current
            else:
                if current > longest:
                    longest = current
                current = 0
                seen = {}

        return longest


    #LeetCode #3
    #Given a string, find the length of the longest substring without repeating characters.
    #Example 1:
    #Input: "abcabcbb"
    #Output: 3
    #Explanation: The answer is "abc", with the length of 3.
    #Example 2:
    #Input: "bbbbb"
    #Output: 1
    #Explanation: The answer is "b", with the length of 1.
    #Example 3:
    #Input: "pwwkew"
    #Output: 3
    #Explanation: The answer is "wke", with the length of 3.
    #             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
class LongestSubstringWithoutRepetition:

    def lengthOfLongest(self,s:str)->int:
        #lets use a string to store a repetition free substring
        #use a for loop, iterating throught the characters of the input string
        #"abcabcbb"
        window= ""
        longestSubstrings=[]
        maxLength=0
        comingFromElse=False
        right=0
        while(right<len(s)):
            #keep the window repetition free
            #check whether a repetition would occur, before adding the character, keeping the window repetition free
            character=s[right]
            if(self.hasRepetition(window+character)):
                #our goal is to let the execution proceed to the else statement
                #the window will grow to "abc" the current character to be added is "a"
                # shrink the window to "bc" before appending "a"
                if(comingFromElse):
                    #here inside the if statements body
                    longestSubstrings.append(window)
                window=window[window.index(character)+1:]
                #in case of window="bc" character="a" 
                #bc+=a wont be inserted to longestSubstrings list, we should let "a" to be added in the else: 's body, so that
                #comingFromElse will be set to True and bca will triggered to be added to longestSubstrings list
                #by postponing executing window+=character, we would lose track of character in the next iteration
                #so we should control by explicitly incrementing a pointer when we want to advance the character that is to be #added in the next iteration, the character that is the next in the input string
                #for example by right+=1
                comingFromElse=False
            else:
                window+=character
                #everytime a character gets added try and replace max
                maxLength= max(len(window),maxLength)
                comingFromElse=True
                right+=1
        return maxLength,longestSubstrings
    
    def hasRepetition(self,s):
        #take the first character, compare every other character to it
        #avoid comparing it to itself, it would result in the result of the method indicating repetition, 
        #even though there isnt any
        #take the second character, ....
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if(s[i]==s[j]):
                    return True
        return False

if __name__=="__main__":
    maxLenght,list=LongestSubstringWithoutRepetition().lengthOfLongest("abcabcbb")
    print("results collected")