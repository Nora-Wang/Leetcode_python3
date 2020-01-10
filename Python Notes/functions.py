1.转换为ASCII
ord()

2.取小写字母
string.lowercase

3.整除
mid = (end - start) // 2

4.取小数后k位
round(num,k)
然而,事实上,直接写1.00000/用float()更有用,参考346

5.随机取值
import random
random.randint(start, last)
random.sample(data, 5)  #从data中随机获取5个元素，作为一个片断返回  
