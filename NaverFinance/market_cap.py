# python 프로젝트는 node js 환경과 다르게 npm init 으로 의존성 관리를 하지 않는다. 가상 환경을 통해서 프로젝트 별 필요한 모듈을 설치한다.
# 가상 환경 생성: python -m venv myenv
# 가상 환경 활성화: myenv\Scripts\activate 활성화되면 (myenv) 가 터미널에 활성됨을 확인할 수 있다. 활성화 후 모듈을 설치하고, 프로젝트를 완성한다.
# 의존성 관리: pip freeze > requirements.txt 현재 환경에 설치된 패키지 목록을 'requirements.txt'로 저장한다. 
# 가상 환경 비활성화: deactivate requirement.txt 파일에 패키지의 이름과 버전이 정상적으로 명시되어 있다면 가상 환경을 비활성화 한다.


# 설치된 모듈: pandas, selenium, webdrive_manager, lxml
# webdrive_manager 의 경우 chrome 버전에 맞는 chrome driver를 설치한다. chrome driver 를 별도로 설치했다면 해당 모듈은 설치할 필요가 없다.
# 터미널에 코드를 붙여넣어 실행하려면 먼저 터미널에 python 을 입력해주어야 한다.


from datetime import datetime
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

now = datetime.now()
today = str(now.date())

browser = webdriver.Chrome()
# 자동화 프로그램 내 Chrome 실행
browser.maximize_window()
# 창 최대화

# 1. 페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='

browser.get(url)

# 2. 조회 항목 초기화(체크되어 있는 항목 체크 해제)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): # 체크된 상태라면
        checkbox.click() # 클릭 (체크 해제)

# 3. 조회 항목 설정(원하는 항목)
items_to_select = ['상장주식수', '시가총액', '영업이익', '당기순이익', 'PER', 'ROE']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..') # 부모 element
    label = parent.find_element(By.TAG_NAME, 'label') # 부모 element 에서 tag name 이 laber 인 값을 찾음
    # print(label.text) # 이름 확인
    if label.text in items_to_select: # 선택 항목과 일치한다면
        checkbox.click() #체크

# 4. 적용하기 클릭
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1, 50): # 1이상 50 미만 페이지 반복
    # 사전 작업: 페이지 이동
    browser.get(url + str(idx)) # http://naver.com ... &page=2


    # 5. 데이터 추출
    df = pd.read_html(browser.page_source)[1]
    # len(df) 를 실행해보면 3개의 테이블이 저장되어있는데, 이 중에서 df[1] 테이블이 원하는 값임을 알 수 있다.

    df.dropna(axis='index', how='all', inplace=True)
    # Nan 값이 많은데, 이렇게 불필요한 값들을 날리는 작업을 한다.
    # index: row 를 기준으로 row 전체(all)가 비어있다면 해당 행을 지운다. (any: 하나라도 있으면 해당 row를 지운다.)
    # inplace = True 옵션은 값을 지우고 df에 반영한다.

    df.dropna(axis='columns', how='all', inplace=True)
    # columns: columns 를 기준으로 columns 전체(all)가 비어있다면 해당 열을 지운다. (any: 하나라도 있으면 해당 columns를 지운다.)
    if len(df) == 0: # 더 이상 가져올 데이터가 없으면? 반복문 종료
        break

    # 6. 파일 저장
    # 파일의 유무 확인은 os 모듈을 통해 수행함.
    f_name = f'{today} 시가총액.csv'
    # 파일 이름 지정: f-string 문법


    if os.path.exists(f_name): #파일이 있다면? 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    # 한글이 깨지지 않기 위해 인코딩 설정, 색인은 생성하지 않고, append 모드: 1페이지가 이미 존재한다면, 뒤에 따라오는 2-3 페이지들은 append 해서 추가
    else: # 파일이 없다면? 헤더 포함
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
    # 모드 기본값은 쓰기 모드, 헤더 옵션 기본값은 True

    print(f'{idx} 페이지 완료')


browser.quit() # 브라우저 종료
