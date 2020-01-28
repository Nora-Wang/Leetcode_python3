Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].


code:
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        self.father = {}
        #初始化把所有的account中的email都指向自己
        self.initialize(accounts)
        
        #把每个account中的email都连起来（12连，23连，34连，45连） 
        for account in accounts:
            for i in range(1,len(account) - 1):
                self.union(account[i], account[i + 1])
                
                
        #设置email_set来存{email的根: 对应的子email} 
        #设置email_to_acct来存{email的根: 对应的姓名name} 
        email_set, email_to_id = self.get_id_to_email_set(accounts)
        
        #从email_set和email_to_acct中取结果 
        result = []
        for root_email in email_set:
            temp = [email_to_id[root_email]] + sorted(list(email_set[root_email]))
            result.append(temp)
            
        return result
    
    def get_id_to_email_set(self, accounts):
        email_set = {}
        email_to_id = {}
        
        for account in accounts:
            #对于每一个email都要找到其根，并且把email存入email_set对应的位置 
            for email in account[1:]:
                #这里不能用root_email = self.father[email],因为前面对email的union只是一个个的path(list)之间的union,
                #而path与path之间还没有union,因此必须重新用find,才能找出每个email的root
                root_email = self.find(email)
                
                #在email_to_id填入对应的名字
                email_to_id[root_email] = account[0]
                
                if root_email not in email_set:
                    email_set[root_email] = set()
                email_set[root_email].add(email)
        
        return email_set, email_to_id
    
        
    def initialize(self, accounts):
        for account in accounts:
            for email in account[1:]:
                self.father[email] = email
                
                
    def union(self, email_a, email_b):
        root_a = self.find(email_a)
        root_b = self.find(email_b)
        
        if root_a != root_b:
            self.father[root_a] = root_b
            
            
    def find(self, email):
        path = []
        
        while self.father[email] != email:
            path.append(email)
            email = self.father[email]
        
        for p in path:
            self.father[p] = email
        
        return email
