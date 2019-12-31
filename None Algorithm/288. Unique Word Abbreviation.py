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


规则解读:
• 假如apple 没在字典中出现过，a3e这个缩写也没出现过
unique (要查找的词在词典中没有出现过)
• 假如 cake 在字典中出现了2次 并且缩写中所有的c2e都是对应cake
unique (要查找的词在词典中出现过，但缩写只对应要查找的词)


思路:
两种情况合并在一起，总结起来的规律就是:
– 单词在字典中出现次数等于对应缩写在字典中出现次数 -> unique
– 单词在字典中出现次数不等于对应缩写在字典中出现次数 -> not unique

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
        #return self.count_abbr.get(abbr) == self.count_dict.get(word)
        #不能直接写self.count_abbr[abbr] == self.count_dict[word];因为self.count_abbr可能不存在key为abbr的值,word同理
        #这句话可以翻译为:
        if abbr not in self.count_abbr:
            return True
        if word not in self.count_dict:
            return False
        return self.count_abbr[abbr] == self.count_dict[word]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
