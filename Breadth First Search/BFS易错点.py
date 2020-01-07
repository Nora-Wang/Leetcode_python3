易错点:

1.用了grid[new_x][new_y] = 1就不用设置self.visited了

2.有count/step/level就一定要有for _ in range(len_level),注意初始值的设置;并且一定要放在pop的后面
#注意将这里的count与word ladder区分一下;knight那道题的count初始值为0,因为这里需要的是path length;而word ladder需要的是word的个数

3.注意题的source和destination是Point类型,使用的时候需要source.x,source.y

4.return的情况要紧跟pop后面




放在pop的后面:count level/return的情况
放在最后的:将neighbor放在visited和queue里
