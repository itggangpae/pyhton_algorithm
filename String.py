# 회문
"""
import re
def isPalindrome(s) -> bool:
    #영문자를 모두 대문자로 변경
    s = s.upper()
    #문자와 숫자가 아니면 제거
    s = re.sub('[^A-Z가-힣0-9]', '', s)
    return s == s[::-1]

print(isPalindrome("우영우"))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
"""

"""
#문자열 뒤집기
#python에는 문자열 뒤집기 함수가 존재합니다.
import copy
def reverseStrtng(s):
    s_copy = copy.deepcopy(s)
    left = 0
    right = len(s_copy) - 1
    while left < right:
        temp = s_copy[left]
        s_copy[left] = s_copy[right]
        s_copy[right] = temp
        left += 1
        right -= 1
    return s_copy

print(reverseStrtng(['h', 'e', 'l', 'l', 'o']))
print(reverseStrtng(['H', 'a', 'n', 'n', 'a', 'h']))
"""

"""
#가장 흔한 단어 찾기
import re
import collections

def solution(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
    .lower().split()
             if word not in banned]

    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]
#문장
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
#금지어(stopword)
banned = ["hit"]
print(solution(paragraph, banned))
"""

"""
#그룹 애너그램
import collections
def solution(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

print(solution(["eat", "tea", "tan", "ate", "nat", "bat"]))
"""

"""
#가장 긴 팰린드롬
def solution(s):
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
    return result

print(solution("babad"))
print(solution("cbbd"))
"""


"""
#문자열 압축
def solution(s):
    answer = len(s)
    for x in range(1, len(s) // 2 + 1):
        comp_len = 0
        comp = ''
        cnt = 1
        for i in range(0, len(s) + 1, x):
            temp = s[i:i + x]
            if comp == temp:
                cnt += 1
            elif comp != temp:
                comp_len += len(temp)
                if cnt > 1: comp_len += len(str(cnt))
                cnt = 1
                comp = temp
        answer = min(answer, comp_len)

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
"""