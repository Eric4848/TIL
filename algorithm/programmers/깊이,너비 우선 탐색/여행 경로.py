def solution(tickets):
    answer = []
    departures = []
    arrivals = []
    tickets.sort(key=lambda x: x[1])
    visits = ['INC']
    for d, a in tickets:
        departures.append(d)
        arrivals.append(a)
    is_visited = [False] * len(tickets)
    goal = len(tickets)

    def flight(now, count):
        nonlocal answer
        if answer:
            return
        if count == goal:
            answer = visits[:]
            return

        for i in range(len(departures)):
            if departures[i] == now and not is_visited[i]:
                visits.append(arrivals[i])
                is_visited[i] = True
                flight(arrivals[i], count+1)
                visits.pop()
                is_visited[i] = False

    flight('ICN', 0)
    answer = list(answer)
    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

# from collections import deque
#
#
# def solution(tickets):
#     visits = []
#     tickets.sort(key=lambda x: x[1])
#     to_visits = deque()
#     for ticket in tickets:
#         if ticket[0] == 'ICN':
#             visits.append(ticket[0])
#             visits.append(ticket[1])
#             to_visits.append(ticket[1])
#             tickets.remove(ticket)
#             break
#
#     while tickets:
#         now = to_visits.popleft()
#         for ticket in tickets:
#             if ticket[0] == now:
#                 visits.append(ticket[1])
#                 to_visits.append(ticket[1])
#                 tickets.remove(ticket)
#                 break
#
#     return visits
