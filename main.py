import streamlit as st
import time

# 페이지 설정
st.set_page_config(page_title="MBTI 동물 추천기", page_icon="🐾", layout="wide")

# 모바일 모드 선택
device_mode = st.sidebar.toggle("📱 모바일 최적화 모드", value=False)
if device_mode:
    st.markdown("<style>img {width: 100% !important;}</style>", unsafe_allow_html=True)

# MBTI 데이터
mbti_data = {
    "INTJ": {"animal": "올빼미", "emoji": "🦉", "desc": "지혜롭고 전략적인 성격의 INTJ는 밤에 사냥하는 올빼미와 닮았어요.",
             "image": "https://i.imgur.com/XdP9qLw.png", "gif": "https://media.giphy.com/media/3o6ZsXR5DM3fRllkIo/giphy.gif",
             "good": ("ENFP", "창의성과 전략이 만나 시너지를 냅니다."),
             "bad": ("ESFP", "즉흥성과 계획성이 충돌할 수 있어요.")},
    "INTP": {"animal": "부엉이", "emoji": "🦉", "desc": "논리적이고 분석적인 INTP는 조용히 관찰하는 부엉이와 닮았어요.",
             "image": "https://i.imgur.com/KqOQwHo.png", "gif": "https://media.giphy.com/media/Zd6P1W0Rjv5MY/giphy.gif",
             "good": ("ENTP", "지적 대화가 끊이지 않아요."),
             "bad": ("ESFJ", "감성 중심 대화에서 어려움을 겪을 수 있어요.")},
    "ENTJ": {"animal": "사자", "emoji": "🦁", "desc": "리더십 강하고 목표 지향적인 ENTJ는 사자와 어울려요.",
             "image": "https://i.imgur.com/4AiXzf8.png", "gif": "https://media.giphy.com/media/J1doTdGCIkPLa/giphy.gif",
             "good": ("INTP", "아이디어를 실행으로 옮기는 좋은 파트너입니다."),
             "bad": ("INFP", "결정 방식에서 큰 차이가 있어요.")},
    "ENTP": {"animal": "여우", "emoji": "🦊", "desc": "재치 있고 즉흥적인 ENTP는 호기심 많은 여우와 닮았어요.",
             "image": "https://i.imgur.com/JEkzP6P.png", "gif": "https://media.giphy.com/media/hp3dmE4gCWA6I/giphy.gif",
             "good": ("INFJ", "서로의 차이가 매력으로 작용합니다."),
             "bad": ("ISFJ", "혼란을 싫어하는 성향과 충돌할 수 있어요.")},
    "INFJ": {"animal": "고양이", "emoji": "😺", "desc": "신비롭고 내향적인 INFJ는 독립적인 고양이와 어울려요.",
             "image": "https://i.imgur.com/0C2rGNC.png", "gif": "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
             "good": ("ENFP", "감정적 유대가 깊어요."),
             "bad": ("ESTP", "즉흥적인 환경에 지칠 수 있어요.")},
    "INFP": {"animal": "사슴", "emoji": "🦌", "desc": "감수성 풍부하고 따뜻한 INFP는 여린 사슴과 닮았어요.",
             "image": "https://i.imgur.com/2FK5m1G.png", "gif": "https://media.giphy.com/media/IY9jKX0u4zA9m/giphy.gif",
             "good": ("ENFJ", "정서적 지지와 이해가 넘쳐요."),
             "bad": ("ESTJ", "지나치게 논리적일 수 있어요.")},
    "ENFJ": {"animal": "강아지", "emoji": "🐶", "desc": "사람을 잘 챙기고 따뜻한 ENFJ는 충성심 강한 강아지와 잘 어울려요.",
             "image": "https://i.imgur.com/LjDiD1a.png", "gif": "https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif",
             "good": ("INFP", "감정 공유가 잘 됩니다."),
             "bad": ("ISTP", "과도한 관심이 부담될 수 있어요.")},
    "ENFP": {"animal": "돌고래", "emoji": "🐬", "desc": "에너지 넘치고 사교적인 ENFP는 장난기 많은 돌고래와 닮았어요!",
             "image": "https://i.imgur.com/G4gXyOw.png", "gif": "https://media.giphy.com/media/11s7Ke7jcNxCHS/giphy.gif",
             "good": ("INFJ", "깊이 있는 대화가 가능해요."),
             "bad": ("ISTJ", "자유성과 규칙성이 충돌해요.")},
    "ISTJ": {"animal": "거북이", "emoji": "🐢", "desc": "신중하고 책임감 있는 ISTJ는 꾸준한 거북이와 닮았어요.",
             "image": "https://i.imgur.com/4m1b1qj.png", "gif": "https://media.giphy.com/media/fdLRZl3lY3eww/giphy.gif",
             "good": ("ESFJ", "같은 생활 리듬을 가지고 있어요."),
             "bad": ("ENFP", "즉흥성에 피로함을 느낄 수 있어요.")},
    "ISFJ": {"animal": "판다", "emoji": "🐼", "desc": "다정하고 조용한 ISFJ는 평화를 사랑하는 판다와 잘 맞아요.",
             "image": "https://i.imgur.com/G0y2Khz.png", "gif": "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
             "good": ("ESFP", "서로를 배려하며 잘 지낼 수 있어요."),
             "bad": ("ENTP", "너무 빠른 변화에 혼란스러워요.")},
    "ESTJ": {"animal": "독수리", "emoji": "🦅", "desc": "실용적이고 체계적인 ESTJ는 통찰력 있는 독수리와 비슷해요.",
             "image": "https://i.imgur.com/Zr1vHtO.png", "gif": "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif",
             "good": ("ISFJ", "현실적인 안정감을 나눌 수 있어요."),
             "bad": ("INFP", "감성 위주의 결정에 답답함을 느낄 수 있어요.")},
    "ESFJ": {"animal": "코끼리", "emoji": "🐘", "desc": "돌봄이 강한 ESFJ는 따뜻하고 사려 깊은 코끼리와 닮았어요.",
             "image": "https://i.imgur.com/gFJY2ut.png", "gif": "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif",
             "good": ("ISFP", "정서적 안정감을 주고 받아요."),
             "bad": ("INTP", "논리 위주의 대화가 피곤할 수 있어요.")},
    "ISTP": {"animal": "표범", "emoji": "🦁", "desc": "조용히 효율적으로 움직이는 ISTP는 날렵한 표범과 비슷해요.",
             "image": "https://i.imgur.com/WxduU2K.png", "gif": "https://media.giphy.com/media/YTbZzCkRQCEJa/giphy.gif",
             "good": ("ESTP", "유사한 성향으로 자연스럽게 통합니다."),
             "bad": ("ENFJ", "감정적 접근이 부담될 수 있어요.")},
    "ISFP": {"animal": "토끼", "emoji": "🐰", "desc": "감성적이고 조용한 ISFP는 순한 토끼와 닮았어요.",
             "image": "https://i.imgur.com/Qov6Y9j.png", "gif": "https://media.giphy.com/media/Q9aD5VYz2tW5C/giphy.gif",
             "good": ("ESFJ", "정서적 케어가 잘 맞아요."),
             "bad": ("ENTJ", "지배적인 태도에 위축될 수 있어요.")},
    "ESTP": {"animal": "치타", "emoji": "🦁", "desc": "모험을 즐기고 즉흥적인 ESTP는 빠른 치타와 어울려요.",
             "image": "https://i.imgur.com/79U5I94.png", "gif": "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif",
             "good": ("ISTP", "함께 활동적인 삶을 즐길 수 있어요."),
             "bad": ("INFJ", "지속적인 자극에 피로할 수 있어요.")}
}

# 세션 상태
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
    st.markdown("## 🔍 당신의 MBTI에 여워든 동물은?")
    with st.spinner("결과 발견 중..."):
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
