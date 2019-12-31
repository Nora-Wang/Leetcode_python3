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

思路:这题直接用set就行.
难点就是如何随机选取数据:set无法实现,只能转list;调用random package,有两个方法random.sample,random.choice

code:
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
        #注意,由于self.cluster是set,最后youge[0]转换一下,因为原方程是random.sample(list,k);为啥,我也不懂....
        return random.sample(self.cluster,1)[0]
