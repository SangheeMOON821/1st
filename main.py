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
    "ISFP": ("🦌 사슴", "https://media.giphy.com/media/xUOwGp2rrb06FfZxHG/giphy.gif", "감성적이고 평화로운 ISFP는 순수한 사슴을 닮았어요."),
    "INFP": ("🐱 고양이", "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif", "내면이 풍부하고 따뜻한 INFP는 독립적인 고양이와 닮았어요."),
    "INTP": ("🐙 문어", "https://media.giphy.com/media/hVtF7I7A0E3E/giphy.gif", "창의적이고 호기심 많은 INTP는 영리한 문어와 잘 어울려요."),
    "ESTP": ("🐯 호랑이", "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif", "대담하고 에너지 넘치는 ESTP는 강렬한 호랑이와 닮았어요."),
    "ESFP": ("🐬 돌고래", "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif", "사교적이고 즐거운 ESFP는 명랑한 돌고래와 잘 어울려요."),
    "ENFP": ("🐶 강아지", "https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif", "열정적이고 따뜻한 ENFP는 충직한 강아지와 닮았어요."),
    "ENTP": ("🦜 앵무새", "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif", "재치 있고 아이디어가 넘치는 ENTP는 활발한 앵무새와 어울려요."),
    "ESTJ": ("🦁 사자", "https://media.giphy.com/media/KDRv3QggAjyo/giphy.gif", "리더십과 현실감각이 뛰어난 ESTJ는 강인한 사자와 닮았어요."),
    "ESFJ": ("🐻 곰", "https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif", "따뜻하고 보호 본능이 강한 ESFJ는 포근한 곰과 닮았어요."),
    "ENFJ": ("🦋 나비", "https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif", "사람을 이끄는 ENFJ는 변화와 희망의 상징인 나비와 닮았어요."),
    "ENTJ": ("🦅 독수리", "https://media.giphy.com/media/3o7aD6vFZQx6MfPpna/giphy.gif", "결단력 있고 야망이 큰 ENTJ는 고공에서 세상을 보는 독수리와 같아요."),
}

st.markdown("<h1 style='text-align: center;'>🌟 MBTI 동물 추천기 ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>당신의 성격 유형에 맞는 동물을 알아보세요 🧠➡️🐾</h3>", unsafe_allow_html=True)

# 드롭다운으로 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요!", options=list(mbti_info.keys()))

# 결과 표시
if selected_mbti:
    animal_name, gif_url, reason = mbti_info[selected_mbti]

    st.markdown(f"## {selected_mbti} 유형의 추천 동물은... {animal_name} ✨")
    st.image(gif_url, use_column_width=False, caption=animal_name)
    st.markdown(f"#### 👉 선택 이유: {reason}")
