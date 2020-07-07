A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.



#time: O(), space: O()
class Transaction:
    def __init__(self, t):
        self.name = t[0]
        self.time = int(t[1])
        self.amount = int(t[2])
        self.city = t[3]
        
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        
        #create trasactions
        transactions = [Transaction(s.split(',')) for s in transactions]
        
        #sort transactions by time
        transactions.sort(key=lambda t:t.time)
        
        #create a hash table to record the transactions by name
        #key = name, value = i(means the time)
        t_index = collections.defaultdict(list)
        for i, t in enumerate(transactions):
            t_index[t.name].append(i)
            
        res = []
        for name, indexs in t_index.items():
            left, right = 0, 0
            
            for i in indexs:
                t = transactions[i]
                
                if t.amount > 1000:
                    res.append(','.join([t.name, str(t.time), str(t.amount), t.city]))
                    continue
                
                #find out the time range, [t - 60, t + 60]
                #in this time range, if the city is different -> t is invalid
                while left < len(indexs) - 1 and transactions[indexs[left]].time < t.time - 60:
                    left += 1
                while right < len(indexs) and transactions[indexs[right]].time <= t.time + 60:
                    right += 1
                
                for index in range(left, right):
                    if transactions[indexs[index]].city != t.city:
                        res.append(','.join([t.name, str(t.time), str(t.amount), t.city]))
                        break
        
        return res
                    
        
        
        
        
        
        
