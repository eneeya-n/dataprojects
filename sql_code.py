import streamlit as st
import sqlite3
import pandas as pd
import sql_code_data as d
from stream_data import val_ip

from streamlit import runtime
from streamlit.runtime.scriptrunner import get_script_run_ctx

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background: #d954fa;
background: -webkit-linear-gradient(146deg, #d954fa 0%, #e591dd 50%, #ddb9dd 100%);
background: linear-gradient(146deg, #d954fa 0%, #e591dd 50%, #ddb9dd 100%);
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
opacity: 1;
}

[data-testid="stToolbar"]{
right: 4rem;
}

[data-testid="stSidebar"]{
background: linear-gradient(to right, #e66465, #9198e5);
opacity: 1;
}

[data-testid="baseButton-secondary"]{
background: #efb1ff;
background: -webkit-linear-gradient(146deg, #efb1ff 0%, #ffe2ff 100%);
background: linear-gradient(146deg, #efb1ff 0%, #ffe2ff 100%);
}

</style>
"""

conn, c, questions, schema_set, schema_title, expected_out_col = d.exc()

def get_remote_ip() -> str:
    """Get remote ip."""

    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None

        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
    except Exception as e:
        return None

    return session_info.request.remote_ip

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
def run():
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Streamlit UI
    st.title("SQL Codebreaker Challenge")

    try:
        # Retrieve username from URL parameter
        username = st.query_params.get_all("username")[0]
        open = True
    
    except:
        st.error("You need to login first...!")
        login_url = "https://dataprojects-s7k5ey6hksc9rvyrpevcwt.streamlit.app/"
        st.markdown(f"Here is the Login Link : [Login]({login_url})")
        open = False
        
    if open:
        cur_user_ip_add = get_remote_ip()
        res = val_ip(cur_user_ip_add)
        if res == True: 
            # Sidebar
            st.sidebar.title("SQL Codebreaker Challenge!")
            st.sidebar.write('''This challenge is designed to test your SQL skills and problem-solving abilities. As a codebreaker, your mission is to unravel complex SQL queries and solve challenging database problems. Put your SQL knowledge to the test as you tackle a series of mind-bending queries and data manipulation tasks. Are you ready to crack the code and emerge as a SQL codebreaking champion?''')

            st.write(f"Welcome back, {username}!")

            # Track current question index
            if "current_question_index" not in st.session_state:
                st.session_state.current_question_index = 0

            # Display selected question
            question, expected_output = questions[st.session_state.current_question_index]
            st.write("Question " + str(st.session_state.current_question_index+1) + ":")
            st.write(question)

            # Display schema for the first question
            for j in range(len(schema_title[st.session_state.current_question_index])):
                st.write(schema_title[st.session_state.current_question_index][j])
                if len(schema_title[st.session_state.current_question_index]) > 1:
                    schema_data = schema_set[st.session_state.current_question_index][j]
                else:
                    schema_data = schema_set[st.session_state.current_question_index]
                schema_df = pd.DataFrame(schema_data)
                schema_df_no_index = schema_df.copy()
                st.markdown(schema_df_no_index.style.hide(axis="index").to_html(), unsafe_allow_html=True)
                st.write(" ")

            # Button to toggle expected output visibility
            st.write(" ")
            expected_output_button_key = f"expected_output_{st.session_state.current_question_index}"
            if st.button("Show/Hide Expected Output", key=expected_output_button_key):
                st.session_state.show_expected_output = not st.session_state.get("show_expected_output", False)
            
            if st.session_state.get("show_expected_output", False):
                st.write("Expected Output:")
                exp_col_name = expected_out_col[st.session_state.current_question_index]
                expected_output_df = pd.DataFrame(expected_output, columns=exp_col_name)
                st.markdown(expected_output_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

            # Get user's SQL query answer
            user_query = st.text_area("Enter your SQL query answer:", height=200)  # Bigger input box

            col1, col2, col3 = st.columns([9, 4, 3])
            # Button to execute the query and show the output
            execute_query_button_key = f"execute_query_{st.session_state.current_question_index}"
            if col1.button("Execute Query", key=execute_query_button_key):
                if user_query.strip() != "":
                    try:
                        c.execute(user_query)
                        user_result = c.fetchall()
                        column_names = [description[0] for description in c.description]
                        st.write("Your Query Output:")
                        if user_result:
                            user_result_df = pd.DataFrame(user_result, columns=column_names)
                            st.markdown(user_result_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
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
                    try:
                        c.execute(user_query)
                        user_result = c.fetchall()
                        column_names = [description[0] for description in c.description]
                        st.write("Your Query Output:")
                        if user_result:
                            user_result_df = pd.DataFrame(user_result, columns=column_names)
                            st.markdown(user_result_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
                        else:
                            st.write("No results")

                        # Call function to check SQL query
                        is_correct, user_result, message = check_sql_query(user_query, expected_output)
                        st.write(" ")
                        st.write("Comparison with Expected Output:")
                        if user_result == expected_output:
                            st.write("Result: Correct")
                        else:
                            st.write("Result: Incorrect")
                    except Exception as e:
                        st.write("Error executing the query:", str(e))
                else:
                    st.write("Please enter a valid SQL query.")

            st.write(" ")
            # Buttons for navigation
            col1, col2, col3 = st.columns([9, 19, 3])
            if col1.button("Previous"):
                st.session_state.current_question_index = max(0, st.session_state.current_question_index - 1)
                st.rerun()
            if col3.button("Next"):
                st.session_state.current_question_index = min(len(questions) - 1, st.session_state.current_question_index + 1)
                st.rerun()
        
        else:
            st.error("You are not authorized to enter this site...!")



# Run the main function
if __name__ == "__main__":
    run()
