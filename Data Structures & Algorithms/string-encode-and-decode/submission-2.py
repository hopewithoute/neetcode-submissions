class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"

        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            # 1. Cari di mana letak '#' untuk membaca panjangnya
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # 2. Ambil tepat 'length' karakter setelah tanda '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # 3. Kursor melompat ke paket data berikutnya
            i = end

        return res
