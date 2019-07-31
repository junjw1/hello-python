# Hello Python

헬로 파이썬 :-)

## 참고

[Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

[마크다운 문법](https://heropy.blog/2017/09/30/markdown/)

## 목표
1. 파이썬 설치, 개발환경 설정, 실행, 디버깅 하기
1. 패키지를 설치하고 사용 하기

## 파이썬 설치

1. https://www.python.org/ 윈도우 설치 // Paht 환경변수에 경로 추가 체크
1. cmd에서 `python --version` 명령어로 버전 확인
```
Python 3.7.4
```

## VS Code에서 파이썬 개발환경 설정

1. vs cdoe 설치 및 실행
1. vs code의 확장 프로그램 **Python extension for Visual Studio Code** 설치
1. 파이썬 인터프리터 **Python: Select Interpreter** 설정
    - ``ctrl + shift + P`` 또는 왼쪽 아래 스테이터스 바 클릭

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

1. 가상 환병 생성 및 활성화
    ```
    py -3 -m -venv .venv
    .venv\scripts\activate
    ```

1. `matplotlib` 패키지 설치

(계속)