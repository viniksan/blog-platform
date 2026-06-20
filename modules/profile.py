import streamlit as st
import sqlite3
from components.navbar import show_navbar

def show_profile():

    show_navbar()

    st.title("👤 Profile")

    conn = sqlite3.connect("blog.db")
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM posts")
    total_posts = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM comments")
    total_comments = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM likes")
    total_likes = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM users")
    total_users = c.fetchone()[0]

    conn.close()

    st.success("Welcome to your profile")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📝 Posts", total_posts)

    with col2:
        st.metric("💬 Comments", total_comments)

    col3, col4 = st.columns(2)

    with col3:
        st.metric("❤️ Likes", total_likes)

    with col4:
        st.metric("👥 Users", total_users)

    st.markdown("---")

    if st.button("⬅ Back To Dashboard", key="profile_back"):
        st.session_state.page = "Dashboard"
        st.rerun()