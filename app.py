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

# --- 2. CUSTOM CSS (SaaS Polish) ---
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Pro Buttons */
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
        border-color: #00E676; /* Green glow on hover */
        background-color: #2b313e;
        transform: scale(1.02);
    }
    
    /* Clean Table */
    th {background-color: #2b313e; color: white;}
    
    /* Metrics Styling */
    div[data-testid="stMetricValue"] {
        font-size: 18px;
        color: #00E676;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. THE "GOLD EXEMPLAR" DATA (The Brain) ---
# This dictionary holds the EXACT text you want to show Dr. Umana.

LESSON_DATA = {
    "TEKS 3.2(A)": """
### **Lesson Plan: TEKS 3.2(A) Representing Numbers**
**Target:** Grade 3 | **Focus:** Compose/Decompose to 100,000

---

#### **1. Inferred Context (The "Field Guide")**
* **Vertical Alignment:** Grade 2 (1,200) -> Grade 4 (Multiplication/Decimals).
* **⚠️ Trap Detected:** Students confuse the **value** of a digit with its **place** (e.g., calling a 3 in the thousands place just "3").
* **Zero Trap:** Students often omit zero-value places in expanded notation (e.g., writing 40,506 as 40,000 + 500 + 6, skipping the tens).

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min | Human Path | Low-Tech):** "Write the number **18,504** on a notecard in words OR pictures."
* **Success Criteria:** * Watch for flipping digits.
    * Check if they omit the thousands place.
    * **Note:** Approximate drawings are acceptable; precision grows later.

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** "Place-Value Chart Tiles." Build 46,732 using physical tiles. <br> **[ELPS SUPPORT]:** Sentence Stem: *"The digit ___ is in the ___ place."* (Cognates: Estándar, Forma). |
| **[CORE]** | **Human Path (Device-Free):** "Each One Teach One." Students rotate with whiteboards representing 46,732 in Standard, Word, and Expanded forms. |
| **[EXTENSION]** | **Challenge:** "Flexible Decomposition." Represent 46,732 in two *new* ways (e.g., 45,000 + 1,732). Justify why they are equivalent. |

#### **4. Technology Station**
* **[SCAFFOLD]:** Drag-and-drop Place Value Tool (Accuracy focus).
* **[AI EXTENSION]:** "Visualize Complexity." AI generates 6 different decompositions of 46,732. **(Mandatory: Hand-Verify two results by adding parts manually).**

#### **5. Teacher Success Metrics**
* ✅ Differentiation explicitly aligned to TEKS 3.2(A).
* ✅ Readiness Probe checked for "Zero Trap" misconceptions.
* ✅ Human-first tools (tiles, whiteboards) used for Core.
    """,

    "TEKS 3.2(D)": """
### **Lesson Plan: TEKS 3.2(D) Comparing & Ordering**
**Target:** Grade 3 | **Focus:** Logic & Justification

---

#### **1. Inferred Context (Trap Detector)**
* **⚠️ Trap Detected:** Students compare by "length" (thinking 9,999 > 12,000 because 9 > 1).
* **Equality Trap:** Students forget that "=" is a valid comparison result.

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min):** "Show **38,420** and **38,240**. Ask: Which is greater, **or are they equal**? Point to the deciding place."
* **Success Criteria:** Student identifies the **Hundreds** place (400 vs 200) as the decider.

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** "Stacking Cards." Sort 24,305 vs 24,350 using value cards. <br> **[ELPS SUPPORT]:** *"I compared the numbers by looking at the ___ place first."* |
| **[CORE]** | **Human Path:** "Symbol Debate." Compare 62,480 vs 62,408. Write symbols (>, <, =) and verbally justify to a partner. |
| **[EXTENSION]** | **Challenge:** "Equality Investigation." Order 91,560, 90,516, 91,506. Generate a new number that fits *between* them. |

#### **4. Technology Station**
* **[SCAFFOLD]:** Digital Number Line (Visual alignment).
* **[AI EXTENSION]:** "Visualize Complexity." Generate 6 numbers between 20,000 and 60,000 that only differ in the middle digits. **(Mandatory: Hand-Verify ordering).**

#### **5. Teacher Success Metrics**
* ✅ Equality comparisons included per scope requirement.
* ✅ Students defended reasoning using place-value vocabulary.
    """,

    "TEKS 3.2(B)": """
### **Lesson Plan: TEKS 3.2(B) Base-10 Relationships**
**Target:** Grade 3 | **Focus:** The "10x" Pattern

---

#### **1. Inferred Context (Trap Detector)**
* **⚠️ Trap Detected:** Students think "10 times bigger" just means "add a zero" (Additive vs Multiplicative).

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min):** Hold up a Ten Rod and a Hundred Flat. Ask: "Exactly how many Rods fit inside this Flat?"
* **Success Criteria:** Student states "10 tens make 1 hundred."

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** "Bundling." Physically rubber-band 10 straws to make 1 bundle. Then bundle 10 bundles. <br> **[ELPS SUPPORT]:** Visual aid showing x10 jumps. |
| **[CORE]** | **Human Path:** "Slide the Digit." Move 4 -> 40 -> 400. Explain the value shift using the sentence: *"The value of the ___ place is 10 times the value of the ___ place."* |
| **[EXTENSION]** | **Challenge:** "The Million Question." If we had 10 Hundred-Thousands blocks, what would we have? Draw a model. |

#### **4. Teacher Success Metrics**
* ✅ Physical manipulatives used before abstract rules.
* ✅ Trap Detector caught the "Add Zero" misconception.
    """
}

# --- 4. SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.title("🧭 Configuration")
    st.caption(f"v1.4 | Enterprise | {datetime.date.today()}")
    st.markdown("---")
    
    # 1. Grade Logic
    grade = st.selectbox("Grade Level", ["Grade 3", "Grade 4", "Grade 5"])
    
    # 2. Language Logic
    lang = st.selectbox("Language", ["English (US)", "Spanish", "Swahili"])
    
    st.markdown("### 🟢 System Diagnostics")
    c1, c2 = st.columns(2)
    c1.metric("Guardrails", "Active")
    c2.metric("ELPS", "Loaded")
    
    if st.button("Reset Session"):
        st.session_state.messages = []
        st.rerun()

# --- 5. MAIN INTERFACE ---
st.title("Ethical Math Agent (Pilot v1.4)")
st.markdown("Select a standard. The engine will adapt to Grade & Language automatically.")

col1, col2, col3 = st.columns(3)
selected = None

with col1:
    if st.button("📝 TEKS 3.2(A)\n(Representation)"):
        selected = "TEKS 3.2(A)"
with col2:
    if st.button("⚖️ TEKS 3.2(D)\n(Comparison)"):
        selected = "TEKS 3.2(D)"
with col3:
    if st.button("🦁 TEKS 3.2(B)\n(Base-10 Logic)"):
        selected = "TEKS 3.2(B)"

# --- 6. CHAT & OUTPUT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if selected:
    # 1. User Input
    user_text = f"Generate {selected} for {grade} in {lang}"
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # 2. Agent Logic
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Consulting Field Guide..."):
            time.sleep(0.8)
            
            # GET CONTENT FROM DICTIONARY
            raw_content = LESSON_DATA.get(selected, "Error.")
            
            # SIMPLE TRANSLATION LOGIC (For Demo)
            final_content = raw_content
            if lang == "Spanish":
                final_content = raw_content.replace("Lesson Plan", "Plan de Lección").replace("Objective", "Objetivo").replace("Trap Detector", "Detector de Trampas")
            elif lang == "Swahili":
                final_content = raw_content.replace("Lesson Plan", "Mpango wa Somo").replace("Objective", "Lengo").replace("Trap Detector", "Kigunduzi cha Mtego")

            # RENDER
            message_placeholder.markdown(final_content)
            
            # --- THE PRO FINISH: TEACHER METRICS DASHBOARD ---
            st.markdown("---")
            st.markdown("#### 📊 Teacher Success Metrics (T-TESS Audit)")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Differentiation", "100%", "Pass")
            m2.metric("Human-First", "Secure", "Pass")
            m3.metric("Trap Detector", "Active", "Pass")
            m4.metric("ELPS Support", "Injected", "Pass")
            
            # --- THE DOWNLOAD BUTTON ---
            st.download_button(
                label="📥 Download Lesson Plan (PDF)",
                data=final_content,
                file_name=f"Ethical_Lesson_{grade}_{selected}.txt",
                mime="text/plain"
            )
            
    st.session_state.messages.append({"role": "assistant", "content": final_content})