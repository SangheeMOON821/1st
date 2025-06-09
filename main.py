import streamlit as st
st.title('나의 첫 웹앱 프로젝트 by SANGHEE')
st.write('OMG 이게 되네?')
import streamlit as st

# 🎯 MBTI 동물 매핑 딕셔너리
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

# 사용자 입력 받기
mbti_input = st.text_input("당신의 MBTI를 입력하세요 (예: INFP)", max_chars=4).upper()

# 추천 결과
if mbti_input in mbti_to_animal:
    animal_name, image_url = mbti_to_animal[mbti_input]
    
    st.markdown(f"### 당신의 MBTI는 `{mbti_input}` 이군요!")
    st.markdown(f"### 추천 동물은... {animal_name} ✨")
    st.image(image_url, use_column_width=True)
    
    st.balloons()  # 🎈풍선 애니메이션
else:
    if mbti_input:
        st.warning("올바른 MBTI 4글자를 입력해주세요! 예: ENFP")
