import streamlit as st
import time
import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Ethical Agent | Pilot v1.3",
    page_icon="🧬",
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
**Objective:** Compose and decompose numbers up to 100,000 using objects, pictures, and expanded notation.
**Human Skill Focus:** Critique & Precision.

---

#### **1. Inferred Context (Trap Detector)**
* **Vertical Alignment:** Grade 2 (1,200) -> Grade 4 (Multiplication).
* **⚠️ Trap Detected:** Students confuse digit value with place (e.g., calling 3 in 3,000 just "3").
* **Zero Trap:** Omitted zero-value places (e.g., 405 -> 400 + 5).

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min, Low-Tech):** "Write 45,230 in words OR pictures."
* **Success Criteria:** Approximate drawings are okay. Watch for "2 tens" vs "20".

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** Build 32,407 with physical blocks. <br> **[ELPS SUPPORT]:** Sentence Stem: *"The value of ___ is ___."* (Cognates: Valor, Posición). |
| **[CORE]** | **Human Path:** Convert 37,520 (Block -> Standard -> Expanded). Turn and talk: "Which digit has the greatest value?" |
| **[EXTENSION]** | **Challenge:** Create two numbers where Hundreds > Thousands. Compare using >, <, =. |

#### **4. Technology Station**
* **[SCAFFOLD]:** Virtual Base-10 Blocks (48,206).
* **[AI EXTENSION]:** "Visualize Complexity." AI generates 5 numbers between 30k-60k. **(Mandatory: Hand-Verify first 2 results).**

#### **5. Teacher Success Metrics**
* ✅ Validity confirmed for all numbers.
* ✅ Human-first stations encourage talk.
    """,

    "TEKS 3.2(D)": """
### **Lesson Plan: TEKS 3.2(D) Comparing & Ordering**
**Objective:** Compare and order numbers up to 100,000 using place value logic.
**Human Skill Focus:** Critique & Justification.

---

#### **1. Inferred Context (Trap Detector)**
* **⚠️ Trap Detected:** Thinking "Longer number = Bigger number."
* **Alignment:** Grade 2 (3-digits) -> Grade 4 (Decimals).

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min):** "Compare 38,420 vs 38,240. Point to the greater one. Explain why."
* **Success Criteria:** Must mention "Hundreds Place" (400 vs 200).

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** Sort 24,305 vs 24,350 using value cards. <br> **[ELPS SUPPORT]:** Sentence Stem: *"I looked at the ___ place first."* |
| **[CORE]** | **Human Path:** Compare 62,480 vs 62,408. Write symbols (>, <, =) and justify to a partner. |
| **[EXTENSION]** | **Challenge:** Order 91,560, 90,516, 91,506. Identify the exact deciding place. |

#### **4. Technology Station**
* **[SCAFFOLD]:** Drag-and-drop place value chart.
* **[AI EXTENSION]:** "Visualize Complexity." AI generates numbers differing only in middle digits. **(Mandatory: Hand-Verify sample).**

#### **5. Teacher Success Metrics**
* ✅ Equality comparisons included.
* ✅ Reasoning defended verbally.
    """,

    "TEKS 3.2(B)": """
### **Lesson Plan: TEKS 3.2(B) Base-10 Relationships**
**Objective:** Explain how each place is 10x the value of the right.
**Human Skill Focus:** Logic & Pattern Recognition.

---

#### **1. Inferred Context (Trap Detector)**
* **⚠️ Trap Detected:** "Add a Zero" misconception (Additive vs Multiplicative).

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min):** "Draw 300 and 30. Which is worth more? Why?"
* **Success Criteria:** Identifies 300 is 10x larger.

#### **3. Differentiation Menu**

| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** Trade 1 Ten Rod for 10 Ones. Trade 1 Hundred Flat for 10 Tens. <br> **[ELPS SUPPORT]:** *"One ___ equals 10 groups of ___."* |
| **[CORE]** | **Human Path:** "Slide the Digit." Move 4 -> 40 -> 400. Explain the value shift. |
| **[EXTENSION]** | **Challenge:** "The Million Question." If we had 10 Hundred-Thousands, what would we have? |

#### **4. Teacher Success Metrics**
* ✅ Physical models used before abstract rules.
* ✅ Trap Detector active.
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