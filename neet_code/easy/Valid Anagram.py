class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dis_s={}
        dis_t={}
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            dis_s[s[i]]= dis_s.get(s[i],0)+1
            dis_t[t[i]]= dis_t.get(t[i],0)+1     
        if dis_s == dis_t:
            return True
        else:
            return False  
#nishanth0962333@gmail.com