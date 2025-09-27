import streamlit as st
from utils.ai_tools import ask_tutor, make_flashcards, make_quiz
from components.flashcards import render_flashcards
from components.quizzes import render_quiz

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Study & Learn Pro", page_icon="🎓", layout="wide")

# ---- SESSION STATE ----
if "history" not in st.session_state: st.session_state.history = []
if "flashcards" not in st.session_state: st.session_state.flashcards = []
if "quiz" not in st.session_state: st.session_state.quiz = None
if "has_ai_answer" not in st.session_state: st.session_state.has_ai_answer = False
if "flashcards_created" not in st.session_state: st.session_state.flashcards_created = 0
if "quizzes_taken" not in st.session_state: st.session_state.quizzes_taken = 0

# ---- SIDEBAR ----
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/graduation-cap.png", width=80)
    st.title("📚 Study Dashboard")
    st.metric("Topics Studied", len([m for m in st.session_state.history if m["role"] == "assistant"]))
    st.metric("Flashcards Created", st.session_state.flashcards_created)
    st.metric("Quizzes Taken", st.session_state.quizzes_taken)
    st.markdown("---")
    style = st.radio("Explanation Style:", ["Concise", "Detailed", "Analogy"])

# ---- HEADER ----
st.markdown(
    "<h1 style='text-align:center; font-size:40px; background: -webkit-linear-gradient(#00ffae, #2563eb);"
    "-webkit-background-clip: text; -webkit-text-fill-color: transparent;'>"
    "🎓 Study & Learn Assistant</h1>",
    unsafe_allow_html=True
)
# Animated developer credit
st.markdown("""
<style>
.dev-credit {
  font-size:20px;
  color:#00ffae;
  text-align:center;
  margin:20px auto;
  font-weight: bold;
  animation: glow 2.5s ease-in-out infinite;
}

/* Neon glow animation */
@keyframes glow {
  0%,100% { text-shadow: 0 0 0px #00ffae; }
  50%     { text-shadow: 0 0 15px #00ffae, 0 0 30px #00ffae; }
}
</style>

<p class="dev-credit">✨ Developed by Abdul Hanan ✨</p>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-size:18px;'>Learn interactively with AI tutor, flashcards, and quizzes 🚀</p>", unsafe_allow_html=True)

# ---- CHAT SECTION ----
st.subheader("💬 Chat with your AI Tutor")
user_input = st.chat_input("Ask me any topic to learn...")

if user_input:
    st.session_state.history.append({"role":"user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            answer = ask_tutor(user_input, style)
        st.write(answer)

    st.session_state.history.append({"role":"assistant", "content": answer})
    st.session_state.has_ai_answer = True

# replay chat history
for msg in st.session_state.history[:-2] if user_input else st.session_state.history:
    role_class = "user-msg" if msg["role"] == "user" else "ai-msg"
    st.markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# ---- ACTION BUTTONS ----
c1, c2, c3, c4 = st.columns(4)
with c1:
    gen_fc = st.button("📝 Generate Flashcards", use_container_width=True, disabled=not st.session_state.has_ai_answer)
with c2:
    gen_qz = st.button("🎲 Generate Quiz", use_container_width=True, disabled=not st.session_state.has_ai_answer)
with c3:
    clear_fc = st.button("🗑️ Clear Flashcards", use_container_width=True, disabled=not st.session_state.flashcards)
with c4:
    clear_qz = st.button("🗑️ Clear Quiz", use_container_width=True, disabled=not st.session_state.quiz)

# ---- FLASHCARDS ----
# ---- FLASHCARDS ----
if gen_fc:
    with st.spinner("Creating flashcards..."):
        last_answer = next(
            (m["content"] for m in reversed(st.session_state.history) if m["role"] == "assistant"),
            ""
        )
        st.session_state.flashcards = make_flashcards(last_answer)

    # update flashcard counter correctly
    st.session_state.flashcards_created = len(st.session_state.flashcards)

if clear_fc:
    st.session_state.flashcards = []
    st.session_state.flashcards_created = 0

if st.session_state.flashcards:
    render_flashcards(st.session_state.flashcards)


# ---- QUIZ ----
if gen_qz:
    with st.spinner("Building quiz..."):
        last_answer = next((m["content"] for m in reversed(st.session_state.history) if m["role"] == "assistant"), "")
        st.session_state.quiz = make_quiz(last_answer)

if clear_qz:
    st.session_state.quiz = None

if st.session_state.quiz:
    render_quiz(st.session_state.quiz)
