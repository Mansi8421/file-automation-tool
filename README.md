
# File Automation Tool

## Overview

The File Automation Tool is a web-based application developed using Python Flask, HTML, JavaScript, and OpenPyXL.

The application enables users to provide personal information along with source and destination folder paths. It automatically scans files from the selected directory and generates an Excel report containing both user details and file metadata.

---

## Features

✅ User Information Capture

- Name
- Email Address
- Phone Number

✅ Dynamic Folder Selection

- Source Folder Path
- Destination Folder Path

✅ Automated File Analysis

✅ Excel Report Generation

✅ File Metadata Extraction

- File Name
- File Size (KB)
- File Extension

✅ User-Friendly Web Interface

---

## Technologies Used

- Python
- Flask
- OpenPyXL
- HTML
- JavaScript

---

## Project Workflow

1. User enters:
   - Name
   - Email Address
   - Phone Number
   - Source Folder Path
   - Destination Folder Path

2. The Flask backend receives the request.

3. The application scans all files available in the source directory.

4. File information is extracted:
   - File Name
   - File Size
   - File Extension

5. OpenPyXL generates an Excel workbook.

6. The report is saved as `report.xlsx` in the destination folder.

7. A success message is displayed to the user.

---

## Excel Report Output

The generated Excel report contains:

### User Details

- Name
- Email Address
- Phone Number

### File Details

- File Name
- File Size (KB)
- File Extension

---

## Installation

Install the required packages:

```bash
pip install flask
pip install openpyxl
