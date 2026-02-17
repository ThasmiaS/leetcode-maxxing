class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        romap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ronum = {} #to save i of roman numbers
        for i,c in enumerate(s): #O(N)
            ronum[i] = c #{0:I, 1:X, 2:I ...}

        for i in range(len(ronum)):
            if i+1<len(ronum) and romap[ronum[i]] < romap[ronum[i+1]]:
                integer -= romap[ronum[i]] # we can have negatives i forgot
                
            else:
                integer += romap[ronum[i]] 
                
        '''while nexti<len(ronum): #O(N) -- 0, 1, 2
            if (nexti+1)<len(ronum) and romap[ronum[nexti]] < romap[ronum[nexti+1]]: # like I < X and check if there a next letter
                integer += (romap[ronum[nexti+1]] - romap[ronum[nexti]]) # i=0, X - I = 10 - 1 = 9
                nexti += 2 #prev 2 letters used up
            else:
                integer += romap[ronum[nexti]] #9 + X = 9 + 10 = 19 wrong
                nexti += 1'''
        return integer
        
        #-------O(2N) --> O(N) good

