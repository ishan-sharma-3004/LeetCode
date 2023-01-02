#Valid Parenthesis
'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
def isValid(self, s: str) -> bool:
        stack=[]
        dicta={']':'[', '}' :'{', ')':'(' }
        for i in s:
            if(i in dicta):
                if stack and stack[-1]==dicta[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False