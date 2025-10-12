class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        The naive solution is:
        - for each word, make a tuple which stores the char count
        - this is the key for a dictionary which stores frequ -> words (list[str])
        """

        import string

        c2idx = {}
        for idx, c in enumerate(string.ascii_lowercase):
            c2idx[c] = idx

        anagrams = defaultdict(list)
        for word in strs:
            key = [0] * len(string.ascii_lowercase)
            for c in word:
                key[c2idx[c]] += 1

            anagrams[tuple(key)].append(word)

        print(anagrams)
        return list(anagrams.values())


class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return None
        if strs == [""]:
            return ""
        return ",".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == None:
            return []
        if s == "":
            return [""]
        return s.split(",")
