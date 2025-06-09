import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 동물 추천기", page_icon="✨")

# CSS 스타일 (sparkle 배경 효과)
st.markdown("""
    <style>
    body {
        background-image: url("https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif");
        background-size: cover;
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# MBTI 정보 사전
mbti_info = {
    "ISTJ": ("🐘 코끼리", "https://media.giphy.com/media/ZFTu1EUQz3r0k/giphy.gif", "책임감 있고 차분한 ISTJ는 조용한 리더 타입의 코끼리와 닮았어요."),
    "ISFJ": ("🦉 부엉이", "https://media.giphy.com/media/L95W4wv8nnb9K/giphy.gif", "조용하지만 깊이 있는 사고를 하는 ISFJ는 지혜로운 부엉이와 잘 어울려요."),
    "INFJ": ("🦄 유니콘", "https://media.giphy.com/media/iicDrNGWxHmDrIni6j/giphy.gif", "이상적이고 희망찬 INFJ는 신비로운 유니콘과 닮았어요."),
    "INTJ": ("🦊 여우", "https://media.giphy.com/media/ToMjGp3FbEtv8Y1y7MI/giphy.gif", "계획적이고 전략적인 INTJ는 날카로운 감각을 가진 여우 같아요."),
    "ISTP": ("🐆 표범", "https://media.giphy.com/media/JqDeI2yjpSRgdh35oe/giphy.gif", "즉흥적이고 모험적인 ISTP는 민첩한 표범과 닮았어요."),
    "ISFP": ("🦌 사슴", "https://media.giphy.com
