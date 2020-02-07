A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
 

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
 

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
 

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3


code:
import string
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        
        if end not in bank:
            return -1
            
        bank.add(start)
        
        queue = collections.deque([start])
        count = 0
        visited = set([start])
        
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                
                for i in range(len(word)):
                    left, right = word[:i], word[i+1:]
                    
                    for c in string.ascii_uppercase:
                        if c == word[i]:
                            continue
                        
                        new_word = left + c + right
                        
                        #这里要想清楚,要+1
                        if new_word == end:
                            return count + 1
                        
                        if new_word not in visited and new_word in bank:
                            visited.add(new_word)
                            queue.append(new_word)
                            
            #因为数的是边数,因此count要放在for循环的后面
            count += 1
        
        return -1
        
        
        
