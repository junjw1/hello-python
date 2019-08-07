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

(계속)