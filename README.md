# Streamlit SharePoint Excel Viewer

This project is a simple Streamlit application that downloads an Excel file from a SharePoint site using the Office365 REST Python Client and displays the first few rows of the "Archive" sheet.

## Features

- **Streamlit UI:** Provides a clean and interactive interface to view data.
- **Secure Credentials Management:** Uses Streamlit's secrets management to securely store your SharePoint credentials.
- **SharePoint File Download:** Authenticates with SharePoint and downloads an Excel file on-demand.
- **Excel Data Display:** Reads and displays the "Archive" sheet from the downloaded Excel file using pandas and openpyxl.

## Prerequisites

- **Python 3.7+**
- Access to the relevant SharePoint site.
- Basic knowledge of Python and Streamlit.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/streamlit-sharepoint-excel-viewer.git
   cd streamlit-sharepoint-excel-viewer
