import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = dict()
for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

wordList = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word, _ in wordList:
    print(word)