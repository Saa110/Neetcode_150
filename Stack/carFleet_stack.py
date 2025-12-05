class Solution:
    def carFleet_stack(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
    def carFleet_iteration(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed=[]
        result=[100]*len(position)
        count=1
        for i in range(len(position)):
            pos_speed.append([position[i],speed[i]])
       # print(pos_speed)
        pos_speed.sort()
        result[-1]=(target-pos_speed[-1][0])/pos_speed[-1][1]
        #print(pos_speed,result)
        for i in range(len(position)-2,-1,-1):
            temp=(target-pos_speed[i][0])/pos_speed[i][1]
            if result[i+1]>=temp:
                result[i]=result[i+1]
                #print("0",temp)
            else:
                #print("1",temp)
                result[i]=temp
                count+=1
        #print(result)
        return count


        
