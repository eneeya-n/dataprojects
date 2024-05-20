
import streamlit as st

# Define all the questions, options, and answers
quiz_questions = [
        {'question': 'What is the keyboard shortcut to move to the next worksheet in Excel?', 'options': ['Ctrl + Shift + Page Down', 'Ctrl + Page Down', 'Ctrl + N', 'Alt + Page Down'], 'answer': 'Ctrl + Page Down', 'explanation': 'Ctrl + Page Down moves to the next worksheet in Excel.'},  
        {'question': 'Which of the following methods is used to select multiple non-adjacent cells?', 'options': ['Shift + Click', 'Ctrl + Click', 'Tab + Click', 'Alt + Click'], 'answer': 'Ctrl + Click', 'explanation': 'Ctrl + Click is used to select multiple non-adjacent cells.'}, 
        {'question': 'Which option allows you to add a new worksheet in Excel?', 'options': ['Press Ctrl + N', "Type 'New' in a cell and press Enter", "Go to the 'Insert' tab and click on 'Worksheet'", "Right-click on a worksheet tab and select 'New'"], 'answer': "Go to the 'Insert' tab and click on 'Worksheet'", 'explanation': "To add a new worksheet in Excel, go to the 'Insert' tab and click on 'Worksheet'."}, 
        {'question': 'Which function is used to find the largest value in a range?', 'options': ['BIG', 'MAXIMUM', 'MAX', 'LARGE'], 'answer': 'MAX', 'explanation': 'The MAX function is used to find the largest value in a range in Excel.'}, 
        {'question': 'Which keyboard shortcut is used to remove filters in Excel?', 'options': ['Ctrl + Shift + R', 'Ctrl + Shift + L', 'Ctrl + Shift + F', 'Ctrl + Shift + X'], 'answer': 'Ctrl + Shift + F', 'explanation': 'Ctrl + Shift + F is used to remove filters in Excel.'}, 
        {'question': 'What does conditional formatting do in Excel?', 'options': ['Copies cells based on specific conditions', 'Deletes cells that meet certain conditions', 'Sorts data based on conditions', 'Applies formatting based on specified criteria'], 'answer': 'Applies formatting based on specified criteria', 'explanation': 'Conditional formatting in Excel applies formatting based on specified criteria.'}, 
        {'question': 'In Excel, which symbol is used to indicate an absolute reference in a formula?', 'options': ['$', '%', '#', '@'], 'answer': '$', 'explanation': "The symbol '$' is used to indicate an absolute reference in an Excel formula."}, 
        {'question': 'Which logical operator is used to combine two or more conditions where all conditions must be true?', 'options': ['NOT', 'AND', 'OR', 'XOR'], 'answer': 'AND', 'explanation': "The 'AND' logical operator is used to combine conditions where all conditions must be true."}, 
        {'question': 'Which function is used to perform a logical test and return one value if the condition is TRUE and another value if FALSE?', 'options': ['IFS', 'IF', 'SWITCH', 'VLOOKUP'], 'answer': 'IF', 'explanation': 'The IF function is used to perform a logical test and return one value if the condition is TRUE and another value if FALSE.'}, 
        {'question': 'Which function is used to find the total number of cells in a range that contain numbers?', 'options': ['AVERAGE', 'SUM', 'MAX', 'COUNT'], 'answer': 'COUNT', 'explanation': 'The COUNT function is used to find the total number of cells in a range that contain numbers.'}, 
        {'question': 'What is the purpose of the COUNTIF function in Excel?', 'options': ['Counts the number of cells in a range that meet multiple criteria', 'Calculates the average of cells in a range that meet a criterion', 'Counts the number of cells in a range that meet a single criterion', 'Determines the maximum value in a range that meets specific criteria'], 'answer': 'Counts the number of cells in a range that meet a single criterion', 'explanation': 'The COUNTIF function counts the number of cells in a range that meet a single criterion.'}, 
        {'question': 'Which function is used to add the cells specified by a given condition or criteria?', 'options': ['SUMIFS', 'COUNTIF', 'AVERAGEIF', 'SUMIF'], 'answer': 'SUMIF', 'explanation': 'The SUMIF function is used to add the cells specified by a given condition or criteria.'}, 
        {'question': 'Which function calculates the average of cells in a range that meet multiple criteria?', 'options': ['AVERAGE', 'AVERAGEA', 'AVERAGEIFS', 'AVERAGEIF'], 'answer': 'AVERAGEIFS', 'explanation': 'The AVERAGEIFS function calculates the average of cells in a range that meet multiple criteria.'}, 
        {'question': 'What combination of functions can be used to perform a lookup in Excel without needing to sort the data?', 'options': ['INDEX/MATCH', 'VLOOKUP/HLOOKUP', 'LOOKUP/SEARCH', 'MATCH/INDEX'], 'answer': 'INDEX/MATCH', 'explanation': 'The combination of INDEX/MATCH functions can be used to perform a lookup in Excel without needing to sort the data.'}, 
        {'question': 'Which function is used to search for a value in the first column of a table array and return a value in the same row from another column?', 'options': ['LOOKUP', 'VLOOKUP', 'INDEX', 'HLOOKUP'], 'answer': 'VLOOKUP', 'explanation': 'The VLOOKUP function is used to search for a value in the first column of a table array and return a value in the same row from another column.'}, 
        {'question': 'Which Excel function can replace both VLOOKUP and HLOOKUP?', 'options': ['MATCH', 'SEARCH', 'XLOOKUP', 'LOOKUP'], 'answer': 'XLOOKUP', 'explanation': 'The XLOOKUP function can replace both VLOOKUP and HLOOKUP in Excel.'}, 
        {'question': 'Which function allows you to filter data based on specified criteria?', 'options': ['FILTER', 'SORT', 'FIND', 'SEARCH'], 'answer': 'FILTER', 'explanation': 'The FILTER function allows you to filter data based on specified criteria.'}, 
        {'question': 'Which function combines the text from multiple ranges and/or strings, and includes a delimiter you specify between each text value?', 'options': ['COMBINE', 'CONCATENATE', 'TEXTJOIN', 'JOINTEXT'], 'answer': 'TEXTJOIN', 'explanation': 'The TEXTJOIN function combines the text from multiple ranges and/or strings, including a delimiter specified between each text value.'}, 
        {'question': 'Which function returns a list of unique values from a range or array, removing any duplicate values?', 'options': ['DISTINCT', 'UNIQUE', 'DUPLICATE', 'UNIQ'], 'answer': 'UNIQUE', 'explanation': 'The UNIQUE function returns a list of unique values from a range or array, removing any duplicate values.'}, 
        {'question': 'Which Excel function is commonly used in conjunction with Data Validation to ensure data integrity?', 'options': ['INDEX', 'IF', 'SUM', 'VLOOKUP'], 'answer': 'IF', 'explanation': 'The IF function is commonly used in conjunction with Data Validation to ensure data integrity.'}, 
        {'question': 'Which Excel feature allows you to summarize and analyze large datasets by organizing them into a customizable table?', 'options': ['Data Validation', 'VLOOKUP', 'Pivot Table', 'Conditional Formatting'], 'answer': 'Pivot Table', 'explanation': 'Pivot Table allows you to summarize and analyze large datasets by organizing them into a customizable table.'}, 
        {'question': 'Which chart type is suitable for showing trends over time?', 'options': ['Line Chart', 'Pie Chart', 'Scatter Plot', 'Bar Chart'], 'answer': 'Line Chart', 'explanation': 'The Line Chart is suitable for showing trends over time.'}, 
        {'question': 'What Excel feature allows users to dynamically filter data in a dashboard or report?', 'options': ['Slicer', 'Conditional Formatting', 'Pivot Table', 'Data Validation'], 'answer': 'Slicer', 'explanation': 'Slicer allows users to dynamically filter data in a dashboard or report.'}, 
        {'question': 'Which of the following is NOT a data validation criteria option in Excel?', 'options': ['Date', 'Decimal', 'Currency', 'Whole Number'], 'answer': 'Currency', 'explanation': 'Currency is NOT a data validation criteria option in Excel.'}, 
        {'question': 'What keyboard shortcut is used to quickly fill cells with data based on adjacent cells in Excel?', 'options': ['Ctrl + F', 'Ctrl + D', 'Ctrl + R', 'Ctrl + E'], 'answer': 'Ctrl + D', 'explanation': 'Ctrl + D is used to quickly fill cells with data based on adjacent cells in Excel.'},
        {'question': "Calculate the total sales revenue for the 'Technology' category. Round it up to 3 decimal points.", 'options': ['812345.123', '923456.789', '836154.033', '735982.456'], 'answer': '836154.033'}, 
        {'question': "Find the average profit for orders in the 'Consumer' segment. Round it up to 3 decimal points.", 'options': ['25.837', '30.567', '28.392', '22.456'], 'answer': '25.837'}, 
        {'question': "Count the number of orders shipped using 'First Class' ship mode.", 'options': ['1456', '1398', '1623', '1538'], 'answer': '1538'}, 
        {'question': "Determine the maximum sales value for the 'Office Supplies' category. Round it up to 3 decimal points.", 'options': ['9892.74', '10500.345', '9234.123', '10012.567'], 'answer': '9892.74'}, 
        {'question': "Calculate the total quantity of products sold in the 'West' region.", 'options': ['12034', '12266', '12987', '11345'], 'answer': '12266'}, 
        {'question': 'Find the order with the highest discount. Round it up to 3 decimal points.', 'options': ['US-2013-102345', 'US-2011-107890', 'US-2012-118983', 'US-2014-110345'], 'answer': 'US-2012-118983'}, 
        {'question': "Calculate the average discount for 'Furniture' category products. Round it up to 3 decimal points.", 'options': ['0.192', '0.156', '0.174', '0.182'], 'answer': '0.174'}, 
        {'question': "Determine the total profit for orders shipped to the 'East' region. Round it up to 3 decimal points.", 'options': ['92312.456', '91522.78', '89765.789', '87345.123'], 'answer': '91522.78'}, 
        {'question': 'Find the product name with the highest sales.', 'options': ['Cisco TelePresence System EX90 Videoconferencing Unit', 'Dell Laptop', 'Samsung Galaxy', 'Apple iPhone'], 'answer': 'Cisco TelePresence System EX90 Videoconferencing Unit'}, 
        {'question': 'Count the number of unique customers.', 'options': ['812', '793', '856', '734'], 'answer': '793'}, 
        {'question': "Calculate the total sales revenue for orders placed on '13-09-2013'. Round it up to 3 decimal points.", 'options': ['1987.456', '2043.792', '2156.789', '2023.345'], 'answer': '2043.792'}, 
        {'question': "Find the average sales revenue for 'Corporate' segment orders. Round it up to 3 decimal points.", 'options': ['238.123', '229.456', '245.567', '233.823'], 'answer': '233.823'}, 
        {'question': "Calculate the total profit for the 'Chairs' sub-category. Round it up to 3 decimal points.", 'options': ['27645.789', '25367.456', '26590.166', '27012.345'], 'answer': '26590.166'}, 
        {'question': "Determine the number of orders placed in the 'Central' region.", 'options': ['2456', '2189', '2323', '2345'], 'answer': '2323'}, 
        {'question': 'Find the earliest order date in the dataset.', 'options': ['40123', '40956', '40547', '40789'], 'answer': '40547'}, 
        {'question': "Calculate the total quantity of 'Paper' sub-category products sold.", 'options': ['5345', '4987', '5123', '5178'], 'answer': '5178'}, 
        {'question': 'Determine the product with the highest profit.', 'options': ['Epson Workforce Pro', 'HP LaserJet Printer', 'Canon imageCLASS 2200 Advanced Copier', 'Brother MFC Printer'], 'answer': 'Canon imageCLASS 2200 Advanced Copier'}, 
        {'question': 'Find the total sales revenue for orders with a discount greater than 20%. Round it up to 3 decimal points.', 'options': ['349876.123', '362770.15', '374567.456', '358912.789'], 'answer': '362770.15'}, 
        {'question': 'Calculate the average quantity of products ordered per order. Round it up to 3 decimal points.', 'options': ['3.67', '4.12', '3.45', '3.79'], 'answer': '3.79'}, 
        {'question': "Determine the total number of products sold in the 'Home Office' segment.", 'options': ['6987', '6744', '6723', '6456'], 'answer': '6744'}, 
        {'question': 'Find the most frequently used ship mode.', 'options': ['Same Day', 'Standard Class', 'Second Class', 'First Class'], 'answer': 'Standard Class'}, 
        {'question': "Calculate the total sales revenue for orders shipped in '2013'. Round it up to 3 decimal points.", 'options': ['479442.502', '500123.456', '470987.321', '489000.123'], 'answer': '479442.502'}, 
        {'question': "Determine the total profit for orders in the 'South' region. Round it up to 3 decimal points.", 'options': ['47250.456', '48000.123', '46749.43', '45000.789'], 'answer': '46749.43'}, 
        {'question': 'Find the order date with the highest number of orders placed.', 'options': ['40500', '41000', '42000', '41523'], 'answer': '41523'}, 
        {'question': 'Calculate the average profit margin (Profit/Sales) for all orders. Round it up to 3 decimal points.', 'options': ['0.18', '0.15', '0.10', '0.12'], 'answer': '0.12'}
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
        st.write("Excel Dataset Link : [Click Here](https://docs.google.com/spreadsheets/d/19M12tVjW3HKPU3Y8nl4zUcGF2nkY4H8vW5-ASvLR8Ns/edit?usp=sharing)")
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
