import streamlit as st
import sqlite3
import bcrypt

def show_login():

    st.subheader("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        conn = sqlite3.connect("blog.db")
        c = conn.cursor()

        c.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = c.fetchone()

        if user:

            stored_password = user[2]

            if bcrypt.checkpw(
                password.encode(),
                stored_password
            ):

                st.success("Login Successful")

                st.session_state.logged_in = True

                st.session_state.page = "Dashboard"

                st.rerun()

            else:

                st.error("Wrong Password")

        else:

            st.error("User Not Found")

    st.markdown("---")

    if st.button("Create Account"):
        st.session_state.page = "Register"
        st.rerun()