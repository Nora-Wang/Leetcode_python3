Implement a load balancer for web servers. It provide the following functionality:

Add a new server to the cluster => add(server_id).
Remove a bad server from the cluster => remove(server_id).
Pick a server in the cluster randomly with equal probability => pick().
At beginning, the cluster is empty. When pick() is called you need to randomly return a server_id in the cluster.

Example

Example 1:

Input:
  add(1)
  add(2)
  add(3)
  pick()
  pick()
  pick()
  pick()
  remove(1)
  pick()
  pick()
  pick()
Output:
  1
  2
  1
  3
  2
  3
  3
Explanation: The return value of pick() is random, it can be either 2 3 3 1 3 2 2 or other.


code:
高频班version:直接用set
class LoadBalancer:
    def __init__(self):
        self.cluster = set()

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        self.cluster.add(server_id)
        return

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id in self.cluster:
            self.cluster.remove(server_id)
        return

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        import random
        
        #Version 1:
        return random.choice(list(self.cluster))
        
        #Version 2
        #注意,由于self.cluster是set,最后youge[0]转换一下,因为原方程是random.sample(list,k
        #random.sample(序列a，n):从序列a(str/list/set)中随机抽取n个元素，并将n个元素生以list形式返回
        #random.sample(序列a，n)[0]返回生成的随机数列表中的第一个值
        return random.sample(self.cluster,1)[0]

      
      
follow up:如何在不使用set的情况下用O(1)的时间实现？

算法班Version:参考380,使用list+dict的方式,能在不用set的前提下实现O(1)
import random
class LoadBalancer:
    def __init__(self):
        self.data = []
        self.record = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        if server_id in self.record:
            return
        
        self.data.append(server_id)
        self.record[server_id] = len(self.data) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id not in self.record:
            return
        
        index = self.record[server_id]
        last = self.data[-1]
        
        self.data[index] = last
        self.record[last] = index
        
        self.data.pop()
        del self.record[server_id]

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        return self.data[random.randint(0, len(self.data) - 1)]
