
from flask import Flask, request, send_from_directory
import os
from openpyxl import Workbook

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/process', methods=['POST'])
def process_file():

    data = request.get_json()

    source = data['source']
    destination = data['destination']

    # Hardcoded customer details
    name = "Mansi Tehra"
    email = "mansi@example.com"
    phone = "9876543210"

    files = os.listdir(source)

    wb = Workbook()
    ws = wb.active

    # Customer information
    ws.append(["Customer Information"])
    ws.append(["Name", name])
    ws.append(["Email", email])
    ws.append(["Phone Number", phone])
    ws.append([])

    # File information
    ws.append(["File Name", "Size(KB)", "Extension"])

    for file in files:
        path = os.path.join(source, file)

        if os.path.isfile(path):
            size = round(os.path.getsize(path) / 1024, 2)
            ext = os.path.splitext(file)[1]

            ws.append([file, size, ext])

    output_file = os.path.join(destination, "report.xlsx")
    wb.save(output_file)

    return f"Excel created at {output_file}"

if __name__ == '__main__':
    app.run(debug=True)
