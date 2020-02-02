############################################################
topological sort：判读一个有向图，是无环的
queue和list都是append，set是add
set用于在graph中，用node去映射sun_node(neighbors)，这时的sun_node(neighbors)是set类型
原因：set判断一个node在不在set里时，可以直接找到有没有这个node，时间负责度为O(1)（因为set是一种没有value的字典，即其存储的数据相当于键，即字典查找键）
而list则需要从头遍历的寻找，时间复杂度为O(n)
############################################################
