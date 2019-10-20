# Book:Python Hacking :: Web Shell
《파이썬 해킹 입문》 책을 읽고 공부한 내용입니다. 

## Info

- `Python 2` 코드로 작성되었습니다.

## What is different from what is existing?

- 도서에서는 단계별로 나뉘어 있습니다.
  1. `포트 스캐닝`
  2. `비밀번호 크래킹`
  3. `디렉터리 목록 조회`
  4. `FTP 웹 셀 공격`
- 각 단계를 하나의 함수로 만들어 `WebShell`이라는 클래스를 구현했습니다.
  - CheckPW : 아이디, 비밀번호, IP로 FTP에 접속합니다.
  - getDirList : FTP의 디렉터리 목록을 가져옵니다.
  - getPW : 유저 아이디와 IP, 비밀번호 리스트로 로그인하여 성공한 패스워드를 반환합니다.
  - PortScanner : IP에 21 포트가 열려 있는지를 확인합니다.
  - getDir : FTP에 접속하여 디렉터리 목록을 출력합니다.
  - UploadWebShell : FTP에 파일을 올립니다.
  - install_input : 웹 셀을 INPUT으로 받아 처리합니다.
  - install_Auto : 파라미터값으로 처리합니다.

## What did you learn?

- Python의 Class 사용방법과 self의 기능에 대해 알게 되었습니다.
- Python에서 입력 받는 방법(Input)을 알게 되었습니다.

## Copyright

- 비상업적 용도로 사용 가능하며 링크를 반드시 포함해주세요.
- 문제가 되는 내용이 있다면 언제든지 [`issue`](https://github.com/Sotaneum/Python-Hacking/issues/new), [`Pull requests`](https://github.com/Sotaneum/Python-Hacking/compare) 부탁드립니다.
