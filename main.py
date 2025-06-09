import streamlit as st

# MBTI ➡ 동물 매핑
mbti_to_animal = {
    "ISTJ": ("🐘 코끼리", "https://example.com/elephant.gif"),
    "ISFJ": ("🦉 부엉이", "https://example.com/owl.gif"),
    "INFJ": ("🦄 유니콘", "https://example.com/unicorn.gif"),
    "INTJ": ("🦊 여우", "https://example.com/fox.gif"),
    "ISTP": ("🐆 표범", "https://example.com/leopard.gif"),
    "ISFP": ("🦌 사슴", "https://example.com/deer.gif"),
    "INFP": ("🐱 고양이", "https://example.com/cat.gif"),
    "INTP": ("🐙 문어", "https://example.com/octopus.gif"),
    "ESTP": ("🐯 호랑이", "https://example.com/tiger.gif"),
    "ESFP": ("🐬 돌고래", "https://example.com/dolphin.gif"),
    "ENFP": ("🐶 강아지", "https://example.com/dog.gif"),
    "ENTP": ("🦜 앵무새", "https://example.com/parrot.gif"),
    "ESTJ": ("🦁 사자", "https://example.com/lion.gif"),
    "ESFJ": ("🐻 곰", "https://example.com/bear.gif"),
    "ENFJ": ("🦋 나비", "https://example.com/butterfly.gif"),
    "ENTJ": ("🦅 독수리", "https://example.com/eagle.gif")
}

st.set_page_config(page_title="MBTI 동물 추천기", page_icon="✨")

st.markdown("<h1 style='text-align: center;'>🌟 MBTI 동물 추천기 ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>당신의 성격 유형에 맞는 동물은? 🧠➡️🐾</h3>", unsafe_allow_html=True)

# 드롭다운 메뉴로 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요!", options=list(mbti_to_animal.keys()))

# 결과 출력
if selected_mbti:
    animal_name, image_url = mbti_to_animal[selected_mbti]
    
    st.markdown(f"### 당신의 MBTI는 `{selected_mbti}` 이군요!")
    st.markdown(f"### 추천 동물은... {animal_name} ✨")
    st.image(image_url, use_column_width=True)
    
    st.balloons()
