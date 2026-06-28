class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.sort()
        merged,ans=[],[]

        for time in occupiedIntervals:
            if not merged or time[0]>merged[-1][1]+1:
                merged.append(time[:])
            else:
                merged[-1][1]=max(merged[-1][1],time[1])

        for l,r in merged:
            if l<freeStart:
                ans.append([l,min(r,freeStart-1)])

            if r>freeEnd:
                ans.append([max(l,freeEnd+1),r])

        return ans