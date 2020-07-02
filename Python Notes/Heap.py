heap性质 (priority queue)
1. 任意节点小于它的所有后裔，最小元素在堆的root上 (增序性) (注意: 与BST做区别,堆并没有左<根<右的rule)
2. 堆总是一颗完全树Complete tree: 因为插入/删除数据的方式
3. 将根节点最大的堆叫做MAX HEAP, 根节点最小的堆叫做最小堆MIN HEAP
4. index of left_Child  = index of parent * 2 + 1
5. index of right_Child = index of parent * 2 + 2
6. Unsorted but follow rules above
  
时间复杂度:
1.找出最大值/最小值 O(1)
2.插入数据push   O(logN):直接放在堆尾,然后往上翻就行
3.删除数据pop    O(logN):删除堆头(即删除最小值或最大值),用堆尾代替堆头,然后往下翻就行
4.更新数据update O(logN):更新heap中的某个数据,再通过上/下翻调整位置
5.直接一个list生成heap -> O(n), 一个一个的append进heap -> O(nlogn)


import heapq(最小堆)
#遍历一遍heap,时间为O(nlogn),因为需要把所有node一个一个的pop出来,每次pop的时间为logn
1.创建一个堆
1.1直接使用list的创建方式Heap = []
1.2使用heapify()函数将一个存在的列表转为堆

2.heapq.heappush(heap, item)
往堆中插入一个值,同时要保持为最小堆

3.heapq.heappop(heap) O(logn)
返回堆中的最小值,并把它从堆中删除,同时保持为最小堆;如果堆为空,发生IndexError
直接通过heap[0]可以获取最小值并不从堆中把它删除
#heap没有提供remove某个特定值的class,强行使用其时间复杂度为O(n)

4.heapq.heappushpop(heap, item)
向堆中插入值后再弹出堆中的最小值,这个函数的速度比直接使用heappush() 和heappop()的效率更加高

5.heapq.heapreplace(heap, item)
弹出和返回堆中的最小值再插入一个新的值.堆的大小没有改变.如果堆为空,产生 IndexError
这一个操作也比直接使用heappush() 和heappop()的效率更加高,尤其适合使用在固定堆大小不变的情况
与上一个函数相比，这个函数返回的值可能要比将要插入到堆的值大

6.heapq.heapify(x)
将一个list转为最小堆,线性时间复杂度,O(n)


原文链接：https://blog.csdn.net/qq_23869697/article/details/82735088

  
  
#heap == Priority Queue,实现最小堆
heapq在实现过程中就是用的优先队列,即heap的本质为一个queue
其原理是:用heapq.heappush(heap, item)将item放入queue,并且对这个queue按照item的数据从小到大的排序
(这里的item可以是一个元组,eg:(a,b,c),queue通过先比较a,然后比较b,最后比较c的顺序将整个queue按从小到大的排序)
这样在heapq.heappop(heap)时,依照queue的pop原理,应该是pop队头,即整个queue的最小值
这样就满足了最小堆的条件
