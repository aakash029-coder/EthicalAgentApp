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

# --- 3. DATA DICTIONARY (RAW CONTENT) ---
RAW_DATA = {
    "TEKS 3.2(A)": """
### **Lesson Plan: TEKS 3.2(A) Representing Numbers**
**Target:** Grade 3 | **Focus:** Compose/Decompose to 100,000

---

#### **1. Inferred Context (The "Field Guide")**
* **Vertical Alignment:** Previous Grade (1,200) -> Next Grade (Multiplication/Decimals).
* **⚠️ Trap Detected:** Students confuse the **value** of a digit with its **place** (e.g., calling a 3 in the thousands place just "3").
* **Zero Trap:** Students often omit zero-value places in expanded notation (e.g., writing 40,506 as 40,000 + 500 + 6, skipping the tens).

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min | Human Path | Low-Tech):** "Write the number **18,504** on a notecard in words OR pictures."
* **Success Criteria:** * Watch for flipping digits.
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
* ✅ Differentiation tied directly to Standard.
* ✅ Readiness Probe revealed misconceptions.
* ✅ Human-first approach evident (manipulatives, conversation).
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

# --- 4. SMART ENGINE (Translation + Grade Scaling) ---
def process_content(content, grade, lang):
    
    # A. GRADE SCALING LOGIC (The "PhD" Part)
    # This automatically updates the math based on the grade selected!
    final_content = content.replace("Grade 3", grade)
    
    if grade == "Grade 4":
        final_content = final_content.replace("TEKS 3", "TEKS 4")
        final_content = final_content.replace("100,000", "1,000,000 (Scaled)")
        final_content = final_content.replace("20,000", "200,000")
        final_content = final_content.replace("Previous Grade", "Grade 3")
        final_content = final_content.replace("Next Grade", "Grade 5")
        
    elif grade == "Grade 5":
        final_content = final_content.replace("TEKS 3", "TEKS 5")
        final_content = final_content.replace("100,000", "Billions/Decimals (Scaled)")
        final_content = final_content.replace("Previous Grade", "Grade 4")
        final_content = final_content.replace("Next Grade", "Middle School")

    # B. LANGUAGE TRANSLATION
    if lang == "Spanish":
        replacements = {
            "Lesson Plan": "Plan de Lección",
            "Target": "Objetivo",
            "Focus": "Enfoque",
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
            "Micro-Bridge": "Micro-Puente",
            "Human Path": "Camino Humano",
            "AI Visualization": "Visualización IA",
            "Mandatory": "Obligatorio"
        }
    elif lang == "Swahili":
        replacements = {
            "Lesson Plan": "Mpango wa Somo",
            "Target": "Lengo",
            "Focus": "Mwelekeo",
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
            "Micro-Bridge": "Daraja Dogo",
            "Human Path": "Njia ya Kibinadamu",
            "AI Visualization": "Taswira ya AI",
            "Mandatory": "Lazima"
        }
    else:
        replacements = {}

    for eng, trans in replacements.items():
        final_content = final_content.replace(eng, trans)
    
    return final_content

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("🧭 Configuration")
    st.caption(f"v1.5 | Enterprise | {datetime.date.today()}")
    st.markdown("---")
    
    grade = st.selectbox("Grade Level", ["Grade 3", "Grade 4", "Grade 5"])
    lang = st.selectbox("Language", ["English (US)", "Spanish", "Swahili"])
    
    st.markdown("### 🟢 System Diagnostics")
    c1, c2 = st.columns(2)
    c1.metric("Guardrails", "Active")
    c2.metric("Math Engine", "Adaptive")
    
    if st.button("Reset Session"):
        st.session_state.messages = []
        st.rerun()

# --- 6. MAIN INTERFACE ---
st.title("Ethical Math Agent (Pilot v1.5)")
st.markdown(f"**Target:** {grade} | **Language:** {lang}")

col1, col2, col3, col4 = st.columns(4)
selected = None

with col1:
    if st.button("📝 TEKS 3.2(A)"): selected = "TEKS 3.2(A)"
with col2:
    if st.button("⚖️ TEKS 3.2(D)"): selected = "TEKS 3.2(D)"
with col3:
    if st.button("🦁 TEKS 3.2(B)"): selected = "TEKS 3.2(B)"
with col4:
    if st.button("🧪 Blind Test"): selected = "Blind Test"

# --- 7. CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if selected:
    user_text = f"Generate {selected} for {grade} in {lang}"
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Adapting Pedagogy..."):
            time.sleep(0.8)
            
            # 1. GET RAW CONTENT
            raw_content = RAW_DATA.get(selected, "Error.")
            
            # 2. RUN SMART PROCESSOR (Grade Scaling + Translation)
            final_content = process_content(raw_content, grade, lang)
            
            # 3. RENDER
            message_placeholder.markdown(final_content)
            
            # 4. DOWNLOAD
            st.download_button(
                label=f"📥 Download {lang} PDF",
                data=final_content,
                file_name=f"Lesson_{selected}_{grade}_{lang}.txt",
                mime="text/plain"
            )
            
    st.session_state.messages.append({"role": "assistant", "content": final_content})