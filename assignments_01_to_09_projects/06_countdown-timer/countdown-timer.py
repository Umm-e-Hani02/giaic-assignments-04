import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer", page_icon="⏳")

st.title("⏰ Countdown Timer using Streamlit")

# Default time set to 1 minute and 0 seconds
minutes = st.number_input("Enter minutes:", min_value=0, value=1)
seconds = st.number_input("Enter seconds:", min_value=0, max_value=60, value=0)

if st.button("Start Timer"):
    total_seconds = int(minutes * 60 + seconds)

    countdown_placeholder = st.empty()
    for i in range(total_seconds, -1, -1):
        mins, secs = divmod(i, 60)
        time_display = f"{mins:02d}:{secs:02d}"
        countdown_placeholder.markdown(f"## ⏳ Time Remaining: `{time_display}`")
        time.sleep(1)

    st.success("⏰ Time's up!")
