class Solution:
    def isPalindrome(self, x: int) -> bool:
        #2 pointer problem
        string = str(x)
        start = 0
        end = len(string) - 1

        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        
        return True
            