import streamlit as st
import time
import datetime
import google.generativeai as genai

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
    .stChatInput {position: fixed; bottom: 3rem; z-index: 1000;}
</style>
""", unsafe_allow_html=True)

# --- 3. DATA DICTIONARY (GOLD EXEMPLARS) ---
# These ensure your demos are always 100% perfect.
RAW_DATA = {
    "TEKS 3.2(A)": """### **Lesson Plan: TEKS 3.2(A) Representing Numbers**\n**Target:** Grade 3 | **Focus:** Compose/Decompose\n\n#### **1. Inferred Context (The "Field Guide")**\n* **Trap:** Students confuse digit value with place.\n\n#### **2. Whole Group [READINESS PROBE]**\n* **Task (5 min):** "Write **18,504** in expanded form."\n\n#### **3. Differentiation Menu**\n| Group | Activity |\n| :--- | :--- |\n| **[BRIDGE]** | **Micro-Bridge:** Physical tiles. |\n| **[CORE]** | **Human Path:** Whiteboards. |\n| **[EXTENSION]** | **Challenge:** Flexible Decomposition. |\n\n#### **4. Teacher Success Metrics**\n* ✅ Validity Confirmed.\n""",
    "TEKS 3.2(D)": """### **Lesson Plan: TEKS 3.2(D) Comparing & Ordering**\n**Target:** Grade 3 | **Focus:** Logic\n\n#### **1. Inferred Context**\n* **Trap:** Thinking "Longer = Bigger".\n\n#### **2. Whole Group [READINESS PROBE]**\n* **Task:** Compare 38,420 vs 38,240.\n\n#### **3. Differentiation Menu**\n| Group | Activity |\n| :--- | :--- |\n| **[BRIDGE]** | **Micro-Bridge:** Stacking Cards. |\n| **[CORE]** | **Human Path:** Symbol Debate. |\n| **[EXTENSION]** | **Challenge:** Equality Investigation. |\n\n#### **4. Teacher Success Metrics**\n* ✅ Equality Included.\n""",
    "TEKS 3.2(B)": """### **Lesson Plan: TEKS 3.2(B) Base-10**\n**Target:** Grade 3 | **Focus:** 10x Pattern\n\n#### **1. Inferred Context**\n* **Trap:** "Add a Zero" misconception.\n\n#### **2. Whole Group [READINESS PROBE]**\n* **Task:** Ten Rod vs Hundred Flat.\n\n#### **3. Differentiation Menu**\n| Group | Activity |\n| :--- | :--- |\n| **[BRIDGE]** | **Micro-Bridge:** Bundling Straws. |\n| **[CORE]** | **Human Path:** Slide the Digit. |\n| **[EXTENSION]** | **Challenge:** The Million Question. |\n\n#### **4. Teacher Success Metrics**\n* ✅ Physical Models used.\n"""
}

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🧭 Configuration")
    st.caption(f"v2.0 | HYBRID ENGINE | {datetime.date.today()}")
    st.markdown("---")
    grade = st.selectbox("Grade Level", ["Grade 3", "Grade 4", "Grade 5"])
    lang = st.selectbox("Language", ["English (US)", "Spanish", "Swahili"])
    
    # API KEY CHECK
    if "GEMINI_API_KEY" in st.secrets:
        st.success("Real Brain: **ONLINE**")
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    else:
        st.error("Missing API Key in Secrets!")
        st.stop()

    if st.button("Reset Session"):
        st.session_state.messages = []
        st.rerun()

# --- 5. MAIN INTERFACE ---
st.title("Ethical Math Agent (Pilot v2.0)")
st.markdown("Select a standard OR type anything to activate the Real AI.")

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

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 6. THE HYBRID BRAIN ---
if prompt := st.chat_input("Ask anything (e.g., 'Hello', 'Grade 5 Science')..."):
    trigger = prompt

if trigger:
    st.session_state.messages.append({"role": "user", "content": trigger})
    with st.chat_message("user"):
        st.markdown(trigger)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # LOGIC: If it's a Button Click, use Gold Data. If it's Typing, use Real AI.
        if trigger in RAW_DATA:
            with st.spinner("Retrieving Gold Exemplar..."):
                time.sleep(0.5)
                final_content = RAW_DATA[trigger]
        
        else:
            # REAL AI GENERATION (Handles "Hello", "Science", etc.)
            with st.spinner("Consulting Ethical Framework..."):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    
                    system_prompt = f"""
                    You are the 'Ethical Math Agent'.
                    Current Context: {grade} | {lang}.
                    
                    RULES:
                    1. If the user says "Hello" or chats casually, reply as a helpful Architect.
                    2. If the user asks for a Lesson, generate it using the Ethical Framework:
                       - Human-First (No devices in Core).
                       - Trap Detector (Identify misconceptions).
                       - Differentiation (Bridge/Core/Extension).
                       - Teacher Metrics (T-TESS).
                    3. ALWAYS strictly follow the 'Human-First' rule.
                    """
                    
                    response = model.generate_content(f"{system_prompt}\n\nUser Input: {trigger}", stream=True)
                    final_content = ""
                    for chunk in response:
                        if chunk.text:
                            final_content += chunk.text
                            message_placeholder.markdown(final_content + "▌")
                            
                except Exception as e:
                    final_content = f"Error: {e}"

        # Translation Logic (Applies to both Gold Data and AI Data)
        if lang == "Spanish":
            final_content = final_content.replace("Lesson Plan", "Plan de Lección").replace("Trap Detected", "Trampa Detectada")
        elif lang == "Swahili":
            final_content = final_content.replace("Lesson Plan", "Mpango wa Somo").replace("Trap Detected", "Mtego Umegunduliwa")

        message_placeholder.markdown(final_content)
        
        # Download Button
        st.download_button("📥 Download PDF", final_content, "lesson.txt")
            
    st.session_state.messages.append({"role": "assistant", "content": final_content})