1.关于层级遍历的count
因为while queue的时候,当queue = deque([])时,也会进行一次循环,这样就导致count会多加一次
与course schedule作对比会发现,之所以course schedule不用减一是因为count从0开始设置的,即第一门课没有被算上,
本来while循环结束count应该 = len(course) - 1,但因为多一次循环,因此count = len(course)
