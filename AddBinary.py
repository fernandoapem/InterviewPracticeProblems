class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        maxl = max(len(a),len(b))
        result = ""
        if len(a) != len(b):
            if maxl == len(a):
                d = len(a)-len(b)
                for char in range(0,d):
                    b = '0' + b
            else:
                d = len(b)-len(a)
                for char in range(0,d):
                    a = '0' + a
        for digit in range(len(a)-1,-1,-1):
            if (a[digit] == '1' and b[digit] == '1') and carry == 0:
                result =  '0'+ result
                carry = 1
            elif a[digit] == '1' and b[digit] == '1' and carry == 1:
                result = '1' + result
                carry = 1
            elif a[digit] == '0' and b[digit] == '0' and carry == 1:
                result =   '1' + result
                carry = 0
            elif a[digit] == '0' and b[digit] == '0' and carry == 0:
                result =  '0' + result
                carry = 0
            elif ((a[digit] == '1' and b[digit] == '0') or (b[digit] == '1' and a[digit] == '0')):
                if carry == 1:
                    result =   '0' + result
                    carry = 1
                else:
                    result =  '1' + result
                    carry = 0
        if carry == 1:
            result = '1' + result
        return result
p = Solution()
print(p.addBinary("1010","1011"))
print(p.addBinary("11","1"))
print(int('1')+1)