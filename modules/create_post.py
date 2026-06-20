import streamlit as st
import sqlite3
from components.navbar import show_navbar

def show_create_post():

    show_navbar()

    st.title("✍️ Create Blog Post")

    title = st.text_input("📝 Blog Title")

    content = st.text_area(
        "📄 Blog Content",
        height=300
    )

    if st.button("🚀 Publish Blog"):

        if title and content:

            conn = sqlite3.connect("blog.db")
            c = conn.cursor()

            c.execute(
                """
                INSERT INTO posts
                (title, content, author)
                VALUES (?, ?, ?)
                """,
                (
                    title,
                    content,
                    "admin"
                )
            )

            conn.commit()
            conn.close()

            st.success("✅ Blog Published Successfully")

        else:
            st.warning("⚠️ Please fill all fields")

    if st.button("⬅ Back To Dashboard", key="back_dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()