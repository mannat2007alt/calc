
import streamlit as st

# Title of the app
st.title("🧮 Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0.0, step=0.1)
num2 = st.number_input("Enter second number", value=0.0, step=0.1)

# Buttons for operations
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("➕ Add"):
        result = num1 + num2
        st.success(f"Result: {result}")

with col2:
    if st.button("➖ Subtract"):
        result = num1 - num2
        st.success(f"Result: {result}")

with col3:
    if st.button("✖ Multiply"):
        result = num1 * num2
        st.success(f"Result: {result}")

with col4:
    if num2 != 0:  # To prevent division by zero
        if st.button("➗ Divide"):
            result = num1 / num2
            st.success(f"Result: {result}")
    else:
        st.warning("Cannot divide by zero!")

# Footer
st.caption("Made with ❤️ using Streamlit")
