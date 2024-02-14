class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        li=list(s)
        l=0
        r=len(li)-1
        while (l<r):
            if (l<r and vowels.find(li[l])==-1):
                l+=1
            elif (l<r and vowels.find(li[r])==-1):
                r-=1
            else:
                li[l],li[r]=li[r],li[l]
                l+=1
                r-=1
        return "".join(li)