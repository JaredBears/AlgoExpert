from collections import deque
def taskAssignment(k, tasks):
    sortedIndex = deque(sorted(range(len(tasks)), key= lambda hr: tasks[hr]))
    answer = []
    while sortedIndex:
        answer.append([sortedIndex.popleft(), sortedIndex.pop()])
    return answer
