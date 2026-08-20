class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        n1,n2=len(s1),len(s2)
        s1map,winmap=[0]*26,[0]*26

        for i in range(n1):
            s1map[ord(s1[i])-ord('a')]+=1
            winmap[ord(s2[i])-ord('a')]+=1

        if s1map==winmap:
            return True
            
        for i in range(n1,n2):
            winmap[ord(s2[i])-ord('a')]+=1
            winmap[ord(s2[i-n1])-ord('a')]-=1

            if winmap==s1map:
                return True
            
        return False