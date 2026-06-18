class Solution:
    def isValid(self, s: str) -> bool:
        open_brac="{(["
        ans=[]
        for  i in s:
            if i in open_brac:
                ans.append(i)
            elif len(ans)!=0 and i==')' and ans[-1]=='(':
                ans.pop()
            elif len(ans)!=0 and i==']' and ans[-1]=='[':
                ans.pop()
            elif len(ans)!=0 and i=='}' and ans[-1]=='{':
                ans.pop()
            else:
                return False
        return len(ans)==0