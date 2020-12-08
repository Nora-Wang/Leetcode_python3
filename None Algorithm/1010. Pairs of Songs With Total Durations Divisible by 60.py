You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500


# 根据模进行配对
# 注意模为0 or 30的情况，其count应用求和公式for range [1,c]
# 为了标记是否已经被算入结果：只要被计算，则将其count归零
# time: O(n), space: O(n)
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return 0
        
        # {model:count of time with model}
        model = collections.defaultdict(int)
        for t in time:
            model[t % 60] += 1
            
        count = 0
        for m,c in model.items():
            if m == 0 or m == 30:
                count += (1 + c - 1) * (c - 1) // 2
                model[m] = 0
                
            elif (60 - m) in model:
                count += c * model[60 - m]
                model[m] = 0
                model[60 - m] = 0
                
        
        return count
        
        
