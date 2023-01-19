## Pynecone

- [Introduction](#introduction)
- [Installing](#installing)
- [Create a Project](#create-a-project)
- [Directory Structure](#directory-structure)
  - [assets](#assets)
  - [my_app_name](#my_app_name)
  - [pcconfig.py](#pcconfigpy)

## Introduction

- 파인콘(pynecone)은 파이썬 언어만으로 개발 가능한 오픈소스 풀스택 프레임워크 입니다.

## Installing

Pynecone is available as a pip library:

```python
pip install pynecone-io
```

## Create a Project

`my_app_name`이라는 프로젝트 생성

```pythone
$ mkdir my_app_name
$ cd my_app_name
$ pc init
```

## Directory Structure

다음과 같이 파일 구조가 생성된다

```python
my_app_name
├── .web
├── assets
├── my_app_name
│   ├── __init__.py
│   └── my_app_name.py
└── pcconfig.py
```

### .my_app_name

프로젝트 루트 폴더
직접 입력한 폴더명으로 생성된다

### .web

컴파일된 js파일 등이 저장되는 폴더

프론트엔드 코드를 작성한 부분은 NextJS 앱으로 컴파일 되어서 동일한 이름의js 파일로 저장된다. 컴파일 결과물은 ` .web` 디렉토리에 저장이 된다.
컴파일된 자바스크립트 파일들과, 이밖에도 node.js 관련모듈 등이 저장된다
js 문접이나 컴파일 오류가 발생할 경우 이 폴더 하위에 생성된 js 파일을 보면 오류의 원인을 파악할 수 있다.
`pc run` 명령어를 통해 서버를 구동할 때 모든 js 파일이 다시 컴파일 된다

### assets

정적 파일 저장소
이미지나 동영상, favicon 및 첨부파일 등 정적파일을 저장한다
ex) 이미지 파일을 사용하고 싶으면 assets/image.png 경로에 파일을 저장하고
` pc.image(src="image.png")` 방식으로 컴포넌트를 만들어서 사용

### my_app_name

터미널에서 pc init을 실행하면 프로젝트 폴더명으로 설정한 폴더가 생성되고, **init**.py 파일이 기본적으로 생성된다

### pcconfig.py

프로젝트 설정파일

```python
import pynecone as pc


config = pc.Config(
    app_name="python",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
```

- app_name - 앱 이름
- db_url - 데이터베이스(sqlite) 설정
- env - 실행환경 (ENV, PROD) 등을 설정
  - 실행환경(env)은 `pc.Env.Dev` or `pc.Env.PROD` 로 설정이 가능
