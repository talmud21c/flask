# Flask Web Service

## 1. 가상환경 설정

1. 작업할 폴더를 만들어 준다.
   

2. 터미널> vscode열고 터미널실행 후 만들어진 폴더로 경로 설정
   ![image-20210924140950957](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924140950957.png)

3. 터미널> pip3 install virtualenv
   ![image-20210924141012675](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924141012675.png)

4. VsCode Explorer에서 해당 폴더 열기
   

5. 가상환경 이름 설정 

   터미널> virtual env

   ![image-20210924141251421](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924141251421.png)

   ![image-20210924141345377](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924141345377.png)
   가상환경 생성 완료

6. 가상환경 실행


   터미널> env\Scripts\activate
   ![image-20210924141649699](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924141649699.png)

   (env)로 가상환경 상태임을 확인
   

7. flask-sqlalchemy 설치

   터미널> pip install flask flask-sqlalchemy
   ![image-20210924143042054](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924143042054.png)

8.  환경설정 완료

   ### ※ 오류 vscode 터미널 powershell 권한 에러

   1. windows powershell 관리자 실행

   ![image-20210924141939201](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924141939201.png)

   2. Get-ExecutionPolicy
      ![image-20210924142215997](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924142215997.png)
      Restricted로 되어있는경우 권한 에러 발생

   3. Set-ExecutionPolicy Unrestricted
      ![image-20210924142554865](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924142554865.png)

      Unrestricted로 권한 변경 후 y

   





## 2. 웹서버 구축

1. 프로젝트 폴더에 app.py 파일 생성

   ![image-20210924143518476](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924143518476.png)
   

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
   ![image-20210924144742193](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924144742193.png)
   주소 Ctrl + 클릭

4.  웹페이지 확인
   ![image-20210924145014442](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924145014442.png)





## 3. html 렌더링하기

1. html 파일을 보관할 templates 디렉토리 생성
   ![image-20210924145720547](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924145720547.png)

2. css, img등을 보관할 static 디렉토리 생성
   ![image-20210924145814223](C:\Users\82107\AppData\Roaming\Typora\typora-user-images\image-20210924145814223.png)

3. 모듈 추가

   ```
   from flask import Flask, render_template, request
   ```

   html을 렌더링 하기 위해 render_template 추가.