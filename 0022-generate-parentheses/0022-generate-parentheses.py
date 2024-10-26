class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        create res array to return
        have a stack to add the current step youre on
        1) check to see if the opening parentheses == closed parentheses == n 
        (meaning if n is 3 there will be 3 open 3 closed)
        2) check to see if closed < open
        (we can add a closed)
        3) check to see if open < n
        (max amount of open we can add) 
        """
        res = []
        stack = []
        def backTrack(open,closed):
            if open == closed == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backTrack(open+1,closed)
                stack.pop()
            if closed < open:
                stack.append(")")
                backTrack(open,closed+1)
                stack.pop()
        backTrack(0,0)
        return res