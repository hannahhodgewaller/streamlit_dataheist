# secret_code_app.py

import streamlit as st

# Secret Code: Change only the word in quotation marks!
# Ensure the word is in quotation marks
# Ensure the text .lower appears after the quotation marks.
# Example code - code = "HEIST9".lower()

code = "HEIST9".lower() 

# --- Session State Setup ---
if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 3
if "code_boxes" not in st.session_state:
    st.session_state.code_boxes = [""] * 6
if "redirect" not in st.session_state:
    st.session_state.redirect = ""

st.markdown("""
### Enter the Secret Code:  
* Use 1 letter or number per box  
* Click or press tab to move between boxes  
* The code is NOT case sensitive  
"""
           )

# Input Boxes
cols = st.columns(len(code))
for i in range(len(code)):
    st.session_state.code_boxes[i] = cols[i].text_input(
        label="",
        value=st.session_state.code_boxes[i],
        max_chars=1,
        key=f"box_{i}"
    )


# Submit Button
if st.button("Submit Code"):
    user_input = ''.join(st.session_state.code_boxes).lower()
    score = sum(1 for a, b in zip(code, user_input) if a == b)

    if score == len(code):
        st.success("Success! Redirecting...")
        st.session_state.redirect = "https://hannahhodgewaller.github.io/streamlit_dataheist/success.html"
    else:
        st.session_state.attempts_left -= 1
        if st.session_state.attempts_left > 0:
            st.warning(f"Incorrect. You have {st.session_state.attempts_left} attempts left.")
            st.session_state.code_boxes = [""] * 6
        else:
            st.error("No attempts left. Redirecting...")
            st.session_state.redirect = "https://hannahhodgewaller.github.io/streamlit_dataheist/failure.html"

# Redirect Text Logic 
if st.session_state.redirect:
    st.markdown(f"""
        <meta http-equiv="refresh" content="2;url={st.session_state.redirect}" />
        <p>Redirecting</p>
    """, unsafe_allow_html=True)








