All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]


思路:
用DNA作为hash的key,用DNA出现的次数作为value,当value值大于等于2时,将DNA加入result


code:
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """     
        dict_s = {}
        for i in range(len(s) - 10 + 1):
            DNA = s[i:i + 10]
            dict_s[DNA] = dict_s.get(DNA, 0) + 1
            
        result = []
        for DNA in dict_s:
            if dict_s[DNA] >= 2:
                result.append(DNA)
                
        return result
