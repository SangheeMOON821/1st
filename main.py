import streamlit as st
import time

# 페이지 설정
st.set_page_config(page_title="MBTI 동물 추천기", page_icon="🐾", layout="wide")

# 모바일 모드 선택
mobile = st.sidebar.toggle("📱 모바일 최적화 모드", value=False)
if mobile:
    st.markdown("<style>img {width: 100% !important;}</style>", unsafe_allow_html=True)

# 데이터 정의 (16개 MBTI 전체 포함) → [이전 응답에서 보여준 구조 유지]

# 세션 상태 초기화
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# 메인 화면
st.markdown("<h1 style='text-align: center;'>🌟 MBTI 동물 추천기 🐾</h1>", unsafe_allow_html=True)

if st.session_state.selected_mbti is None:
    st.markdown("### 👉 당신의 MBTI는 무엇인가요?")
    cols = st.columns(4)
    for i, mbti in enumerate(mbti_data):
        with cols[i % 4]:
            st.image(mbti_data[mbti]["image"], caption=mbti, use_column_width=True)
            if st.button(f"{mbti} 선택하기"):
                st.session_state.selected_mbti = mbti
                st.session_state.show_result = False
                st.experimental_rerun()

elif not st.session_state.show_result:
    st.markdown("## 🔍 당신의 MBTI에 어울리는 동물은?")
    with st.spinner("결과 분석 중..."):
        time.sleep(3)
    st.session_state.show_result = True
    st.experimental_rerun()

else:
    mbti = st.session_state.selected_mbti
    data = mbti_data[mbti]

    st.markdown(f"## 🎉 {mbti} 유형의 추천 동물은?")
    st.markdown(f"# {data['emoji']} {data['animal']}")
    st.image(data["gif"], caption=f"{data['animal']} GIF", use_column_width=False)
    st.markdown(f"#### 👉 이유: {data['desc']}")

    st.markdown("---")
    st.markdown(f"### ❤️ 잘 맞는 MBTI: **{data['good'][0]}**")
    st.markdown(f"🔎 이유: {data['good'][1]}")

    st.markdown(f"### 💔 잘 안 맞는 MBTI: **{data['bad'][0]}**")
    st.markdown(f"🔎 이유: {data['bad'][1]}")

    st.markdown("---")
    if st.button("🔄 다시 선택하기"):
        st.session_state.selected_mbti = None
        st.session_state.show_result = False
        st.experimental_rerun()
