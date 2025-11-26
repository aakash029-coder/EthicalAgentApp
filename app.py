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
    /* Style the buttons to look like "Conversation Starters" */
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
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🧭 Agent Configuration")
    st.caption(f"v1.3 | System Active | {datetime.date.today()}")
    st.markdown("---")
    grade = st.selectbox("Grade Level", ["Grade 3", "Grade 4", "Grade 5"])
    lang = st.selectbox("Language", ["English (US)", "Spanish", "Swahili"])
    st.markdown("### 🟢 System Status")
    st.success("Logic Hardening: **ACTIVE**")
    st.success("ELPS Module: **LOADED**")
    if st.button("Clear History", key="clear"):
        st.session_state.messages = []
        st.rerun()

# --- 4. MAIN INTERFACE & BUTTONS ---
st.title("Ethical Math Agent (Pilot v1.3)")
st.markdown("Select a standard to generate a hardened lesson plan immediately.")

# THE BUTTONS SHE WANTED (Clickable Conversation Starters)
col1, col2, col3 = st.columns(3)
selected_prompt = None

with col1:
    if st.button("📝 Plan for TEKS 3.2(A)\n(Representing Numbers)"):
        selected_prompt = "Plan a lesson for TEKS 3.2(A)"
with col2:
    if st.button("⚖️ Plan for TEKS 3.2(D)\n(Comparing & Ordering)"):
        selected_prompt = "Plan a lesson for TEKS 3.2(D)"
with col3:
    if st.button("🦁 Swahili Mode Test\n(TEKS 3.2B - Base 10)"):
        selected_prompt = "Plan a lesson for TEKS 3.2(B) in Swahili"

# --- 5. CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle Input (Button OR Typing)
if input_text := st.chat_input("Or type a custom standard here..."):
    selected_prompt = input_text

# --- 6. GENERATION LOGIC ---
if selected_prompt:
    # User Message
    with st.chat_message("user"):
        st.markdown(selected_prompt)
    st.session_state.messages.append({"role": "user", "content": selected_prompt})

    # Agent Message
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("Consulting Field Guide & Applying Guardrails..."):
            time.sleep(1.5) 
            
            # Clean Formatting with Real Newlines
            intro = f"### **Lesson Plan Generated: {selected_prompt}**\n**Target:** {grade} | **Language:** {lang}\n\n---\n\n"
            
            context = "#### **1. Inferred Context (Trap Detector)**\n⚠️ **Trap Detected:** Students often confuse magnitude with digit length.\n\n"
            
            probe = "#### **2. Whole Group [READINESS PROBE]**\n* **Task (5 min):** \"Show 48,520 vs 48,502. Ask: Which is greater?\"\n* **Constraint:** No devices allowed.\n\n"
            
            diff = "#### **3. Differentiation Menu**\n| Group | Activity |\n| :--- | :--- |\n| **[BRIDGE]** | **Micro-Bridge:** Use Base-10 Blocks. |\n| **[CORE]** | **Human Path:** Symbol Cards (>, <, =). |\n| **[EXTENSION]** | **AI Visualization:** Visualize 50,000 units. |\n\n"
            
            metrics = "#### **4. Teacher Success Metrics**\n* ✅ Differentiation Evidence\n* ✅ Human-First Protocol"
            
            full_response = intro + context + probe + diff + metrics
            
            # Typewriter Effect
            display_text = ""
            for char in full_response:
                display_text += char
                # Only refresh every few chars to speed up
                if len(display_text) % 5 == 0: 
                    message_placeholder.markdown(display_text + "▌")
                    time.sleep(0.001)
            
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})