class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)

        # Fase 2: Pelihara heap berkapasitas k berisi tuple: (frekuensi, angka)
        min_heap: list[tuple[int, int]] = []
        for num, freq in count.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                # Masukkan kandidat baru & buang elemen dengan frekuensi paling kecil
                heapq.heappushpop(min_heap, (freq, num))

        # Ekstrak nilai angkanya (elemen ke-1 dari tuple)
        return [num for freq, num in min_heap]