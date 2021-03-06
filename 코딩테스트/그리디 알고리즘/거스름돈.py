Q. 거스름돈 계산
    거스름돈 500원, 100원, 50원, 10원 단위
    거슬러줘야 할 동전의 최소 개수 구하기
    
 # 나의 풀이
 def calc_change(change):
    cnt_500 = change//500
    cnt_100 = change%500//100
    cnt_50 = change%500%100//50
    cnt_10 = change%500%100%50//10
    
    print(cnt_500+cnt_100+cnt_50+cnt_10)

calc_change(1260)

# 해답
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n//coin
    n %= coin

print(count)
