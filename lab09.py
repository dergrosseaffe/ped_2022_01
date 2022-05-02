N = int(input())

dict = {}

for _ in range(N):
    for i in range(5):
        player = input()
        count = 0
        if (player in dict):
            count = dict[player]
        count += 6-i
        if (i > 0):
            count -= 1
        dict[player] = count

counters = []
reverse_dict = {}
for (word, count) in dict.items():
    counters.append(count)
    reverse_dict[count] = word

for c in sorted(counters, reverse=True):
    print(reverse_dict[c] + ":", c)