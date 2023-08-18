#강제로 수정
'''
#괄호 Shift
def isCorrect(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
    return 1 if len(stack) == 0 else 0

def solution(s):
    answer = 0

    for i in range(len(s)):
        if isCorrect(s):
            answer += 1
        s = s[1:] + s[:1]
    return answer


s1 = "[](){}"
s2 = "}]()[{"
s3 = "[)(]"
s4 = "}}}"

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
'''

'''
# 주식 가격
def solution(prices):
    size = len(prices)
    answer = [0] * size
    for i in range(size):
        for j in range(i + 1, size):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


print(solution([1, 2, 3, 2, 3]))

'''

'''
#오큰수 구하기
def solution(ar):
    stack = []

    for i in range(len(ar)):
        # 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
        while stack and ar[stack[-1]] < ar[i]:
            ar[stack.pop()] = ar[i]  # 정답 배열에 오큰수를 현재 수열로 저장하기
        stack.append(i)

    while stack:  # 반복문을 다 돌고 나왔는데 스택이 비어 있지 않다면 빌 때까지
        ar[stack.pop()] = -1  # 스 택에 쌓인 index에 -1을 넣기

    result = ""
    for i in range(len(ar)):
        result += str(ar[i]) + " "

    return result


print(solution([3, 5, 2, 7]))
print(solution([9, 5, 4, 8]))
'''


'''
#카드 게임
from collections import deque

def solution(n):
    myqueue = deque()
    for i in range(1, n+1):
        myqueue.append(i)
    while len(myqueue) > 1:     # 카드가 1장 남을 때까지
        myqueue.popleft()       # 맨 위의 카드를 버림
        myqueue.append(myqueue.popleft())   # 맨 위의 카드를 가장 아래 카드 밑으로 이동
    return myqueue[0]   # 마지막으로 남은 카드 출력


print(solution(6))
'''



'''
#Queue를 이용한 기능 개발

def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt > 0: answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
'''


def solution(bridge_length, weight, truck_weights):
    answer = 0

    list = [0]*bridge_length

    while list:  ##list가 존재할때까지
        answer += 1
        list.pop(0)
        #print(list)
        if truck_weights: ##truck_weights가 존재할때까지
            if sum(list) + truck_weights[0] <= weight:
                list.append(truck_weights.pop(0))
                # print(list)
            else:
                list.append(0)
                # print(list)

    # print(answer)
    return answer

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
