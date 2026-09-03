class Solution:
    # -------------------------------------------------------------
    # Pendekatan 1: Bucket Sort - O(N) Time, O(N) Space (Optimal LeetCode)
    # -------------------------------------------------------------
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Fase 1: Sensus frekuensi
        count = Counter(nums)

        # Fase 2: Siapkan rak loker (indeks = frekuensi 0 s/d len(nums))
        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # Fase 3: Ambil k elemen teratas (jalan mundur dari frekuensi tertinggi)
        res: list[int] = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
