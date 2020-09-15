# Data Structure
1. Array物理连续town house
2. Stack逻辑概念可用别的物理概念来实现，先进后出
3. Queue逻辑概念，先进先出
4. Linked List利用物理地址
5. Tree
6. Heap
7. Graph
8. Hash Table

# Abstract Data Types

********************************************************************************************
#dict和set中的key都是不可重复的,与list的index对应;但list中包含的值,以及dict的value都是可以重复的
dict:
#1,2,3都是O(1)
1.删除key:
del dict[key]

2.添加key和value:
dict[key] = dict.get(key, value)
eg:dict[key] = dict.get(key, 0) 或者 dict[item] = dict.get(key, set([word]))
dict[key] = dict.get(key, 0) + 1
#若value为list
dict = collections.defaultdict(list)
dict[key].append(value)

3.取值
dict.keys()
dict.values()

4.排序
#注意排序后的返回值是一个list
key:sorted(dict.items(), key = lambda item:item[0])
value:sorted(dict.items(), key = lambda item:item[1])
sorted函数的结构:sorted(iterable, cmp=None, key=None, reverse=False);具体可参考functions文档
  
5.统计频率
dict = collections.Counter(key的集合)
dict中value为每个key出现的次数


********************************************************************************************
# set里的数据不能是list
set 没有value的dict:
1.删除:
set.remove(key)

2.添加:
set.add(key)

3.注意set的初始化:
item = 'ab'
set([item])结果为set('ab')
set(item)结果为set('a','b')

set([(i,j)])结果为set((i,j))

********************************************************************************************
#两个list相加,相当于重建一个新list;可用extend来省空间
#同一list中数据类型都是一样的
#对list中的值进行重新赋值时,一定要用nums[index]的形式,不能直接num = item,这样无法成功赋值

list:
1.删除:
#O(n)
list.remove(item)item是list中所包含的值
del list[index]
#O(1)
item = list.pop() pop出list中的最后一个值
#deque为O(1),普通为O(n)
item = list.pop(0) pop出list中的第一个值

2.添加:
list.append(item) #O(1)
list1 + list2 = list1.extend(list2) extend直接在list1的基础上改变,不会新建一个list
list.inset(index, item) #time:O(n). insert不会产生新list，但效率低

3.查找index:
list.index(x[, start[, end]]),x为可查找对象;该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。

4.创建一个长度为n的list
list = [None for _ in range(n)]



********************************************************************************************
###queue和stack本质上是list
queue(先进先出):
1.初始化:
#一般使用双端队列deque
queue = collections.deque()因为deque这个函数所要调用的数据类型规定为list
eg:一个数时,queue = collections.deque([root]); 一个点时,queue = collections.deque([(x,y)])
当加入的数据不是list时,要另写括号;但若直接初始化,则直接写deque()即可,不要用deque([]),这样生成的queue会多出一个[]

#popleft+append可以使queue从头(左)出,从尾(右)进
2.删除: dequeue from the front
item = queue.popleft()
用popleft是因为这样才是用头开始pop的,才满足queue的先进先出;若queue.pop(),则是从尾pop
3.添加: enqueue from the back
queue.append(item)
用append是这样是从右端,即尾部开始加入item,满足queue的特性

4.count计数:
queue.count('a')计出queue中有多少个'a'

5.反转
queue.reverse()

6.队头是最左,删除操作
queue[0]
7.队尾是最右,插入操作
queue[-1]

********************************************************************************************
stack(先进后出):
1.初始化
stack = []

2.删除
stack.pop()

3.添加
stack.append(item)

4.栈顶是最右;入栈和出栈都在栈顶
stack[-1]
5.栈底是最左
stack[0]

********************************************************************************************
tuple不可更改,但可以进行连接组合
tup3 = tup1 + tup2

********************************************************************************************

dict和set查找/添加/删除key,时间复杂度为O(1)
list,tuple,queue,stack查找/删除item,时间复杂度为O(n);tuple = ()为不可变的list
