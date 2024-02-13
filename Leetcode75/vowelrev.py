"""345. Reverse Vowels of a String
Solved
Easy
Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters."""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set('aeiouAEIOU')
        p1,p2=0,len(s)-1
        s=list(s)
        while p1<p2:
            while p1<p2 and s[p1] not in vowels:
                p1+=1
            while p1<p2 and s[p2] not in vowels:
                p2-=1
            s[p1],s[p2]=s[p2],s[p1]
            p1+=1
            p2-=1
        return ''.join(s)
