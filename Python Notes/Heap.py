heap
插入一个数:直接放在堆尾,然后往上翻就行 O(logn)
删除堆头(即删除最小值或最大值):用堆尾代替堆头,然后往下翻就行 O(logn)


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
