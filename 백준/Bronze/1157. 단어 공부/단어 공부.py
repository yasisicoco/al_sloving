import sys

S = sys.stdin.readline().strip().upper()
words = {}
for ch in S:
    words[ch] = words.get(ch, 0) + 1

max_count = max(words.values())
max_keys = [k for k, v in words.items() if v == max_count]

print('?' if len(max_keys) > 1 else max_keys[0])
