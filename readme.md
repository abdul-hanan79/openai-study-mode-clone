# 📚 Study & Learn Mode Clone

An AI-powered study assistant inspired by ChatGPT’s *Study Mode*.
Built with **Streamlit + OpenAI + Python**, as part of my **Certified Agentic & Robotic AI Engineer** assignment under **PIAIC**.

---

## ✨ Features

* 💬 **AI Tutor Chat** – learn any topic with detailed, concise, or analogy-based explanations.
* 📝 **Flashcards Generator** – create flip-style flashcards with gradient UI.
* 🎲 **Interactive Quizzes** – multiple-choice quizzes with glowing feedback, balloons 🎈 for perfect scores, and snow ❄️ for encouragement.
* 📊 **Progress Tracker** – dashboard with topics studied, flashcards created, and quizzes taken.
* 🎨 **Modern UI/UX** – gradient header, glowing credits, gamified design.
* 🗑️ **Clear Controls** – reset flashcards & quizzes without clearing the chat.

---

## 🛠️ Tech Stack

* **Streamlit** – UI framework
* **Python** – backend logic
* **OpenAI GPT-4o-mini** – AI responses, flashcards, quizzes
* **Custom CSS** – pro-level UI styling and animations

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repo & open virtual environment
```bash
# clone the repo
git clone <your-repo-link>
cd study-mode-clone

# create and activate virtual environment (Windows example)
python -m venv venv
venv\Scripts\activate
```

For Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Add your OpenAI API key

Create a `.env` file in the root folder and add:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ Note: You **must have an OpenAI API key** to run this project.

---

### 4️⃣ Start the project

```bash
streamlit run app.py
```

Now open the link (usually `http://localhost:8501`) in your browser. 🎉

---

## Note

This project was developed as part of **Certified Agentic & Robotic AI Engineer** program under **PIAIC**.



