import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: (x[1], x[0]))
        res = 0
        curr_time = 0
        courses_taken = []
        for dur, last_day in courses:
            if curr_time + dur <= last_day:
                curr_time += dur
                res += 1
                heapq.heappush(courses_taken, (-dur, last_day))
            elif courses_taken and -courses_taken[0][0] > dur:
                top = heapq.heappushpop(courses_taken, (-dur, last_day))
                curr_time -= -top[0] - dur
            else:
                continue

        return res
