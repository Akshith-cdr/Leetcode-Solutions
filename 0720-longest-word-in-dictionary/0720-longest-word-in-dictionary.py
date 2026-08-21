class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        wset=set([""])
        longest=""

        for w in words:
            if w[:-1] in wset:
                wset.add(w)
                if len(w)>len(longest):
                    longest=w
        
        return longest