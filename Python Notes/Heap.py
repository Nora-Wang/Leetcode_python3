1.创建一个堆
1.1直接使用list的创建方式Heap = []
1.2使用heapify()函数将一个存在的列表转为堆

2.heapq.heappush(heap, item)
往堆中插入一个值,同时要保持为最小堆

3.heapq.heappop(heap)
返回堆中的最小值,并把它从堆中删除,同时保持为最小堆;如果堆为空,发生IndexError
直接通过heap[0]可以获取最小值并不从堆中把它删除

4.heapq.heappushpop(heap, item)
向堆中插入值后再弹出堆中的最小值,这个函数的速度比直接使用heappush() 和heappop()的效率更加高

5.heapq.heapreplace(heap, item)
弹出和返回堆中的最小值再插入一个新的值.堆的大小没有改变.如果堆为空,产生 IndexError
这一个操作也比直接使用heappush() 和heappop()的效率更加高,尤其适合使用在固定堆大小不变的情况
与上一个函数相比，这个函数返回的值可能要比将要插入到堆的值大

6.heapq.heapify(x)
将一个list转为最小堆,线性时间复杂度,O(n)


原文链接：https://blog.csdn.net/qq_23869697/article/details/82735088
