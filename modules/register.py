import streamlit as st
import sqlite3
import bcrypt

def show_register():

    st.subheader("Create Account")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Register"):

        if password != confirm_password:
            st.error("Passwords do not match")
            return

        conn = sqlite3.connect("blog.db")
        c = conn.cursor()

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        try:

            c.execute(
                """
                INSERT INTO users
                (username,password)
                VALUES(?,?)
                """,
                (username, hashed)
            )

            conn.commit()

            st.success(
                "Registration Successful"
            )

        except:
            st.error(
                "Username already exists"
            )

    if st.button("Go To Login"):
        st.session_state.page = "Login"
        st.rerun()