import streamlit as st

# Function to perform calculations
def calculate(operation, num1, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."

# Streamlit app layout
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

# Dropdown for operations
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Button to calculate
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"Result: {result}")
