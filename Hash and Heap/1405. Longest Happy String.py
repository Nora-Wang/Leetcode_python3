A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0


# utilize max heap (-freq, char)
# if current char is the same as the last 2 in result string, then add the second max frequency char into result string
# time O(n), space O(n)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # O(n)
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(heap)
        
        res = []
        
        while heap:
            highest_freq, highest_char = heapq.heappop(heap)
            freq, char = highest_freq, highest_char

            # find the second max frequency char
            if len(res) >= 2 and res[-1] == res[-2] == char:
                freq, char = heapq.heappop(heap)
                # remomber add the max freq char back to heap
                heapq.heappush(heap, (highest_freq, highest_char))

            # it means cannot find a suitable char now(avoid duplicating char above)
            if freq == 0:
                break
            
            res.append(char)
            heapq.heappush(heap, (freq + 1, char))
        
        return ''.join(res)


# time O(nlogn), space O(n)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # time complexity for heap generation is O(nlogn)
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        res = []
        
        while heap:
            highest_freq, highest_char = heapq.heappop(heap)
            freq, char = highest_freq, highest_char
            
            if len(res) >= 2 and res[-1] == res[-2] == char:
                # because when we generate heap, there has a limitation: the frequency must larger than 0, 
                # which means the heap may be empty after pop max freq char.
                # So we need to add the limitaion in there
                # Sample input: (0,0,2)
                if not heap:
                    break
                freq, char = heapq.heappop(heap)
                heapq.heappush(heap, (highest_freq, highest_char))
            
            if freq == 0:
                break
            
            res.append(char)
            heapq.heappush(heap, (freq + 1, char))
        
        return ''.join(res)
