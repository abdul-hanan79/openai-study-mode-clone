import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Study & Learn Clone",
    page_icon="📚",
    layout="wide"
)

# --- SIDEBAR ---
with st.sidebar:
    st.title("📚 Study Mode")
    st.markdown("### Progress Tracker")
    st.metric("Topics Studied", 5)
    st.metric("Flashcards Created", 12)
    st.metric("Quizzes Taken", 3)

    st.markdown("---")
    st.subheader("⚙️ Settings")
    style = st.radio("Explanation Style:", ["Concise", "Detailed", "Analogy"])

# --- MAIN CONTENT ---
st.title("🎓 Study & Learn Assistant")
st.caption("Your AI-powered tutor for explanations, flashcards, and quizzes.")

# --- CHAT SECTION ---
st.subheader("💬 Ask your tutor")
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Type your question here...")
if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    # (placeholder AI response)
    st.session_state.history.append({"role": "assistant", "content": "This is a sample explanation with key points and a quiz."})

for msg in st.session_state.history:
    st.chat_message(msg["role"]).write(msg["content"])

# --- FLASHCARDS ---
st.subheader("📝 Flashcards")
with st.expander("View Generated Flashcards", expanded=True):
    st.markdown("**Q:** What is photosynthesis?\n\n**A:** The process by which plants make food using sunlight.")
    st.markdown("**Q:** What is the chemical formula for water?\n\n**A:** H₂O")

# --- QUIZ ---
st.subheader("🎲 Quick Quiz")
st.markdown("**Q1:** Which gas do plants absorb for photosynthesis?")
quiz_answer = st.radio("Choose your answer:", ["Oxygen", "Carbon Dioxide", "Nitrogen"], index=None)
if st.button("Check Answer"):
    if quiz_answer == "Carbon Dioxide":
        st.success("✅ Correct! Plants absorb CO₂.")
    else:
        st.error("❌ Incorrect. The correct answer is Carbon Dioxide.")

# --- FOOTER ---
st.markdown("---")
st.caption("Made with ❤️ by Abdul Hanan Software Engineer")
