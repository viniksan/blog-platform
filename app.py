import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Blog Platform",
    page_icon="📝",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -----------------------------
# SESSION STATE
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "Login"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# APP TITLE
# -----------------------------
st.title("📝 Blog Platform")

# -----------------------------
# NAVIGATION
# -----------------------------
if st.session_state.logged_in:

    if st.session_state.page == "Create Post":
        from modules.create_post import show_create_post
        show_create_post()

    elif st.session_state.page == "All Posts":
        from modules.all_posts import show_all_posts
        show_all_posts()

    elif st.session_state.page == "My Posts":
        from modules.my_posts import show_my_posts
        show_my_posts()

    elif st.session_state.page == "Profile":
        from modules.profile import show_profile
        show_profile()

    else:
        from modules.dashboard import show_dashboard
        show_dashboard()

else:

    if st.session_state.page == "Login":
        from modules.login import show_login
        show_login()

    elif st.session_state.page == "Register":
        from modules.register import show_register
        show_register()