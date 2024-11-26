import streamlit as st

# Function to get the correct number suffix
def get_number_suffix(number):
    if 10 <= number % 100 <= 20:  # Special case for teens
        return "th"
    last_digit = number % 10
    if last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"

# Instructions at the top of the app
st.markdown(
    """
    <h2 style="text-align: center;">Hello.</h2>
    <p style="text-align: center; font-size: 18px;">I've heard it's someone's birthday. I'm delighted if that person is you...but I need to be sure. Answer these questions below to confirm.</p>
    """,
    unsafe_allow_html=True,
)

# Input fields for name and age
name = st.text_input("What's your name?")
age = st.number_input("How old are you?", min_value=0, max_value=150, step=1)

# Additional question: Favorite tank engine
tank_engine = st.text_input("Which tank engine was your favorite?")

# Food preferences
st.markdown("### I like the following foods:")
mango = st.checkbox("Mango")
persimmon = st.checkbox("Persimmon")
berries = st.checkbox("Berries")
apple = st.checkbox("Apple")
feta = st.checkbox("Feta")

# Check if all inputs are provided
if name and age and tank_engine:
    # Determine the correct suffix for the age
    suffix = get_number_suffix(int(age))

    # Check correctness
    correct_foods = mango and persimmon and berries and apple and not feta
    correct_tank_engine = tank_engine.lower() == "thomas"
    correct_name_and_age = name == "Benjamin" and age == 13

    if correct_name_and_age and correct_tank_engine and correct_foods:
        # Giant text and balloons for correct answers
        st.markdown(
            f"<h1 style='color: gold; font-size: 80px; text-align: center;'>Happy {int(age)}{suffix} Birthday, {name}!</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align: center; font-size: 24px;'>🎉 You passed the birthday quiz! Enjoy endless (sort of) balloons! <br> I am so proud of my artistic, musical, fun-loving (sometimes) TEENAGER 🎈</p>",
            unsafe_allow_html=True,
        )
        # Lots of balloons!
        for _ in range(5):  # Display multiple streams of balloons
            st.balloons()
    else:
        # Spooky graphics for wrong answers
        st.markdown(
            f"""
            <h1 style="color: red; font-size: 60px; text-align: center;">👻 WRONG ANSWERS DETECTED 👻</h1>
            <p style="text-align: center; font-family: 'Creepster', cursive; color: white; background-color: black; padding: 10px;">
                Not everyone's birthday is meant to be celebrated... try again if you dare!
            </p>
            """,
            unsafe_allow_html=True,
        )
        st.snow()  # Optional spooky snow animation
