class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        group = Counter(nums)
        topk = sorted(group.items(), key=lambda item: item[1], reverse=True)[:k]

        return [item[0] for item in topk]