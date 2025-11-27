import streamlit as st
import time
import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Ethical Agent | Pilot v1.3",
    page_icon="🤖",
    layout="wide"
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
        border-radius: 10px;
        height: 80px;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        border-color: #6200EA;
        background-color: #2b313e;
    }
    /* Clean Table Styling */
    th {background-color: #2b313e; color: white;}
</style>
""", unsafe_allow_html=True)

# --- 3. DATA DICTIONARY (The "Fake Brain") ---
# Note: I replaced "Grade 3" with "{grade}" so it updates based on the sidebar!

LESSON_DATA = {
    "TEKS 3.2(A)": """
### **Lesson Plan: TEKS 3.2(A) Representing Numbers**
**Target:** {grade} | **Language:** {lang} | **Focus:** Compose/Decompose

---

#### **1. Inferred Context (Trap Detector)**
* **Vertical Alignment:** Previous Grade -> Future Grade.
* **⚠️ Trap Detected:** Students often think "Expanded Form" means just listing digits (e.g., writing 4, 2, 5 instead of 400 + 20 + 5).

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min, Low-Tech):** "Write the number **24,306** in expanded form using place-value blocks drawn on your whiteboard."
* **Success Criteria:** Correctly handles the ZERO in the tens place.

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge (8-12 min):** Use physical Base-10 blocks to build numbers. <br> **[ELPS SUPPORT]:** Sentence Stem: *"The value of the ___ place is ___."* |
| **[CORE]** | **Human Path (Device-Free):** Place Value Carousel. Stations with cards. Students write word form and explain value to a partner. |
| **[EXTENSION]** | **Challenge:** "Create the smallest change." If you change one digit in 70,090, what is the smallest value change possible? |

#### **4. Technology Station**
* **[SCAFFOLD]:** Virtual Base-10 Builder.
* **[AI EXTENSION]:** "Visualize Complexity." Use AI to generate a dataset of 50 cities and filter by population magnitude. **(Mandatory: Hand-Verify first 3 results).**

#### **5. Teacher Success Metrics**
* ✅ ELPS scaffolds present for Bridge group.
* ✅ Trap Detector addressed the "Zero Placeholder" error.
    """,

    "TEKS 3.2(D)": """
### **Lesson Plan: TEKS 3.2(D) Comparing & Ordering**
**Target:** {grade} | **Language:** {lang} | **Focus:** Logic & Justification

---

#### **1. Inferred Context (Trap Detector)**
* **⚠️ Trap Detected:** Students look at the "length" of the number rather than the highest place value.
* **Equality Trap:** Students forget that "=" is a valid comparison result.

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min):** "Show 48,520 vs 48,502. Ask: Which is greater, **or are they equal**? Prove it without speaking."
* **Success Criteria:** Pointing to the TENS place as the deciding factor.

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** "Stacking Cards." Use index cards to physically stack digits and compare column by column. <br> **[ELPS SUPPORT]:** Cognates: *Comparar* (Compare), *Igual* (Equal). |
| **[CORE]** | **Human Path:** "Symbol Debate." Students draw two cards, place a symbol (<, >, =), and must verbally justify to a partner why. |
| **[EXTENSION]** | **Challenge:** "Equality Investigation." Give students 47,300 and "40,000 + 7,300". Ask them to prove they are equal. |

#### **4. Technology Station**
* **[SCAFFOLD]:** Digital Number Line (Drag and Drop).
* **[AI EXTENSION]:** "Visualize Complexity." Ask AI to generate a list of 5-digit numbers that share the same first 3 digits. Students must order them manually.

#### **5. Teacher Success Metrics**
* ✅ Equality was explicitly tested.
* ✅ Students justified reasoning using Place Value vocabulary.
    """,

    "TEKS 3.2(B)": """
### **Lesson Plan: TEKS 3.2(B) Base-10 Relationships**
**Target:** {grade} | **Language:** {lang} | **Focus:** The "10x" Pattern

---

#### **1. Inferred Context (Trap Detector)**
* **⚠️ Trap Detected:** Students think "10 times bigger" just means "add a zero" (additive thinking) instead of shifting position (multiplicative).

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min):** Hold up a Ten Rod and a Hundred Flat. Ask: "Exactly how many Rods fit inside this Flat?"
* **Success Criteria:** Student states "10 tens make 1 hundred."

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** "Bundling." Physically rubber-band 10 straws to make 1 bundle. Then bundle 10 bundles. <br> **[ELPS SUPPORT]:** Visual aid showing x10 jumps. |
| **[CORE]** | **Human Path:** "The 10x Sentence." Students fill in: "The value of the ___ place is 10 times the value of the ___ place." |
| **[EXTENSION]** | **Challenge:** "The Million Question." If we had 10 of these Hundred-Thousands blocks, what would we have? |

#### **4. Teacher Success Metrics**
* ✅ Physical manipulatives used before abstract rules.
* ✅ Trap Detector caught the "Add Zero" misconception.
    """
}

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🧭 Agent Configuration")
    st.caption(f"v1.3 | System Active | {datetime.date.today()}")
    st.markdown("---")
    
    # 1. Grade Logic
    grade = st.selectbox("Grade Level", ["Grade 3", "Grade 4", "Grade 5"])
    
    # 2. Language Logic
    lang = st.selectbox("Language", ["English (US)", "Spanish", "Swahili"])
    
    st.markdown("### 🟢 System Status")
    st.success("Logic Hardening: **ACTIVE**")
    st.success("ELPS Module: **LOADED**")
    
    if st.button("Clear Output"):
        st.session_state.messages = []
        st.rerun()

# --- 5. MAIN INTERFACE ---
st.title("Ethical Math Agent (Pilot v1.3)")
st.markdown("Select a standard to generate a hardened lesson plan immediately.")

col1, col2, col3 = st.columns(3)
selected_standard = None

with col1:
    if st.button("📝 Plan for TEKS 3.2(A)\n(Representing Numbers)"):
        selected_standard = "TEKS 3.2(A)"
with col2:
    if st.button("⚖️ Plan for TEKS 3.2(D)\n(Comparing & Ordering)"):
        selected_standard = "TEKS 3.2(D)"
with col3:
    if st.button("🦁 Plan for TEKS 3.2(B)\n(Base-10 Relationships)"):
        selected_standard = "TEKS 3.2(B)"

# --- 6. CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 7. GENERATION LOGIC ---
if selected_standard:
    
    # Add User Request
    user_text = f"Generate lesson for {selected_standard} ({lang})"
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("Consulting Field Guide & Applying Guardrails..."):
            time.sleep(1.5) # Fake thinking time
            
            # Get Base Content
            base_content = LESSON_DATA.get(selected_standard, "Standard not found.")
            
            # --- REAL-TIME TRANSLATION SIMULATION ---
            # This swaps words based on the Sidebar Selection!
            
            final_content = base_content # Start with base
            
            if lang == "Spanish":
                final_content = final_content.replace("Lesson Plan", "Plan de Lección")
                final_content.replace("Inferred Context", "Contexto Inferido")
                final_content.replace("Trap Detected", "Trampa Detectada")
                final_content.replace("Whole Group", "Grupo Entero")
                final_content.replace("READINESS PROBE", "PRUEBA DE PREPARACIÓN")
                final_content.replace("Differentiation Menu", "Menú de Diferenciación")
                final_content.replace("Teacher Success Metrics", "Métricas de Éxito Docente")
                final_content.replace("Bridge", "Puente")
            
            elif lang == "Swahili":
                final_content = final_content.replace("Lesson Plan", "Mpango wa Somo")
                final_content.replace("Inferred Context", "Muktadha Uliohitimishwa")
                final_content.replace("Trap Detected", "Mtego Umegunduliwa")
                final_content.replace("Whole Group", "Kikundi Kizima")
                final_content.replace("READINESS PROBE", "JARIBIO LA UTAYARI")
                final_content.replace("Differentiation Menu", "Menú ya Utofautishaji")
                final_content.replace("Teacher Success Metrics", "Vipimo vya Mafanikio ya Mwalimu")
            
            # Inject Grade and Language Variables
            final_content = final_content.format(grade=grade, lang=lang)
            
            # Typewriter Effect
            display_text = ""
            for char in final_content:
                display_text += char
                if len(display_text) % 5 == 0: 
                    message_placeholder.markdown(display_text + "▌")
                    time.sleep(0.001)
            
            message_placeholder.markdown(final_content)
            
    st.session_state.messages.append({"role": "assistant", "content": final_content})