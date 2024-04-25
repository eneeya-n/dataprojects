import streamlit as st
import sqlite3
import pandas as pd
import data as d

# Streamlit UI
st.title("SQL Query Checker")

conn, c, questions, schema_set = d.exc()

# Function to compile and check SQL query
def check_sql_query(query, expected_output):
    try:
        # Execute the user's SQL query
        c.execute(query)
        user_result = c.fetchall()
        if user_result == expected_output:
            return True, user_result, "Correct answer!"
        else:
            return False, user_result, "Incorrect answer!"
    except Exception as e:
        # If there's an error, return False and the error message
        return False, None, str(e)

# Main function
def main():
    # Track current question index
    if "current_question_index" not in st.session_state:
        st.session_state.current_question_index = 0

    # Display selected question
    question, expected_output = questions[st.session_state.current_question_index]
    st.write("Question:", question)

    # Display schema for the first question
    if st.session_state.current_question_index == 0:
        st.write("Schema for the 'icc_world_cup' table:")
        schema_data = schema_set[st.session_state.current_question_index]
        schema_df = pd.DataFrame(schema_data)
        schema_df_no_index = schema_df.copy()
        st.markdown(schema_df_no_index.style.hide(axis="index").to_html(), unsafe_allow_html=True)

    else:
        # Display previous schema for the remaining questions
        st.write("Customers Schema:")
        previous_schema_data = schema_set[st.session_state.current_question_index]
        previous_schema_df = pd.DataFrame(previous_schema_data)
        previous_schema_df_no_index = previous_schema_df.copy()
        st.markdown(previous_schema_df_no_index.style.hide(axis="index").to_html(), unsafe_allow_html=True)

    # Button to toggle expected output visibility
    st.write(" ")
    expected_output_button_key = f"expected_output_{st.session_state.current_question_index}"
    if st.button("Show/Hide Expected Output", key=expected_output_button_key):
        st.session_state.show_expected_output = not st.session_state.get("show_expected_output", False)

    if st.session_state.get("show_expected_output", False):
        st.write("Expected Output:")
        for row in expected_output:
            st.write(row)

    # Get user's SQL query answer
    user_query = st.text_input("Enter your SQL query answer:")
    col1, col2, col3 = st.columns([9, 4, 3])
    # Button to execute the query and show the output
    execute_query_button_key = f"execute_query_{st.session_state.current_question_index}"
    if col1.button("Execute Query", key=execute_query_button_key):
        if user_query.strip() != "":
            try:
                c.execute(user_query)
                user_result = c.fetchall()
                st.write("Your Query Output:")
                if user_result:
                    for row in user_result:
                        st.write(row)
                else:
                    st.write("No results")
            except Exception as e:
                st.write("Error executing the query:", str(e))
        else:
            st.write("Please enter a valid SQL query.")

    # Button to check the query
    check_query_button_key = f"check_query_{st.session_state.current_question_index}"
    if col3.button("Submit Query", key=check_query_button_key):
        if user_query.strip() != "":
            # Call function to check SQL query
            is_correct, user_result, message = check_sql_query(user_query, expected_output)
            st.write("Your Query Output:")
            if user_result:
                for row in user_result:
                    st.write(row)
            else:
                st.write("Error:", message)
            st.write("Comparison with Expected Output:")
            if user_result == expected_output:
                st.write("Result: Correct")
            else:
                st.write("Result: Incorrect")
        else:
            st.write("Please enter a valid SQL query.")

    # Buttons for navigation
    col1, col2, col3 = st.columns([9, 19, 3])
    if col1.button("Previous"):
        st.session_state.current_question_index = max(0, st.session_state.current_question_index - 1)
        st.rerun()
    if col3.button("Next"):
        st.session_state.current_question_index = min(len(questions) - 1, st.session_state.current_question_index + 1)
        st.rerun()


# Run the main function
if __name__ == "__main__":
    main()
