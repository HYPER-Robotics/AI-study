# 이번에 배운 점

1. **venv 사용법**: 프로젝트마다 Python 패키지와 버전을 분리할 수 있다. 가상환경 폴더를 `.gitignore`에 넣지 않으면 `git add .` 할 때 패키지까지 커밋 대상에 포함될 수 있다.

2. **requirements.txt 만들기**: 가상환경을 활성화하고 `python -m pip freeze > requirements.txt`를 실행하면 설치된 패키지와 버전을 저장할 수 있다. 다른 환경에서는 `python -m pip install -r requirements.txt`로 다시 설치하면 된다.

3. **.gitignore 적용 방식**: 상위 폴더와 하위 폴더의 규칙이 함께 적용된다. `*-venv/`는 `week1-venv`에만 해당하고, `*venv/`는 `week1venv`도 포함하므로 실제 폴더 이름에 맞게 작성해야 한다.

4. **데이터 분석과 시각화**: pandas로 CSV를 읽어 데이터 개수, 기록 시간, 평균·최대 속도를 계산하고, Matplotlib으로 시간에 따른 속도 그래프를 PNG로 저장할 수 있다. 그래프에는 제목과 축 이름, 단위를 표시해야 결과를 이해하기 쉽다.