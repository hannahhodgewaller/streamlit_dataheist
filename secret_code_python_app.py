# secret_code_app.py

import streamlit as st

# Initialize session state
if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 3
if "code_boxes" not in st.session_state:
    st.session_state.code_boxes = [""] * 6
if "redirect" not in st.session_state:
    st.session_state.redirect = ""

# Secret code
code = "HEISTS".lower()

st.title("🔐 Enter the Secret Code")

# Display input boxes
cols = st.columns(6)
for i in range(6):
    st.session_state.code_boxes[i] = cols[i].text_input(
        label="",
        value=st.session_state.code_boxes[i],
        max_chars=1,
        key=f"box_{i}"
    )

# Submit button
if st.button("Submit Code"):
    user_input = ''.join(st.session_state.code_boxes).lower()
    score = sum(1 for a, b in zip(code, user_input) if a == b)

    if score == len(code):
        st.success("✅ Success! Redirecting...")
        st.session_state.redirect = "https://example.com/success"  # Replace with your success URL
    else:
        st.session_state.attempts_left -= 1
        if st.session_state.attempts_left > 0:
            st.warning(f"❌ Incorrect. You have {st.session_state.attempts_left} attempts left.")
        else:
            st.error("🚫 No attempts left. Redirecting...")
            st.session_state.redirect = "https://example.com/failure"  # Replace with your failure URL

# Redirect if needed
if st.session_state.redirect:
    st.markdown(f"""
        <meta http-equiv="refresh" content="2;url={st.session_state.redirect}" />
        <p>Redirecting to <a href="{st.session_state.redirect}">{st.session_state.redirect}</a>...</p>
    """, unsafe_allow_html=True)

# Reset button
if st.button("Reset"):
    st.session_state.code_boxes = [""] * 6
    st.session_state.attempts_left = 3
    st.session_state.redirect = ""
    st.experimental_rerun()