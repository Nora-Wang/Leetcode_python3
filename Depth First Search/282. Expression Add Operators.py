Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []


油管讲解https://www.youtube.com/watch?v=AXNb-stFNb4
时间复杂度:O(4^(n-1))
空间复杂度:O(n)

code:
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        
        result = []
        
        self.dfs(num, target, '', 0, 0, 0, result)
        
        return result
    
    #temp:记录path;
    #index:记录每一次在num中循环的开始index;
    #sum:记录当前的和;
    #last_num:记录上一次的结果,便于乘法那的处理;
    def dfs(self, num, target, temp, index, sum, last_num, result):
        #出口:num都取完了 + sum == target
        if index == len(num):
            if sum == target:
                result.append(temp)
            return
        
        #拆解:所有num的组合 * 3个运算符
        for i in range(index, len(num)):
            #corner case:'06'不是数字;即数字长度大于1,并且以0开头的时候,break
            if i > index and num[index] == '0':
                break
            
            curt = int(num[index:i+1])
            
            #当是第一位时,不需要运算符
            if index == 0:
                self.dfs(num, target, str(curt), i + 1, curt, curt, result)
                continue
                
            self.dfs(num, target, temp + '+' + str(curt), i + 1, sum + curt, curt, result)
            self.dfs(num, target, temp + '-' + str(curt), i + 1, sum - curt, -curt, result)
            #乘法的时候,先把前一个数给剪掉,再用前一个数*curt
            self.dfs(num, target, temp + '*' + str(curt), i + 1, sum - last_num + last_num * curt, last_num * curt, result)
