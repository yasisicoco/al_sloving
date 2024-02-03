N = int(input())
one = set()
word = []
for i in range(N):
    word = input()
    one.add(word)
# print(one)
 
world_lst = list(one) # 셋 one을 리스트로 만들기
world_lst.sort() # 오름차순 정렬

len_lst = []
word_lst = []
new_num = len(world_lst) # 새로운 길이 생성

for n in range(new_num):
    word_lst.append(world_lst[n])
    len_lst.append(len(world_lst[n]))

# word_lst.sort()
# len_lst.sort()
# print(word_lst, len_lst)

for i in range(new_num-1, 0, -1):
    for j in range(i):
        if len_lst[j] > len_lst[j+1]:
            len_lst[j], len_lst[j+1] = len_lst[j+1], len_lst[j]
            word_lst[j], word_lst[j+1] = word_lst[j+1], word_lst[j]

for result in word_lst:
    print(result)