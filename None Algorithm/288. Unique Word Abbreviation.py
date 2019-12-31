An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true


code:
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.count_abbr, self.count_dict = {}, {}
        for word in dictionary:
            abbr = self.get_abbr(word)
            self.count_abbr[abbr] = self.count_abbr.get(abbr, 0) + 1
            self.count_dict[word] = self.count_dict.get(word, 0) + 1
    
    def get_abbr(self, word):
        if len(word) > 2:
            return word[0] + str(len(word) - 2) + word[-1]
        return word

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.get_abbr(word)
        return self.count_abbr.get(abbr) == self.count_dict.get(word)


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
