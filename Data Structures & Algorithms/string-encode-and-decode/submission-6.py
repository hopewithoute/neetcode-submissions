class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            # Langsung cari letak '#' tercepat di level C
            j = s.find("#", i)
            length = int(s[i:j])

            # Direct slice konten
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # Lompat ke paket berikutnya
            i = end

        return res