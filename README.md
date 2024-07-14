# BE_deploy_hw
백엔드 아기사자 배포세션 과제용 레포

## 배포 순서
1. 레포 포크하기
2. 배포하기 ㅎ

## 로컬에서 실행할 때 사전설정하기 (윈도우)
```bash
# 최초 한 번
pip install virtualenv
virtualenv venv
source venv/Scripst/activate
pip install -r requirements.txt
# 백엔드 톡방에서 .env 파일 다운
# .env 파일 manage.py와 같은 경로에 넣어주기

# 켤 때마다 반복
source venv/Scripts/activate

# 버전 확인
python -m django —version # 5.0.7

# 마이그레이션, 런서버
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 로컬에서 실행할 때 사전설정하기 (맥)
```zsh
# 최초 한 번
pip3 install virtualenv # 안되면 pip install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt # 안되면 pip install -r requirements.txt
# 백엔드 톡방에서 .env 파일 다운
# .env 파일 manage.py와 같은 경로에 넣어주기

# 켤 때마다 반복
source venv/bin/activate

# 버전 확인
python -m django —version # 5.0.7

# 마이그레이션, 런서버
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```