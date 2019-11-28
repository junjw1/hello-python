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

1. https://www.python.org/ 윈도우 설치 *// Path 환경변수에 경로 추가 체크했음*
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

1. `00-hello` 폴더 생성 및 `hello.py` 작성

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

1. `01-hello-django` 폴더 생성

1. 다음 명령어로 `env`라는 이름의 가상 환경 생성
    ```
    python -m venv env
    ```
1. `Ctrl+Shift+P`로 **Python: Select Interpreter** 선택

1. `.\env`로 시작하는 가상 환경 선택

1. 새 터미널 열기. 자체 활성화 스크립트를 실행하며 가상 환경이 자동으로 활성화된다. *// 커맨드 프롬프트에 `(.venv)`라 보임*

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

    - `wsgi.py` : WSGI-호환 웹서버 진입 지점 *// ? 이게 뭐지 ?*

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

1. `01-hello-django` 프로젝트 폴더에서 다음 커맨드 실행

    ```
    ..\01-hello-django>python manage.py startapp hello
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

## HTML과 Vue.js코드로 todo 앱 만들기

Vue.js의 핵심은 **간단한 템플릿 구문을 사용해 선언적으로 DOM에 데이터를 렌더링하는 것**이다.

[Vue.js 가이드](https://kr.vuejs.org/v2/guide/)

DOM은 문서(HTML, XML)의 구조화된 표현을 제공하고, 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공한다.

[DOM이란?](https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model/%EC%86%8C%EA%B0%9C) *// dom 설명이 엄청 추상적이네.. 이해하기 힘듦.. 반복해서 읽으니 이해될듯 말듯*

[DOM이란? 2](https://shldhee.github.io/2018/04/08/DOM/) 

`02-html-todo/todo.html` 문서

```
생략
```

## Django 프로젝트 뼈대 완성하기

1. `03-django-todo` 폴더 생성 및 가상환경 생성 및 활성화 하기

    `>python -m venv env`

    ```
    ..\03-django-todo>python -m venv env
    ```

    `03-django-todo/env` 폴더로 가상환경이 생성됨
    
    `Ctrl+Shift+P`를 눌러 **Python: Select Interpreter** 선택하여 `.\env`로 시작하는 가상 환경 선택하기. *// ? 왜 안보이지 ? 해당 `03-django-todo` 폴더가 최상위가 아니라서 그런가봄*

    `activate` 가상환경 활성화 스크립트 직접 실행하여 가상환경 직접 활성화

    ```

    `>env\Scripts\activate`
    
    ..\03-django-todo>env\Scripts\activate

    (env) ..\03-django-todo>
    ```

1. 가상환경 위에 Django 설치

    `>python -m pip install django`

    ```
    (env) ..\03-django-todo>python -m pip install django
    Collecting django
    ..생략..
    ```

    시간이 좀 걸릴 수 있음. django 설치 후 버전 확인해보기.

    `>django-admin --version`
    
    ```
    (env) ..\03-django-todo>django-admin --version
    2.2.6
    ```

1. Djnago 프로젝트 뼈대 만들기
    
    mysite 프로젝트 폴더를 현재폴더에 생성하기

    `>django-admin startproject mysite .`

    ```
    (env) ..\03-django-todo>django-admin startproject mysite .

    (env) ..\03-django-todo>dir

    2019-10-08  오후 09:30    <DIR>          .
    2019-10-08  오후 09:30    <DIR>          ..
    2019-10-08  오후 09:32    <DIR>          env
    2019-10-08  오후 09:57               647 manage.py // django 명령어 파일
    2019-10-08  오후 09:57    <DIR>          mysite // 프로젝트 폴더
                1개 파일                 647 바이트
                4개 디렉터리  970,414,096,384 바이트 남음
    ```

    엡 폴더 생성하기

    `>django-admin startapp todo`

    ```
    (env) ..\03-django-todo>django-admin startapp todo

    (env) ..\03-django-todo>dir

    2019-10-08  오후 09:30    <DIR>          .
    2019-10-08  오후 09:30    <DIR>          ..
    2019-10-08  오후 09:32    <DIR>          env
    2019-10-08  오후 09:57               647 manage.py // django 명령어 파일
    2019-10-08  오후 09:57    <DIR>          mysite // 프로젝트 폴더
    2019-10-08  오후 09:58    <DIR>          todo // 앱 폴더
                1개 파일                 647 바이트
                5개 디렉터리  970,406,756,352 바이트 남음
    ```

    DB 및 테이블 생성하기

    `>python manage.py migrate`

    ```
    (env) ..\03-django-todo>python manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    
    ..생략..

    (env) ..\03-django-todo>dir

    2019-10-08  오후 09:30    <DIR>          .
    2019-10-08  오후 09:30    <DIR>          ..
    2019-10-08  오후 09:32    <DIR>          env
    2019-10-08  오후 09:57               647 manage.py // django 명령어 파일
    2019-10-08  오후 09:57    <DIR>          mysite // 프로젝트 폴더
    2019-10-08  오후 09:58    <DIR>          todo // 앱 폴더
    2019-10-08  오후 10:02           131,072 db.sqlite3 // DB
                2개 파일             131,719 바이트
                5개 디렉터리  970,401,513,472 바이트 남음
    ```

    관리자 계정 생성하기

    `>python manage.py createsuperuser`

    ```
    (env) ..\03-django-todo>python manage.py createsuperuser
    Username (leave blank to use 'junjw'): jjw
    Email address: junjw1@daum.net
    Password:
    Password (again):
    The password is too similar to the username.
    This password is too short. It must contain at least 8 characters.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
    ```

## Django에 HTML 파일 수용하기

### MVT 순서로 코딩하기

- settings.py
- models.py
- urls.py
- views.py
- templates

코딩 시작

1. `mysite/settings.py`

    todo앱 등록하기. *// 클래스까지 명시해줌*

    프로젝트 템플릿 디렉토리 지정하기.

    타임존 수정하기.

    STATICFILES_DIR 지정하기.

1. `mysite/models.py`

    테이블 추가할 사항 없으므로 스킵

1. `mysite/urls.py`

    todo.urls를 include 하기.

1. `todo/urls.py`

    app namespace는 todo

    todo 다음에 vonly라는 url이 들어왔을 때

    뷰 이름은 TodoVueOnlyTV

    url 패턴 이름은 vonly

1. `todo/views.py`

    클래스 이름 TodoVueOnlyTV

    템플릿 이름 'todo/todo_vueonly.html'

1. HTML 생성하기

    todo/templates/todo 디렉토리 생성하고
    
    `todo_vueonly.html` 작성하기. (이전 html 복사)

1. 서버 실행하고 접속하기.

    `>manage.py runserver`

    ```
    (env) ..\03-django-todo>manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    October 08, 2019 - 22:59:17
    Django version 2.2.6, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```

    http://127.0.0.1:8000/todo/vonly/ 에 접속

    만들었던 html 문서가 잘 나오는가?

    todo 리스트 등록은 잘 되는가?

    Vue.js의 머스태쉬 문법과 장고의 템플릿 문법과 충돌하기 때문이다.

    Vue.js에서 머스태쉬 문법을 수정하자. 뷰 객체에서 delimiters 옵션 적용하여 중괄호를 1개만 쓰기.

    todo 리스트 등록 동작 확인.

1. `Ctrl+C`로 서버 정지

### 체크포인트

- [x] 파이썬 가상환경 생성 및 활성화
- [x] django 설치 및 프로젝트 뼈대 생성
- [x] MVT 순서로 코드 편집
- [x] 서버 정상 실행 및 접속
- [x] todo 리스트 등록 동작 확인

## Django로 todo앱 코딩하기

Vue.js없이 Django로만 todo앱 만들어보기

### 클래스형 뷰

자주 사용되는 기능들을 Django에서 미리 만들어 클래스형 뷰로 제공하고 있다.

- ListView : DB에서 레코드 목록을 가져와 보여주는 뷰
- CreateView : 폼에 입력한 내용으로 DB에 레코드 생성하는 뷰
- UpdateView : DB에 있는 특정 레코드를 수정하는 뷰
- DeleteView : DB에 있는 특정 레코드를 삭제하는 뷰

MVT 순서로 코딩 시작

1. `mysite/models.py`

    이름이 Todo인 모델(테이블)을 정의하기.

    ```python
    from django.db import models

    class Todo(models.Model):
            name = models.CharField('NAME', max_length=5, blank=True) # 이름 컬럼
            todo = models.CharField('TODO', max_length=50) # 내용 컬럼

            def __str__(self): # 스트링 메서드
                return self.todo
    ```

1. `todo/admin.py`

    테이블 신규 정의 시 admin 사이트에서도 보이도록 등록하자.

    ```python
    from django.contrib import admin
    from todo.models import Todo

    @admin.register(Todo) # 등록 위한 데코레이트
    class TodoAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'todo') # admin 사이트에서 보여줄 컬럼들
    ```

1. 모델이 변경되면 변경된 데이터를 DB에 반영하도록 설정하기.

    1. 현재 상태 확인
    
        `>python manage.py showmigrations`

        ```
        (env) ..\03-django-todo>python manage.py showmigrations
        admin
        [X] 0001_initial
        [X] 0002_logentry_remove_auto_add
        [X] 0003_logentry_add_action_flag_choices
        auth
        [X] 0001_initial
        [X] 0002_alter_permission_name_max_length
        [X] 0003_alter_user_email_max_length
        [X] 0004_alter_user_username_opts
        [X] 0005_alter_user_last_login_null
        [X] 0006_require_contenttypes_0002
        [X] 0007_alter_validators_add_error_messages
        [X] 0008_alter_user_username_max_length
        [X] 0009_alter_user_last_name_max_length
        [X] 0010_alter_group_name_max_length
        [X] 0011_update_proxy_permissions
        contenttypes
        [X] 0001_initial
        [X] 0002_remove_content_type_name
        sessions
        [X] 0001_initial
        todo
        (no migrations)
        ```

    1. 마이그레이션 파일 만들기

        `>python manage.py makemigrations`

        ```
        (env) ..\03-django-todo>python manage.py makemigrations
        Migrations for 'todo':
        todo\migrations\0001_initial.py
            - Create model Todo
        ```

    1. DB에 반영하여 테이블 만들기

        `>python manage.py migrate`

        ```
        (env) ..\03-django-todo>python manage.py migrate
        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions, todo
        Running migrations:
        Applying todo.0001_initial... OK
        ```

    1. 서버 실행하여 생성된 테이블 확인하기

        `>manage.py runserver`

        `http://127.0.0.1:8000/admin`로 접속 하면 Todo테이블이 생성 된 것을 볼 수 있음

        *// 데이터를 입력하여 저장해보자*

        *// 캐굿*

1. Django URL 설계

    URL 패턴, 뷰, 템플릿 파일은 하나씩 매핑이 되므로 그 관계를 미리 정의해두는게 좋다.
    
     URL 패턴 | 뷰 | 템플릿 파일
    -|-|-
    /todo/create/ | TodoCV | todo_form.html
    /todo/list/ | TodoLV | todo_list.html
    /todo/99/delete/ | TodoDelV | todo_confirm_delete.html

1. url 패턴 설정

    `todo/urls.py`

    ```python
    from django.urls import path
    from . import views

    app_name = 'todo'
    urlpatterns = [
        path('create/', views.TodoCV.as_view(), name='create'),
        path('list/', views.TodoLV.as_view(), name='list'),
        path('<int:pk>/delete/', views.TodoDelV.as_view(), name='delete'), # path convert. 숫자가 들어오면 정수로 변환하여 뷰로 넘겨줌
    ]

    ```
1. 뷰 생성

    `todo/views.py`

    ```python
    class TodoCV(CreateView):
        model = Todo # 테이블
        fields = '__all__' # 폼을 만들기 위해 필드 필요. 모든 필드 사용
        template_name = 'todo/todo_form.html' # 주요속성. redirectView를 제외한 모든 뷰에서 사용됨
        success_url = reverse_lazy('todo:list') # 리다이렉트 할 url


    class TodoLV(ListView):
        model = Todo
        template_name = 'todo/todo_list.html'


    class TodoDelV(DeleteView):
        model = Todo # 특정 레코드를 삭제해야하므로 테이블 지정
        template_name = 'todo/todo_confirm_delete.html'
        success_url = reverse_lazy('todo:list') # reverse() 또는 reverse_lazy() 사용해야
    ```

1. 템플릿 코딩

    *// 코딩 순서를 기능 순서대로 하는 것이 좋음 (뷰1-템플릿1 작업, 뷰2-템플릿2 작업)*

    `todo_vueonly.html` 와 비교하며 코딩해보자.

    `todo_form.html`

    ``` html
    <h1>my to do</h1>
    <strong>할 일 관리</strong>

    <form action="." method="post"> {% csrf_token %} <!-- form 태그에 action, method 속성 지정 --> <!-- django에서 제공하는 템플릿 태그. csrf 공격 방지 -->
        <input type="text" placeholder="이름" name="name"> <!-- name 변수명은 todo테이블의 컬럼명과 동일해야 -->
        <input type="text" placeholder="내용" name="todo">
        <button type="submit">등록</button> <!-- 클릭 시 서버로 전송하기 위해 submit 타입 지정 -->
    </form>
    ```

    `todo_list.html`

    ``` html
    <h1>my to do</h1>
    <strong>할 일 관리</strong>

    <ul>
        {% for todo in object_list %} <!-- v-for 대신 django의 템플릿 태그로 변경. ListView에서는 object_list 라는 컨택스트 변수를 넘겨준다. -->
        <li>
            <span>{{ todo.name }} :: {{ todo.todo }}</span> <!-- vue.js의 머스태시 문법을 django의 문법으로 변경 -->
            <span><a href="{% url 'todo:delete' todo.id %}">&#x00D7</a></span> <!-- 삭제 버튼 클릭 시 동작. 클릭 시 delete url을 요청하고, todo.id를 파라미터로 설정 -->
        </li>
        {% endfor %}
    </ul>
    ```

    `todo_confirm_delete.html`

    ``` html
    <h1>Todo Delete</h1>
    <p>정말로 삭제하시겠습니까? {{ object }} </p> <!-- 컨택스트 변수 object를 넘겨줌 -->
    <br>

    <form action="." method="post"> {% csrf_token %} 
        <button type="submit">확인</button>
    </form>
    ```
1. 저장하고, 조회하고, 삭제해보자.

    http://127.0.0.1:8000/todo/create/

(계속)
