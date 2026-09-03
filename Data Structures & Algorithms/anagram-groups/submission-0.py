class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for str in strs:
            #hitung frequency map of string
            key = "".join(sorted(str))
            #simpan sorted str as key
            groups[key].append(str)

        return list(groups.values())