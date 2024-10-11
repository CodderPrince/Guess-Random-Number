import streamlit as st

st.title("🔗Contact")

# Facebook icon and URL
facebook_icon_url = "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"
facebook_url = "https://facebook.com/md.annahian"

# GitHub icon and URL
github_icon_url = "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg"
github_url = "https://github.com/CodderPrince"

# LinkedIn icon and URL
linkedin_icon_url = "https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg"
linkedin_url = "https://www.linkedin.com/in/md-an-nahian-prince-409659332/"

# Display Facebook link with text and icon on the same line
st.markdown(
    f'# Connect with me on Facebook <a href="{facebook_url}" target="_blank">'
    f'<img src="{facebook_icon_url}" width="50" style="vertical-align:middle; margin-left:10px"/></a>',
    unsafe_allow_html=True
)

# Display GitHub link with text and icon on the same line
st.markdown(
    f'# Connect with me on GitHub <a href="{github_url}" target="_blank">'
    f'<img src="{github_icon_url}" width="50" style="vertical-align:middle; margin-left:10px"/></a>',
    unsafe_allow_html=True
)

# Display LinkedIn link with text and icon on the same line
st.markdown(
    f'# Connect with me on LinkedIn <a href="{linkedin_url}" target="_blank">'
    f'<img src="{linkedin_icon_url}" width="80" style="vertical-align:middle; margin-left:10px"/></a>',
    unsafe_allow_html=True
)
