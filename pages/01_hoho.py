import streamlit as st
import time

# 페이지 설정
st.set_page_config(page_title="MBTI 동물 추천기", page_icon="🐾", layout="wide")

# 데이터: MBTI → (이모지, 동물이름, 동물GIF, 설명, 잘 맞는 MBTI + 이유, 안 맞는 MBTI + 이유, 버튼용 이미지)
mbti_data = {
    "ISTJ": {"emoji": "🐘", "animal": "코끼리", "gif": "https://media.giphy.com/media/ZFTu1EUQz3r0k/giphy.gif", "desc": "책임감 있고 차분한 ISTJ는 조용한 리더 타입의 코끼리와 닮았어요.", "good": ("ESFJ", "서로의 책임감과 조직력을 존중하며 잘 협력해요."), "bad": ("ENFP", "즉흥적인 ENFP는 계획적인 ISTJ에게 혼란을 줄 수 있어요."), "image": "https://i.pinimg.com/originals/aa/fb/8c/aafb8c1aa63a8c7f2e4b4d79e6b662a5.jpg"},
    "ISFJ": {"emoji": "🦥", "animal": "나무늘보", "gif": "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", "desc": "성실하고 따뜻한 ISFJ는 느긋하고 조용한 나무늘보와 닮았어요.", "good": ("ESFP", "사교적인 ESFP가 ISFJ의 내향성을 보완해줘요."), "bad": ("ENTP", "과도하게 활동적인 ENTP는 ISFJ를 지치게 만들 수 있어요."), "image": "https://i.pinimg.com/originals/48/31/57/483157f0a32599979280520aa406f630.jpg"},
    "INFJ": {"emoji": "🦄", "animal": "유니콘", "gif": "https://media.giphy.com/media/iicDrNGWxHmDrIni6j/giphy.gif", "desc": "이상적이고 희망찬 INFJ는 신비로운 유니콘과 닮았어요.", "good": ("ENFP", "열정적인 ENFP가 INFJ의 이상을 현실로 도와줘요."), "bad": ("ESTP", "즉흥적이고 현실적인 ESTP는 INFJ의 깊이를 이해하기 어려워요."), "image": "https://i.pinimg.com/564x/16/54/f2/1654f2f25b4f3ef423cc169bcf1f9e21.jpg"},
    "INTJ": {"emoji": "🦉", "animal": "올빼미", "gif": "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif", "desc": "계획적이고 전략적인 INTJ는 통찰력 있는 올빼미와 닮았어요.", "good": ("ENTP", "창의적인 ENTP가 INTJ의 전략에 자극을 줘요."), "bad": ("ESFP", "즉흥적이고 감성적인 ESFP는 INTJ의 논리적 사고와 충돌할 수 있어요."), "image": "https://i.pinimg.com/originals/80/5a/49/805a495c9b0e5f8d5a7d82850973b3b3.jpg"},
    "ISTP": {"emoji": "🐆", "animal": "치타", "gif": "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif", "desc": "독립적이고 실용적인 ISTP는 빠르고 날렵한 치타와 닮았어요.", "good": ("ESTP", "유사한 성향을 통해 함께 모험을 즐길 수 있어요."), "bad": ("ENFJ", "감성 중심의 ENFJ는 ISTP의 감정 표현 부족을 힘들어해요."), "image": "https://i.pinimg.com/564x/06/d3/cb/06d3cb0843aa5e2054a7b13d0195aaf3.jpg"},
    "ISFP": {"emoji": "🦋", "animal": "나비", "gif": "https://media.giphy.com/media/3oEjHV0z8Aans4V5HW/giphy.gif", "desc": "감성적이고 자유로운 ISFP는 섬세한 나비와 닮았어요.", "good": ("ESFP", "서로의 감성과 자유를 존중하며 함께 즐겨요."), "bad": ("ENTJ", "계획적인 ENTJ는 자유로운 ISFP에게 부담이 될 수 있어요."), "image": "https://i.pinimg.com/564x/1b/da/18/1bda1879ce9f515524ca44b8cc19b084.jpg"},
    "INFP": {"emoji": "🦌", "animal": "사슴", "gif": "https://media.giphy.com/media/8FNlmD5QW3tbm/giphy.gif", "desc": "이상주의적인 INFP는 섬세하고 조용한 사슴과 닮았어요.", "good": ("ENFJ", "타인을 잘 이해하는 ENFJ는 INFP를 따뜻하게 감싸줘요."), "bad": ("ESTJ", "엄격하고 규율 중심적인 ESTJ는 INFP에게 억압적으로 느껴질 수 있어요."), "image": "https://i.pinimg.com/564x/9d/17/91/9d179131e6cfdfc60e72fc75c8cfcd3f.jpg"},
    "INTP": {"emoji": "🦉", "animal": "부엉이", "gif": "https://media.giphy.com/media/TPl5Nn8c9mAjM/giphy.gif", "desc": "논리적이고 분석적인 INTP는 지혜로운 부엉이와 닮았어요.", "good": ("ENTP", "비슷한 지적 호기심과 사고방식을 공유해요."), "bad": ("ESFJ", "감성적이고 체계적인 ESFJ는 INTP의 즉흥성을 받아들이기 힘들 수 있어요."), "image": "https://i.pinimg.com/564x/b8/5c/2a/b85c2acb7ffbbf334d74813fc697df7c.jpg"},
    "ESTP": {"emoji": "🐯", "animal": "호랑이", "gif": "https://media.giphy.com/media/LHZyixOnHwDDy/giphy.gif", "desc": "모험심 강하고 에너지 넘치는 ESTP는 용감한 호랑이와 닮았어요.", "good": ("ISFP", "신중한 ISFP는 ESTP의 활력을 잘 받아줘요."), "bad": ("INFJ", "INFJ의 내면 세계를 ESTP는 이해하기 어려울 수 있어요."), "image": "https://i.pinimg.com/originals/f2/96/9b/f2969b172b1356ffb1bdf6e9a9ce7bcf.jpg"},
    "ESFP": {"emoji": "🐬", "animal": "돌고래", "gif": "https://media.giphy.com/media/Qr9l1o4nx6Fos/giphy.gif", "desc": "사교적이고 에너지 넘치는 ESFP는 장난기 많은 돌고래와 닮았어요.", "good": ("ISFJ", "섬세한 ISFJ는 ESFP의 에너지를 안정적으로 받아줘요."), "bad": ("INTJ", "계획적이고 논리적인 INTJ는 ESFP의 즉흥성을 이해하지 못할 수 있어요."), "image": "https://i.pinimg.com/564x/23/ea/07/23ea0716b042b3f3a7a3b3ad294a7c57.jpg"},
    "ENFP": {"emoji": "🐶", "animal": "강아지", "gif": "https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif", "desc": "열정적이고 따뜻한 ENFP는 충직한 강아지와 닮았어요.", "good": ("INFJ", "깊이 있는 INFJ와 ENFP의 에너지가 조화를 이뤄요."), "bad": ("ISTJ", "ENFP의 즉흥성이 ISTJ의 계획을 방해할 수 있어요."), "image": "https://i.pinimg.com/564x/b4/80/86/b4808642f8673f30a4e3184f1d95ec12.jpg"},
    "ENTP": {"emoji": "🦊", "animal": "여우", "gif": "https://media.giphy.com/media/l0K4kWJir7C9H1vAA4/giphy.gif", "desc": "재치 있고 논리적인 ENTP는 영리한 여우와 닮았어요.", "good": ("INFJ", "이상적인 INFJ는 ENTP의 깊이를 더해줘요."), "bad": ("ISFJ", "조용한 ISFJ는 ENTP의 에너지에 지칠 수 있어요."), "image": "https://i.pinimg.com/564x/80/8f/6d/808f6d28e2135021a1ff62ef0cf6761e.jpg"},
    "ESTJ": {"emoji": "🦁", "animal": "사자", "gif": "https://media.giphy.com/media/13borq7Zo2kulO/giphy.gif", "desc": "강인하고 지도력 있는 ESTJ는 위엄 있는 사자와 닮았어요.", "good": ("ISFJ", "섬세한 ISFJ는 ESTJ의 리더십을 지지해줘요."), "bad": ("INFP", "감성적이고 이상주의적인 INFP는 ESTJ의 논리를 부담스러워해요."), "image": "https://i.pinimg.com/564x/36/87/e1/3687e17a590f6c45ac1db9f87291e6b5.jpg"},
    "ESFJ": {"emoji": "🦢", "animal": "백조", "gif": "https://media.giphy.com/media/Xi2Xu0MejhsUo/giphy.gif", "desc": "사교적이고 배려심 깊은 ESFJ는 우아한 백조와 닮았어요.", "good": ("ISFP", "감성적인 ISFP는 ESFJ의 배려심에 따뜻하게 반응해요."), "bad": ("INTP", "자기 세계에 집중하는 INTP는 ESFJ에게 무심하게 느껴질 수 있어요."), "image": "https://i.pinimg.com/564x/17/62/1c/17621c17ee197ee7b44d2b3c6f73f699.jpg"},
    "ENFJ": {"emoji": "🦓", "animal": "얼룩말", "gif": "https://media.giphy.com/media/hEc4k5pN17GZq/giphy.gif", "desc": "열정적이고 배려심 있는 ENFJ는 유쾌하고 따뜻한 얼룩말과 닮았어요.", "good": ("INFP", "이상적인 INFP는 ENFJ의 헌신에 감동받아요."), "bad": ("ISTP", "감정 표현이 적은 ISTP는 ENFJ에게 답답할 수 있어요."), "image": "https://i.pinimg.com/564x/8c/6d/f5/8c6df5b2c43c92460f1a3210bb6616a3.jpg"},
    "ENTJ": {"emoji": "🦅", "animal": "독수리", "gif": "https://media.giphy.com/media/ToMjGpA1uC0ZGU7UduE/giphy.gif", "desc": "리더십과 추진력이 강한 ENTJ는 날카로운 독수리와 닮았어요.", "good": ("INTP", "지적인 INTP는 ENTJ의 비전을 뒷받침해줘요."), "bad": ("ISFP", "자유로운 ISFP는 ENTJ의 통제를 부담스러워할 수 있어요."), "image": "https://i.pinimg.com/564x/0b/2a/1b/0b2a1b7b3ac558b2dc91c017c2ea2df7.jpg"}
}

# 세션 상태 초기화
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None
    st.session_state.show_result = False
    st.session_state.mobile = False

# 모바일 최적화 버튼
st.sidebar.markdown("## ⚙️ 설정")
st.session_state.mobile = st.sidebar.checkbox("모바일 최적화 (간단 UI)", value=st.session_state.mobile)

# 앱 제목
st.markdown("<h1 style='text-align: center;'>🌟 MBTI 동물 추천기 🐾</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>당신의 성격 유형에 맞는 동물과 궁합까지 알려드려요!</h4>", unsafe_allow_html=True)
st.markdown("---")

# 선택 안 했을 때: 버튼으로 MBTI 고르기
if st.session_state.selected_mbti is None:
    st.markdown("### 👉 당신의 MBTI는 무엇인가요?")
    mbti_list = list(mbti_data.keys())
    cols = st.columns(2 if st.session_state.mobile else 4)

    for i, mbti in enumerate(mbti_list):
        col = cols[i % len(cols)]
        with col:
            st.image(mbti_data[mbti]["image"], caption=mbti, use_column_width=True)
            if st.button(f"{mbti} 선택하기"):
                st.session_state.selected_mbti = mbti
                st.session_state.show_result = False
                st.experimental_rerun()

# 선택 완료: 질문 후 카운트다운 → 결과 출력
else:
    if not st.session_state.show_result:
        st.markdown(f"## 🤔 당신의 MBTI에 어울리는 동물은?")
        with st.spinner("결과를 분석 중입니다..."):
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
