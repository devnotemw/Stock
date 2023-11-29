# 종목별 상세 실적 가져오기
# 분기의 실적을 가져오기 위함
import csv
import os

# 현재 스크립트 파일이 있는 디렉토리
current_directory = os.path.dirname(__file__)

# newCodeList.csv 파일의 경로
csv_file_path = os.path.join(current_directory, '../newCodeList.csv')

# CSV 파일에서 데이터 읽어오기
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # 첫 번째 행을 읽어옴
    for row in csv_reader:
        newCodeList = row

# newCodeList를 출력하여 확인
print(newCodeList)
listLen = len(newCodeList)
print(f'{listLen}개의 종목 코드를 불러왔습니다.')