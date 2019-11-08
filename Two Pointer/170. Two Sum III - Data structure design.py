Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false


这道题的解法有3种情况

1.要求add和find的时间复杂度较平均

2.add调用的很多，而find调用的很少；即要求add的时间复杂度到最低

3.find调用的很多，而add调用的很少；即要求find的时间复杂度到最低
