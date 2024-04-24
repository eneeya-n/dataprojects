
import streamlit as st

# Define all the questions, options, and answers
quiz_questions = [
    {
        "question": "What is SQL primarily used for?",
        "options": ["Managing and manipulating relational databases", "Writing complex algorithms", 
                    "Designing user interfaces", "Creating web applications"],
        "answer": "Managing and manipulating relational databases"
    },
    {
        "question": "Which SQL command is used to insert new rows of data into a table?",
        "options": ["UPDATE", "DELETE", "INSERT", "CREATE TABLE"],
        "answer": "INSERT"
    },
    {
        "question": "Which constraint ensures that each row in a table is uniquely identified and cannot contain NULL values?",
        "options": ["PRIMARY KEY", "FOREIGN KEY", "UNIQUE", "NOT NULL"],
        "answer": "PRIMARY KEY"
    },
    {
        "question": "What does the SQL command SELECT DISTINCT do?",
        "options": ["Retrieves unique data entries", "Retrieves all records from a table", 
                    "Deletes duplicate records from a table", "Retrieves data based on specified conditions"],
        "answer": "Retrieves unique data entries"
    },
    {
        "question": "Which SQL command is used to filter query results based on specified conditions?",
        "options": ["WHERE", "ORDER BY", "GROUP BY", "HAVING"],
        "answer": "WHERE"
    },
    {
        "question": "What logical operator is used to combine multiple conditions in SQL?",
        "options": ["AND", "OR", "NOT", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Which SQL function calculates the average of a set of values?",
        "options": ["SUM()", "AVG()", "COUNT()", "MIN()"],
        "answer": "AVG()"
    },
    {
        "question": "What does the SQL command LIMIT do?",
        "options": ["Specifies the maximum number of records to return", 
                    "Specifies the maximum number of columns to return", 
                    "Specifies the maximum length of a text field", 
                    "Specifies the maximum value for a numeric column"],
        "answer": "Specifies the maximum number of records to return"
    },
    {
        "question": "Which SQL join type returns all rows from the left table and the matched rows from the right table?",
        "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"],
        "answer": "LEFT JOIN"
    },
    {
        "question": "Which SQL function returns the current date and time?",
        "options": ["NOW()", "CURDATE()", "CURTIME()", "DATE()"],
        "answer": "NOW()"
    },
    {
        "question": "What is the purpose of Common Table Expressions (CTEs) in SQL?",
        "options": ["Defining temporary tables for complex queries", "Storing encrypted data", 
                    "Optimizing database performance", "Automating backup processes"],
        "answer": "Defining temporary tables for complex queries"
    },
    {
        "question": "Which SQL command is used to create a new index on a table?",
        "options": ["CREATE INDEX", "DROP INDEX", "ALTER TABLE", "CREATE TABLE"],
        "answer": "CREATE INDEX"
    },
    {
        "question": "What does the SQL command DROP TABLE do?",
        "options": ["Deletes an existing table from the database", "Deletes all records from a table", 
                    "Deletes a specific column from a table", "Deletes a specific index from a table"],
        "answer": "Deletes an existing table from the database"
    },
    {
        "question": "Which SQL function returns the day of the week for a given date?",
        "options": ["DAYNAME()", "DAYOFWEEK()", "DAYOFMONTH()", "DAYOFYEAR()"],
        "answer": "DAYOFWEEK()"
    },
    {
        "question": "What is the purpose of the SQL command HAVING?",
        "options": ["Filtering rows before grouping them", "Sorting rows based on specified criteria", 
                    "Applying conditions to groups after grouping", 
                    "Limiting the number of rows returned by a query"],
        "answer": "Applying conditions to groups after grouping"
    },
    {
        "question": "Which SQL join type returns only the rows that have matching values in both tables?",
        "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"],
        "answer": "INNER JOIN"
    },
    {
        "question": "Which SQL command is used to modify an existing table by adding or dropping columns?",
        "options": ["CREATE TABLE", "ALTER TABLE", "DROP TABLE", "CREATE INDEX"],
        "answer": "ALTER TABLE"
    },
    {
        "question": "What is the purpose of the SQL command UNION?",
        "options": ["Combining the result sets of two or more SELECT statements", 
                    "Deleting duplicate records from a table", 
                    "Sorting rows based on specified criteria", 
                    "Creating a new table in the database"],
        "answer": "Combining the result sets of two or more SELECT statements"
    },
    {
        "question": "Which SQL function is used to calculate the difference between two datetime expressions in terms of a specified unit?",
        "options": ["DATEDIFF()", "DATE_ADD()", "DATE_SUB()", "TIMESTAMPDIFF()"],
        "answer": "TIMESTAMPDIFF()"
    },
    {
        "question": "What does the SQL command NOT LIKE do?",
        "options": ["Searches for a specified pattern", "Excludes records matching a pattern", 
                    "Retrieves unique data entries", 
                    "Combines the result sets of two or more SELECT statements"],
        "answer": "Excludes records matching a pattern"
    },
    {
        "question": "Which SQL function is used to retrieve the last value in a window frame?",
        "options": ["FIRST_VALUE()", "LAST_VALUE()", "LEAD()", "LAG()"],
        "answer": "LAST_VALUE()"
    },
    {
        "question": "What is the purpose of the SQL command EXISTS?",
        "options": ["Tests whether a subquery returns any rows", 
                    "Combines the result sets of two or more SELECT statements", 
                    "Applies conditions to groups after grouping", 
                    "Retrieves the first value in a window frame"],
        "answer": "Tests whether a subquery returns any rows"
    },
    {
        "question": "Which SQL join type returns all rows from both tables, matching records from the left table with NULL values where there is no match in the right table?",
        "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"],
        "answer": "FULL OUTER JOIN"
    },
    {
        "question": "Which SQL function returns the hour for a given time?",
        "options": ["HOUR()", "MINUTE()", "SECOND()", "TIMESTAMPDIFF()"],
        "answer": "HOUR()"
    },
    {
        "question": "What is the purpose of SQL aliases?",
        "options": ["To provide a temporary name to a table or a column in a query", 
                    "To encrypt sensitive data in a database", 
                    "To perform logical tests and return values", 
                    "To calculate aggregate functions over a set of rows related to the current row"],
        "answer": "To provide a temporary name to a table or a column in a query"
    }
]

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #e5e5f7;
opacity: 1;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #e5e5f7 10px ), repeating-linear-gradient( #444cf755, #444cf7 ); 
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
opacity: 1;
}

[data-testid="stToolbar"]{
right: 4rem;
}

</style>
"""
que = """
<style>
[data-testid="stVerticalBlockBorderWrapper"]{
background-color: rgba(135,206,235); /* Change the color and opacity as needed */
border-radius: 40px; /* Adjust the border radius to control the roundness */
padding: 10px;
}

[data-testid="element-container"]{
left: 1rem;
}

</style>
"""

wel = """
<style>
[data-testid="stVerticalBlockBorderWrapper"]{
background-color: #e5e5f7;
opacity: 1;
background-image: radial-gradient(circle at center center, #45f775, #e5e5f7), repeating-radial-gradient(circle at center center, #45f775, #45f775, 5px, transparent 10px, transparent 5px);
background-blend-mode: multiply;
border-radius: 40px; /* Adjust the border radius to control the roundness */
padding: 40px;
}  

}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Initialize session state if not already done
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.user_answers = [None] * len(quiz_questions)
    st.session_state.quiz_started = False  # New session state variable

# Define the action to be taken on pressing the submit button
def submit_answers():
    st.session_state.show_score = True
    st.session_state.current_question = 0  # Reset for restart purposes
    st.rerun()

# Display welcome page
if not st.session_state.quiz_started:
    st.title("Welcome, IQMath Analytics enthusiasts! 📊")
    st.write("Are you ready to dive deep into the world of structured query language and emerge as a SQL superstar?")
    st.markdown(wel, unsafe_allow_html=True)
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
        st.rerun()
else:
    # Display questions and handle navigation
    st.title("SQL Smarts: Dive into Data Analytics with Our Quiz!")
    if not st.session_state.get('show_score', False):
        q = quiz_questions[st.session_state.current_question]
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(quiz_questions)}")
        st.write(q['question'])
        user_answer = st.radio("Choose one option:", q['options'], key=str(st.session_state.current_question))
        st.session_state.user_answers[st.session_state.current_question] = user_answer

        col1, col2 = st.columns(2)
        if st.session_state.current_question > 0:
            if col1.button("Previous"):
                st.session_state.current_question -= 1
                st.rerun()

        if col2.button("Next"):
            if st.session_state.current_question < len(quiz_questions) - 1:
                st.session_state.current_question += 1
                st.rerun()
            else:
                st.session_state.current_question = 0  # Reset to start on submission
                submit_answers()
    else:
        # Calculate score
        score = sum(1 for i, question in enumerate(quiz_questions) if question['answer'] == st.session_state.user_answers[i])
        st.subheader(f"Congratulations, quiz takers! 🎉\n Your score is {score} out of {len(quiz_questions)}.")
        if st.button("Restart Quiz"):
            st.session_state.user_answers = [None] * len(quiz_questions)
            st.session_state.show_score = False
            st.session_state.current_question = 0
            st.session_state.quiz_started = False
            st.rerun()
    st.markdown(que, unsafe_allow_html=True)
