import streamlit as st
import pandas as pd
from io import BytesIO
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

# Define your SharePoint site URL
site_url = "https://netorg245148.sharepoint.com/sites/PandoShipping"

# Retrieve credentials from Streamlit secrets
username = st.secrets["sharepoint"]["username"]
password = st.secrets["sharepoint"]["password"]

# Authenticate with SharePoint
ctx_auth = AuthenticationContext(site_url)
if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(site_url, ctx_auth)
    
    # Define the file_relative_url (decoded path)
    file_relative_url = "/sites/PandoShipping/Shared Documents/Easton Shipping/Docking System - Easton (V2) (1).xlsm"
    
    # Get the file from SharePoint and download it into a BytesIO buffer
    file_obj = ctx.web.get_file_by_server_relative_url(file_relative_url)
    file_buffer = BytesIO()
    file_obj.download(file_buffer).execute_query()
    file_buffer.seek(0)  # Reset buffer pointer to the beginning
    
    # Read the "Archive" sheet using pandas
    try:
        df_archive = pd.read_excel(file_buffer, sheet_name="Archive")
        st.write("First few rows of the Archive sheet:")
        st.dataframe(df_archive.head())
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
else:
    st.error("Authentication failed")
