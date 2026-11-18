class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''.join(f"{len(s)}#{s}" for s in strs)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j = j + 1
            l = int(s[i:j])
            decoded_str.append(s[j + 1: j + 1 + l])
            i = j + 1 + l
        return decoded_str