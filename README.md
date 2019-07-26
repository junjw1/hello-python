 Hello Python

헬로 파이썬

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

`hello` 폴더 생성 및 `hello.py` 작성

hello/hello.py :

```python
msg = 'Hello World'
print(msg)
```

터미널에서 `python hello.py` 실행
```
Hello World
```

## 환경 설정 및 디버거 실행

1. 왼쪽 사이드바의 디버그 뷰 선택
1. 셋팅 아이콘 클릭 또는 **Debug > Open configurations** 메뉴 사용
1. `"stopOnEntry": true` 설정 추가

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
                "stopOnEntry": true, // 프로그램이 시작할 때 첫 줄에서 자동 멈춤 위함
            }
        ]
    }
    ```

    >"pythonPath": "${workspaceFolder}", // 디버깅에 사용할 인터프리터를 가진 특정 폴더 지정할 경우 
    
    >"args": [], // 파이선 프로그램을 위한 커맨드라인 아규먼트 지정할 경우

1. `F5`로 디버거 실행하여 `msg` 변수의 현재 값 나타내보자