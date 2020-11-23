class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      
        if len(intervals)==0:
            return [newInterval]
        else:
            intervals.append(newInterval)
            intervals.sort()
            s=0
            e=1
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
            return intervals