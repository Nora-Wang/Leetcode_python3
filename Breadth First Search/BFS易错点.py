易错点:

1.用了grid[new_x][new_y] = 1就不用设置self.visited了

2.有count/step/level就一定要有for _ in range(len_level),它们的初始值都设为0
如何判断应该放在while queue中的最上面还是最下面:如果需要的结果是node的个数,则是上面;如果需要的是边数(即变化次数),则是下面


3.注意题的source和destination是Point类型,使用的时候需要source.x,source.y

4.return的情况要紧跟pop后面




放在pop的后面:count level/return的情况
放在最后的:将neighbor放在visited和queue里
