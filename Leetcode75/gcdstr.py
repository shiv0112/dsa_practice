"""1071. Greatest Common Divisor of Strings
Solved
Easy
Topics
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        s1 = max(str1, str2, key = lambda x: len(x))
        if s1 == str1:
            s2 = str2
        else:
            s2 = str1
        a1, a2 = len(s1), len(s2)

        if s2 * (a1//a2) == s1:
            return s2
        
        for i in range(2, a2//2 + 1):
            if (a2 / i) % 1 == 0:
                if s2[:a2//i]*i == s2:
                    if s1[:a2//i]*int(i*a1/a2) == s1:
                        if s2[:a2//i] == s1[:a2//i]:
                            return s2[:a2//i] 

        if s1.count(s1[0]) == a1:
            if s2.count(s2[0]) == a2:
                if s1[0] == s2[0]:
                    return s1[0]

        return ''

## Easier approach str1 + str2 == str2 + str1
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]s