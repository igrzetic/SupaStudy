import pdfplumber


def keep_table_object(obj):
    if obj["object_type"] != "rect":
        return True

    return obj["width"] < 2 or obj["height"] < 2

def read_pdf_tables(file_path):
    tables = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            filtered_page = page.filter(keep_table_object)

            for table_number, rows in enumerate(filtered_page.extract_tables(), start=1):
                tables.append({
                    "page": page.page_number,
                    "table": table_number,
                    "rows": rows,
                })

    return tables
