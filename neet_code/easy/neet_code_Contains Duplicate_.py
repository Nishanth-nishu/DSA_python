class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check=[]
        for i in range(0,len(List)):
            if List[i] in check:
                return True
            else:
                check.append(List[i])
        return False

#nishanth0962333@gmail.com       