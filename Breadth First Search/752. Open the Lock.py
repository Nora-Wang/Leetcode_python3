You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1
Note:

The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.



套BFS模板
难点就是如何滚动wheel

对于每个node,即当前lock的四位数,每一位数可以有两种变化(往上滚,往下滚),这样一共就有8种变化;而当变化的结果为deadend时,则停止这一条线,否则继续滚动

code:
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if not deadends or not deadends[0]:
            return -1
        
        #一定要设为set,否则会超时
        deadends = set(deadends)
        visited = set()
        queue = collections.deque(['0000'])
        #将起始点放进visited,避免重复
        visited.add('0000')
        step = 0
        
        while queue:
            for _ in range(len(queue)):
                num = queue.popleft()
                if num == target:
                    return step
                    
                #当为deadend时,直接停止当前的滚动
                if num in deadends:
                    continue
                
                #对于lock的四位数
                for i in range(4):
                    #这里要int一下,因为后续会直接用来进行计算,原始的str不能用
                    left, curt, right = num[:i], int(num[i]), num[i+1:]
                    #每一位数能有两个next值可取
                    #这里就是数学知识:对当前数字进行转动,可以+1或者-1,然后取其个位(如果转到10，则取0)
                    #(0 - 1) % 10 = 9 = (-1) % 10 = -1 - (-1 // 10) * 10 = -1 - (-1)* 10 = -1 + 10 = 9
                    #//是向下取整
                    for change_num in [(curt + 1) % 10, (curt - 1) % 10]:
                        #change_num是int,需要转换一下
                        new_num = left + str(change_num) + right
                        if new_num in visited:
                            continue
                        queue.append(new_num)
                        visited.add(new_num)
                        
            #因为题目中第一个数0000不被算在内,因此step要放在后面,这样相当于确定能有下一个lock的时候再+1,即第二个lock为1
            step += 1
            
        return -1
