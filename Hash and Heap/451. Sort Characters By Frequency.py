Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


# hash + sort
# time: O(nlogn), space: O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ''
        
        count = collections.Counter(s)
        sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
        
        res = []
        for c, num in sorted_count:
            for _ in range(num):
                res.append(c)
        
        return ''.join(res))


# stack + heap
# time: O(n), space: O(n)
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ''
        
        count = collections.Counter(s)
        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)
        
        res = []
        while heap:
            count, c = heapq.heappop(heap)
            for _ in range(-count):
                res.append(c)
        
        return ''.join(res)
            
