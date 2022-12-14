class Solution:
    def romanToInt(self, s: str) -> int:
        prefix = {}
        prefix['I'] = ['V','X']
        prefix['X'] = ['L','C']
        prefix['C'] = ['D','M']
        result = 0
        roman = 0
        while roman < len(s):
            if s[roman] not in prefix:
                if s[roman] == 'V':
                    result += 5
                elif s[roman] == 'L':
                    result += 50
                elif s[roman] == 'D':
                    result += 500
                elif s[roman] == 'M':
                    result += 1000
            else:
                if s[roman] == 'I':
                    if roman == len(s)-1:
                        result += 1
                    elif s[roman+1] in prefix[s[roman]]:
                        if s[roman+1] == 'V':
                            result += 4
                            roman += 1
                        elif s[roman+1] == 'X':
                            result += 9
                            roman += 1
                    else:
                        result += 1
                elif s[roman] == 'X':
                    if roman == len(s)-1:
                        result += 10
                    elif s[roman+1] in prefix[s[roman]]:
                        if s[roman+1] == 'L':
                            result += 40
                            roman += 1
                        elif s[roman+1] == 'C':
                            result += 90
                            roman += 1
                    else:
                        result += 10
                elif s[roman] == 'C':
                    if roman == len(s)-1:
                        result += 100
                    elif s[roman+1] in prefix[s[roman]]:
                        if s[roman+1] == 'D':
                            result += 400
                            roman += 1
                        elif s[roman+1] == 'M':
                            result += 900
                            roman += 1
                    else:
                        result += 100
            roman += 1
        return result