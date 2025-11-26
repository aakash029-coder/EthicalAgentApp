import streamlit as st
import time
import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Ethical Agent | Pilot v1.3",
    page_icon="🤖",
    layout="wide"
)

# --- 2. CUSTOM CSS (Dark Mode Polish) ---
st.markdown("""
<style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Chat Input Styling */
    .stChatInput {
        position: fixed;
        bottom: 3rem;
    }
    
    /* User Message Style */
    .st-emotion-cache-janbn0 {
        background-color: #2b313e;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (The "Brain" Settings) ---
with st.sidebar:
    st.title("🧭 Agent Configuration")
    st.caption(f"v1.3 | System Active | {datetime.date.today()}")
    st.markdown("---")
    
    grade = st.selectbox("Grade Level", ["Grade 3", "Grade 4", "Grade 5"])
    lang = st.selectbox("Language", ["English (US)", "Spanish", "Swahili"])
    
    st.markdown("### 🟢 System Status")
    st.success("Logic Hardening: **ACTIVE**")
    st.success("ELPS Module: **LOADED**")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# --- 4. CHAT LOGIC (Session State) ---
# This remembers the conversation like real ChatGPT
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. THE CHAT INPUT (The "Magic" Bar) ---
if prompt := st.chat_input("Enter a standard (e.g., 'TEKS 3.2(D)') or ask a question..."):
    
    # 1. Show User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Agent "Thinking"
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Consulting Field Guide & Epistemic Rules..."):
            time.sleep(1.5) # Fake processing time
            
            # LOGIC: This simulates the Agent's output based on your Prompt
            output_text = f"""
### **Lesson Plan Generated: {prompt}**
**Target:** {grade} | **Language:** {lang}

---

#### **1. Inferred Context (Trap Detector)**
⚠️ **Trap Detected:** Students often confuse magnitude with digit length.

#### **2. Whole Group [READINESS PROBE]**
* **Task (5 min):** "Show 48,520 vs 48,502. Ask: Which is greater?"
* **Constraint:** No devices allowed.

#### **3. Differentiation Menu**
| Group | Activity |
| :--- | :--- |
| **[BRIDGE]** | **Micro-Bridge:** Use Base-10 Blocks. |
| **[CORE]** | **Human Path:** Symbol Cards (>, <, =). |
| **[EXTENSION]** | **AI Visualization:** Visualize 50,000 units. |

#### **4. Teacher Success Metrics**
* ✅ Differentiation Evidence
* ✅ Human-First Protocol
            """
            
            # Typing effect
            for chunk in output_text.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})