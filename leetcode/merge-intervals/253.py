# https://leetcode.com/problems/meeting-rooms-ii/
# 이 문제는 프리미엄 문제이다.
# chatgpt를 통해서 문제를 확인하고 풀었다.


import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # 시작 시간을 기준으로 회의 일정을 정렬합니다.
    intervals.sort(key=lambda x: x[0])

    # 첫 번째 회의의 종료 시간을 최소 힙에 추가합니다.
    meeting_rooms = [intervals[0][1]]
    heapq.heapify(meeting_rooms)

    # 나머지 회의 일정을 순회합니다.
    for interval in intervals[1:]:
        start_time, end_time = interval

        # 현재 회의실을 사용할 수 있는지 확인합니다.
        if meeting_rooms[0] <= start_time:
            # 회의실을 사용할 수 있다면, 종료 시간을 업데이트합니다.
            heapq.heappop(meeting_rooms)

        # 새로운 회의의 종료 시간을 힙에 추가합니다.
        heapq.heappush(meeting_rooms, end_time)

    # 필요한 회의실의 수를 반환합니다.
    return len(meeting_rooms)

intervals = [[0, 30],[5, 10],[15, 20]]
print(minMeetingRooms(intervals))  # 출력: 2

intervals = [[7, 10],[2, 4]]
print(minMeetingRooms(intervals))  # 출력: 1

