class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        ans = 0
        
        while i<len(chars):
            cur = chars[i]
            count = 0
            while i<len(chars) and chars[i]==cur:
                count+=1
                i+=1
            chars[ans]=cur
            ans+=1
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans+=1
        return ans