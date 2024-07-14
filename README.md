# BE_deploy_hw
백엔드 아기사자 배포세션 과제용 레포

## 배포 순서
1. 레포 포크하기
2. 배포하기

## 로컬에서 실행할 때 사전설정하기 (윈도우)
```bash
# 최초 한 번
pip install virtualenv
virtualenv venv
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
pip3 install virtualenv # pip install virtualenv 도 가능하면 이걸로
virtualenv venv
# 켤 때마다 반복
source venv/bin/activate
# 버전 확인
python -m django —version # 5.0.7
# 마이그레이션, 런서버
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```