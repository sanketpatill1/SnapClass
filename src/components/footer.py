import streamlit as st


def _render_footer(color):
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; flex-direction:column; gap:4px; align-items:center; justify-content:center; color:{color};">
            <p style="font-weight:bold; margin:0;">Built with ❤️ by the SnapClass Team</p>
            <p style="margin:0;">AI-Powered Smart Attendance System</p>
        </div>
    """, unsafe_allow_html=True)


def footer_home():
    _render_footer("white")


def footer_dashboard():
    _render_footer("black")
