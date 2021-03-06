Q. 큰 수의 법칙
  : 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
    단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과할 수 없다.
    배열의 크기 N, 숫자가 더해지는 횟수 M, 연속 합가능수 K가 주어질 때 큰 수의 법칙 결과
   
    ex) [2, 4, 5, 4, 6], M = 8, K = 3 => 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5
   
# 나의 풀이
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort(reverse=True)
max = data[0]
max2 = data[1]

for i in range(1, M+1):
    if(i%(K+1) == 0):
        result += max2
        print(result)
    else:
        result += max
        print(result)

print(result)

# 해답1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
print(result)

# 해답2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)
