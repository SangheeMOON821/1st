import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 동물 추천기", page_icon="🐾")

# MBTI 데이터 (이모지, 동물 이름, 설명)
mbti_info = {
    "ISTJ": ("🐘", "코끼리", "책임감 있고 차분한 ISTJ는 조용한 리더 타입의 코끼리와 닮았어요."),
    "ISFJ": ("🦉", "부엉이", "조용하지만 깊이 있는 사고를 하는 ISFJ는 지혜로운 부엉이와 잘 어울려요."),
    "INFJ": ("🦄", "유니콘", "이상적이고 희망찬 INFJ는 신비로운 유니콘과 닮았어요."),
    "INTJ": ("🦊", "여우", "계획적이고 전략적인 INTJ는 날카로운 감각을 가진 여우 같아요."),
    "ISTP": ("🐆", "표범", "즉흥적이고 모험적인 ISTP는 민첩한 표범과 닮았어요."),
    "ISFP": ("🦌", "사슴", "감성적이고 평화로운 ISFP는 순수한 사슴을 닮았어요."),
    "INFP": ("🐱", "고양이", "내면이 풍부하고 따뜻한 INFP는 독립적인 고양이와 닮았어요."),
    "INTP": ("🐙", "문어", "창의적이고 호기심 많은 INTP는 영리한 문어와 잘 어울려요."),
    "ESTP": ("🐯", "호랑이", "대담하고 에너지 넘치는 ESTP는 강렬한 호랑이와 닮았어요."),
    "ESFP": ("🐬", "돌고래", "사교적이고 즐거운 ESFP는 명랑한 돌고래와 잘 어울려요."),
    "ENFP": ("🐶", "강아지", "열정적이고 따뜻한 ENFP는 충직한 강아지와 닮았어요."),
    "ENTP": ("🦜", "앵무새", "재치 있고 아이디어가 넘치는 ENTP는 활발한 앵무새와 어울려요."),
    "ESTJ": ("🦁", "사자", "리더십과 현실감각이 뛰어난 ESTJ는 강인한 사자와 닮았어요."),
    "ESFJ": ("🐻", "곰", "따뜻하고 보호 본능이 강한 ESFJ는 포근한 곰과 닮았어요."),
    "ENFJ": ("🦋", "나비", "사람을 이끄는 ENFJ는 변화와 희망의 상징인 나비와 닮았어요."),
    "ENTJ": ("🦅", "독수리", "결단력 있고 야망이 큰 ENTJ는 고공에서 세상을 보는 독수리와 같아요."),
}

# 앱 타이틀
st.markdown("<h1 style='text-align: center;'>🌟 MBTI 동물 추천기 🐾</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>당신의 성격 유형에 맞는 동물은?</h3>", unsafe_allow_html=True)

# 세션 상태로 MBTI 저장
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

# 선택되지 않았을 때 질문 표시
if st.session_state.selected_mbti is None:
    st.markdown("## 👉 당신의 MBTI는 무엇인가요?")
    
    # MBTI 버튼 나열 (4열 그리드)
    cols = st.columns(4)
    mbti_list = list(mbti_info.keys())

    for i, mbti in enumerate(mbti_list):
        col = cols[i % 4]
        if col.button(mbti):
            st.session_state.selected_mbti = mbti

# MBTI가 선택되면 결과 출력
else:
    mbti = st.session_state.selected_mbti
    emoji, animal, reason = mbti_info[mbti]

    st.markdown(f"## {mbti} 유형의 추천 동물은...")
    st.markdown(f"# {emoji} {animal}")
    st.markdown(f"### 👉 선택 이유: {reason}")
    
    if st.button("🔄 다시 선택하기"):
        st.session_state.selected_mbti = None
