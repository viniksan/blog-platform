import streamlit as st
import sqlite3
from components.navbar import show_navbar

def show_dashboard():

    show_navbar()

    st.title("🏠 Dashboard")

    st.success("Welcome to Blog Platform")

    conn = sqlite3.connect("blog.db")
    c = conn.cursor()

    # Total Posts
    c.execute("SELECT COUNT(*) FROM posts")
    total_posts = c.fetchone()[0]

    # Total Comments
    c.execute("SELECT COUNT(*) FROM comments")
    total_comments = c.fetchone()[0]

    # Total Users
    c.execute("SELECT COUNT(*) FROM users")
    total_users = c.fetchone()[0]

    # Total Likes
    c.execute("SELECT COUNT(*) FROM likes")
    total_likes = c.fetchone()[0]

    conn.close()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📝 Posts", total_posts)

    with col2:
        st.metric("💬 Comments", total_comments)

    with col3:
        st.metric("👤 Users", total_users)

    with col4:
        st.metric("❤️ Likes", total_likes)

    st.markdown("---")

    st.subheader("📈 Platform Overview")

    st.info(
        f"""
        👥 Registered Users: {total_users}

        📝 Total Blog Posts: {total_posts}

        💬 Total Comments: {total_comments}

        ❤️ Total Likes: {total_likes}
        """
    )