#! /usr/bin/python3.7
import heapq
def UglyNumber(n):
    heap=[1]
    for i in range(n-1):
        cur=heapq.heappop(heap)
        for i in [2,3,5]:
            temp=cur*i
            if temp not in heap:
                heapq.heappush(heap,temp)
    return heapq.heappop(heap)
print(UglyNumber(9))
