# utils/ai_tools.py
import os, json, re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def _extract_json(text: str):
    """
    Try to pull a JSON object from a model response safely.
    Looks for ```json ... ``` blocks first, then falls back to first {...} block.
    """
    m = re.search(r"```json\s*(\{.*?\})\s*```", text, flags=re.S)
    if not m:
        m = re.search(r"(\{.*\})", text, flags=re.S)
    if not m:
        raise ValueError("No JSON found in model response")
    return json.loads(m.group(1))

def ask_tutor(question, style="Concise"):
    system_prompt = (
        f"You are a study tutor. Explain in a {style.lower()} style. "
        "Return plain text (NOT JSON). Include: explanation + bullet key points + 1 short self-check question."
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":question}
        ]
    )
    return resp.choices[0].message.content

def make_flashcards(source_text: str):
    """
    Return list of flashcards as [{"front": "...", "back": "..."}]
    """
    prompt = (
        "Create 4 crisp flashcards from the content below. "
        "Only return JSON matching this schema exactly:\n"
        "{ \"cards\": [ {\"front\": \"Question side\", \"back\": \"Answer side\"} ] }\n\n"
        "Content:\n" + source_text
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    data = _extract_json(resp.choices[0].message.content)
    return data.get("cards", [])

def make_quiz(source_text: str):
    """
    Return quiz dict:
    { "title": "Quiz title",
      "questions": [
        {"question":"...", "options":["...","...","...","..."], "answer_index": 2}
      ]
    }
    """
    prompt = (
        "Generate a 3-question multiple-choice quiz from the content below. "
        "Do NOT reveal the answers in the options. Do NOT add checkmarks or explanations. "
        "Return ONLY JSON in this exact schema:\n"
        "{ \"title\": \"Short quiz title\", "
        "\"questions\":[{\"question\":\"...\",\"options\":[\"...\",\"...\",\"...\",\"...\"],\"answer_index\":0}] }\n\n"
        "Content:\n" + source_text
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return _extract_json(resp.choices[0].message.content)
