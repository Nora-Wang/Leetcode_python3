Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


code:
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.father = {}
        
        #initial self.father
        #注意定义清楚self.father里数据的结构:self.father[被除数] = [除数, 结果]
        for i in range(len(equations)):
            a, b, a_d_b = equations[i][0], equations[i][1], values[i]
            self.union(a,b,a_d_b)
        
        result = []
        
        #对queries中的值一对一对的判断
        for x,y in queries:
            #若不在self.father中,则说明不存在关系,则直接输出-1.0
            if x not in self.father or y not in self.father:
                result.append(-1.0)
                continue
            
            #若在self.father中,判断其root节点是否相等
            root_x, x_d_root_x = self.find(x)
            root_y, y_d_root_y = self.find(y)
            
            #若相等,则说明x和y之间可以通过root节点相连接,即(x / root) * (y / root) = x / y
            if root_x == root_y:
                result.append(x_d_root_x / y_d_root_y)
            else:
                result.append(-1.0)
        
        return result
            
    
    def union(self, a, b, a_d_b):
        #self.father的初始化
        #[a] / a = 1
        if a not in self.father:
            self.father[a] = [a, 1]
        if b not in self.father:
            self.father[b] = [b, 1]
        
        #注意这里的意思是为a和b找到共同的root,证明存在a/root和b/root,这样就能得到a/b
        root_a, a_d_root_a = self.find(a)
        root_b, b_d_root_b = self.find(b)
        
        if root_a != root_b:
            #这里的结果为self.father[root_a] = [root_b, root_a_d_root_b]
            self.father[root_a] = [root_b, a_d_b * b_d_root_b / a_d_root_a]
            
    
    def find(self, point):
        #因为后期需要输出self.father[point],但point后续被改变,因此需要记录一下
        temp = point
        
        path = []#path用于压缩路径
        
        #比如 a->b->c->d
        prev = []#prev里就是 [a/b, b/c, c/d]
        curt = 1 #curt用于记录被压缩后的结果,即a->d, 就是prev里的相乘 a/b * b/c * c/d = a/d
        
        while self.father[point][0] != point:
            path.append(point)
            prev.append(self.father[point][1])
            curt *= self.father[point][1]
            point = self.father[point][0]
        
        for i in range(len(path)):
            self.father[path[i]][0] = point
            self.father[path[i]][1] = curt
            curt /= prev[i]
            
        return self.father[temp]
    
    
