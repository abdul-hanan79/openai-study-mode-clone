import streamlit as st

def render_flashcards(cards):
    st.subheader("📝 Flashcards")

    st.markdown("""
    <style>
    .flashcard {
        border-radius: 16px;
        width: 100%;
        height: 180px;
        perspective: 1000px;
        margin-bottom: 20px;
    }
    .flashcard-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
    }
    .flashcard:hover .flashcard-inner { transform: rotateY(180deg); }
    .flashcard-front, .flashcard-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 16px;
        font-size: 18px;
        padding: 12px;
        font-weight: bold;
        color: white;
    }
    .flashcard-front {
        background: linear-gradient(135deg, #00ffae, #2563eb);
    }
    .flashcard-back {
        background: linear-gradient(135deg, #2563eb, #00ffae);
        transform: rotateY(180deg);
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

    cols = st.columns(2)
    for i, card in enumerate(cards):
        col = cols[i % 2]
        with col:
            st.markdown(f"""
            <div class="flashcard">
              <div class="flashcard-inner">
                <div class="flashcard-front"><b>Q:</b> {card.get("front","")}</div>
                <div class="flashcard-back"><b>A:</b> {card.get("back","")}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)
