import streamlit as st


def teacher_screen():
	st.title("Teacher Portal")
	st.info("The teacher portal is not implemented yet.")
	if st.button("Back"):
		st.session_state.login_type = None
		st.rerun()
