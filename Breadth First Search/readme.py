############################################################
topological sort：判读一个有向图，是无环的

queue和list都是append，set是add

set用于在graph中，用node去映射sun_node(neighbors)，这时的sun_node(neighbors)是set类型

原因：set判断一个node在不在set里时，可以直接找到有没有这个node，时间负责度为O(1)
（因为set是一种没有value的字典，即其存储的数据相当于键，即字典查找键）
而list则需要从头遍历的寻找，时间复杂度为O(n)
############################################################


1.先判断要不要建图:
  1.1要: 题目是将点和边分开给出的, 就建立一个adjacency list(用一个list或者一个int表示点，然后用一个list[list]来表示边)
  1.2不要: 给出grid,并且所需结果直接可以根据grid step by step的跑node得出,相当于整个图已经都给出来了

2.图建好后,根据题目判断是用dfs还是bfs

3.indegrees在无法找到root或者在需要找mid-node时使用,即若题目为一个有向图,但题目只给了有几个点,却没给哪个点为root,这时就需要用indegrees的数据判断root
若为无向图,则图中任意点都可以是root,直接取node 0即可
