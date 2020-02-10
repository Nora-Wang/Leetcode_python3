模板

题目list = [num1, num2, ...], 从左往右看,求每个值之后第一个比该值大的数

stack = []
result = []

for i in range(len(list)):
    while stack and list[stack[-1]] < list[i]:
        result[stack[-1]] = list[i]
        stack.pop()
       
    stack.append(i)


