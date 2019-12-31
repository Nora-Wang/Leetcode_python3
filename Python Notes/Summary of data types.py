Python 中有六个标准的数据类型：Number（数字）, String（字符串）, List（列表）, Tuple（元组）, Set（集合）, Dictionary（字典）
Python 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

#dict和set查找/添加/删除key,时间复杂度为O(1)
#list,tuple,queue,stack查找/删除item,时间复杂度为O(n);tuple = ()为不可变的list
***********************
dict:
1.删除key:
del dict[key]

2.添加key和value:
dict[key] = dict.get(key, value)
eg:dict[key] = dict.get(key, 0) 或者 dict[item] = dict.get(key, set([word]))


***********************
set 没有value的dict:
1.删除:
set.remove(key)

2.添加:
set.add(key)

3.注意set的初始化:
item = 'ab'
set([item])结果为set('ab')
set(item)结果为set('a','b')

***********************
list:
1.删除:
list.remove(item)

2.添加:
list.append(item)

***********************
###queue和stack本质上是list
queue(先进先出):
1.初始化:
#一般使用双端队列deque
queue = collections.deque([])因为deque这个函数所要调用的数据类型规定为list
eg:一个数时,queue = collections.deque([root]); 一个点时,queue = collections.deque([(x,y)]),要有括号

#popleft+append可以使queue从头(左)出,从尾(右)进
2.删除:
item = queue.popleft()
用popleft是因为这样才是用头开始pop的,才满足queue的先进先出;若queue.pop(),则是从尾pop
3.添加:
queue.append(item)
用append是这样是从右端,即尾部开始加入item,满足queue的特性

4.count计数:
queue.count('a')计出queue中有多少个'a'

5.反转
queue.reverse()

***********************
stack(先进后出):
1.初始化
stack = []

2.删除
stack.pop()

3.添加
stack.append(item)

4.栈顶
stack[-1]
