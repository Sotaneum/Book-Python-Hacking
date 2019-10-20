# Book:Python Hacking :: API Hooking
《파이썬 해킹 입문》 책을 읽고 공부한 내용입니다. 

## Info

- `Python 2` 코드로 작성되었습니다.
- `pydbg` 모듈이 필요합니다.
  - 도서의 `5.3.2` 장을 보시면 설치 및 적용을 할 수 있습니다.

## What is different from what is existing?

- 도서에서는 메모장을 기준으로 API Hooking 하는 예제를 [`EditPlus`](https://www.editplus.com/kr/)로 변경했습니다.

    ```python
    orgPattern="love"
    repPattern="hate"
    processName="notepad.exe"
    ```
    에서
    ```python
    orgPattern="love"
    repPattern="hate"
    processName="editplus.exe"
    ```
    으로 변경했습니다.

## What did you learn?

- process 이름으로만 가지 접근 할 수 있다는 점을 배웠습니다.

## Copyright

- 비상업적 용도로 사용 가능하며 링크를 반드시 포함해주세요.
- 문제가 되는 내용이 있다면 언제든지 [`issue`](https://github.com/Sotaneum/Python-Hacking/issues/new), [`Pull requests`](https://github.com/Sotaneum/Python-Hacking/compare) 부탁드립니다.
