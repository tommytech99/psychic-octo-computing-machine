# Import the required modules
import PyPDF2
import jsonlines

# Open the PDF file in binary mode
pdf_file = open("data.pdf", "rb")

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF
num_pages = len(pdf_reader.pages)

# Open a JSON lines file for writing
json_file = open("data.jsonl", "w")

# Create a JSON lines writer object
json_writer = jsonlines.Writer(json_file)

# Loop through each page of the PDF
for i in range(num_pages):
    # Get the page object
    page = pdf_reader.pages[i]

    # Extract the text from the page
    text = page.extract_text()

    # Convert the text to a dictionary
    data = {"text": text}

    # Write the dictionary to the JSON lines file
    json_writer.write(data)

# Close the files
pdf_file.close()
json_file.close()