class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        group = {}
        for number in nums:
            group[number] = group.get(number, 0) + 1

        topk = sorted(group.items(), key=lambda item: item[1], reverse=True)[:k]

        return [item[0] for item in topk]