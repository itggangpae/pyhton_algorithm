#!/usr/bin/env python
# coding: utf-8


import collections

def maxSlidingWindow(nums, k):
    results = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue

        # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        # 최대값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float('-inf')
    return results

print(maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(maxSlidingWindow(nums=[1], k=1))


# ## 부분 문자열 최소 윈도우

# In[4]:


import collections

def minWindow(s, t):
    need = collections.Counter(t)
    missing = len(t)
    left = start = end = 0

    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1

        # 필요 문자가 0이면 왼쪽 포인터 이동 판단
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1

            if not end or right - left <= end - start:
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(minWindow(s = "a", t = "a"))
print(minWindow(s = "a", t = "aa"))


# ## 가장 긴 반복 문자 대체

# In[5]:


import collections

def characterReplacement(s, k):
    left = right = 0
    counts = collections.Counter()
    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1
        # 가장 흔하게 등장하는 문자 탐색
        max_char_n = counts.most_common(1)[0][1]

        # k 초과시 왼쪽 포인터 이동
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right - left

print(characterReplacement(s="AAABBC", k=2))
print(characterReplacement(s="ABAB", k=2))
print(characterReplacement(s="AABABBA", k=1))


# ## DNA 비밀번호 수

# In[7]:


checkArr = [0] * 4
myArr = [0] * 4
checkSecret = 0

# 함수 정의
def myadd(c): #새로 들어온 문자를 처리하는 함수
    global checkArr,myArr,checkSecret
    if c == 'A':
        myArr[0] += 1
        if myArr[0] == checkArr[0]:
            checkSecret += 1
    elif c == 'C':
        myArr[1] += 1
        if myArr[1] == checkArr[1]:
            checkSecret += 1
    elif c == 'G':
        myArr[2] += 1
        if myArr[2] == checkArr[2]:
            checkSecret += 1
    elif c == 'T':
        myArr[3] += 1
        if myArr[3] == checkArr[3]:
            checkSecret += 1

def myremove(c): #제거되는 문자를 처리하는 함수
    global checkArr, myArr, checkSecret
    if c == 'A':
        if myArr[0] == checkArr[0]:
            checkSecret -= 1
        myArr[0] -= 1
    elif c == 'C':
        if myArr[1] == checkArr[1]:
            checkSecret -= 1
        myArr[1] -= 1
    elif c == 'G':
        if myArr[2] == checkArr[2]:
            checkSecret -= 1
        myArr[2] -= 1
    elif c == 'T':
        if myArr[3] == checkArr[3]:
            checkSecret -= 1
        myArr[3] -= 1

'''
S, P = 9, 8
Result = 0
A = "CCTGGATTG"
checkArr = [2, 0, 1, 1]
'''

S, P = 4, 2
Result = 0
A = "GATA"
checkArr = [1, 0, 0, 1]

for i in range(4):
    if checkArr[i] == 0:
        checkSecret += 1
for i in range(P):  #초기 P 부분 문자열 처리 부분
    myadd(A[i])
    
if checkSecret == 4: #4자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
    Result += 1
    
for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1
print(Result)


# In[ ]:




