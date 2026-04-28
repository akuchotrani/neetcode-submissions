"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 0:
            return True
        intervals.sort(key=lambda x: x.start)
        meetingHistory = [intervals[0]]
        for currMeeting in range(1, len(intervals)):
            if (meetingHistory[-1].start <= intervals[currMeeting].start 
                and meetingHistory[-1].end > intervals[currMeeting].start):
                return False
            else:
                meetingHistory.append(intervals[currMeeting])
        return True
