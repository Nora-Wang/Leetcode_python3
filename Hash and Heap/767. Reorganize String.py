Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.



Solution 1:
Utilize Map and sorted array with odd-even feature to resolve.
1. generate a Map {char:count}
2. get a sorted char list, sorted with freq, from large to small
3. if the most freq char's freq is larger than the half of the string length, return ""
4. inject the chars start from even index, after all even index injected, then back to odd index to start secound round inject

Time: O(nlogn)
Space: O(n)
class Solution:
    def reorganizeString(self, s: str) -> str:
        countMap = collections.Counter(s)
        charList = sorted(countMap.keys(), key = lambda x:countMap[x], reverse = True)
        
        if countMap[charList[0]] > (len(s) + 1) // 2:
            return ""
        
        index = 0
        res = [None] * len(s)
        
        for char in charList:
            for _ in range(countMap[char]):
                if index >= len(s):
                    index = 1
                
                res[index] = char
                index += 2
        
        return "".join(res)



Solution 2
Utilize priority queue / heap to resolve
1. create a max heap {[-freq, char]}
2. use prev to record the latest pop value, which could help to avoid duplication
    1. if heap is empty but still has prev, it means we need to add the same char now -> return ""
    2. after we pop a new char, append the char to res, and refresh the freq data
    3. push the prev back to heap, because, the next time, the duplicate situation will not exist, and reset the prev to None, because before setting the prev, we need to validate the freq data
    4. if the freq data is still smaller than 0, it means we still have char not used, we could set prev = [freq, char] to avoid duplication.

Time: O(nlogn)
Space: O(n)
class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = collections.Counter(list(s))
        maxHeap = sorted([-freq, char] for char, freq in freqMap.items())
        heapq.heapify(maxHeap)
        
        res = []
        prev = None
        
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            
            freq, char = heapq.heappop(maxHeap)
            res.append(char)
            freq += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if freq != 0:
                prev = [freq, char]
                
        return "".join(res)


