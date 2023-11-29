# 종목 코드만 가져오기
# 종목 코드를 통해서 해당 종목 상세 페이지에 접근하면 연간 데이터가 아닌 분기별 세부 실적을 확인할 수 있다.
# 종목 코드를 리스트화하여 csv 파일로 저장한다.
# 종목 코드를 차례로 불러와 상세 실적을 가져오기 위해 특정 종목 URL을 크롤링하기 위해 코드 리스트를 가져온다.


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv

browser = webdriver.Chrome()
# 자동화 프로그램 내 Chrome 실행
browser.maximize_window()
# 창 최대화

# 1. 페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='

browser.get(url)


# 2. 종목의 코드 리스트 생성
newCodeList = []

# 3. 반복문 - 1부터 45번 페이지까지 반복문을 돕니다. - td 2부터 80까지 반복문을 돕니다.
# tr [2]가 첫번째 코드, [78]이 마지막 코드를 가지고 있는 요소입니다. 요소에 href 가 없으면 pass합니다.
for idx in range(1, 45): 
    browser.get(url + str(idx))
    for i in range(2, 81):
        try:
            itemPath = browser.find_element(By.XPATH, f'//*[@id="contentarea"]/div[3]/table[1]/tbody/tr[{i}]/td[2]/a')
            newCode = (str(itemPath.get_attribute('href')))[-6:]
            newCodeList.append(newCode)
        except NoSuchElementException:
            pass

# 4. 추출된 종목 코드의 수를 알려줍니다.
listLen = len(newCodeList)
print(f'{listLen}개 종목 코드가 검색되었습니다.')

# 자동화 브라우저 종료
browser.quit()


# CSV 파일에 저장
csv_file_path = 'newCodeList.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # 데이터 가로로 한줄로 작성
    csv_writer.writerow(newCodeList)

# 엑셀 저장용(세로 방향 1줄 저장)
# csv_file_path = 'newCodeList.csv'
# with open(csv_file_path, 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)

#     for item in newCodeList:
#         csv_writer.writerow([item])

