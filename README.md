# Hello Python

헬로 파이썬 :-)

## 참고

[Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

[마크다운 문법](https://heropy.blog/2017/09/30/markdown/)

## 목표
1. 파이썬 설치, 개발환경 설정, 실행, 디버깅 하기
1. 패키지를 설치하고 사용 하기
1. Django 튜토리얼

## 파이썬 설치

1. https://www.python.org/ 윈도우 설치 *//Path 환경변수에 경로 추가 체크*
1. cmd에서 `python --version` 명령어로 버전 확인
    ```
    Python 3.7.4
    ```

## VS Code에서 파이썬 개발환경 설정

1. vs code 설치 및 실행
1. vs code의 확장 프로그램 **Python extension for Visual Studio Code** 설치
1. 파이썬 인터프리터 **Python: Select Interpreter** 설정
    - `ctrl+shift+P` 또는 왼쪽 아래 스테이터스 바 클릭

## Hello World 실행

1. `hello` 폴더 생성 및 `hello.py` 작성

    hello/hello.py :

    ```python
    msg = 'Hello World'
    print(msg)
    ```

1. 터미널에서 `python hello.py` 실행
    ````
    Hello World
    ````

## 환경 설정 및 디버거 실행

1. 왼쪽 사이드바의 디버그 뷰 선택
1. 셋팅 아이콘 클릭 또는 **Debug > Open configurations** 메뉴 사용
1. `"stopOnEntry": true` 설정 추가하여 프로그램이 시작할 때 첫 줄에서 멈춤 설정

    launch.json :
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "stopOnEntry": true,
            }
        ]
    }
    ```

    > "pythonPath": "${workspaceFolder}" 디버깅에 사용할 인터프리터를 가진 특정 폴더 지정할 경우 
    
    > "args": [] 파이선 프로그램을 위한 커맨드라인 아규먼트 지정할 경우

    [더 많은 디버깅 환경설정 보기](https://code.visualstudio.com/docs/python/debugging#_additional-configurations)

1. `F5`로 디버거 실행  
    왼쪽 사이드바 또는 코드 위에 마우스오버하여 `msg` 변수의 현재 값 확인 가능
1. **디버그 콘솔**로 변수 작업 가능
    ```
    msg
    'Hello World'
    msg.capitalize()
    'Hello world'
    msg.split()
    ['Hello', 'World']
    ```
1. **[Logpoints](https://code.visualstudio.com/docs/editor/debugging#_logpoints)** 사용하여 중단점 적중시 로그메시지 콘솔에 띄우기 가능


## 패키지 설치 및 사용

파이썬에는 유용한 코드 라이브러리가 많음. `matplotlib`와 `numpy` 패키지를 사용해서 간단한 그래프 생성해보자.

1. `standardploy.py` 작성

    hello/standardploy.py :
    ``` python
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
    plt.plot(x, np.sin(x))       # Plot the sine of each x point
    plt.show()                   # Display the plot
    ```

    > `as`를 타이핑한 후 엔터치면 자동완성 되는데 싫다면 스페이스 친 후 엔터

1. 디버거에서 파일 실행
    ```
    예외가 발생했습니다. ModuleNotFoundError
    No module named 'matplotlib'
    ```
    유효하지 않은 패키지라는 메시지를 확인할 수 있다.

1. 가상 환경 생성 및 활성화
    ```
    py -3 -m -venv .venv
    ```

1. `matplotlib` 패키지 설치
    ```
    python -m pip install matplotlib
    ```

1. 명령어 `python standardploy.py`로 프로그램 실행. 그래프가 그려진 윈도우 창이 뜬다.

1. 가상 환경 비활성화 하기위해 `deactivate` 터미널에 타이핑

## Django 튜토리얼

Django는 빠르고 안전하고 확장성있는 웹개발을 위한 파이썬 프레임워크. 풍부한 라이브러리 포함.

기본 형태의 페이지 3개를 가진 간단한 Django 앱을 만들어보자.

[Django Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-django)

1. `hello_django` 폴더 생성

1. 다음 명령어로 `env`라는 이름의 가상 환경 생성
    ```
    python -m venv env
    ```
1. `Ctrl+Shift+P`로 **Python: Select Interpreter** 선택

1. `.\env`로 시작하는 가상 환경 선택

1. 새 터미널 열기. 자체 활성화 스크립트를 실행하며 가상 환경이 자동으로 활성화된다. *//커맨드 프롬프트에 `(.venv)`라 보임*

1. 다음 명령어로 가상 환경 위에 Django 설치

    ```
    python -m pip install django
    ```

1. Django 관리 유틸리티인 `django-admin` 생성

    가상 환경이 실행되고 있는 상태에서, 다음 명령어 실행
    
    ```
    django-admin startproject web_project .
    ```

    `manage.py`는 Django 커맨드라인 관리 유틸리티. `python manage.py <command> [options]` 으로 관리 명령 실행 가능.
    
    `web_projcet` 이하에는 다음 파일들이 포함

    - `__init__.py` : 해당 폴더는 파이썬 패키지라는 것을 의미하는 빈 파일

    - `wsgi.py` : WSGI-호환 웹서버 진입 지점 *//?*

    - `settings.py` : 웹 앱 개발 시 Django 프로젝트 설정

    - `urls.py` : Django 프로젝트 목차 포함

1. `python manage.py runserver` 명령어로 Django 개발 서버 시작.

    기본 포트 번호는 8000.
    
    ```
    You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    August 07, 2019 - 18:42:05
    Django version 2.2.4, using settings 'web_project.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```

    브라우저에서 `http://127.0.0.1:8000/`에 접속해 보자.

1. `Ctrl+C`로 서버 정지 

## Django 앱 생성하기

1. `hello_django` 프로젝트 폴더에서 다음 커맨드 실행

    ```
    python manage.py startapp hello
    ```
    
    위 커맨드를 실행하면 `hello` 라는 폴더를 생성함. 그 폴더 아래에는 여러개의 코드 파일과 하나의 폴더가 있음. 그 중에서 `views.py`와 `models.py`를 자주 작업하게 될 거임

    `views.py`는 웹 앱 페이지들을 정의한 함수들을 포함하는 파일

    `models.py`는 데이터 오브젝트들을 정의하는 클래스들을 포함하는 파일

    `migrations` 폴더는 django의 데이터베이스 버전을 관리하는 관리자 유틸리티

    `apps.py`는 앱 환경설정, `admin.py`는 관리자 인터페이스를 생성하기 위한 것, `tests.py`는 테스트를 위한 것.

1. `hello/views.py`를 수정하자. 앱의 홈페이지를 위한 싱글 뷰를 생성한다.

   ```python
    from django.http import HttpResponse

    def home(request):
        return HttpResponse("Hello, Django !! ")
   ``` 

1. `hello/urls.py` 파일을 생성하자. 이 파일은 다른 URL들이 찾는 뷰에 안내하기 위한 패턴들을 지정할 수 있다.

    ```python
    from django.urls import path
    from hello import views

    urlpatterns = [
        path("", views.home, name="home"),
    ]
    ```

    위 코드는 앱(`""`)의 루트 URL을 `views.home` 함수로 매핑하는 하나의 루트가 있다.

1. `web_project` 폴더에도 `urls.py` 파일이 있다. 이 파일은 URL 라우팅을 실제로 다룬다. 해당 파일은 열어서 아래 코드로 수정해보자. 
    
    ```python
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path("", include("hello.urls")),
    ]
    ```

    이 코드는 `hello/urls.py`를 `django.urls.include`를 사용해서 당겨온다. 이런 분리는 한 프로젝트가 여러 앱들을 포함하게 될 때 유용하다.

1. 수정한 파일들을 수정하고, 가상 환경을 활성화 한 후, 개발 서버를 실행해보자. `python manage.py runserver`로 서버를 실행하고, `http://127.0.0.1:8000/`을 열어보자.


## 디버거 런치 프로파일 생성하기

매번 `python manage.py runserver`를 타이핑하기 귀찮을 것이다. VS Code에서 커스터마이징 런치 프로파일을 생성하면 더 쉽게 서버를 생성하고 앱을 테스트 할 수 있다.

1. Debug 뷰(왼쪽에 벌레 아이콘)에서 톱니바퀴 아이콘 눌러 `launch.json`파일 수정하기

    해당 파일에는 디버깅 환경 설정 항목들이 포함되어 있다.

    ```json
    {
        "name": "Python: Django",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/manage.py",
        "console": "integratedTerminal",
        "args": [
            "runserver",
            "--noreload"
        ],
        "django": true
    },
    ```
    
    이 환경설정은 VS Code에게 `"${worksapceFolder}/manage.py"`를 선택된 파이썬 인터프리터와 `args` 리스트에 있는 아규먼트를 사용하여 실행하라고 하는 것이다. 
    
    디버거를 런칭해보면 `python mamage.py runserver --noreload` 커맨드를 가상 환경이 활성화된 터미널에 실행하는 것과 같다. (포트 번호를 `args`에 추가해줘도 됨)
    
    `"django": true`는 VS Code가 Django 페이지 템플릿 디버깅을 가능하게 한다.

1. `launch.json` 을 저장하고, 디버그 환경설정 드랍다운 리스트에서 **Python: Django** 환결 설정을 선택한다.

1. `F5`를 눌러 디버깅 실행. `http://127.0.0.1:8000/`에 접속 가능.

1. `Shift+F5` 눌러 디버깅 종료.

1. 앱을 테스트하기 위해 언제든 디버깅을 시작할 수 있고, 모든 수정된 파일을 자동으로 저장해주는 이점이 있다.


## 디버거 사용해보기

변수 테스트, 디버그 콘솔 페널에서 코드 실행, 디버깅 상에 묘사된 기능들의 이점을 취할 수 있음.

1. `hello/urls.py`의 `urlpatterns` 리스트에 루트 하나 추가

    ```python
    path("hello/<name>", views.hello_there, name="hello_there"),
    ```
    
    `path`의 첫 아규먼트는 name이라 불리는 다양한 문자열을 수용하는 "helle/" 루트를 정의힌다. 문자열은 두번째 아규면트에 기입된 `views.hello_there`함수로 넘겨진다.

    URL 루트는 대소문자 구분함. `/hello/<name>` 이랑 `/Hello/<name>` 이랑 다름.

1. `view.py`에 `hello_there` 함수를 정의하자.
    
    ```python
    import re
    from datetime import datetime
    from django.http import HttpResponse

    def home(request):
        return HttpResponse("Hello, Django!")

    def hello_there(request, name):
        
        now = datetime.now()
        formatted_now = now.strftime("%A, %d %B, %Y at %X")

        match_object = re.match("[a-zA-Z]+", name)

        if match_object:
            clean_name = match_object.group(0)
        else:
            clean_name = "Friend"

        content = "Hello there, " + clean_name + "! It's " + formatted_now
        return HttpResponse(content)
    ```

    URL 루트에서 정의된 `name` 변수는  `hello_there` 함수의 아규먼트로 주어진다. 

    오직 문자로만 이뤄진 이름 아규먼트로 거른다. 이런 코드가 없어도 Django는 자동 필터링함.

1. `now = datetime.now()` 라인에 브레이크 포인트를 설정 (`F9`)

1. 디버깅 시작 (`F5`) 

1. 브라우저에서 `http://127.0.0.1:8000/hello/VSCode` 접속하면 설정한 브레이크포인트에 프로그램이 일시정지함.

1. `now = datetime.now()` 문장을 실행하기 위해 스텝 오버 (`F10`)

    디버그 창 외쪽에서 로컬 변수를 보여주는 **변수** 목록(`now`, `name` 등)과, 그 아래로 **조사식**, **호출 스택**, **중단점** 목록이 보인다. 

    이 변수의 로컬 섹션에서 더블 클릭하거나 `F2`로 변수값을 수정할 수 있음. 

1. **디버그 콘솔** 패널에서 프로그램 최신 상태의 코드를 사용해서 많은 표현식들을 실험해볼 수 있다.

    ```
    now.strftime("%a, %d %B, %Y at %X")
    'Fri, 07 September, 2018 at 07:46:32'
    now.strftime("%a, %d %b, %Y at %X")
    'Fri, 07 Sep, 2018 at 07:46:32'
    now.strftime("%a, %d %b, %y at %X")
    'Fri, 07 Sep, 18 at 07:46:32'
    ```

1. `F5`눌러 프로그램 계속 실행. 브라우저에서 다음과 같은 결과가 나온다.
    
    ```
    Hello there, VSCode ! It's Sunday, 22 September, 2019 at 20:47:44
    ```

1. 브라우저 닫고 디버거 정지(`Shift+F5`)

(계속 ... )