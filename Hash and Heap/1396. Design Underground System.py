Implement the class UndergroundSystem that supports three methods:

1. checkIn(int id, string stationName, int t)

A customer with id card equal to id, gets in the station stationName at time t.
A customer can only be checked into one place at a time.
2. checkOut(int id, string stationName, int t)

A customer with id card equal to id, gets out from the station stationName at time t.
3. getAverageTime(string startStation, string endStation) 

Returns the average time to travel between the startStation and the endStation.
The average time is computed from all the previous traveling from startStation to endStation that happened directly.
Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. All events happen in chronological order.

 

Example 1:

Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.00000
Example 2:

Input
["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
[[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]

Output
[null,null,null,5.00000,null,null,5.50000,null,null,6.66667]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.00000
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.50000
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30);
undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 6.66667
 

Constraints:

There will be at most 20000 operations.
1 <= id, t <= 10^6
All strings consist of uppercase, lowercase English letters and digits.
1 <= stationName.length <= 10
Answers within 10^-5 of the actual value will be accepted as correct.


#######################################################################################################################
Clarification:
1. input and output:
checkIn(id: int, stationName: str, t: int) -> None, 
checkOut(id: int, stationName: str, t: int) -> None, 
getAverageTime(startStation: str, endStation: str) -> float

give a case:
checkIn  [1, A, 1]
checkOut [1, B, 3]
checkIn  [2, A, 4]
checkOut [2, B, 6]

2. 对于checkIn函数来说，can I assume that the customer can only be checked into one place at a time?
3. 对于所有的time来说，can I assume that all the input t are increasing, follow the time increasing logical order?
4. 对于getAverageTime函数来说，is there has a situation that the startStation or endStation not exist in our database? 
   this function is always valid?

#######################################################################################################################
solution:
1. 因为要search station name or id frequently -> use hashmap

self.check_in: #key = id, value = [station_name, start_time]
self.check_out: #route = startStation_endStation, value = [total_time = all(end_time - start_time), count]

#######################################################################################################################
time: all O(1)
space: self.check_in O(P) + self.check_out O(S^2) -> O(P + S^2); P = number of passengers, S = number of stations

#######################################################################################################################
from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        # key = id, value = [station_name, start_time]
        self.check_in = defaultdict(list)

        # route = startStation_endStation, value = [total_time = all(end_time - start_time), count]
        self.check_out = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in[id]
        route = start_station + '_' + stationName

        if route in self.check_out:
            self.check_out[route][0] += t - start_time
            self.check_out[route][1] += 1
        else:
            self.check_out[route] = [t - start_time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = startStation + '_' + endStation

        if route not in self.check_out:
            return 0.0

        return self.check_out[route][0] / self.check_out[route][1]

solution = UndergroundSystem()

solution.checkIn(1, "A", 1)
solution.checkOut(1, "B", 5)
solution.checkIn(1, "A", 10)
solution.checkOut(1, "B", 20)
res = solution.getAverageTime("A","B")

print(res)

#######################################################################################################################
test case:
1.  checkIn  [1, A, 1]
    checkOut [1, B, 3]
    checkIn  [1, A, 4]
    checkOut [1, B, 6]
2. edge case: the customer take a circle travel
    checkIn  [1, A, 1]
    checkOut [1, A, 3]
    checkIn  [1, A, 4]
    checkOut [1, A, 6]



#######################################################################################################################
#######################################################################################################################
别人的面经, from https://www.1point3acres.com/bbs/thread-642142-1-1.html
我首先问了两个clarification的问题：
1. 会不会有人坐地铁转圈玩，从同一个车站进出？
2. 如何处理人还在地铁里的时候再次出现刷卡进入的情况？

和面试官讨论了一下给出了自己认为比较reasonable的处理方式，面试官说make sense之后提出可以用两个map，一个map存储还在地铁里的人和他们上车的时间地点，
另一个map存储已经完成的trip，key是起始和结束的车站，value是一个自己发明的数据结构，包含了同样的trip发生的次数和总共的时间，同时主动说了一下三个API
都是O(1)时间复杂度。面试官说可以开始写代码了。

因为当时考虑到这道题太简单了，于是所有的变量都拿驼峰命名法来保证可读性，同时将一些重复代码专门拿出来写了helper function，还说了一句自己设计的
data model增加了一个API为了和主要的business logic decouple。这算是我在面试之中代码写得最像production code的一次了。同时和面试官保持交流，
适时问一下遇到的corner case如我所说地处理可不可以。最后面试官指出了代码里遗漏了的两个点（没有做map.put），其中一个她说对了于是自己改了过来，另一个
我说不会有这样的问题因为java的object是由hashcode来identify的，只改里面的变量是不会修改hashcode的，面试官说自己不熟悉java还感谢我指出了这一点。

我本来还想写个test case来测试，结果面试官说直接walk through一下代码就好了，遂照做之。本来我以为还会有诸如large scale或者multithread之类的
followup，结果面试官直接就说我们进入Q&A吧。
