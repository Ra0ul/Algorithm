import sys

n = int(sys.stdin.readline())
grade_list = list(map(int, sys.stdin.readline().split()))
grade_list.sort()

max_grade = max(grade_list)

answer = (sum(grade_list) / max_grade * 100) / n
print(answer)