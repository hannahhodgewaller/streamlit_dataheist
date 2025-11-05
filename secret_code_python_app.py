# secret_code_app.py

import streamlit as st

# --- Theme Toggle ---
theme = st.radio("Choose Theme:", ["Light", "Dark"], horizontal=True)
if theme == "Dark":
    st.markdown("""
        <style>
        body { background-color: #1e1e1e; color: #ffffff; }
        input, textarea { background-color: #333333 !important; color: #ffffff !important; }
        </style>
    """, unsafe_allow_html=True)

# --- Session State Setup ---
if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 3
if "code_boxes" not in st.session_state:
    st.session_state.code_boxes = [""] * 6
if "redirect" not in st.session_state:
    st.session_state.redirect = ""

# --- Secret Code ---
code = "HEISTS".lower()

st.markdown("""
### Enter the Secret Code:  
Use 1 letter per box  
Click or press tab to move between boxes  
The code is NOT case sensitive  
"""
           )

# --- Input Boxes ---
cols = st.columns(6)
for i in range(6):
    st.session_state.code_boxes[i] = cols[i].text_input(
        label="",
        value=st.session_state.code_boxes[i],
        max_chars=1,
        key=f"box_{i}"
    )


# --- Submit Button ---
if st.button("Submit Code"):
    user_input = ''.join(st.session_state.code_boxes).lower()
    score = sum(1 for a, b in zip(code, user_input) if a == b)

    if score == len(code):
        st.success("Success! Redirecting...")
        st.session_state.redirect = "https://your-username.github.io/your-repo-name/success.html"
    else:
        st.session_state.attempts_left -= 1
        if st.session_state.attempts_left > 0:
            st.warning(f"Incorrect. You have {st.session_state.attempts_left} attempts left.")
            st.session_state.code_boxes = [""] * 6
        else:
            st.error("No attempts left. Redirecting...")
            st.session_state.redirect = "https://your-username.github.io/your-repo-name/failure.html"

# --- Redirect Logic ---
if st.session_state.redirect:
    st.markdown(f"""
        <meta http-equiv="refresh" content="2;url={st.session_state.redirect}" />
        <p>Redirecting</p>
    """, unsafe_allow_html=True)


