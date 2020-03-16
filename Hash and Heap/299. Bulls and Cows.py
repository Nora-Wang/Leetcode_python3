You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.


code:
#03/16/2020 100%
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_s = collections.Counter(secret)
        count_g = collections.Counter(guess)
        
        all_same_c = 0
        for c in count_s:
            if c in count_g:
                all_same_c += min(count_s[c], count_g[c])
        
        same_index_c = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                same_index_c += 1
        
        return str(same_index_c) + 'A' + str(all_same_c - same_index_c) + 'B'
    
    
    
    
    
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_A = 0
        count_B = 0
        
        #check how many A
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                count_A += 1
        
        hash_A = collections.Counter(secret)
        hash_B = collections.Counter(guess)
        
        #count how many same num
        for num in hash_A:
            if num in hash_B:
                count_B += min(hash_B[num], hash_A[num])
        
        #count_B includes A's cases
        count_B -= count_A
        
        return str(count_A) + 'A' + str(count_B) + 'B'
