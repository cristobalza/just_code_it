class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        '''
        ['dog, 'banana', 'orange', 'apple']
        '6?banana3?dog'
        '''
        res = ""
        for _str in strs:
            res += f"{len(_str)}?{_str}"
        return res
            
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '?':
                j+=1
            size = int(s[i:j])
            res.append(s[j+1:j+1+size])
            i = j+1+size
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))