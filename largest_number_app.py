import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")

    # Input fields for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Button to find the largest number
    if st.button("Find Largest Number"):
        largest_number = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest_number}")

if __name__ == "__main__":
    main()
