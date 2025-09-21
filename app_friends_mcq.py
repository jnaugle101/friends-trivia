# friends_trivia/app_friends_mcq.py
import math
import random
from pathlib import Path

import streamlit as st
from PIL import Image, UnidentifiedImageError
from question_bank import QUESTIONS

APP_LABEL = "Friends Trivia (Multiple Choice)"

# ---------------- Images ----------------
ALLOWED_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif"}
IMG_DIR = (Path(__file__).parent / "images").resolve()

def _valid_image(p: Path) -> bool:
    """Fast integrity check so we don't crash during the game."""
    try:
        with Image.open(p) as im:
            im.verify()
        return True
    except Exception:
        return False

def _scan_image_pool():
    """Return (valid_paths, invalid_paths) as lists of strings."""
    valid, invalid = [], []
    for p in IMG_DIR.glob("*"):
        if p.is_file() and p.suffix.lower() in ALLOWED_SUFFIXES:
            if _valid_image(p):
                valid.append(str(p))
            else:
                invalid.append(str(p))
    return valid, invalid

DEFAULT_IMAGE_POOL, _INVALID_IMAGES = _scan_image_pool()

def pick_image_for_question(q: dict, uid: str):
    """
    Choose an image for this question, deterministically by uid:
      - if q["image"] is set, use it
      - elif q["images"] is set, pick one deterministically
      - elif we have a global pool, pick one deterministically
      - else None
    """
    if q.get("image"):
        return q["image"]
    if q.get("images"):
        rng = random.Random(uid)
        return rng.choice(q["images"])
    if DEFAULT_IMAGE_POOL:
        rng = random.Random(uid)
        return rng.choice(DEFAULT_IMAGE_POOL)
    return None

# ---------------- Helpers ----------------
def prepare_round(pool, k, allow_repeats=False):
    """
    Returns a list of question dicts with:
      - uid, q, choices (shuffled), correct_idx
    """
    base = random.choices(pool, k=k) if allow_repeats else random.sample(pool, k=k)
    out = []
    for i, q in enumerate(base):
        uid = f"q{i}"
        options = list(q["options"])
        correct = q["answer"]  # index into options (0..3)

        order = list(range(len(options)))
        random.shuffle(order)
        choices = [options[j] for j in order]
        correct_idx = order.index(correct)

        out.append({
            "uid": uid,
            "q": q["q"],
            "choices": choices,
            "correct_idx": correct_idx,
            # carry through optional per-question images if you ever add them
            "image": q.get("image"),
            "images": q.get("images"),
        })
    return out

# ---------------- UI Setup ----------------
st.set_page_config(page_title=APP_LABEL, page_icon="🧠", layout="centered")
st.title(f"🧠 {APP_LABEL}")
st.caption("Build: 2025-09-21")

# Show a quick image health summary once (start screen only)
if _INVALID_IMAGES:
    with st.expander("⚠️ Image health check (click to view)"):
        st.write(f"Valid images found: **{len(DEFAULT_IMAGE_POOL)}**")
        st.write(f"Invalid images skipped: **{len(_INVALID_IMAGES)}**")
        for bad in _INVALID_IMAGES:
            st.write(f"- {bad}")

# ---------------- Session State ----------------
ss = st.session_state
if "started" not in ss: ss.started = False
if "idx" not in ss: ss.idx = 0
if "order" not in ss: ss.order = []
if "history" not in ss: ss.history = []
if "skipped_once" not in ss: ss.skipped_once = set()

# ---------------- Start Screen ----------------
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
        ss.order = prepare_round(pool, num_q, allow_repeats=allow_repeats)
        ss.history = []
        ss.idx = 0
        ss.started = True
        ss.skipped_once = set()
        st.rerun()

# ---------------- Game Flow ----------------
else:
    i = ss.idx
    total = len(ss.order)

    if i < total:
        qobj = ss.order[i]
        st.subheader(f"Question {i + 1} of {total}")
        st.write(qobj["q"])

        # Image (safe)
        img = pick_image_for_question(qobj, qobj["uid"])
        if img:
            try:
                st.image(img, use_column_width=True)
            except UnidentifiedImageError:
                st.caption("⚠️ Image failed to load; continuing…")
            except Exception as e:
                st.caption(f"⚠️ Image error: {e}; continuing…")

        # Choices (A/B/C/D)
        labels = [f"{chr(65 + j)}. {txt}" for j, txt in enumerate(qobj["choices"])]

        pick_key = f"pick_{qobj['uid']}"
        try:
            chosen_idx = st.radio(
                "Your choice:",
                options=list(range(len(labels))),
                format_func=lambda j: labels[j],
                index=None,
                key=pick_key,
            )
        except TypeError:
            chosen_idx = st.radio(
                "Your choice:",
                options=list(range(len(labels))),
                format_func=lambda j: labels[j],
                index=0,
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
                st.rerun()

        with col3:
            already_skipped = qobj["uid"] in ss.skipped_once
            if st.button("Skip", key=f"skip_{i}", disabled=already_skipped):
                moved = ss.order.pop(i)
                ss.order.append(moved)
                ss.skipped_once.add(moved["uid"])
                st.rerun()

        st.progress(i / total if total else 0.0)
        pending_skips = sum(1 for q in ss.order[i:] if q.get("uid") in ss.skipped_once)
        if pending_skips:
            st.caption(f"⏭️ Skipped to revisit: {pending_skips}")

    else:
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
            st.rerun()
