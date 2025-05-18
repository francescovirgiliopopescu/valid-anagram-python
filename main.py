from collections import Counter

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
  
sol = Solution()

s, t = "anagram", "nagaram"

print(sol.isAnagram(s, t))