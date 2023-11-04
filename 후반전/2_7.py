n = int(input('도착지에 할당된 값을 입력해주세요:' ))
# 인수를 저장할 리스트 변수 설정
factors = []
# n을 인수분해하여 인수들을 리스트에 저장
for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)

# 약수들을 가장 작은 약수와 가장 큰 약수부터 차례대로 묶어서 저장
factor_pairs = []
left, right = 0, len(factors) - 1
while left <= right:
    if left == right:
        # 길이가 홀수일 때 가운데 값을 두 번 저장 ex)16의 경우 1,2,4,8,16 이기 때문에 4를 두번 저장
        factor_pairs.append([factors[left], factors[left]])
    else:
        factor_pairs.append([factors[left], factors[right]])
    left += 1
    right -= 1

# 묶음들을 최소의 합으로 정렬
factor_pairs.sort(key=lambda pair: sum(pair))

# 결과 출력
print(factor_pairs)

sums = [sum(pair) for pair in factor_pairs]
min_sum = min(sums)
print(min_sum-2)