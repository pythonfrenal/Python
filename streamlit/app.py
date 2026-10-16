import streamlit as st
def atm():
    correct_pin="1234"
    if"attempts" not in st.session_state:
        st.session_state.attempts=0

    if st.session_state.attempts>=3:
        st.error("ATM Locked! Too Many Attempts.")
        return
    pin=st.text_input("Enter your ATM PIN",type="password")

    if st.button("submit"):
        if pin==correct_pin:
            st.success("Correct Pin! Access Granted.")

        else:
            st.session_state.attempts += 1
            remaining = 3-st.session_state.attempts
            if remaining == 0:
                st.error("ATM Locked!")
            else:
                st.warning(f"Wrong PIN! {remaining} attempts left")

st.title("ATM PIN System")
atm()

    
