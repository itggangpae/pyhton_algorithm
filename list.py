#!/usr/bin/env python
# coding: utf-8

# ## 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴

# In[2]:


# 브루트 포스를 이용하는 방식
def bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
print(bruteforce(nums, 9))


# In[3]:


#in 연산자 이용
def inOperator(nums, target):
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

nums = [2, 7, 11, 15]
print(inOperator(nums, 9))


# In[4]:


#Dictionary 이용
def dictionary(nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

nums = [2, 7, 11, 15]
print(dictionary(nums, 9))


# In[6]:


#조회 구조 개선
def searchAdvance(nums, target):
    nums_map = {}
    # 하나의 `for`문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

nums = [2, 7, 11, 15]
print(searchAdvance(nums, 9))


# In[7]:


#2개의 포인터 이용
def twoPointer(nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

nums = [2, 7, 11, 15]
print(twoPointer(nums, 9))


# In[8]:


def twoPointer(nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

nums = [2, 7, 11, 15]
print(twoPointer(nums, 9))


# In[ ]:





# ## 주식의 팔고 사기 좋은 시점 찾기

# In[9]:


import sys


def solution(prices):
    profit = 0
    min_price = sys.maxsize

    # 최소값과 최대값 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


print(solution([7, 1, 5, 3, 6, 4]))
print(solution([7, 6, 4, 3, 1]))


# In[ ]:





# ## 주몽의 명령

# In[10]:


def solution(inputs, hap):
    #데이터 정렬
    inputs.sort()
    count = int(0)
    i = int(0)
    j = int(len(inputs) - 1)
    while i < j:  # 투 포인터 이동 원칙 따라 포인터를 이동하며 처리
        if inputs[i] + inputs[j] < hap:
            i += 1
        elif inputs[i] + inputs[j] > hap:
            j -= 1
        else:
            count += 1
            i += 1
            j -= 1
    return count


print(solution([2, 7, 4, 1, 5, 3], 9))


# In[ ]:





# ## 달팽이

# In[12]:


def solution():
    snail = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    end = 5
    k = 1
    right = -1
    bottom = 0
    top = 1
    
    for i in range(5, 0, -1):
        for j in range(0, end, 1):
            right += top
            snail[bottom][right] = k
            k += 1

        end -= 1

        for j in range(0, end, 1):
            bottom += top
            snail[bottom][right] = k
            k += 1

        top = top * (-1)

    return snail


print(solution())


# In[ ]:





# ## 행렬의 곱

# In[13]:


def solution(ar1, ar2):
    answer = [[0 for _ in range(len(ar2[0]))] for _ in range(len(ar1))]
    for i in range(len(ar1)):
        for j in range(len(ar2[0])):
            for k in range(len(ar1[0])):
                answer[i][j] += (ar1[i][k] * ar2[k][j])
    return answer


print(solution([[1,4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

