# You are given a 0-indexed integer array forts of length n representing the positions of several forts. forts[i] can be -1, 0, or 1 where:

# -1 represents there is no fort at the ith position.
# 0 indicates there is an enemy fort at the ith position.
# 1 indicates the fort at the ith the position is under your command.
# Now you have decided to move your army from one of your forts at position i to an empty position j such that:

# 0 <= i, j <= n - 1
# The army travels over enemy forts only. Formally, for all k where min(i,j) < k < max(i,j), forts[k] == 0.
# While moving the army, all the enemy forts that come in the way are captured.

# Return the maximum number of enemy forts that can be captured. In case it is impossible to move your army, or you do not have any fort under your command, return 0.

 

# Example 1:

# Input: forts = [1,0,0,-1,0,0,0,0,1]
# Output: 4
# Explanation:
# - Moving the army from position 0 to position 3 captures 2 enemy forts, at 1 and 2.
# - Moving the army from position 8 to position 3 captures 4 enemy forts.
# Since 4 is the maximum number of enemy forts that can be captured, we return 4.
# Example 2:

# Input: forts = [0,0,1,-1]
# Output: 0
# Explanation: Since no enemy fort can be captured, 0 is returned.
 

# Constraints:

# 1 <= forts.length <= 1000
# -1 <= forts[i] <= 1


from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        control = []
        enemy = []

        for i in range(len(forts)):
            if forts[i] == 1:
                control.append(i)
            if forts[i] == -1:
                enemy.append(i)
         
        if len(control) == 0:
            return 0
        
        if len(enemy) == -1:
            return 0
        
        maxCapture = 0

        for i in range(len(control)):
            # move left
            if control[i] < len(forts):
                temp_i = control[i]+1
                counta = 0
                while temp_i < len(forts) and forts[temp_i] == 0:
                    counta+=1
                    temp_i += 1

                if(temp_i<len(forts) and forts[temp_i]==-1):
                    maxCapture = max(maxCapture,counta)  

            # move right
            if control[i] > -1:
                temp_j = control[i]-1
                counta=0
                while temp_j >=0 and forts[temp_j] == 0:
                    counta +=1
                    temp_j -= 1

                if(temp_j > -1 and forts[temp_j]==-1):
                    maxCapture = max(maxCapture,counta) 

        return maxCapture
    

class Solution1:
    def captureForts(self, forts: List[int]) -> int:
            n = len(forts)
            max_captured = 0
            
            for i in range(n):
                if forts[i] == 1:
                    # Move right
                    count = 0
                    for j in range(i + 1, n):
                        if forts[j] == -1:
                            max_captured = max(max_captured, count)
                            break
                        elif forts[j] == 0:
                            count += 1
                        else:
                            break
                    
                    # Move left
                    count = 0
                    for j in range(i - 1, -1, -1):
                        if forts[j] == -1:
                            max_captured = max(max_captured, count)
                            break
                        elif forts[j] == 0:
                            count += 1
                        else:
                            break
            
            return max_captured

    

if __name__ == '__main__':
    s = Solution1()
    print(s.captureForts([1,0,0,-1,0,0,0,0,1]))
    print(s.captureForts([0,0,1,-1]))