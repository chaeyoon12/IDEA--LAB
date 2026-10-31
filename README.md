# IDEA LAB 홈페이지

업로드한 HTML 홈페이지 시안을 Streamlit에서 실행할 수 있도록 구성한 프로젝트입니다.

## 파일 구성
- `app.py`: Streamlit 실행 파일
- `website.html`: 홈페이지 디자인과 화면 동작
- `requirements.txt`: 필요한 Python 패키지

## GitHub 업로드
1. GitHub에서 새 저장소(repository)를 만듭니다.
2. 위 파일 3개를 저장소 최상위(root)에 업로드합니다.
3. Streamlit Community Cloud에서 GitHub 계정으로 로그인합니다.
4. `Create app`을 선택하고 저장소와 브랜치를 지정합니다.
5. Main file path에 `app.py`를 입력하고 배포합니다.

## 실행
로컬 또는 Codespaces 터미널에서:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 현재 시안의 기능 범위
- 상단 메뉴와 버튼으로 섹션 이동
- 아이디어 공감 버튼 (현재 브라우저 화면 안에서만 변경)
- 아이디어 제안 폼 (현재 화면에 카드로 표시)
- 로그인 안내 모달

주의: 현재 시안은 프론트엔드 데모입니다. 아이디어 제출 내용과 공감 수는 데이터베이스에 저장되지 않으며, 새로고침하면 초기 상태로 돌아갑니다. 실제 회원가입·로그인, 영구 저장, 관리자 기능은 별도 백엔드/데이터베이스 연결이 필요합니다.
