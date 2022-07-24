import heapq

l = [7, 9, 1, 3]
heapq.heapify(l)
for elm in [6, 8, 4, 2]:
    heapq.heappush(l, elm)

while l:
    print(heapq.heappop(l))
