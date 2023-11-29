# 주식정보 시가총액 및 실적 크롤링하기

유튜브 강의 시청 및 실습 - 나도코딩, <주식정보 크롤링하기 (파이썬)> [유튜브 강의 링크](https://www.youtube.com/watch?v=ZDh1C7qw0Rs&t=191s)  

네이버 페이 증권에서 시가총액 기준 내림차순으로, 종목별 실적을 크롤링해옵니다.

해당 코드에서는 [상장수식수(천), 시가총액(억), 영업이익(억), 당기순이익(억), PER(배), ROE(%)] 옵션 6가지를 선택해서 크롤링해옵니다.

해당 코드를 실행하면 '23-11-28 시가총액.csv'와 같이 오늘 날짜를 기준으로 파일명이 저장됩니다.


## <의존성 설치 방법>
다른 사용자가 Git에서 프로젝트를 클론한 후에는 다음 단계를 따라 해당 프로젝트의 의존성을 가상 환경에 설치할 수 있습니다.
### 요구사항: Python 3.9 version 이상


### 1. 가상 환경 생성
Windows:
```
python -m venv myvenv
```

macOS:
```
python3 -m venv myvenv
```


### 2. 가상 환경 활성화
Windows:
```
myvenv\Scripts\activate
```

macOS/Linux:
```
source myvenv/bin/activate
```
또는 shift + ctrl + p 단축키(Mac 단축키: ctrl + cmd + p)를 누른 후 "Python: 인터프린터 선택-생성된 가상 환경 인터프리터 선택" - 후 터미널을 실행시킬 수도 있습니다.

가상환경이 정상적으로 활성화 되었다면 터미널을 켰을 때 (myvenv)와 같이 표시됩니다.


### 3. requirements.txt에 명시된 패키지 설치
bash
```
pip install -r requirements.txt
```
이 명령은 requirements.txt 파일에 나열된 모든 패키지와 해당 버전을 가상 환경에 설치합니다.
***이때 명령어는 root 경로, 즉 requirements.txt 파일이 있는 디렉토리에서 수행해야합니다.**


### 4. 프로젝트 실행 또는 개발
필요한 모듈은 정상적으로 설치되었으므로, 프로젝트를 실행해보거나 추가 개발을 진행합니다.

