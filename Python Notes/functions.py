# 是否为数字
string.isdigit()
只接受0～9
'-1' -> 
# 是否为字母
string.isalpha()
包括大小写
# 是否为字母or数字
string.isalnum()

# 取整
round down: int(3.75) = 3
round number(四舍五入): round(3.75) = 4
round up: math.ceil(3.75) = 4; c = a // b, if a % b -> c += 1
# 取小数后k位
round(num,k)
然而,事实上,直接写1.00000/用float()更有用,参考346


# 排序
无论是sort还是sorted,其本质上空间复杂度都是O(n),因为recursion会消耗空间.但面试的时候提前说好recursion的stack不消耗额外空间即可.
sorted有返回值,不会改变原数据
#return的是[(key, value)]
sorted_w = sorted(f_count.items(), key=lambda x:(x[1], x[0]), reverse=True) #先以value为标准,再以key为标准
sorted_w = sorted(f_count.items(), key=lambda x:x[1]) #以value为标准


# 随机取值
import random
random.randint(start, last) # including last
random.sample(序列a，n):从序列a(str/list/set)中随机抽取n个元素，并将n个元素生以list形式返回
  
# 平方根 square root of num
8.1 num_sqrt = num ** 0.5 # num只能为正数
    num_cubic = num ** (1.0 / 3) # cubic root of num
8.2 都可用
from cmath import sqrt
num_sqrt = sqrt(num)

# factorial
import math
math.factorical(num)

# reverse
list.reverse()
reversed(tuple/list/string/range) 的返回值类型是iterator并不是list，因此如果需要，要再套上一个list()
list/str[::-1] #返回值被reverse了,但list/str并没有被reverse
sorted(reverse=True)


# 数据类型转换
int -> str: str()
str -> int: int()
str -> list: list = str.split('c')默认为空格 # 'ab cd ef' -> ['ab', 'cd', 'ef']
str -> list: list = list(str)              # 'abcdef'   -> ['a', 'b'...]
list -> str: str = '分隔符'.join(list) #注意list里的内容必须是str

'''
print(list('abcd'))       -> ['a', 'b', 'c', 'd']
print(list('ab cd'))      -> ['a', 'b', ' ', 'c', 'd']
print('abcd'.split())     -> ['abcd']
print('ab cd'.split())    -> ['ab', 'cd']

s = "a good   example"
print(s.split())      -> ['a', 'good', 'example']
print(s.split(' '))   -> ['a', 'good', '', '', 'example']
print(s.split(''))    -> ValueError
'''

ascii_int = ord(string) # 转换为ASCII
string = chr(ascii_int) # 转换为字母
string.lower()
string.upper()
string.ascii_lowercase # 取到所有的小写字母
string.ascii_uppercase


# strip
str.strip('c')移除 string 前后的字符串，默认来移除空格，但是也可以给一个字符串，然后会移除含有这个字符串的部分
str.rstrip()移除右侧字符串
str.lstrip()移除左侧字符串


#穷举所有信息
list -> for index, item in enumerate(list)
hash -> for key, value in hash.items()


#不换行
print (123,end='')

# 数组的创建
#一维
dp = [0] * n
#二维
dp = [[0 for _ in range(col)] for _ in range(row))]
#如果使用后面两个种方法 -> 会出现[[0,1],[0,1],[0,1]]的情况，因为外层在*的时候，只会copy pointer，
#这样会使得所有的内层list都是对应的同一pointer，即改变其中一个，其他的都会变
dp = [[0] * 2] * len(nums)
dp = [0, 0] * len(nums)

# map
map(function, iterable, ...)会根据提供的函数对指定序列做映射
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
eg: map(int, str([1,2,3,4,5])) -> 12345      map(square, [1,2,3,4,5]) -> [1, 4, 9, 16, 25]
  
# 切片
python中切片会创建一个新的容器，新容器对原容器的每个指向的地址进行引用。修改新容器并不会影响原容器
因此如果需要对原nums数组进行改变时，应传入(nums, 新的起点, 新的终点)

# 进制转换
十进制 -> 二进制   bin(10)
十进制 -> 八进制   oct(10) 
十进制 -> 十六进制 hex(10)
