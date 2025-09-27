import streamlit as st

def render_quiz(quiz_dict):
    st.subheader("🎲 Quiz Time")

    st.markdown("""
    <style>
    .quiz-card {
        background: #1f2937;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .quiz-card:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 16px rgba(0,0,0,0.6);
    }
    .correct {
        background: #00ffae;
        color: black;
        font-weight: bold;
        padding: 8px 12px;
        border-radius: 8px;
        display: inline-block;
        animation: pop 0.4s ease;
    }
    .incorrect {
        background: #ef4444;
        color: white;
        font-weight: bold;
        padding: 8px 12px;
        border-radius: 8px;
        display: inline-block;
        animation: shake 0.4s ease;
    }
    @keyframes pop {
        0% {transform: scale(0.8);}
        100% {transform: scale(1);}
    }
    @keyframes shake {
        0%, 100% {transform: translateX(0);}
        25% {transform: translateX(-5px);}
        75% {transform: translateX(5px);}
    }
    </style>
    """, unsafe_allow_html=True)

    answers = {}
    total = len(quiz_dict.get("questions", []))

    for i, q in enumerate(quiz_dict.get("questions", [])):
        st.markdown(f"<div class='quiz-card'><b>Q{i+1}:</b> {q['question']}</div>", unsafe_allow_html=True)
        answers[i] = st.radio(
            label="",
            options=q["options"],
            index=None,
            key=f"quiz_q_{i}"
        )

    if st.button("🎉 Submit Quiz", use_container_width=True):
        correct = 0
        for i, q in enumerate(quiz_dict["questions"]):
            if answers[i] == q["options"][q["answer_index"]]:
                st.markdown(f"<span class='correct'>Q{i+1}: ✅ Correct</span>", unsafe_allow_html=True)
                correct += 1
            else:
                st.markdown(
                    f"<span class='incorrect'>Q{i+1}: ❌ Wrong — Correct: {q['options'][q['answer_index']]}</span>",
                    unsafe_allow_html=True
                )

        st.progress(correct / total)
        st.info(f"🏆 Your Score: {correct}/{total}")

        # update counter
        st.session_state.quizzes_taken += 1

        if correct == total:
            st.success("🔥 Perfect! All correct!")
            st.balloons()
        elif correct >= total // 2:
            st.warning("👌 Good effort! Keep practicing.")
            st.snow()
        else:
            st.error("😢 Try again.")
