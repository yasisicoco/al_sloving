# state 변영인 강사님 
# T = 10  # -> 10개 주어짐
# for tc in range(1, T+1):
#     print(f'#{tc}', end=' ')
#     _ = input()  # 전체 식의 길이
#     cal = input()  # 조작 안하고 단순 for문 쓸거면 굳이 list X
#     # +랑 *가 섞여있어서 map(int 적절하지 X)
#     postfix = ''
#     st = []  # 스택
#     for c in cal:  # 계산식을 앞으로부터 탐색
#         # 1.
#         # 후위표기식 -> 연산자가 뒤로 오게...
#         if c not in '+*':  # + 또는 * (연산자)가 아닐 것
#             # 숫자일 것
#             postfix += c  # 숫자는 그냥 새로운 식에 추가
#         # 연산자
#         else:
#             if not st:  # 스택비어있으면 채워야지
#                 st.append(c)  # push
#                 continue
#             # 스택이 빈 상태면 현재 라인에 접근 X
#             # + * => + +, + *, *, *
#             # 스택 맨위에가 +가 아니고 탐색중인 글자가 *이 아님
#             # 우선순위 문제가 없다면 ++, **, *+
#             #  스택에서 가장 밖에/최신에 있는 데이터
#             if not (st[-1] == '+' and c == '*'):
#                 # top != '+' or top != '*'
#                 # (기존에 스택에 존재하던 연산자가)
#                 # 우선순위가 더 높은 연산자를 만난게 아니라면
#                 while st and not (st[-1] == '+' and c == '*'):
#                     postfix += st.pop()
#             st.append(c)
#             # 새롭게 들어오려는 *이 +를 눌러버리는 효과
#             # 나중에 같은 *이 들어오면 어차파 띠쳐나갈 거지만...
#             # 스택 상에 존재하는 +의 경우엔 마주치게 되면...
#     while st: # 끝으로 스택 안에 잔존하는 연산자들을 식으로 이동
#         postfix += st.pop()
#     # 2.
#     # 후위표기식 -> stack을 통해서 피연산자1, 2를 pop()하고
#     # 나중에 pop된 것 -> 왼쪽 + 연산자 + 먼저 pop된 것 오른쪽
#     # -> 연산 후 다시 stack에 넣고.... 최종적으로 가장 스택에
#     # 마지막으로 남은...
#     st.clear()
#     for p in postfix:
#         if p not in '+*':
#             st.append(int(p))  # 숫자
#         else:
#             pop1 = st.pop()
#             pop2 = st.pop()
#             if p == '+':
#                 st.append(pop2 + pop1)
#             elif p == '*':
#                 st.append(pop2 * pop1)
#     print(st[-1])