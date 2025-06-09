import streamlit as st
import time
import json

# 페이지 설정
st.set_page_config(page_title="MBTI 동물 추천기", page_icon="🐾", layout="wide")

# 세션 상태 초기화
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None
if "mobile" not in st.session_state:
    st.session_state.mobile = False
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# 사이드바: 모바일 최적화 선택
st.session_state.mobile = st.sidebar.checkbox("📱 모바일 최적화 (간단 UI)", value=st.session_state.mobile)

# 16가지 MBTI 데이터 로딩
with open("mbti_animal_data.json", "r", encoding="utf-8") as f:
    mbti_data = json.load(f)

# 앱 제목
st.markdown("<h1 style='text-align: center;'>🌟 MBTI 동물 추천기 🐾</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>당신의 성격 유형에 맞는 동물과 궁합까지 알려드리어요!</h4>", unsafe_allow_html=True)
st.markdown("---")

# MBTI 선택 화면
if st.session_state.selected_mbti is None:
    st.markdown("### 🔜 당신의 MBTI는 무엇인가요?")
    mbti_list = list(mbti_data.keys())
    cols = st.columns(4 if not st.session_state.mobile else 2)

    for i, mbti in enumerate(mbti_list):
        col = cols[i % (4 if not st.session_state.mobile else 2)]
        with col:
            st.image(mbti_data[mbti]["image"], caption=mbti, use_column_width=True)
            if st.button(f"{mbti} 선택하기", key=mbti):
                st.session_state.selected_mbti = mbti
                st.session_state.show_result = False

# MBTI 선택 후: 동물 추천 전 기본질문 및 3초 수신
elif not st.session_state.show_result:
    st.markdown(f"## 🤔 당신의 MBTI에 연관된 동물은?")
    st.info("3초 후에 결과를 표시해드릴게요...", icon="⏳")
    time.sleep(3)
    st.session_state.show_result = True
    st.experimental_rerun()

# 결과 화면
else:
    mbti = st.session_state.selected_mbti
    data = mbti_data[mbti]

    st.markdown(f"## 🎉 {mbti} 유형의 추천 동물은?")
    st.markdown(f"# {data['emoji']} {data['animal']}")
    st.image(data["gif"], caption=f"{data['animal']} GIF", use_column_width=False)
    st.markdown(f"#### 🔗 이유: {data['desc']}")

    st.markdown("---")
    st.markdown(f"### ❤️ 잘 맞는 MBTI: **{data['good'][0]}**")
    st.markdown(f"🔎 이유: {data['good'][1]}")

    st.markdown(f"### 💔 잘 안 맞는 MBTI: **{data['bad'][0]}**")
    st.markdown(f"🔎 이유: {data['bad'][1]}")

    st.markdown("---")
    if st.button("🔄 다시 선택하기"):
        st.session_state.selected_mbti = None
        st.session_state.show_result = False
