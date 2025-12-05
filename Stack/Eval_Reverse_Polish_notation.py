class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        flag=1
        operators=["+","-","*","/"]
        for i in tokens:
            if i in operators:
                temp2=stack.pop()
                temp1=stack.pop()
                stack.append(str(int(eval(temp1 +" "+i+" "+temp2))))
                
            else:
                stack.append(i)
        return int(stack.pop())
                    

        
