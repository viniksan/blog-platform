import streamlit as st
import sqlite3
from components.navbar import show_navbar

def show_my_posts():

    show_navbar()

    st.title("📝 My Blogs")

    conn = sqlite3.connect("blog.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM posts WHERE author=?",
        ("admin",)
    )

    posts = c.fetchall()

    if not posts:
        st.info("No posts found.")

    for post in posts:

        post_id = post[0]

        st.markdown("---")

        st.subheader(post[1])

        st.write(post[2])

        c.execute(
            "SELECT COUNT(*) FROM likes WHERE post_id=?",
            (post_id,)
        )

        likes = c.fetchone()[0]

        c.execute(
            "SELECT COUNT(*) FROM comments WHERE post_id=?",
            (post_id,)
        )

        comments = c.fetchone()[0]

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"❤️ Likes: {likes}")

        with col2:
            st.write(f"💬 Comments: {comments}")

        if st.button(
            "🗑 Delete Post",
            key=f"delete_{post_id}"
        ):

            c.execute(
                "DELETE FROM posts WHERE id=?",
                (post_id,)
            )

            conn.commit()

            st.success("Post Deleted")

            st.rerun()

    conn.close()

    st.markdown("---")

    if st.button("⬅ Back To Dashboard", key="my_back"):
        st.session_state.page = "Dashboard"
        st.rerun()