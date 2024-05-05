
import streamlit as st

# Define all the questions, options, and answers
quiz_questions = [
        {
            'question': 'Which key combination moves the cursor to the beginning of a worksheet in Excel?',
            'options': ['Ctrl + End', 'Home', 'Ctrl + Home', 'Alt + Home'],
            'answer': 'Ctrl + Home',
            'explanation': 'Ctrl + Home moves the cursor to the beginning of the worksheet.'
        },
        {
            'question': 'How do you extend the cell selection with the keyboard?',
            'options': ['Shift + Click', 'Ctrl + Shift + Arrow Key', 'Alt + Shift + Arrow Key', 'Shift + Arrow Key'],
            'answer': 'Shift + Arrow Key',
            'explanation': 'Shift + Arrow Key extends the cell selection with the keyboard.'
        },
        {
            'question': "What does pressing 'Ctrl + Space' in Excel do?",
            'options': ['Opens the space menu', 'Selects the entire row', 'Selects the entire column', 'Selects the entire worksheet'],
            'answer': 'Selects the entire column',
            'explanation': 'Ctrl + Space selects the entire column in Excel.'
        },
        {
            'question': 'Which shortcut inserts a new worksheet in Excel?',
            'options': ['Ctrl + T', 'Ctrl + N', 'Ctrl + K', 'Shift + F11'],
            'answer': 'Shift + F11',
            'explanation': 'Shift + F11 inserts a new worksheet in Excel.'
        },
        {
            'question': 'How can you save a workbook using keyboard shortcuts?',
            'options': ['Shift + S', 'Ctrl + Save', 'Ctrl + B', 'Ctrl + S'],
            'answer': 'Ctrl + S',
            'explanation': 'Ctrl + S saves a workbook using keyboard shortcuts.'
        },
        {
            'question': "What function does 'Ctrl + A' perform when the active cell is not in a table?",
            'options': ['Selects the entire worksheet', 'Selects the entire column', 'Selects the entire row', 'Selects the active table'],
            'answer': 'Selects the entire worksheet',
            'explanation': 'Ctrl + A selects the entire worksheet when the active cell is not in a table.'
        },
        {
            'question': 'Which of the following is used to open the Print dialog in Excel?',
            'options': ['Alt + P', 'Ctrl + P', 'Shift + P', 'Ctrl + Print'],
            'answer': 'Ctrl + P',
            'explanation': 'Ctrl + P is used to open the Print dialog in Excel.'
        },
        {
            'question': 'To apply bold formatting to selected cells, which shortcut should be used?',
            'options': ['Ctrl + B', 'Ctrl + U', 'Ctrl + I', 'Alt + B'],
            'answer': 'Ctrl + B',
            'explanation': 'Ctrl + B is used to apply bold formatting to selected cells.'
        },
        {
            'question': 'Which of these shortcuts will copy the selected cells?',
            'options': ['Ctrl + X', 'Ctrl + C', 'Ctrl + V', 'Ctrl + Z'],
            'answer': 'Ctrl + C',
            'explanation': 'Ctrl + C copies the selected cells.'
        },
        {
            'question': 'If you need to undo the last action, which shortcut would you use?',
            'options': ['Ctrl + Y', 'Ctrl + W', 'Ctrl + Z', 'Ctrl + U'],
            'answer': 'Ctrl + Z',
            'explanation': 'Ctrl + Z is used to undo the last action.'
        },
        {
            'question': "What does 'Ctrl + End' do in Excel?",
            'options': ['Ends the current function', 'Ends the Excel program', 'Clears the selected cells', 'Moves to the last cell with content'],
            'answer': 'Moves to the last cell with content',
            'explanation': 'Ctrl + End moves to the last cell with content in Excel.'
        },
        {
            'question': 'Which key combination is used to extend the selection to the last non-empty cell in Excel?',
            'options': ['Shift + Arrow Key', 'Ctrl + Shift + Arrow Key', 'Ctrl + Arrow Key', 'Alt + Shift + Arrow Key'],
            'answer': 'Ctrl + Shift + Arrow Key',
            'explanation': 'Ctrl + Shift + Arrow Key extends the selection to the last non-empty cell in Excel.'
        },
        {
            'question': 'To insert a hyperlink in a cell, you would use:',
            'options': ['Ctrl + K', 'Ctrl + L', 'Ctrl + J', 'Ctrl + H'],
            'answer': 'Ctrl + K',
            'explanation': 'Ctrl + K is used to insert a hyperlink in a cell.'
        },
        {
            'question': "What does pressing 'Alt + Page Down' do in Excel?",
            'options': ['Moves one screen to the left', 'Prints the current page', 'Moves to the bottom of the current page', 'Moves one screen to the right'],
            'answer': 'Moves one screen to the right',
            'explanation': 'Alt + Page Down moves one screen to the right in Excel.'
        },
        {
            'question': "How would you open the 'Find and Replace' dialog using keyboard shortcuts?",
            'options': ['Ctrl + R', 'Ctrl + S', 'Ctrl + F', 'Ctrl + H'],
            'answer': 'Ctrl + H',
            'explanation': "Ctrl + H is used to open the 'Find and Replace' dialog using keyboard shortcuts."
        },
        {
            'question': 'Which function is NOT associated with copying, cutting, and pasting in Excel?',
            'options': ['Ctrl + V', 'Ctrl + C', 'Ctrl + X', 'Ctrl + Z'],
            'answer': 'Ctrl + Z',
            'explanation': 'Ctrl + Z is NOT associated with copying, cutting, and pasting in Excel.'
        },
        {
            'question': "What is the effect of pressing 'Ctrl + Home' in Excel?",
            'options': ['Prints the current worksheet', 'Saves the current workbook', 'Moves to the beginning of the worksheet', 'Closes the current workbook'],
            'answer': 'Moves to the beginning of the worksheet',
            'explanation': 'Ctrl + Home moves to the beginning of the worksheet in Excel.'
        },
        {
            'question': 'Which shortcut will cut the selected cells?',
            'options': ['Ctrl + Z', 'Ctrl + V', 'Ctrl + X', 'Ctrl + C'],
            'answer': 'Ctrl + X',
            'explanation': 'Ctrl + X cuts the selected cells.'
        },
        {
            'question': 'To apply or remove underline formatting, you would use:',
            'options': ['Ctrl + B', 'Ctrl + Y', 'Ctrl + U', 'Ctrl + I'],
            'answer': 'Ctrl + U',
            'explanation': 'Ctrl + U is used to apply or remove underline formatting.'
        },
        {
            'question': "What does 'Ctrl + F' open in Excel?",
            'options': ['File menu', 'Find dialog', 'Font settings', 'Format cells dialog'],
            'answer': 'Find dialog',
            'explanation': 'Ctrl + F opens the Find dialog in Excel.'
        },
        {
            'question': 'How can you move one screen up in the worksheet using the keyboard?',
            'options': ['Alt + Page Up', 'Ctrl + Page Up', 'Page Up', 'Page Down'],
            'answer': 'Page Up',
            'explanation': 'Page Up moves one screen up in the worksheet using the keyboard.'
        },
        {
            'question': 'If you wanted to select the entire row where your active cell is located, which shortcut would you use?',
            'options': ['Ctrl + Shift + Space', 'Shift + Space', 'Ctrl + Space', 'Alt + Space'],
            'answer': 'Shift + Space',
            'explanation': 'Shift + Space selects the entire row where the active cell is located.'
        },
        {
            'question': 'To quickly navigate to the edge of data regions, you should press:',
            'options': ['Shift + Arrow Key', 'Alt + Arrow Key', 'Ctrl + Arrow Key', 'Arrow Key alone'],
            'answer': 'Ctrl + Arrow Key',
            'explanation': 'Ctrl + Arrow Key is used to quickly navigate to the edge of data regions.'
        },
        {
            'question': "What action is performed by 'Ctrl + B' in Excel?",
            'options': ['Insert a blank row', 'Bold formatting', 'Start a new bullet list', 'Open bookmarks'],
            'answer': 'Bold formatting',
            'explanation': 'Ctrl + B performs bold formatting in Excel.'
        },
        {
            'question': "What does 'Shift + F11' accomplish in Excel?",
            'options': ['Applies a filter', 'Finds and replaces text', 'Opens the field settings', 'Inserts a new worksheet'],
            'answer': 'Inserts a new worksheet',
            'explanation': 'Shift + F11 inserts a new worksheet in Excel.'
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
left: 3rem;
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
    st.session_state.answers_checked = [False] * len(quiz_questions)  # New session state variable
    st.session_state.show_answer = [False] * len(quiz_questions)  # New session state variable

# Define the action to be taken on pressing the submit button
def submit_answers():
    st.session_state.show_score = True
    st.session_state.current_question = 0  # Reset for restart purposes
    
    # Count attended questions with locked answers and calculate score
    correct_answers = sum(1 for i, question in enumerate(quiz_questions) if st.session_state.answers_checked[i] and question['answer'] == st.session_state.user_answers[i])
    total_locked_answers = sum(st.session_state.answers_checked)
    
    st.write(f"You have answered {correct_answers} questions correctly out of {total_locked_answers} attended questions where the answer was locked.")
    st.rerun()


# Function to display question and options
def display_question(question):
    st.subheader(f"Question {st.session_state.current_question + 1} of {len(quiz_questions)}")
    st.write(question['question'])
    
    # Determine if the radio button group should be disabled
    disabled = st.session_state.answers_checked[st.session_state.current_question]
    
    # Display the radio button group
    user_answer = st.radio("Choose one option:", question['options'], key=f"option_{st.session_state.current_question}", disabled=disabled)
    
    # Update user_answers only if not disabled
    if not disabled:
        st.session_state.user_answers[st.session_state.current_question] = user_answer
    
    # Check Answer Button
    if st.button("Lock Answer", key=f"check_{st.session_state.current_question}"):
        st.session_state.answers_checked[st.session_state.current_question] = True
        st.rerun()
        # Disable the radio button group after checking the answer
        disabled = True
    
    # Show/Hide Answer Button
    if st.session_state.answers_checked[st.session_state.current_question]:
        if st.button("Show/Hide Answer", key=f"toggle_{st.session_state.current_question}"):
            st.session_state.show_answer[st.session_state.current_question] = not st.session_state.show_answer[st.session_state.current_question]
    
    # Display Answer and Explanation if enabled
    if st.session_state.show_answer[st.session_state.current_question]:
        st.write(f"The correct answer is: {question['answer']}")
        st.write(f"Explanation: {question['explanation']}")

# Display welcome page
if not st.session_state.quiz_started:
    st.title("Welcome, IQMath Analytics enthusiasts! 📊")
    st.write("Are you ready to put your analytical skills to the test in our Excel quiz?")
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
        st.rerun()
else:
    # Display questions and handle navigation
    st.title("Excel Explorer: Dive into Data Analytics with our Quiz!")
    if not st.session_state.get('show_score', False):
        q = quiz_questions[st.session_state.current_question]
        display_question(q)

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
            st.session_state.answers_checked = [False] * len(quiz_questions)  # New session state variable
            st.session_state.show_answer = [False] * len(quiz_questions)  # New session state variable
            st.rerun()
    st.markdown(que, unsafe_allow_html=True)
