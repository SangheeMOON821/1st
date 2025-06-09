import streamlit as st
import time

# Streamlit 설정
st.set_page_config(page_title="MBTI 동물 추천기", page_icon="🐾", layout="wide")

# 세션 상태 초기화
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "mobile" not in st.session_state:
    st.session_state.mobile = False

# 사이드바 옵션
st.sidebar.header("옵션")
st.session_state.mobile = st.sidebar.checkbox("모바일 최적화 (간단 UI)", value=st.session_state.mobile)

# MBTI 데이터 정의
mbti_data = {
    "ISTJ": {"emoji": "🐘", "animal": "코끼리", "gif": "https://media.giphy.com/media/ZFTu1EUQz3r0k/giphy.gif", "desc": "책임감 있고 차분한 ISTJ는 조용한 리더 타입의 코끼리와 닮았어요.", "good": ("ESFJ", "서로의 책임감과 조직력을 존중하며 잘 협력해요."), "bad": ("ENFP", "즉흥적인 ENFP는 계획적인 ISTJ에게 혼란을 줄 수 있어요."), "image": "https://i.pinimg.com/originals/aa/fb/8c/aafb8c1aa63a8c7f2e4b4d79e6b662a5.jpg"},
    "ISFJ": {"emoji": "🦜", "animal": "사슴", "gif": "https://media.giphy.com/media/cCqEIPqAmzHtK/giphy.gif", "desc": "섬세하고 배려심 많은 ISFJ는 온순한 사슴을 닮았어요.", "good": ("ESFP", "활발한 ESFP가 ISFJ를 즐겁게 해줘요."), "bad": ("ENTP", "너무 토론을 좋아하는 ENTP는 ISFJ에게 피로를 줄 수 있어요."), "image": "https://i.pinimg.com/originals/d1/fb/6d/d1fb6db2991dc77fc84ee86a8dcb328a.jpg"},
    "INFJ": {"emoji": "🦄", "animal": "유니콘", "gif": "https://media.giphy.com/media/iicDrNGWxHmDrIni6j/giphy.gif", "desc": "이상적이고 희망찬 INFJ는 신비로운 유니콘과 닮았어요.", "good": ("ENFP", "열정적인 ENFP가 INFJ의 이상을 현실로 도와줘요."), "bad": ("ESTP", "즉흥적이고 현실적인 ESTP는 INFJ의 깊이를 이해하기 어려워요."), "image": "https://i.pinimg.com/564x/16/54/f2/1654f2f25b4f3ef423cc169bcf1f9e21.jpg"},
    "INTJ": {"emoji": "🦖", "animal": "용", "gif": "https://media.giphy.com/media/MFz2kTCLVqFeo/giphy.gif", "desc": "전략적이고 독립적인 INTJ는 전설의 용과 같은 기운이 있어요.", "good": ("ENTP", "혁신적인 아이디어로 서로 자극을 줘요."), "bad": ("ESFP", "즉흥적이고 감정적인 ESFP는 INTJ에게 혼란스러울 수 있어요."), "image": "https://i.pinimg.com/originals/c6/5a/33/c65a33c94ec785e3b36fc4e6231f93c5.jpg"},
    "ISTP": {"emoji": "🐭", "animal": "너구리", "gif": "https://media.giphy.com/media/12HZukMBlutpoQ/giphy.gif", "desc": "논리적이고 유연한 ISTP는 영리한 너구리와 닮았어요.", "good": ("ESTP", "모험을 좋아하는 스타일이 잘 맞아요."), "bad": ("ENFJ", "감정 중심의 ENFJ는 ISTP에게 부담이 될 수 있어요."), "image": "https://i.pinimg.com/originals/8a/f4/f0/8af4f06e52f6477a84c3c3e9ab2a52f5.jpg"},
    "ISFP": {"emoji": "🐾", "animal": "고양이", "gif": "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", "desc": "감성적이고 조용한 ISFP는 독립적인 고양이와 닮았어요.", "good": ("ESFP", "비슷한 감성을 공유하며 즐거운 시간을 보내요."), "bad": ("ENTJ", "계획적이고 통제하려는 ENTJ는 ISFP를 불편하게 만들 수 있어요."), "image": "https://i.pinimg.com/originals/46/4b/9c/464b9cba379b57fc77b3687502b7e6e3.jpg"},
    "INFP": {"emoji": "🐦", "animal": "부엉이", "gif": "https://media.giphy.com/media/XIqCQx02E1U9W/giphy.gif", "desc": "이상주의자 INFP는 조용하고 지혜로운 부엉이와 닮았어요.", "good": ("ENFJ", "이해심 깊은 ENFJ가 INFP의 감정을 존중해줘요."), "bad": ("ESTJ", "현실적인 ESTJ는 INFP의 이상을 이해하지 못할 수 있어요."), "image": "https://i.pinimg.com/originals/d6/91/c9/d691c91cf7cfda3f54b45bdfdfb64da7.jpg"},
    "INTP": {"emoji": "🐍", "animal": "도마뱀", "gif": "https://media.giphy.com/media/NMufrvxO8bvvW/giphy.gif", "desc": "논리적이고 호기심 많은 INTP는 독특한 도마뱀과 닮았어요.", "good": ("ENTP", "서로의 아이디어를 공유하며 성장해요."), "bad": ("ESFJ", "감정 중심의 ESFJ는 INTP의 논리를 받아들이기 어려워요."), "image": "https://i.pinimg.com/originals/4b/70/64/4b70645e30e8f536e4e4df51020d5af9.jpg"},
    "ESTP": {"emoji": "🦁", "animal": "호랑이", "gif": "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif", "desc": "활동적이고 현실적인 ESTP는 용맹한 호랑이와 닮았어요.", "good": ("ISFP", "감성적인 ISFP가 ESTP에게 안정감을 줘요."), "bad": ("INFJ", "깊은 내면의 INFJ와 ESTP는 성향 차이가 커요."), "image": "https://i.pinimg.com/originals/59/10/e2/5910e2eb6f7a1e3a7255a6a6c2353a75.jpg"},
    "ESFP": {"emoji": "🦊", "animal": "팬더", "gif": "https://media.giphy.com/media/ya4eevXU490Iw/giphy.gif", "desc": "사교적이고 긍정적인 ESFP는 귀여운 팬더와 닮았어요.", "good": ("ISFJ", "차분한 ISFJ가 ESFP에게 편안함을 줘요."), "bad": ("INTJ", "과묵하고 계획적인 INTJ는 ESFP와 다를 수 있어요."), "image": "https://i.pinimg.com/originals/cd/ef/e2/cdefe270e7747d126b5c8fe171f3d6f5.jpg"},
    "ENFP": {"emoji": "🐶", "animal": "강아지", "gif": "https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif", "desc": "열정적이고 따뜻한 ENFP는 충직한 강아지와 닮았어요.", "good": ("INFJ", "깊이 있는 INFJ와 ENFP의 에너지가 조화를 이뤄요."), "bad": ("ISTJ", "ENFP의 즉흥성이 ISTJ의 계획을 방해할 수 있어요."), "image": "https://i.pinimg.com/564x/b4/80/86/b4808642f8673f30a4e3184f1d95ec12.jpg"},
    "ENTP": {"emoji": "🤠", "animal": "원숭이", "gif": "https://media.giphy.com/media/xTiTnGkt9wVjF0iC2M/giphy.gif", "desc": "창의적이고 도전적인 ENTP는 호기심 많은 원숭이와 닮았어요.", "good": ("INTJ", "서로의 아이디어로 자극을 주며 발전해요."), "bad": ("ISFJ", "보수적인 ISFJ는 ENTP의 자유로움을 이해하기 어려워요."), "image": "https://i.pinimg.com/originals/e4/c9/23/e4c923c348a60b17bc7c83bfb4c91e01.jpg"},
    "ESTJ": {"emoji": "🐮", "animal": "소", "gif": "https://media.giphy.com/media/l4EoX1c4J8y6mV3EY/giphy.gif", "desc": "실용적이고 책임감 강한 ESTJ는 성실한 소와 닮았어요.", "good": ("ISTJ", "비슷한 성향으로 안정적인 관계를 유지해요."), "bad": ("INFP", "이상주의적인 INFP는 ESTJ의 현실주의를 답답해할 수 있어요."), "image": "https://i.pinimg.com/originals/50/14/7b/50147be7f3ac8ce33f20be3e09eeabcb.jpg"},
    "ESFJ": {"emoji": "🦟", "animal": "강치", "gif": "https://media.giphy.com/media/y4pAQv58ETJgRQb6t8/giphy.gif", "desc": "친절하고 사교적인 ESFJ는 사람을 좋아하는 강치와 닮았어요.", "good": ("ISFP", "서로 감정을 존중하며 따뜻한 관계를 만들어가요."), "bad": ("INTP", "논리적인 INTP는 감성적인 ESFJ를 이해하기 어려워요."), "image": "https://i.pinimg.com/originals/66/b2/ae/66b2ae0b90d76f3a1b8cdbcf4cfb3e9a.jpg"},
    "ENFJ": {"emoji": "🐇", "animal": "토끼", "gif": "https://media.giphy.com/media/1LweXxLDPx3xC/giphy.gif", "desc": "사려 깊고 리더십 있는 ENFJ는 따뜻한 토끼와 닮았어요.", "good": ("INFP", "감정적으로 잘 통하며 서로를 지지해줘요."), "bad": ("ISTP", "과묵한 ISTP는 ENFJ의 감정 표현을 어렵게 느낄 수 있어요."), "image": "https://i.pinimg.com/originals/8c/f8/6e/8cf86e4f6f4eaa1b1d8bb58eb8857ae2.jpg"},
    "ENTJ": {"emoji": "🦅", "animal": "독수리", "gif": "https://media.giphy.com/media/l41YfI7fMzkvjPReo/giphy.gif", "desc": "통솔력과 목표지향적인 ENTJ는 높은 곳을 나는 독수리와 닮았어요.", "good": ("INTP", "전략적인 사고를 공유하며 함께 성장해요."), "bad": ("ISFP", "자유로운 ISFP는 ENTJ의 통제를 답답해할 수 있어요."), "image": "https://i.pinimg.com/originals/d7/0a/18/d70a185f8a6ba54cfd85ad2f33e0ce15.jpg"}
}

# UI 표시
st.markdown("""<h1 style='text-align: center;'>🌟 MBTI 동물 추천기 🐾</h1>""", unsafe_allow_html=True)

if st.session_state.selected_mbti is None:
    st.markdown("### 🔎 당신의 MBTI는 무엇인가요?")
    mbti_list = list(mbti_data.keys())
    cols = st.columns(4)
    for i, mbti in enumerate(mbti_list):
        col = cols[i % 4]
        with col:
            st.image(mbti_data[mbti]["image"], caption=mbti, use_column_width=True)
            if st.button(f"{mbti} 선택하기"):
                st.session_state.selected_mbti = mbti
                st.session_state.show_result = False
                st.rerun()

elif not st.session_state.show_result:
    st.markdown(f"## 🤔 당신의 MBTI에 여우린 동물은?")
    with st.empty():
        for i in range(3, 0, -1):
            st.info(f"{i}초 후 결과가 나오어요!", icon="⏳")
            time.sleep(1)
    st.session_state.show_result = True
    st.rerun()

else:
    mbti = st.session_state.selected_mbti
    data = mbti_data[mbti]

    st.markdown(f"## 🎉 {mbti} 유형의 추천 동물은?")
    st.markdown(f"# {data['emoji']} {data['animal']}")
    st.image(data["gif"], caption=f"{data['animal']} GIF", use_column_width=st.session_state.mobile)
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
        st.rerun()
