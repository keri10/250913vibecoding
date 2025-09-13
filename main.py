import streamlit as st
st.title('나의 첫 웹앱')
st.write('이걸 내가 만들었다고?')


import streamlit as st
import time

# 페이지 설정
st.set_page_config(
    page_title="MBTI 공부법 추천",
    page_icon="📚",
    layout="centered"
)

# CSS 스타일링
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
        animation: gradient 3s ease infinite;
    }
    
    @keyframes gradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 3rem;
    }
    
    .mbti-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .study-method {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #4ECDC4;
    }
    
    .tip-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #FF6B6B;
    }
    
    .stSelectbox > div > div {
        background-color: #f8f9fa;
        border-radius: 10px;
    }
    
    .floating-emoji {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
</style>
""", unsafe_allow_html=True)

# MBTI 데이터
mbti_data = {
    "INTJ (건축가)": {
        "emoji": "🏗️",
        "personality": "독립적이고 전략적인 사고를 가진 완벽주의자",
        "study_methods": [
            "📊 체계적인 학습 계획 수립",
            "🎯 명확한 목표 설정과 단계별 접근",
            "📖 독서와 심화 학습 선호", 
            "🔍 개념의 본질과 원리 파악",
            "⏰ 혼자만의 조용한 공간에서 집중 학습"
        ],
        "tips": "장기적 관점에서 학습 로드맵을 만들고, 이론과 실무를 연결하여 학습하세요."
    },
    "INTP (논리술사)": {
        "emoji": "🔬",
        "personality": "호기심 많고 독립적인 사색가",
        "study_methods": [
            "🤔 개념 간의 연관성과 논리적 구조 파악",
            "💡 창의적이고 자유로운 학습 방식",
            "📚 다양한 관점에서 주제 탐구",
            "🧩 문제 해결 과정에서 학습",
            "🌟 흥미로운 주제에 몰입하여 깊이 있게 학습"
        ],
        "tips": "호기심을 자극하는 주제부터 시작하고, 이론을 실제 문제에 적용해보세요."
    },
    "ENTJ (통솔자)": {
        "emoji": "👑",
        "personality": "대담하고 상상력이 풍부한 강력한 지도자",
        "study_methods": [
            "🎯 명확한 학습 목표와 데드라인 설정",
            "📈 효율적이고 결과 중심적 학습",
            "👥 스터디 그룹 리드하며 학습",
            "📊 학습 진도 관리와 성과 측정",
            "🏆 경쟁적 환경에서 동기부여 받기"
        ],
        "tips": "리더십을 발휘할 수 있는 그룹 스터디를 조직하고, 학습 성과를 정기적으로 평가하세요."
    },
    "ENTP (변론가)": {
        "emoji": "💭",
        "personality": "똑똑하고 호기심 많은 사색가",
        "study_methods": [
            "🗣️ 토론과 브레인스토밍을 통한 학습",
            "🔄 다양한 학습 방법 시도",
            "🎨 창의적이고 혁신적인 접근",
            "👥 다른 사람들과의 아이디어 교환",
            "⚡ 변화하는 학습 환경 선호"
        ],
        "tips": "다양한 학습법을 실험해보고, 토론과 발표를 통해 지식을 정리하세요."
    },
    "INFJ (옹호자)": {
        "emoji": "🌟",
        "personality": "선의의 옹호자, 창의적이고 통찰력이 뛰어난 이상주의자",
        "study_methods": [
            "🎨 창의적이고 의미 있는 학습 방식",
            "📝 노트 정리와 시각화",
            "🤝 소규모 그룹 스터디",
            "🔮 미래 비전과 연결하여 학습",
            "💫 조용하고 평화로운 환경에서 집중"
        ],
        "tips": "학습 내용을 개인적 가치와 연결하고, 마인드맵이나 다이어그램을 활용하세요."
    },
    "INFP (중재자)": {
        "emoji": "🎭",
        "personality": "이상주의적이고 충성심이 강한 중재자",
        "study_methods": [
            "💖 개인적 관심사와 연결하여 학습",
            "🎨 창의적 표현을 통한 학습",
            "📖 스토리텔링과 사례 중심 학습",
            "🌸 유연한 학습 일정",
            "🤗 협력적이고 지지적인 환경"
        ],
        "tips": "자신만의 학습 스타일을 찾고, 관심 분야부터 점진적으로 확장해나가세요."
    },
    "ENFJ (주인공)": {
        "emoji": "🌈",
        "personality": "카리스마 넘치고 영감을 주는 지도자",
        "study_methods": [
            "👥 협력적 학습과 팀워크",
            "🎤 설명하고 가르치며 학습",
            "🌍 실제 상황과 연결하여 학습",
            "💬 토론과 대화를 통한 이해",
            "🎯 명확한 목적의식을 가진 학습"
        ],
        "tips": "다른 사람들과 함께 학습하고, 배운 내용을 누군가에게 설명해보세요."
    },
    "ENFP (활동가)": {
        "emoji": "🎪",
        "personality": "열정적이고 창의적인 자유로운 영혼",
        "study_methods": [
            "🎉 재미있고 다양한 학습 활동",
            "👥 활발한 그룹 활동과 토론",
            "🌟 영감을 주는 스토리와 사례",
            "🔄 학습 방법의 지속적 변화",
            "💡 아이디어 연결과 창의적 사고"
        ],
        "tips": "학습을 재미있는 게임처럼 만들고, 다양한 활동을 통해 지루함을 피하세요."
    },
    "ISTJ (현실주의자)": {
        "emoji": "📋",
        "personality": "실용적이고 사실에 기반한 신뢰할 수 있는 사람",
        "study_methods": [
            "📅 체계적이고 순서대로 학습",
            "📚 반복 학습과 암기",
            "✅ 체크리스트와 학습 계획표 활용",
            "🏠 조용하고 정돈된 환경",
            "📖 검증된 교재와 자료 사용"
        ],
        "tips": "꾸준한 학습 루틴을 만들고, 단계별로 차근차근 진행하세요."
    },
    "ISFJ (수호자)": {
        "emoji": "🛡️",
        "personality": "따뜻하고 책임감 있는 수호자",
        "study_methods": [
            "📝 꼼꼼한 노트 정리",
            "👥 소규모 스터디 그룹",
            "🤝 협력적이고 지지적인 학습",
            "📖 단계별 체계적 학습",
            "💕 인간관계 중심의 학습 환경"
        ],
        "tips": "안정적인 학습 환경을 만들고, 꾸준히 복습하는 습관을 기르세요."
    },
    "ESTJ (경영자)": {
        "emoji": "💼",
        "personality": "뛰어난 관리자, 전통과 질서를 중시하는 사람",
        "study_methods": [
            "📊 목표 지향적이고 효율적인 학습",
            "📈 진도 관리와 성과 측정",
            "👥 구조화된 그룹 스터디",
            "⏰ 엄격한 학습 스케줄",
            "🏆 경쟁과 성취를 통한 동기부여"
        ],
        "tips": "명확한 학습 목표를 세우고, 정해진 일정에 따라 체계적으로 진행하세요."
    },
    "ESFJ (집정관)": {
        "emoji": "🤗",
        "personality": "배려심 많고 사교적인 협력자",
        "study_methods": [
            "👥 함께하는 그룹 스터디",
            "💬 설명하고 토론하며 학습",
            "🌟 격려와 지지가 있는 환경",
            "📚 구조화된 학습 자료",
            "🎯 실용적이고 현실적인 학습"
        ],
        "tips": "스터디 그룹에 참여하고, 서로 격려하며 함께 성장하세요."
    },
    "ISTP (가상가)": {
        "emoji": "🔧",
        "personality": "대담하고 실용적인 실험가",
        "study_methods": [
            "🛠️ 실습과 체험 중심 학습",
            "🔍 문제 해결 과정에서 학습",
            "⚡ 필요할 때 집중적으로 학습",
            "🎯 실용적이고 즉시 적용 가능한 지식",
            "🤫 혼자서 조용히 학습"
        ],
        "tips": "이론보다는 실습을 통해 배우고, 직접 해보면서 경험을 쌓으세요."
    },
    "ISFP (모험가)": {
        "emoji": "🌺",
        "personality": "유연하고 매력적인 예술가",
        "study_methods": [
            "🎨 창의적이고 개성 있는 학습",
            "🌱 자신만의 속도로 학습",
            "💖 관심사와 연결된 학습",
            "🤝 지지적이고 비경쟁적 환경",
            "📖 시각적이고 감성적인 자료"
        ],
        "tips": "자신의 관심사부터 시작하고, 스트레스 없는 환경에서 천천히 학습하세요."
    },
    "ESTP (사업가)": {
        "emoji": "⚡",
        "personality": "똑똑하고 에너지 넘치는 사업가",
        "study_methods": [
            "🎯 즉석에서 활용 가능한 실용적 학습",
            "👥 활동적이고 역동적인 그룹 학습",
            "🎮 게임과 경쟁을 통한 학습",
            "📱 멀티미디어와 기술 활용",
            "⏰ 짧고 집중적인 학습 세션"
        ],
        "tips": "재미있고 활동적인 방법으로 학습하고, 즉시 실습해볼 수 있는 내용을 선택하세요."
    },
    "ESFP (연예인)": {
        "emoji": "🎭",
        "personality": "자발적이고 열정적인 연예인",
        "study_methods": [
            "🎉 재미있고 상호작용이 많은 학습",
            "👥 사람들과 함께하는 활발한 학습",
            "🌈 다채롭고 시각적인 자료",
            "🎵 음악이나 리듬을 활용한 학습",
            "💡 아이디어를 즉시 공유하고 피드백 받기"
        ],
        "tips": "학습을 즐거운 경험으로 만들고, 다른 사람들과 함께 활기차게 공부하세요."
    }
}

# 메인 타이틀
st.markdown('<h1 class="main-title">📚 MBTI 맞춤 공부법 추천 🎯</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">당신의 성격 유형에 딱 맞는 학습법을 찾아보세요!</p>', unsafe_allow_html=True)

# MBTI 선택
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    selected_mbti = st.selectbox(
        "🧠 당신의 MBTI 유형을 선택해주세요:",
        list(mbti_data.keys()),
        index=None,
        placeholder="MBTI 유형을 선택하세요..."
    )

if selected_mbti:
    # 로딩 효과
    with st.spinner('맞춤 학습법을 분석하고 있습니다...'):
        time.sleep(1)
    
    data = mbti_data[selected_mbti]
    
    # 성공 메시지
    st.success(f"✨ {selected_mbti} 유형의 맞춤 학습법을 준비했습니다!")
    
    # MBTI 카드
    st.markdown(f"""
    <div class="mbti-card">
        <div style="text-align: center;">
            <div class="floating-emoji" style="font-size: 4rem; margin-bottom: 1rem;">{data['emoji']}</div>
            <h2>{selected_mbti}</h2>
            <p style="font-size: 1.1rem; opacity: 0.9;">{data['personality']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 추천 학습법
    st.markdown("## 🎯 맞춤 학습법")
    
    for i, method in enumerate(data['study_methods']):
        st.markdown(f"""
        <div class="study-method">
            <strong>{method}</strong>
        </div>
        """, unsafe_allow_html=True)
        
        # 애니메이션 효과를 위한 작은 지연
        if i < len(data['study_methods']) - 1:
            time.sleep(0.1)
    
    # 특별 팁
    st.markdown("## 💡 특별 팁")
    st.markdown(f"""
    <div class="tip-box">
        <strong>🌟 {data['tips']}</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # 추가 격려 메시지
    st.balloons()
    st.markdown("""
    ---
    ### 🌟 화이팅! 당신만의 최적화된 학습법으로 목표를 달성하세요! 🚀
    """)
    
    # 재선택 버튼
    if st.button("🔄 다른 MBTI 유형도 궁금해요!", use_container_width=True):
        st.rerun()

else:
    # 아직 선택하지 않았을 때의 안내
    st.markdown("""
    <div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 15px; margin: 2rem 0;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🤔</div>
        <h3>MBTI 유형을 선택하면</h3>
        <p>당신만을 위한 맞춤형 학습법을 추천해드려요!</p>
    </div>
    """, unsafe_allow_html=True)

# 푸터
st.markdown("""
---
<div style="text-align: center; color: #666; padding: 1rem;">
    Made with ❤️ for better learning | MBTI 맞춤 공부법 추천 서비스
</div>
""", unsafe_allow_html=True)
