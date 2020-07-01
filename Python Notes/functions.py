1.字母与ASCII互相转换
ord()转换为ASCII
chr()转换为字母

2.取小写字母
string.lowercase

3.整除
mid = (end - start) // 2
次方
2**8 = 2^8

4.取小数后k位
round(num,k)
然而,事实上,直接写1.00000/用float()更有用,参考346

5.随机取值
import random
random.randint(start, last)
random.sample(序列a，n):从序列a(str/list/set)中随机抽取n个元素，并将n个元素生以list形式返回
  
6.排序
#有返回值,不会改变原数据
new_list = sorted(list/str/dirc/tuple, cmp=None, key=None, reverse=False)
#没有返回值,会改变原list
list.sort(cmp=None, key=None, reverse=False)

7.绝对值
abs(num)

8.平方根
8.1 num_sqrt = num ** 0.5 num只能为正数
8.2 都可用
import cmath
num_sqrt = cmath.sqrt(num)

9.反转
API	          改变原list	  返回值
list.reverse()	是	         无
reversed(list)	否	         有
Note：reversed() 的返回值类型并不是list，因此如果需要，要再套上一个list()

list/str[::-1] #返回值被reverse了,但list/str并没有被reverse
sorted(reverse=True)

10.取值范围
range(start, stop[, step])
平时step是直接默认为1,而start为0时也可以不写
#当step!=1,需要被单独写出且start=0时,一定要记得把start写上,不然系统会将step当作stop用
eg: range(0, end, 2)

11.list化
list()
#string不能直接改变其中的内容,需要先list化,改变后再join

12.无穷大和无穷小
sys.maxsize或float('inf')
-sys.maxsize或-float('inf')

13.除法
3 / 2 = 1
3 // 2 =  1.5
float(3) / 2 = 1.5
3.0 / 2 = 1.5

14.string去掉头尾指定的字符（默认为空格或换行符）或字符序列。
str.strip([chars])
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

15.'sep'.join(seq)
sep：分隔符,可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
注意seq为list时,list里的内容必须是str

16.lambda
pairs = [[3,4],[2,3],[1,2]]
pairs.sort(key=lambda x : x[0], reverse = True),以pairs每一组的第一个数值为标准进行排序

sorted(dict.items(), key=lambda x:x[1])dict以value的值进行排序#结果为list中包含tuple,eg:[(key1,value1),(key2,value2)]

17.split把str分为list
list = str.split('c')默认为空格

18.str.strip('c')移除 string 前后的字符串，默认来移除空格，但是也可以给一个字符串，然后会移除含有这个字符串的部分
str.rstrip()移除右侧字符串
str.lstrip()移除左侧字符串

19.for index, item in enumerate(list)

20.不换行
print (123,end='')

21.数组的创建
#一维
dp = [0] * n
#二维
dp = [[0, 0] for _ in range(len(nums))]
#如果使用后面两个种方法 -> 会出现[[0,1],[0,1],[0,1]]的情况，因为外层在*的时候，只会copy pointer，
#这样会使得所有的内层list都是对应的同一pointer，即改变其中一个，其他的都会变
dp = [[0] * 2] * len(nums)
dp = [0, 0] * len(nums)

22.map
map(function, iterable, ...)会根据提供的函数对指定序列做映射
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
eg: map(int, str([1,2,3,4,5])) -> 12345      map(square, [1,2,3,4,5]) -> [1, 4, 9, 16, 25]
  
23. 切片
python中切片会创建一个新的容器，新容器对原容器的每个指向的地址进行引用。修改新容器并不会影响原容器。
因此如果需要对原nums数组进行改变时，应传入(nums, 新的起点, 新的终点)

