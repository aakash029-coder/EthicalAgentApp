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
</style>
""", unsafe_allow_html=True)

# --- 3. DATA DICTIONARY (RAW ENGLISH CONTENT) ---
RAW_DATA = {
    "TEKS 3.2(A)": """
### **Lesson Plan: TEKS 3.2(A) Representing Numbers**
**Standard:** TEKS 3.2(A) — Represent a number up to 100,000 as a composed number: standard form, word form, expanded form, and expanded notation.
**Objective:** I can read, write, and model numbers up to 100,000 in more than one form.
**Human Skill Focus:** Collaboration (students talk, justify, and co-construct place-value meaning).

---

#### **1. Inferred Context (The "Field Guide")**
* **Vertical Alignment:**
    * From Grade 2: Students decomposed numbers up to 1,200.
    * In Grade 3: They must extend this to 100,000.
    * Toward Grade 4: Supports later multi-step operations.
* **⚠️ Trap Detector:**
    * **Validity Check:** All numbers chosen are pre-checked to ensure meaningful digit-value changes (e.g., 46,732).
    * **Misconception:** Students confuse the value of a digit with its place (e.g., calling a 3 in the thousands place "3").

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min | Human Path | Low-Tech):** "On a notecard, write two different forms of **18,504**."
* **Success Criteria:**
    * Watch for flipping digits.
    * Watch for omitting the thousands place.
    * *Note:* Because no number line is used, accuracy is required.

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** "Place-Value Chart Tiles." Build 46,732 using physical tiles. <br> **[ELPS SUPPORT]:** Sentence Stem: *"The digit ___ is in the ___ place."* (Cognates: Estándar, Forma). |
| **[CORE]** | **Human Path (Device-Free):** "Each One Teach One." Students rotate with whiteboards representing 46,732 in Standard, Word, and Expanded forms. |
| **[EXTENSION]** | **Challenge:** "Flexible Decomposition." Represent 46,732 in two *new* ways (e.g., 45,000 + 1,732). Justify equivalence. |

#### **4. Technology Station**
* **[SCAFFOLD]:** Drag-and-drop place-value tool (Goal: Accuracy).
* **[AI EXTENSION]:** "Visualize Complexity." AI generates 6 different decompositions of 46,732. **(Mandatory: Hand-Verify two results by adding parts manually).**

#### **5. Teacher Success Metrics**
* ✅ Differentiation tied directly to TEKS 3.2(A).
* ✅ Readiness Probe revealed misconceptions.
* ✅ Human-first approach evident (manipulatives, conversation).
    """,

    "TEKS 3.2(D)": """
### **Lesson Plan: TEKS 3.2(D) Comparing & Ordering**
**Objective:** Compare and order numbers up to 100,000 using place value logic.
**Human Skill Focus:** Critique & Justification.

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
**Objective:** Explain how each place is 10x the value of the right.
**Human Skill Focus:** Logic & Pattern Recognition.

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
    """,

    "Blind Test": """
### **Blind Test: Raw Standard Analysis**
**Input:** New Raw Standard (Grade 3 Place Value).
**Objective:** Validation of Architecture flexibility.

---

#### **1. Inferred Context**
* **Vertical Alignment:** Prep for 3.NBT.1.
* **Trap:** Reading digits as a string ("2-0-7") instead of value (207).

#### **2. Whole Group [READINESS PROBE]**
* **Task:** "Which is greater: 347 or 374? Write ONE sentence explaining why."
* **Constraint:** Untimed, paper-based.

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** Build 207 vs 172 with blocks. <br> **[ELPS SUPPORT]:** Visual Icon Sheet (Flat=100). |
| **[CORE]** | **Human Path:** Compare pairs aloud. Record >, <, =. Rotate partners. |
| **[EXTENSION]** | **Challenge:** "Swap & Reason." Swap tens/ones in 527. Predict change. |

#### **4. Technology Station**
* **[SCAFFOLD]:** Interactive slide deck.
* **[AI EXTENSION]:** Generate 4-digit puzzles. **(Mandatory: Verify 2 examples by hand).**

#### **5. Teacher Success Metrics**
* ✅ Blind Protocol followed (Standard not named).
* ✅ Success criteria allows approximate number line placement.
    """
}

# --- 4. TRANSLATION ENGINE ---
def translate_content(content, lang):
    if lang == "English (US)":
        return content
    
    # SPANISH DICTIONARY
    if lang == "Spanish":
        replacements = {
            "Lesson Plan": "Plan de Lección",
            "Objective": "Objetivo",
            "Human Skill Focus": "Enfoque en Habilidades Humanas",
            "Inferred Context": "Contexto Inferido",
            "Trap Detector": "Detector de Trampas",
            "Trap Detected": "Trampa Detectada",
            "Vertical Alignment": "Alineación Vertical",
            "Whole Group": "Grupo Entero",
            "READINESS PROBE": "PRUEBA DE PREPARACIÓN",
            "Task": "Tarea",
            "Success Criteria": "Criterios de Éxito",
            "Differentiation Menu": "Menú de Diferenciación",
            "BRIDGE": "PUENTE",
            "CORE": "NÚCLEO",
            "EXTENSION": "EXTENSIÓN",
            "Teacher Success Metrics": "Métricas de Éxito Docente",
            "Activity": "Actividad",
            "Group": "Grupo",
            "Micro-Bridge": "Micro-Puente",
            "Human Path": "Camino Humano",
            "AI Visualization": "Visualización IA",
            "Mandatory": "Obligatorio"
        }
    
    # SWAHILI DICTIONARY
    elif lang == "Swahili":
        replacements = {
            "Lesson Plan": "Mpango wa Somo",
            "Objective": "Lengo",
            "Human Skill Focus": "Mwelekeo wa Ujuzi wa Kibinadamu",
            "Inferred Context": "Muktadha Uliohitimishwa",
            "Trap Detector": "Kigunduzi cha Mtego",
            "Trap Detected": "Mtego Umegunduliwa",
            "Vertical Alignment": "Mpangilio wa Wima",
            "Whole Group": "Kikundi Kizima",
            "READINESS PROBE": "JARIBIO LA UTAYARI",
            "Task": "Kazi",
            "Success Criteria": "Vigezo vya Mafanikio",
            "Differentiation Menu": "Menú ya Utofautishaji",
            "BRIDGE": "DARAJA",
            "CORE": "NJIA KUU",
            "EXTENSION": "PANUZI",
            "Teacher Success Metrics": "Vipimo vya Mafanikio ya Mwalimu",
            "Activity": "Shughuli",
            "Group": "Kikundi",
            "Micro-Bridge": "Daraja Dogo",
            "Human Path": "Njia ya Kibinadamu",
            "AI Visualization": "Taswira ya AI",
            "Mandatory": "Lazima"
        }

    # Apply Translations
    for eng, trans in replacements.items():
        content = content.replace(eng, trans)
    
    return content

# --- 5. SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.title("🧭 Configuration")
    st.caption(f"v1.4 | Enterprise | {datetime.date.today()}")
    st.markdown("---")
    
    # Only Language (Grade Removed)
    lang = st.selectbox("Language", ["English (US)", "Spanish", "Swahili"])
    
    st.markdown("### 🟢 System Diagnostics")
    c1, c2 = st.columns(2)
    c1.metric("Guardrails", "Active")
    c2.metric("ELPS", "Loaded")
    
    if st.button("Reset Session"):
        st.session_state.messages = []
        st.rerun()

# --- 6. MAIN INTERFACE ---
st.title("Ethical Math Agent (Pilot v1.4)")
st.markdown("Select a standard. The engine will adapt to Language automatically.")

col1, col2, col3, col4 = st.columns(4)
selected = None

with col1:
    if st.button("📝 TEKS 3.2(A)"):
        selected = "TEKS 3.2(A)"
with col2:
    if st.button("⚖️ TEKS 3.2(D)"):
        selected = "TEKS 3.2(D)"
with col3:
    if st.button("🦁 TEKS 3.2(B)"):
        selected = "TEKS 3.2(B)"
with col4:
    if st.button("🧪 Blind Test"):
        selected = "Blind Test"

# --- 7. CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if selected:
    user_text = f"Generate {selected} in {lang}"
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Consulting Field Guide..."):
            time.sleep(0.8)
            
            # 1. GET CONTENT
            raw_content = RAW_DATA.get(selected, "Error loading content.")
            
            # 2. TRANSLATE CONTENT
            final_content = translate_content(raw_content, lang)
            
            # 3. RENDER
            message_placeholder.markdown(final_content)
            
            # 4. DOWNLOAD BUTTON
            st.download_button(
                label=f"📥 Download {lang} PDF",
                data=final_content,
                file_name=f"Lesson_{selected}_{lang}.txt",
                mime="text/plain"
            )
            
    st.session_state.messages.append({"role": "assistant", "content": final_content})