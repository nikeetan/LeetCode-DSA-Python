class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map = {}
        word_heap = []
        for i in words:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                freq_map[i] += 1

        for key, val in freq_map.items():
            heapq.heappush(word_heap, (- val, key))
        res = []
        while k:
            res.append(heapq.heappop(word_heap)[-1])
            k -= 1
        return res
        