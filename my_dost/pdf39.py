import os
output_folder_path = os.path.join(
    os.path.abspath(r'C:\Users\Public\PyBots'), 'My-DOST', 'PDF Folder')

# create output folder if not present
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)


def pdf_extract_all_tables(pdf_file_path: str = "", output_folder: str = "", output_file_name: str = "", table_with_borders=True):
    """
    Description:
        Extract all tables from a pdf file and save them to a text file.
    Args:
        pdf_file_path (str): [description]. Defaults to "".
        output_folder (str): [description]. Defaults to "".
        output_file_name (str): [description]. Defaults to "".
    Returns:
        [status]
        status (bool) : Whether the pdf file was extracted or not.
    """
    # Import Section
    import pdfplumber
    import pandas as pd
    import datetime
    from my_dost.CrashHandler import report_error

    # Response Section
    error = None

    # Logic Section
    if not pdf_file_path:
        raise Exception("PDF file path cannot be empty")
    if not output_folder:
        output_folder = output_folder_path

    if not output_file_name:
        output_file_name = "pdf_" + \
            str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".xlsx"
    else:
        if not output_file_name.endswith(".xlsx"):
            output_file_name += ".xlsx"

    pdf = pdfplumber.open(pdf_file_path)

    tables = []

    if table_with_borders:
        for each_page in pdf.pages:
            tables.append(each_page.extract_tables())
    else:
        table_settings = {
            "vertical_strategy": "text",
            "horizontal_strategy": "text"
        }
        for each_page in pdf.pages:
            tables.append(each_page.extract_tables(table_settings))

    # excel writer
    writer = pd.ExcelWriter(os.path.join(
        output_folder, output_file_name), engine='openpyxl')

    for table in tables:
        df_main = []
        # list of the rows to dataframe
        for i in range(len(table)):
            df = pd.DataFrame(table[i])
            df_main.append(df)

        df_main = pd.concat(df_main)
        table_index = str(tables.index(table) + 1)

        df_main.to_excel(writer, sheet_name=table_index,
                            index=False, header=False)

    writer.save()

# write a function to extract desired table from desired page of pdf