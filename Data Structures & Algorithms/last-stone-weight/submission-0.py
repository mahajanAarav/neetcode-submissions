class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxheap = [-s for s in stones]
        heapq.heapify(self.maxheap)

        while len(self.maxheap) > 1:
            y = heapq.heappop(self.maxheap)
            x = heapq.heappop(self.maxheap)

            if x != y:
                heapq.heappush(self.maxheap, y - x)

        if self.maxheap:
            return abs(self.maxheap[0])

        return 0