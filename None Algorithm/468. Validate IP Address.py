Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

Example 1:

Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
Example 4:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
Output: "Neither"
Example 5:

Input: IP = "1e1.4.5.6"
Output: "Neither"
 

Constraints:

IP consists only of English letters, digits and the characters '.' and ':'.


# 2024/02/08
# Method 1
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            return self.validate_ipv4(queryIP.split('.'))
        if ':' in queryIP:
            return self.validate_ipv6(queryIP.split(':'))
        
        return "Neither"
    
    def validate_ipv4(self, ip_list):
        if len(ip_list) != 4:
            return "Neither"
        
        for x in ip_list:
            if not x.isdigit():
                return "Neither"
            
            if len(x) > 1 and x[0] == '0':
                return "Neither"
            
            x_int = int(x)
            if x_int < 0 or x_int > 255:
                return "Neither"
            
        return "IPv4"
    
    def validate_ipv6(self, ip_list):
        if len(ip_list) != 8:
            return "Neither"
        
        valid_v = set()
        for d in string.digits:
            valid_v.add(d)
        for a in string.ascii_lowercase[:6]:
            valid_v.add(a)
        for a in string.ascii_uppercase[:6]:
            valid_v.add(a)
            
        for x in ip_list:
            if len(x) > 4 or len(x) < 1:
                return "Neither"
            for v in x:
                if v not in valid_v:
                    return "Neither"
            
        return "IPv6"
            
# Method 2
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            return self.validate_ipv4(queryIP.split('.'))
        if ':' in queryIP:
            return self.validate_ipv6(queryIP.split(':'))
        
        return "Neither"
    
    def validate_ipv4(self, ip_list):
        if len(ip_list) != 4:
            return "Neither"
        
        for x in ip_list:
            if not x.isdigit():
                return "Neither"
            
            if len(x) > 1 and x[0] == '0':
                return "Neither"
            
            x_int = int(x)
            if x_int < 0 or x_int > 255:
                return "Neither"
            
        return "IPv4"
    
    def validate_ipv6(self, ip_list):
        if len(ip_list) != 8:
            return "Neither"
        
        valid_v = '0123456789abcdefABCDEF'
        valid_v = set(valid_v)
            
        for x in ip_list:
            if len(x) > 4 or len(x) < 1:
                return "Neither"
            for v in x:
                if v not in valid_v:
                    return "Neither"
            
        return "IPv6"
            






class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP and self.is_IPv4(IP.split('.')):
            return 'IPv4'
        elif ':' in IP and self.is_IPv6(IP.split(':')):
            return 'IPv6'
        return 'Neither'
    
    # IPv4条件：
    # 1. 可被分为4个部分
    # 2. 每个部分0 <= val <= 255,且只能包含digit
    # 3. cannot contain leading zeros
    def is_IPv4(self, ip):
        if len(ip) != 4:
            return False
        
        for num in ip:
            if not num or (len(num) > 1 and num[0] == '0'):
                return False
            if not num.isdigit() or not (0 <= int(num) <= 255):
                return False
            
        return True
    
    # IPv6条件：
    # 1. 可被分为8个部分
    # 2. 每个部分不能为空，且长度为1～4
    # 3. 每个部分的letter只能包含数字，a~f,A~F
    def is_IPv6(self, ip):
        if len(ip) != 8:
            return False
        
        for num in ip:
            if not (1 <= len(num) <= 4):
                return False
            
            for c in num:
                if c not in '0123456789abcdefABCDEF':
                    return False
        
        return True
