class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        s,e=0,1
        if len(intervals)==1:
             return intervals
        else:
            while s<=e and e<len(intervals):
                if intervals[s][1]>=intervals[e][0]:
                    if intervals[s][0]>intervals[e][0]:
                        intervals[s][0]=intervals[s][1]
                    if intervals[s][1]<intervals[e][1]:
                        intervals[s][1]=intervals[e][1]
                    intervals.remove(intervals[e])
                else:
                    s+=1
                    e+=1
                    
        return(intervals)
        
            
        