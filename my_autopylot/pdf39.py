import os
output_folder_path = os.path.join(
    os.path.abspath(r'C:\Users\Public\PyBots'), 'My-AutoPylot', 'PDF Folder')

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
    from my_autopylot.CrashHandler import report_error

    # Response Section
    error = None
    status = False

    # Logic Section
    try:
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

    except Exception as ex:
        report_error(ex)
        error = ex

    else:
        status = True

    finally:
        if error is not None:
            raise Exception(error)
        return [status]

# write a function to extract desired table from desired page of pdf


def pdf_extract_table(pdf_file_path: str = "", table_number: int = 0, page_number: int = 0):
    """
    Description:
        Extract a table from a pdf file and save it to a text file.
    Args:
        pdf_file_path (str): [description]. Defaults to "".
        table_number (int): [description]. Defaults to 0.
        page_number (int): [description]. Defaults to 0.
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
    from my_autopylot.CrashHandler import report_error

    # Response Section
    error = None
    status = False
    Data = None

    # Logic Section
    try:
        if not pdf_file_path:
            raise Exception("PDF file path cannot be empty")

        elif not table_number:
            raise Exception("Table number cannot be empty")

        elif not page_number:
            raise Exception("Page number cannot be empty")

        # check if pdf_file_path exists
        if not os.path.exists(pdf_file_path):
            raise Exception("PDF file path does not exist")

        else:
            pdf = pdfplumber.open(pdf_file_path)

            tables = []

            for each_page in pdf.pages:
                tables.append(each_page.extract_tables())

            # list of the rows to dataframe
            df = pd.DataFrame(tables[page_number - 1][table_number - 1],
                              columns=tables[page_number - 1][table_number - 1][0])
            df = df.drop(df.index[0])
            df = df.reset_index(drop=True)

            Data = df

    except Exception as ex:
        report_error(ex)
        error = ex

    else:
        status = True

    finally:
        if error is not None:
            raise Exception(error)
        return [status, Data]


# if __name__ == "__main__":
#     from my_autopylot.excel39 import dataframe_to_excel
#     # pdf_extract_all_tables(r"C:\Users\mrmay\Downloads\ACH Payment from Charter Communications - 1 Apr.PDF", output_folder_path, "pdf_test.xlsx")
#     # print(output_folder_path)
#     s, df = pdf_extract_table(r"C:\Users\mrmay\Downloads\ACH Payment from Charter Communications - 1 Apr.PDF", 1, 9)
#     s = dataframe_to_excel(df,output_folder_path , "pdf_test_11", "Sheet1")
#     print(output_folder_path)
