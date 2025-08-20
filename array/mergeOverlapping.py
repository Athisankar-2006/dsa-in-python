## merge overlapping intervals

## sorting + merged (time-O(n log n) (space-O(n)))
def merge_intervals(intervals):
    if not intervals:
        return[]
    intervals.sort(key=lambda x:x[0])
    merged=[intervals[0]]
    for i in intervals[1:]:
        last=merged[-1]
        if i[0]<=last[1]:
            last[1]=max(last[1],i[1])
        else:
            merged.append(i)
    return merged


print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))

        

 