import streamlit as st

def show_navbar():

    st.markdown("---")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        if st.button("🏠 Dashboard", key="nav_dashboard"):
            st.session_state.page = "Dashboard"
            st.rerun()

    with col2:
        if st.button("✍️ Create", key="nav_create"):
            st.session_state.page = "Create Post"
            st.rerun()

    with col3:
        if st.button("📚 Blogs", key="nav_blogs"):
            st.session_state.page = "All Posts"
            st.rerun()

    with col4:
        if st.button("📝 My Posts", key="nav_my_posts"):
            st.session_state.page = "My Posts"
            st.rerun()

    with col5:
        if st.button("👤 Profile", key="nav_profile"):
            st.session_state.page = "Profile"
            st.rerun()

    with col6:
        if st.button("🚪 Logout", key="nav_logout"):
            st.session_state.logged_in = False
            st.session_state.page = "Login"
            st.rerun()

    st.markdown("---")