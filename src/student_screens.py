import streamlit as st


def student_screen():
	st.title("Student Portal")
	st.info("The student portal is not implemented yet.")
	if st.button("Back"):
		st.session_state.login_type = None
		st.rerun()
