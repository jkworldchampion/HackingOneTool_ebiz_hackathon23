import numpy as np

# 블럭 받침대 사이즈 n값 입력받기
n = int(input("블럭 받침대 사이즈를 입력해주세요 (n x n): "))

# 블럭배열 변수 지정
skyline = []
# 각 행별로 블럭 높이 입력받기
for i in range(n):
    # 공백 없이 문자열로 높이를 입력받기
    row_str = input(f"{i+1}번째 행의 블럭 높이를 입력해주세요 :")
    # n개이상의 문자가 입력될 경우 오류 표시 
    if len(row_str) != n:
        raise ValueError(f"각 행은 정확히 {n}개의 높이 값을 가져야 합니다.")
    if not row_str.isdigit():
        raise ValueError("입력된 값 중 숫자가 아닌 문자가 포함되어 있습니다.")
    # 문자열의 각 문자를 정수형 리스트로 변환
    row = [int(height_str) for height_str in row_str]
    skyline.append(row)

skyline = np.array(skyline)
print(skyline)

# 각 행과 각 열의 최댓값 계산
max_val_rows = np.max(skyline, axis=1)
max_val_columns = np.max(skyline, axis=0)

# 추가로 사용할 수 있는 레고 블록의 수를 계산
additional_blocks = 0

# 각 칸에 대해 추가할 수 있는 레고 블록의 수 계산
for i in range(n):
    for j in range(n):
        # 각 칸의 최대 높이는 그 칸이 포함된 행과 열의 최대 높이 중 작은 값
        max_val_for_cell = min(max_val_rows[i], max_val_columns[j])
        # 현재 칸에 추가로 쌓을 수 있는 블록 수를 계산
        additional_blocks += max_val_for_cell - skyline[i, j]

print("동서남북에서 보이는 도시의 높이를 유지하면서 사용할 수 있는 최대 추가 블록 수:", additional_blocks)