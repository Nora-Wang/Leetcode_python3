  题目：
  Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, 
  write a function to compute the researcher's h-index.

  According to the definition of h-index on Wikipedia: 
  "A scientist has index h if h of his/her N papers have at least h citations each, 
  and the other N − h papers have no more than h citations each."


思路：
理解题意if h of his/her N papers have at least h citations each，有h篇paper都至少有h个citations
h = len(citations) - mid  (有h篇paper)
citations[mid] >= h       (因为sorted in ascending order，最小值citations[mid]至少有h个citations，后面的都会满足)

code:

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if(len(citations) == 0):
            return 0
        start = 0
        end = len(citations) - 1
        while(start < end):
            mid = start + (end - start) / 2
            h = len(citations) - mid
            if(citations[mid] >= h):
                end = mid
            else:
                start = mid + 1
        #if特判没懂？？？？？？？
        #解释：避免全0数组或全7数组之类的情况
        if(len(citations) - start <= citations[start]):
            return len(citations) - start
        return 0
            

                
