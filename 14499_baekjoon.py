import sys
input = sys.stdin.readline

class Dice:
    
    def __init__(self):
        self.bottom = 0
        self.top = 0
        self.right = 0
        self.left = 0
        self.front = 0
        self.back = 0
        
    def move(self, n):
        t_bottom = self.bottom
        t_top = self.top
        t_right = self.right
        t_left = self.left
        t_front = self.front
        t_back = self.back

        if( n== 1):
            self.bottom = t_right
            self.left = t_bottom
            self.right = t_top
            self.top = t_left
        elif(n == 2):
            self.bottom = t_left
            self.right = t_bottom
            self.left = t_top
            self.top = t_right
        elif(n == 3):
            self.bottom = t_back
            self.front = t_bottom
            self.back = t_top
            self.top = t_front
        else:
            self.bottom = t_front
            self.front = t_top
            self.top = t_back
            self.back = t_bottom
    
n, m, x, y, k = map(int, input().split())
graph = []


for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

order = list(map(int, input().split()))

dice = Dice()

move = [(0,1), (0,-1), (-1,0), (1,0)]

for i in order:
    
    dx = x + move[i-1][0]
    dy = y + move[i-1][1]
    
    if(dx < 0 or dy < 0 or dx >= n or dy >= m):
        continue
    
    dice.move(i)
    
    if(graph[dx][dy] == 0):
        graph[dx][dy] = dice.bottom
    else:
        dice.bottom = graph[dx][dy]
        graph[dx][dy] = 0
    
    x = dx
    y = dy
    print(dice.top)