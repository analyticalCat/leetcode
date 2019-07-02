class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0: return 0
        g.sort()
        s.sort()
        
        gi=0
        si=0
        maxs = max(s)

        while g[gi] <= maxs:
            while g[gi] > s[si]:
                si+=1

            gi += 1
            si += 1
            if gi>=len(g) or si>=len(s): return gi
    

        return gi