# 사용자 입력을 받습니다.
input_string = input("글자를 입력해주세요: ")
spanish_alphabet = []  # 스페인어 알파벳을 담을 리스트

i = 0  # 문자열을 순회할 인덱스 변수
while i < len(input_string):
    # 쉼표가 나오고 앞 문자가 모음이면 합칩니다.
    if i > 0 and input_string[i] == ',' and input_string[i - 1] in 'aeiou':
        spanish_alphabet[-1] += ','
        i += 1
    # 물결표시가 나오고 앞 문자가 'n'이면 합칩니다.
    elif i > 0 and input_string[i] == '~' and input_string[i - 1] == 'n':
        spanish_alphabet[-1] += '~'
        i += 1
    # 점 두 개가 나오고 앞 문자가 'u'이면 합칩니다.
    elif i > 0 and input_string[i:i + 2] == '..' and input_string[i - 1] == 'u':
        spanish_alphabet[-1] += '..'
        i += 2
    else:
        # 위 조건에 해당하지 않으면 현재 문자를 리스트에 추가합니다.
        spanish_alphabet.append(input_string[i])
        i += 1
# 결과를 출력합니다.
len(spanish_alphabet)
