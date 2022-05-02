visited = {}

def jump(platform, i):
    if (i < 0 or i >= len(platform)):
        return 1
    elif (i in visited):
        return 0
    else:
        jump_size = int(platform[i])

        visited[i] = True
      
        sum = 0
        for k in range(1, jump_size+1):
            sum += jump(platform, i - k) + jump(platform, i + k)
        
        return sum

platform = input().split()
initial  = int(input())-1

if (jump(platform, initial) > 0):
    print("Saiu da plataforma")
else:
    print("Loop")