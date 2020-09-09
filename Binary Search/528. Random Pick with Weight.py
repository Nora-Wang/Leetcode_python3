You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).

 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.



'''
method 1:
1. create an array with index * the number of weight
eg: [1,3,1] -> [0, 1,1,1, 2]
2. random create a index in range 0 ~ len(array) - 1
3. return array[index]
this method will spend a lot of time and space in creating the array, but only O(1) time to execute the function self.pickIndex()

method 2:
1. create an array with the prefix_sum
eg: [1,3,1] -> [1,4,5]
2. random create a num in range [array[0], array[-1] + 1] 
3. find the closest array[index] with num 
4. return index

step 3:
1. brute force: find the array[index] linearly
2. optimization: use binary search
'''

# method 2 + binary search
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.w[-1])
        
        start, end = 0, len(self.w) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if self.w[mid] == target:
                return mid
            
            if self.w[mid] < target:
                start = mid
            else:
                end = mid
        
        # 这个return在做题的时候卡了一下
        return start if self.w[start] >= target else end


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
