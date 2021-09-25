# Flask Web Service

## 1. 가상환경 설정

1. 작업할 폴더를 만들어 준다.
   

2. 터미널> vscode열고 터미널실행 후 만들어진 폴더로 경로 설정

   ![image-20210924140950957](https://user-images.githubusercontent.com/85037782/134764141-d3e3cedb-6348-460f-8a8d-de7942fa6831.png)

3. 터미널> pip3 install virtualenv

   ![image-20210924141012675](https://user-images.githubusercontent.com/85037782/134764152-55dafa99-fe9c-4b70-a581-d9af2ad444c7.png)

4. VsCode Explorer에서 해당 폴더 열기
   

5. 가상환경 이름 설정 

   터미널> virtual env

   ![image-20210924141251421](https://user-images.githubusercontent.com/85037782/134764166-d08e49ec-aea4-4e7e-baab-a4e6c13ef041.png)

   ![image-20210924141345377](https://user-images.githubusercontent.com/85037782/134764168-f7370712-9961-4a4e-9efd-4a30a5acfdba.png)

   가상환경 생성 완료

6. 가상환경 실행


   터미널> env\Scripts\activate

   ![image-20210924141649699](https://user-images.githubusercontent.com/85037782/134764169-57d3c5f5-8aa7-499e-9660-e7aa2580934e.png)

   (env)로 가상환경 상태임을 확인
   

7. flask-sqlalchemy 설치

   터미널> pip install flask flask-sqlalchemy

   ![image-20210924143042054](https://user-images.githubusercontent.com/85037782/134764176-3fdde277-0c0c-4b89-b54d-4d118086bbb0.png)

8.  환경설정 완료

   ### ※ 오류 vscode 터미널 powershell 권한 에러

   1. windows powershell 관리자 실행

      ![image-20210924141939201](https://user-images.githubusercontent.com/85037782/134764170-20ccf3f3-fb82-4efc-a3b6-12dca4c4024a.png)

   2. Get-ExecutionPolicy

      ![image-20210924142215997](https://user-images.githubusercontent.com/85037782/134764171-8313b052-25a2-458d-9e9a-0bbb81f3bf44.png)

      Restricted로 되어있는경우 권한 에러 발생

   3. Set-ExecutionPolicy Unrestricted

      ![image-20210924142554865](https://user-images.githubusercontent.com/85037782/134764174-1493a75a-9a24-4725-a7dd-d2be251f8305.png)

      Unrestricted로 권한 변경 후 y

   





## 2. 웹서버 구축

1. 프로젝트 폴더에 app.py 파일 생성

   ![image-20210924143518476](https://user-images.githubusercontent.com/85037782/134764177-505fa0b6-18ae-4c56-8cc6-e7eb0825d94a.png)
   

2.  서버 만들기

   ```python
   from flask import Flask
   app = Flask(__name__)
   @app.route('/')
   def index():
       return "안녕하세요.<h1>홈페이지 입니다.</h1>"
   ```

   

3.  실행확인

   터미널> flask run

   ![image-20210924144742193](https://user-images.githubusercontent.com/85037782/134764178-4cb00e39-6866-4e54-b8da-9ebea007e99e.png)

   주소 Ctrl + 클릭

4.  웹페이지 확인

      ![image-20210924145014442](https://user-images.githubusercontent.com/85037782/134764180-6ea358b2-f00b-47d1-af70-bf61c6810f79.png)





## 3. html 렌더링하기

1. html 파일을 보관할 templates 디렉토리 생성

      ![image-20210924145720547](https://user-images.githubusercontent.com/85037782/134764181-a9f5d799-1b3b-48f3-8748-adab25c7079f.png)

2. css, img등을 보관할 static 디렉토리 생성

      ![image-20210924145814223](https://user-images.githubusercontent.com/85037782/134764182-22e4afb5-44e3-4104-9446-ac47b60d68e2.png)

3. 모듈 추가

   ```
   from flask import Flask, render_template, request
   ```

   html을 렌더링 하기 위해 render_template 추가.
