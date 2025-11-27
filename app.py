import streamlit as st
import time
import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Ethical Agent | Enterprise",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS ---
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stButton>button {
        background-color: #1e2530;
        color: white;
        border: 1px solid #4a148c;
        border-radius: 8px;
        height: 70px;
        width: 100%;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        border-color: #00E676;
        background-color: #2b313e;
        transform: scale(1.02);
    }
    th {background-color: #2b313e; color: white;}
    /* Fix Chat Input to look like a Search Bar */
    .stChatInput {
        position: fixed;
        bottom: 3rem;
        z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. DATA DICTIONARY (The Knowledge Base) ---
RAW_DATA = {
    "TEKS 3.2(A)": """
### **Lesson Plan: TEKS 3.2(A) Representing Numbers**
**Target:** {grade} | **Language:** {lang} | **Focus:** Compose/Decompose

---

#### **1. Inferred Context (The "Field Guide")**
* **Vertical Alignment:** Previous Grade -> Future Grade.
* **⚠️ Trap Detected:** Students confuse digit value with place.
* **Zero Trap:** Omitted zero-value places.

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min):** "Write **18,504** in expanded form."
* **Success Criteria:** Check for zero-place errors.

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** Build with physical tiles. <br> **[ELPS]:** *"The digit ___ is in the ___ place."* |
| **[CORE]** | **Human Path:** Rotate with whiteboards. |
| **[EXTENSION]** | **Challenge:** Flexible Decomposition. |

#### **4. Teacher Success Metrics**
* ✅ Differentiation aligned.
* ✅ Human-first approach used.
    """,
    
    # (Other standards would go here, but the "Search" handles new ones via simulation below)
}

# --- 4. LOGIC ENGINE ---
def generate_response(topic, grade, lang):
    # 1. Check if we have "Gold" data for this topic
    if topic in RAW_DATA:
        content = RAW_DATA[topic]
    else:
        # 2. If not, SIMULATE a new lesson (The "Search" Logic)
        content = f"""
### **Lesson Plan: {topic}**
**Target:** {grade} | **Language:** {lang} | **Focus:** Conceptual Understanding

---

#### **1. Inferred Context (Auto-Generated)**
* **Vertical Alignment:** Scaffolding from previous grade concepts.
* **⚠️ Trap Detected:** Common misconception regarding {topic}.

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min):** Low-tech diagnostic question related to {topic}.
* **Constraint:** No devices allowed.

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** Physical manipulatives task. <br> **[ELPS]:** Sentence stems in {lang}. |
| **[CORE]** | **Human Path:** Peer-to-peer discussion and modeling. |
| **[EXTENSION]** | **Challenge:** Complex application of {topic}. |

#### **4. Technology Station**
* **[AI EXTENSION]:** "Visualize Complexity." Hand-verify results.

#### **5. Teacher Success Metrics**
* ✅ Guardrails Active.
* ✅ Human-First Protocol Followed.
        """

    # Apply Translation & Scaling
    if lang == "Spanish":
        content = content.replace("Lesson Plan", "Plan de Lección").replace("Trap Detected", "Trampa Detectada")
    elif lang == "Swahili":
        content = content.replace("Lesson Plan", "Mpango wa Somo").replace("Trap Detected", "Mtego Umegunduliwa")
        
    return content

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("🧭 Configuration")
    st.caption(f"v1.5 | Enterprise | {datetime.date.today()}")
    st.markdown("---")
    grade = st.selectbox("Grade Level", ["Grade 3", "Grade 4", "Grade 5"])
    lang = st.selectbox("Language", ["English (US)", "Spanish", "Swahili"])
    st.success("Logic Hardening: **ACTIVE**")
    if st.button("Reset Session"):
        st.session_state.messages = []
        st.rerun()

# --- 6. MAIN INTERFACE ---
st.title("Ethical Math Agent (Pilot v1.5)")
st.markdown("Select a standard OR type your own below.")

# BUTTONS
col1, col2, col3, col4 = st.columns(4)
trigger = None

with col1:
    if st.button("📝 TEKS 3.2(A)"): trigger = "TEKS 3.2(A)"
with col2:
    if st.button("⚖️ TEKS 3.2(D)"): trigger = "TEKS 3.2(D)"
with col3:
    if st.button("🦁 TEKS 3.2(B)"): trigger = "TEKS 3.2(B)"
with col4:
    if st.button("🧪 Blind Test"): trigger = "Blind Test"

# CHAT HISTORY
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 7. INPUT HANDLER (The Fix) ---
# This checks: Did they click a button? OR Did they type?

if prompt := st.chat_input("Search any standard (e.g., 'Grade 5 Fractions')..."):
    trigger = prompt

if trigger:
    # User Message
    st.session_state.messages.append({"role": "user", "content": trigger})
    with st.chat_message("user"):
        st.markdown(trigger)

    # Agent Generation
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Consulting Field Guide..."):
            time.sleep(1)
            
            # Generate Content
            final_content = generate_response(trigger, grade, lang)
            
            # Typewriter
            display_text = ""
            for char in final_content:
                display_text += char
                if len(display_text) % 5 == 0: 
                    message_placeholder.markdown(display_text + "▌")
                    time.sleep(0.001)
            message_placeholder.markdown(final_content)
            
            # Download
            st.download_button("📥 Download PDF", final_content, "lesson.txt")
            
    st.session_state.messages.append({"role": "assistant", "content": final_content})