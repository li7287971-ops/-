
import streamlit as st
import random

# 1. 페이지 레이아웃 설정
st.set_page_config(page_title="사회 공부 퀴즈", layout="wide")

# 2. CSS를 이용한 글자 크기 및 색상 스타일 정의
st.markdown("""
    <style>
    .big-font { font-size: 24px !important; font-weight: bold; }
    .correct { color: blue; font-weight: bold; }
    .wrong { color: red; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 나만의 사회 공부 퀴즈")

# 3. 문제 불러오기 함수
def load_questions():
    questions = []
    try:
        with open("study.txt", "r", encoding="utf-8") as f:
            for line in f:
                if "," in line:
                    word, sentence = line.strip().split(",", 1)
                    questions.append({"word": word, "sentence": sentence})
    except FileNotFoundError:
        st.error("❌ 'study.txt' 파일을 찾을 수 없습니다.")
    return questions

# 4. 세션 상태 관리 (문제 초기화 및 랜덤 섞기)
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = load_questions()
    random.shuffle(st.session_state.quiz_data)

# 5. 퀴즈 화면 구성
for i, q in enumerate(st.session_state.quiz_data):
    masked = q['sentence'].replace(q['word'], "___")
    
    # 문제 출력
    st.markdown(f"<p class='big-font'>문제 {i+1}: {masked}</p>", unsafe_allow_html=True)
    
    # 답변 입력창
    user_ans = st.text_input(f"답변을 입력하세요 #{i+1}", key=f"input_{i}")
    
    # 정답/오답 확인
    if user_ans:
        if user_ans == q['word']:
            st.markdown(f"<p class='correct'>✅ 정답입니다! 아주 잘했어요! (정답: {q['word']})</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='wrong'>❌ 틀렸어요. 정답은 '{q['word']}'입니다.</p>", unsafe_allow_html=True)

# 6. 새로고침 버튼 (퀴즈 섞기)
if st.button("🔄 퀴즈 섞기 (새로 시작)"):
    del st.session_state.quiz_data
    st.rerun()
    # 현재 총 문제 수 출력하기
