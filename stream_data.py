import streamlit as st
from google.oauth2.service_account import Credentials
import gspread
import json
import webbrowser
import gmail as t

from streamlit import runtime
from streamlit.runtime.scriptrunner import get_script_run_ctx

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
      radial-gradient(50% 50% at 100% 0,#fafeff 0%  5% ,#e3c3c3 6%  15%,#fafeff 16% 25%,#e3c3c3 26% 35%,#fafeff 36% 45%,
       #e3c3c3 46% 55%,#fafeff 56% 65%,#e3c3c3 66% 75%,#fafeff 76% 85%,#e3c3c3 86% 95%,
       #0000 96%),
      radial-gradient(50% 50% at 0 100%,#fafeff 0%  5% ,#e3c3c3 6%  15%,#fafeff 16% 25%,#e3c3c3 26% 35%,#fafeff 36% 45%,
       #e3c3c3 46% 55%,#fafeff 56% 65%,#e3c3c3 66% 75%,#fafeff 76% 85%,#e3c3c3 86% 95%,
       #0000 96%),
      radial-gradient(50% 50%,#fafeff 0%  5% ,#e3c3c3 6%  15%,#fafeff 16% 25%,#e3c3c3 26% 35%,#fafeff 36% 45%,
       #e3c3c3 46% 55%,#fafeff 56% 65%,#e3c3c3 66% 75%,#fafeff 76% 85%,#e3c3c3 86% 95%,
       #0000 96%),
      radial-gradient(50% 50%,#fafeff 0%  5% ,#e3c3c3 6%  15%,#fafeff 16% 25%,#e3c3c3 26% 35%,#fafeff 36% 45%,
       #e3c3c3 46% 55%,#fafeff 56% 65%,#e3c3c3 66% 75%,#fafeff 76% 85%,#e3c3c3 86% 95%,
       #0000 96%) 32px 32px;
background-size: 64px 64px;
background-color: #fafeff;
opacity: 5;
}

[data-testid="element-container"]{
   font-family: 'freight-big-pro';
   font-size: 10px;
   font-weight: normal;
   letter-spacing: 2px;
}

[class="st-emotion-cache-1629p8f e1nzilvr2"] h1{
   color: #E30000;
   font-family: 'freight-big-pro';
   font-size: 55px;
   font-weight: bold;
   letter-spacing: 6px;
   overflow-wrap: break-world;
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
opacity: 1;
}

[data-testid="stToolbar"]{
right: 4rem;
}

[data-testid="stTabs"]{
background: rgba(182,242,204,0.45);
-webkit-backdrop-filter: blur(2px);
backdrop-filter: blur(2px);
border: 1px solid rgba(182,242,204,0.225);
border-radius: 25px; /* Adjust the value to change the roundness */
padding: 20px;
}

[data-testid="stForm"]{
    border: 0px
}

[data-testid="baseButton-secondaryFormSubmit"]{
background: rgb(222,195,207);
background: linear-gradient(90deg, rgba(222,195,207,0.7036064425770308) 0%, rgba(179,233,189,0.49352240896358546) 100%);
}

[data-testid="stMarkdownContainer"]{
    font-family: 'freight-big-pro';
    font-size: 7px;
    font-weight: normal;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Setup Google Sheets connection
path_to_credentials = r"iqmath-database-39cfa26e6243.json"

# Load credentials
creds = None
with open(path_to_credentials, 'r') as file:
    creds_json = json.load(file)
    creds = Credentials.from_service_account_info(creds_json, scopes=[
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ])

# Authorize with gspread using the loaded credentials
client = gspread.authorize(creds)
sheet = client.open("database").sheet1

# List of universities (Example subset)
universities = [
    "Indian Institute of Technology Bombay",
    "Indian Institute of Technology Delhi",
    "Indian Institute of Technology Madras",
    "Indian Institute of Technology Kanpur",
    "Indian Institute of Technology Kharagpur",
    "National Institute of Technology Trichy",
    "Delhi University",
    "Jawaharlal Nehru University",
    "University of Mumbai",
    "University of Pune"
]

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

ip_add = get_remote_ip()

def val_ip(user_ip_add):
    if ip_add == user_ip_add:
        return True
    else:
        return False

# Helper functions to check if user exists and authenticate them
def check_user(username):
    username = username.strip()
    cell_list = sheet.findall(username)
    return any(cell.row for cell in cell_list)

def authenticate(username, password):
    username = username.strip()
    password = password.strip()
    try:
        cell = sheet.find(username)
        actual_password = sheet.cell(cell.row, 2).value
        return actual_password.strip() == password
    except:
        return False

# Streamlit app
def main():
    session_state = st.session_state

    if "mac_otp" not in session_state:
        session_state.mac_otp = None
        session_state.new_username = None
        session_state.new_password = None
        session_state.new_phone = None
        session_state.new_email = None
        session_state.new_college = None
        session_state.new_year = None

    st.title("IQMath User Authentication Portal")

    # Tabs for Signup and Login
    tab1, tab2, tab3 = st.tabs(["Sign Up", "Verify your account", "Login"])

    with tab1:
        with st.form("Sign Up Form"):
            new_username = st.text_input("Username", "")
            new_password = st.text_input("Password", type="password")
            new_phone = st.text_input("Phone Number", "")
            new_email = st.text_input("Email", "")
            new_college = st.selectbox("College", [""] + universities)  # Dropdown for universities
            new_year = st.number_input("Passed Out Year", min_value=1900, max_value=2100, step=1, format="%d")
            submit_button = st.form_submit_button("Sign Up")

            if submit_button:
                if not all([new_username, new_password, new_phone, new_email, new_college, new_year]):
                    st.error("All fields are required.")
                elif check_user(new_username):
                    st.error("Username already exists. Try a different username.")
                else:
                    mac_otp = t.send_otp(new_email)
                    st.success("OTP has sent to your mail successfully, Verify your account to attend the coding test!")
                    session_state.mac_otp = int(mac_otp)
                    session_state.new_username = new_username
                    session_state.new_password = new_password
                    session_state.new_phone = new_phone
                    session_state.new_email = new_email
                    session_state.new_college = new_college
                    session_state.new_year = new_year
        if session_state.mac_otp:
            with st.form(key="resend_otp_form"):
                st.write("Didn't receive OTP?")
                resend_button = st.form_submit_button("Resend OTP")
                if resend_button:
                    session_state.mac_otp = int(t.send_otp(new_email))
                    st.success("OTP has sent to your mail successfully...!")

    with tab2:
        with st.form("Verify OTP Form"):
            user_name_new = st.text_input("Username", "")
            user_mail_new = st.text_input("Email", "")
            user_otp = st.text_input("Enter OTP", "")
            check = session_state.mac_otp
            verify_button = st.form_submit_button("Verify OTP")
            if verify_button:
                if not check_user(user_name_new):
                    if user_mail_new == session_state.new_email and user_name_new == session_state.new_username:
                        if user_otp and int(user_otp) == session_state.mac_otp:
                            sheet.append_row([session_state.new_username, session_state.new_password, session_state.new_phone, session_state.new_email, session_state.new_college, session_state.new_year])
                            st.success("You have successfully verified your account, Login to attend the SQL coding test!")
                        elif user_otp:
                            st.error("Incorrect OTP. Please try again.")
                    else:
                        st.error("Incorrect Username or Password...!")
                else:
                    st.error("Username already exists.")

    with tab3:
        with st.form("Login Form"):
            username = st.text_input("Username", "")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")

            if login_button:
                if authenticate(username, password):
                    st.success(f"Welcome to IQMath Analytics, {username}!")
                    # Redirect to the dashboard app with username as query parameter
                    dashboard_url = "https://dataprojects-nkmeng7q9oqyrvce3abdxp.streamlit.app/?username=" + username
                    st.markdown(f"[Click Here]({dashboard_url}) to launch the Coding Application...")
                    webbrowser.open_new_tab(dashboard_url)
                else:
                    st.error("The username or password is incorrect")
    

if __name__ == "__main__":
    main()
