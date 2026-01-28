import streamlit as st
from hybrid_engine import hybrid_response

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="☕ Coffee Shop Assistant",
    page_icon="☕",
    layout="centered"
)

st.title("☕ Coffee Shop AI Assistant")
st.caption("Ask about coffee menu, prices, or recommendations")

# -----------------------------------
# INIT CHAT HISTORY
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
    # 🤖 BOT SPEAKS FIRST (ONE TIME)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "Hello ☕ I can help you with coffee menu, prices, and recommendations."
        }
    )

# -----------------------------------
# DISPLAY CHAT HISTORY
# -----------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------------
# USER INPUT
# -----------------------------------
user_input = st.chat_input("Type your question here...")

if user_input:
    # 👤 USER MESSAGE
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # 🤖 BOT RESPONSE
    with st.chat_message("assistant"):
        with st.spinner("☕ Thinking..."):
            response = hybrid_response(user_input)
            st.markdown(response)

    # SAVE BOT RESPONSE
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
