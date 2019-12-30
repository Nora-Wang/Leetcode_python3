Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:

Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.


题意:
abbr的规则是保留头尾字符,中间缩写为数字
最终得到的缩写不能映射到多个原始单词,即abbr的结果不能重复
如果缩写不会使单词更短，则不进行缩写，保持原样

思路:
做一个和dict对应的abbreviate的数组。也就是说dict[i] => result[i] 对应。 然后用一个哈希abbr_record纪录一下result[i]出现的次数
遇到多次的缩写，那就更新这个缩写，并更新哈希表
更新的方式:用count记录第几次循环,通过一个不停增加保留前面字母个数的函数实现

eg:
          like god internal me internet interval intension face intrusion
round 1   l2e  god i6l      me i6t      i6l      i7n       f2e  i7n 
round 2            in5l                 in5l     in6n           in6n
round 3            int4l                int4l    int5n          int5n
round 4            inte3l               inte3l   inte4n         intr4n
round 5            inter2l              inter2l
round 6            internal             interval

result    l2e god internal  me i6t      interval inte4n    f2e  intr4n



class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        #以后尽量用not dict
        if not dict:
            return []
           
        #list需要提前定义长度
        result = [''] * len(dict)
        abbr_record = {}
        count = 1
        
        #round 1
        for i in range(len(dict)):
            #注意带入get_abbr函数的应该是dict[i],即原本的word
            result[i] = self.get_abbr(dict[i], count)
            
            #后面的3句话可以简化为一句
            #abbr_record[result[i]] = abbr_record.get(result[i], 0) + 1
            if result[i] not in abbr_record:
                abbr_record[result[i]] = 0
            abbr_record[result[i]] += 1
        
        #Further rounds
        while True:
            #unique用于记录目前是否所有的dict对应的result的出现次数均为1;若不是,则继续循环
            unique = True
            count += 1
            
            for i in range(len(result)):
                if abbr_record[result[i]] > 1:
                    #注意带入get_abbr函数的应该是dict[i],即原本的word
                    result[i] = self.get_abbr(dict[i], count)
                    
                    #下面3句话简化为1句
                    #abbr_record[result[i]] = abbr_record.get(result[i], 0) + 1
                    if result[i] not in abbr_record:
                        abbr_record[result[i]] = 0
                    abbr_record[result[i]] += 1
                    
                    #由于存在次数大于1的情况,则不满足所有dict的word的abbr结果都是unique的条件,因此需要继续循环
                    unique = False
            
            #当所有的abbr都是unique的,则直接退出循环,return结果
            if unique == True:
                break
        
        return result
    
    #得到当前word的abbr结果
    #注意逻辑(看eg,当word的长度<=round + 2时,则直接返回改word)
    def get_abbr(self, word, count):
        if len(word) <= count + 2:
            return word
        
        #注意结果为str
        return word[:count] + str(len(word) - count - 1) + word[-1]
