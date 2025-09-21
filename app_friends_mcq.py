# friends_trivia/app_friends_mcq.py
import math
import random
from pathlib import Path
BASE_DIR = Path(__file__).parent
DEFAULT_IMAGE_POOL = [str(p) for p in (BASE_DIR / "images").glob("friends*.jpg")]

import streamlit as st
from question_bank import QUESTIONS

APP_LABEL = "Friends Trivia (Multiple Choice)"

# ------------- Helpers -------------
def prepare_round(pool, k, allow_repeats=False):
    """
    Returns a list of question dicts with:
      - uid
      - q
      - choices (shuffled list of 4 options)
      - correct_idx (index into choices)
    """
    base = random.choices(pool, k=k) if allow_repeats else random.sample(pool, k=k)
    out = []
    for i, q in enumerate(base):
        uid = f"q{i}"
        options = list(q["options"])          # list of 4 strings
        correct = q["answer"]                 # index into options (0..3)

        order = list(range(len(options)))
        random.shuffle(order)

        choices = [options[j] for j in order]
        correct_idx = order.index(correct)

        out.append({
            "uid": uid,
            "q": q["q"],
            "choices": choices,
            "correct_idx": correct_idx,
            # keep original for review (optional)
            "_orig_options": options,
            "_orig_answer": correct,
            # pass-through optional per-question images if you add them in the bank
            "image": q.get("image"),
            "images": q.get("images"),
        })
    return out

# Build an image pool from /images (your 11 photos)
# Accepts common image types; works with upper/lower-case file extensions.
DEFAULT_IMAGE_POOL = [
    str(p)
    for p in Path("images").glob("*.*")
    if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"}
]

def pick_image_for_question(q, uid):
    """
    Returns a single path/URL to render for this question.
    Priority:
      - q["image"] (single)
      - random choice from q["images"] (stable by uid)
      - fallback random from DEFAULT_IMAGE_POOL (stable by uid)
      - None if nothing found
    """
    if q.get("image"):
        return q["image"]

    if q.get("images"):
        rng = random.Random(uid)  # stable choice per question
        return rng.choice(q["images"])

    if DEFAULT_IMAGE_POOL:
        rng = random.Random(uid)
        return rng.choice(DEFAULT_IMAGE_POOL)

    return None

# ------------- UI Setup -------------
st.set_page_config(page_title=APP_LABEL, page_icon="🧠", layout="centered")
st.title(f"🧠 {APP_LABEL}")
st.caption("Build: 2025-09-21")

# Session state
ss = st.session_state
if "started" not in ss: ss.started = False
if "idx" not in ss: ss.idx = 0
if "order" not in ss: ss.order = []         # list of prepared question dicts (with choices & correct_idx)
if "history" not in ss: ss.history = []     # dicts: {q, choices, chosen_idx, correct_idx, is_correct}
if "skipped_once" not in ss: ss.skipped_once = set()
if "images" not in ss: ss.images = {}       # uid -> image path

# ------------- Start Screen -------------
if not ss.started:
    pool = QUESTIONS
    if not pool:
        st.warning("No questions found.")
        st.stop()

    st.caption(f"{len(pool)} question(s) available in **Friends**.")
    allow_repeats = st.checkbox("Allow repeats (sample with replacement)", value=False)

    MAX_BASE = 70
    max_q = MAX_BASE if allow_repeats else min(MAX_BASE, len(pool))
    num_default = min(10, max_q)
    num_q = st.slider("How many questions?", min_value=5, max_value=max_q, value=num_default, step=1)

    with st.expander("📋 Rules & Tips", expanded=True):
        st.markdown(
            "- Choose one of the **four** options for each question.\n"
            "- Click **Skip** to revisit a question at the end (once per question).\n"
            "- Click **Quit** anytime and start over.\n"
        )

    if st.button("Start"):
        # Prepare questions for this round
        ss.order = prepare_round(pool, num_q, allow_repeats=allow_repeats)

        # Pick one image per question (stable during the game)
        ss.images = {q["uid"]: pick_image_for_question(q, q["uid"]) for q in ss.order}

        ss.history = []
        ss.idx = 0
        ss.started = True
        ss.skipped_once = set()
        st.rerun()

# ------------- Game Flow -------------
else:
    i = ss.idx
    total = len(ss.order)

    if i < total:
        qobj = ss.order[i]
        st.subheader(f"Question {i + 1} of {total}")
        st.write(qobj["q"])

        # Show image if available
        img = ss.images.get(qobj["uid"])
        if img:
            st.image(img, use_column_width=True)

        # Build labeled options (A/B/C/D)
        labels = [f"{chr(65 + j)}. {txt}" for j, txt in enumerate(qobj["choices"])]

        # Radio returns the index we pass in; format_func shows labels
        pick_key = f"pick_{qobj['uid']}"
        chosen_idx = st.radio(
            "Your choice:",
            options=list(range(len(labels))),
            format_func=lambda j: labels[j],
            index=None,  # set to 0 if your Streamlit version doesn't support None
            key=pick_key,
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Submit", key=f"submit_{i}"):
                if chosen_idx is None:
                    st.warning("Please select an option.")
                else:
                    ok = (chosen_idx == qobj["correct_idx"])
                    ss.history.append({
                        "q": qobj["q"],
                        "choices": qobj["choices"],
                        "chosen_idx": chosen_idx,
                        "correct_idx": qobj["correct_idx"],
                        "is_correct": ok
                    })
                    ss.idx += 1
                    st.rerun()

        with col2:
            if st.button("Quit"):
                ss.started = False
                ss.idx = 0
                ss.order = []
                ss.history = []
                ss.skipped_once = set()
                ss.images = {}
                st.rerun()

        with col3:
            already_skipped = qobj["uid"] in ss.skipped_once
            if st.button("Skip", key=f"skip_{i}", disabled=already_skipped):
                moved = ss.order.pop(i)
                ss.order.append(moved)
                ss.skipped_once.add(moved["uid"])
                st.rerun()

        # Progress + optional skipped count
        st.progress(i / total if total else 0.0)
        pending_skips = sum(1 for q in ss.order[i:] if q.get("uid") in ss.skipped_once)
        if pending_skips:
            st.caption(f"⏭️ Skipped to revisit: {pending_skips}")

    else:
        # End screen
        right = sum(1 for h in ss.history if h["is_correct"])
        needed = math.ceil(total * 0.70)
        pct = (right / total) * 100 if total else 0.0

        st.success(f"Game over! Your score: **{right}/{total}** ({pct:.2f}%)")
        if right >= needed:
            st.info("🌟 Nice work!")
        else:
            st.warning(f"😬 You needed at least **{needed}/{total}** (70%).")

        st.markdown("### Review answers")
        st.write(f"✅ Correct: {right} ❌ Incorrect: {total - right}")

        for idx, h in enumerate(ss.history, start=1):
            icon = "✅" if h["is_correct"] else "❌"
            correct_label = f"{chr(65 + h['correct_idx'])}. {h['choices'][h['correct_idx']]}"
            chosen_label = (
                f"{chr(65 + h['chosen_idx'])}. {h['choices'][h['chosen_idx']]}"
                if h.get("chosen_idx") is not None else "—"
            )
            st.markdown(
                f"**Q{idx} {icon}**  \n"
                f"{h['q']}  \n"
                f"**Your choice:** {chosen_label}  \n"
                f"**Correct answer:** {correct_label}"
            )

        if st.button("Play again"):
            ss.started = False
            ss.idx = 0
            ss.order = []
            ss.history = []
            ss.skipped_once = set()
            ss.images = {}
            st.rerun()
