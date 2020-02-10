模板

题目list = [num1, num2, ...], 从左往右看,求每个值之后第一个比该值大的数

stack = []
#若后续需要进行对结果的查找,即用num找结果:若num是数字,直接使用index即可;若num不是数字,则result设为hash table即可
result = []

for i in range(len(list)):
    while stack and list[stack[-1]] < list[i]:
        result[stack[-1]] = list[i]
        stack.pop()
       
    stack.append(i)


