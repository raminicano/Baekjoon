
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

data = input()
count = 0

import re
    
# 크로아티아 알파벳  찾기
for i in li:
    data, num = re.subn(i, ' ', data)   # 띄어쓰기를 줘서 사라져도 인식하지 못하게 함
    count += num

# 남은 알파벳 개수 세서 더하기
count += len(data.replace(' ', '')) # 공백 준거 다시 삭제함

print(count)
