Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 

Constraints:

1 <= chars.length <= 2000
chars[i].length == 1
chars[i] is a lower-case English letter, upper-case English letter, digit or a symbol.


code:
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        if len(chars) == 1:
            return 1
        
        slow, fast = 0, 1
        count = 1
        # fast可以取到len(chars) -> 为了保证结果的最后一位也能在while loop中一起被处理掉
        # test case: ["a","b","c"]
        while fast <= len(chars):
            if fast < len(chars) and chars[fast] == chars[fast - 1]:
                count += 1
                fast += 1
                continue
            
            # set char position
            chars[slow] = chars[fast - 1]
            slow += 1

            # have duplicate char -> use count to set number position
            if count != 1:
                length = len(str(count))
                chars[slow:slow + length] = list(str(count))
                slow += length
                
            # renew count
            count = 1
            
            fast += 1
        
        return slow
