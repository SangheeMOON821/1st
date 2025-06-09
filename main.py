import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 동물 추천기", page_icon="🐾", layout="wide")

# 데이터: MBTI → (이모지, 동물이름, 동물GIF, 설명, 잘 맞는 MBTI + 이유, 안 맞는 MBTI + 이유, 버튼용 이미지)
mbti_data = {
    "ISTJ": {
        "emoji": "🐘", "animal": "코끼리",
        "gif": "https://media.giphy.com/media/ZFTu1EUQz3r0k/giphy.gif",
        "desc": "책임감 있고 차분한 ISTJ는 조용한 리더 타입의 코끼리와 닮았어요.",
        "good": ("ESFJ", "서로의 책임감과 조직력을 존중하며 잘 협력해요."),
        "bad": ("ENFP", "즉흥적인 ENFP는 계획적인 ISTJ에게 혼란을 줄 수 있어요."),
        "image": "https://i.pinimg.com/originals/aa/fb/8c/aafb8c1aa63a8c7f2e4b4d79e6b662a5.jpg"
    },
    "ENFP": {
        "emoji": "🐶", "animal": "강아지",
        "gif": "https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif",
        "desc": "열정적이고 따뜻한 ENFP는 충직한 강아지와 닮았어요.",
        "good": ("INFJ", "깊이 있는 INFJ와 ENFP의 에너지가 조화를 이뤄요."),
        "bad": ("ISTJ", "ENFP의 즉흥성이 ISTJ의 계획을 방해할 수 있어요."),
        "image": "https://i.pinimg.com/564x/b4/80/86/b4808642f8673f30a4e3184f1d95ec12.jpg"
    },
    "INFJ": {
        "emoji": "🦄", "animal": "유니콘",
        "gif": "https://media.giphy.com/media/iicDrNGWxHmDrIni6j/giphy.gif",
        "desc": "이상적이고 희망찬 INFJ는 신비로운 유니콘과 닮았어요.",
        "good": ("ENFP", "열정적인 ENFP가 INFJ의 이상을 현실로 도와줘요."),
        "bad": ("ESTP", "즉흥적이고 현실적인 ESTP는 INFJ의 깊이를 이해하기 어려워요."),
        "image": "https://i.pinimg.com/564x/16/54/f2/1654f2f25b4f3ef423cc169bcf1f9e21.jpg"
    },
    # 추가 MBTI 항목은 여기 이어서 추가 가능
}

# 앱 제목
st.markdown("<h1 style='text-align: center;'>🌟 MBTI 동물 추천기 🐾</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>당신의 성격 유형에 맞는 동물과 궁합까지 알려드려요!</h4>", unsafe_allow_html=True)
st.markdown("---")

# 세션 상태 초기화
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

# 선택 안 했을 때: 버튼으로 MBTI 고르기
if st.session_state.selected_mbti is None:
    st.markdown("### 👉 당신의 MBTI는 무엇인가요?")
    mbti_list = list(mbti_data.keys())
    cols = st.columns(4)

    for i, mbti in enumerate(mbti_list):
        col = cols[i % 4]
        with col:
            st.image(mbti_data[mbti]["image"], caption=mbti, use_column_width=True)
            if st.button(f"{mbti} 선택하기"):
                st.session_state.selected_mbti = mbti

# MBTI 선택됨: 결과 화면
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
