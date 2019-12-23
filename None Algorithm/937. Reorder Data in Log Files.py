You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

#要求
1. Reorder the logs so that all of the letter-logs come before any digit-log.  
2. The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
3. The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.


同lintcode 1380. Log Sorting
思路：
怎么样进行多关键字排序?
– 任何两个元素之间一定有个大小关系

code:
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        #先将logs分为字母和数字两种,因为在要求3中数字的直接按照放入顺序输出即可
        letter_logs, digit_logs = [], []
        
        for log in logs:
            #str.split(' ', 1 ); # 以空格为分隔符，分隔成两个
            log_id, log_content = log.split(' ', 1)
            
            #这里需要比较的是log_content[0],因为在log_content中还有空格,不能直接用isdigit
            if log_content[0].isdigit():
                digit_logs.append(log)
            else:
            #这里是将log_id和log_content以元组(不可变的list)的方式分开放入letter_logs,因为要求2中需要单独使用log_id和log_content
                letter_logs.append((log_id, log_content))
                
        result = []
        #sort函数具体参考56题
        letter_logs.sort(key = lambda x: (x[1], x[0]))
        
        #将letter_logs加入result中,注意写法
        for log_id, log_content in letter_logs:
            result.append(log_id + ' ' + log_content)
        
        #两个list组合直接用+
        result += digit_logs
        
        return result
