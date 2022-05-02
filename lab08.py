N = int(input())

phrases = []
dict = {}

special_symbols = ".:,;!?"

for _ in range(N):
    phrase = input()
    for i in range(len(special_symbols)):
        phrase = phrase.replace(special_symbols[i], "")
    phrases.append(phrase.lower())

for phrase in phrases:
    split_phrase = phrase.split(" ")
    for i in range(len(split_phrase)):
        word = split_phrase[i]

        # checks if is a palindrome
        palindrome = True

        for k in range(len(word)//2):
            if (word[k] != word[len(word)-k-1]):
                palindrome = False
                break

        if (palindrome):
            count = 0
            if (word in dict):
                count = dict[split_phrase[i]]
            count += 1
            dict[split_phrase[i]] = count

for (word, count) in dict.items():
    print(word, count)