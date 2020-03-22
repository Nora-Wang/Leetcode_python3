
If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
 

Constraints:

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5



code:
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        self.res = 0
        for num in nums:
            self.get(num)
        
        return self.res
    
    def get(self, num):
        i = 2
        temp = [1, num]
        
        for i in range(2, num + 1):
            if i * i > num:
                break
                
            if num % i != 0:
                continue
            
            temp.append(i)
            if num // i != i:
                temp.append(num // i)
            
            if len(temp) > 4:
                return
        
        if len(temp) == 4:
            for num in temp:
                self.res += num 
        return
