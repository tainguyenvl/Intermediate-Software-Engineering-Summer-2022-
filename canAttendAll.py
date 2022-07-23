def canAttendAll(intervals):
    new_intervals = intervals
    new_intervals.sort()
    for i in range(1,len(new_intervals)):
        if new_intervals[i-1][1] > new_intervals[i][0]:return False
    return True


intervals = [[1,4], [2,5], [7,9]]

print (canAttendAll(intervals))



    

