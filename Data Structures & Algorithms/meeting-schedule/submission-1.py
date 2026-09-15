"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        lastEnd = -1
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start < lastEnd:
                return False
            else:
                lastEnd = end
        return True