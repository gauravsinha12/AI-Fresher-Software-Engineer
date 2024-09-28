
import streamlit as st

def login_form():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    return username, password

def check_password(username, password):
    # Replace with your own password checking logic
    return password == "12345"

def main():
    st.title("Simple Login App")
    username, password = login_form()
    if st.button("Login"):
        if check_password(username, password):
            st.write("Login successful!")
        else:
            st.error("Incorrect username or password")

if __name__ == "__main__":
    main()
