import os

output_folder_path = os.path.join(os.path.abspath(
    r'C:\Users\Public\PyBots'), 'My-DOST', 'Excel Folder')

# create output folder if not present
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)


def authenticate_google_spreadsheet(credential_file_path=""):
    """
    Description:
        Authenticates Google Spreadsheet.
    Args:
        credential_file_path (str, optional): Path of credential file. Defaults to "".
    Returns:
        [status, data]
        status (bool): Whether the function is successful or failed.
        data (object): Google Spreadsheet Auth object.
    """

    # import section
    from my_dost.CrashHandler import report_error
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    # Response section
    error = None
    # status = False
    data = None

    # Logic section
    if not credential_file_path:
        raise Exception("credential (json) file path cannot be empty")

    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        credential_file_path, scope)

    gc = gspread.authorize(creds)

    return data


def excel_get_dataframe_from_google_spreadsheet(auth, spreadsheet_url="", sheet_name="Sheet1"):
    # Description:
    """
    Description:
        Get dataframe from google spreadsheet.
    Args:
        URL (str, optional): (Only in Windows)Name of Window you want to activate.
        Eg: Notepad. Defaults to "".

    Returns:
        [status, data]
        status (bool): Whether the function is successful or failed.
        data (object): Dataframe object.
    """

    # import section
    from my_dost.CrashHandler import report_error
    import pandas as pd

    # Response section
    error = None
    # status = False
    data = None
    # Logic section

    if not auth:
        raise Exception(
            "Please call authenticate_google_spreadsheet function to get auth")

    if not spreadsheet_url:
        raise Exception("spreadsheet url cannot be empty")

    sh = auth.open_by_url(url=spreadsheet_url)

    # get all the worksheets from sh
    worksheet_list = sh.worksheets()

    # check if sheet_name is already present in worksheet_list
    sheet_present = False
    for worksheet in worksheet_list:
        if worksheet.title == sheet_name:
            sheet_present = True
            break

    if not sheet_present:
        raise Exception("Sheet name not found")
    else:
        worksheet = sh.worksheet(sheet_name)

    data_frame = pd.DataFrame(worksheet.get_all_records())

    # except Exception as ex:
    #     # check if it is a permission error
    #     if 'PERMISSION_DENIED' in str(ex):
    #         raise Exception(
    #             "Permission Denied. Please share the spreadsheet with client email as per Credential JSON File")
    #     else:
    #         report_error(ex)
    #         error = ex

    # return data


def excel_tabular_data_from_website(website_url="", table_number=""):
    """
    Description:
        Gets Website Table Data Easily as an Excel using Pandas. Just pass the URL of Website having HTML Tables.
    Args:
        website_url (str, optional): URL of Website. Defaults to "".
        table_number (int, optional): Table Number. Defaults to all.

    Returns:
        [status, data]
        status (bool): Whether the function is successful or failed.
        data (object): Dataframe object.
    """

    # Import Section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response Section
    error = None
    # status = False
    data = None

    # Logic Section
    
    if not website_url:
        raise Exception("Website URL cannot be empty")

    all_tables = pd.read_html(website_url)

    if not table_number:
        data = all_tables
    else:
        if table_number > len(all_tables):
            raise Exception(
                "Table number cannot be greater than number of tables")

        if table_number < 1:
            raise Exception("Table number cannot be less than 1")

        data = all_tables[table_number - 1]

    return data

# [status, data]
# browser_get_html_tabular_data_from_website(website_url="https://en.wikipedia.org/wiki/List_of_footballers_with_500_or_more_goals",output_folder=r"C:\Users\mrmay\OneDrive\Desktop\Misc")
# print(excel_tabular_data_from_website(
#     "https://en.wikipedia.org/wiki/Scoring_in_association_football", 1))


def excel_upload_dataframe_to_google_spreadsheet(auth, spreadsheet_url="", sheet_name="Sheet1", df=""):
    # Description:
    """
    Description:
        Uploads dataframe to google spreadsheet.

    Args:
        URL (str, optional): (Only in Windows)Name of Window you want to activate.
        Eg: Notepad. Defaults to "".

    Returns:
        [status]
        status (bool): Whether the function is successful or failed.
    """

    # import section
    from my_dost.CrashHandler import report_error
    from gspread_dataframe import set_with_dataframe
    import pandas as pd

    # Response section
    error = None
    # status = False

    # Logic section

    if not auth:
        raise Exception(
            "Please call authenticate_google_spreadsheet function to get auth")

    if not spreadsheet_url:
        raise Exception("spreadsheet url cannot be empty")

    if not isinstance(df, pd.DataFrame):
        raise Exception("dataframe must be a pandas dataframe")

    sh = auth.open_by_url(url=spreadsheet_url)

    # get all the worksheets from sh
    worksheet_list = sh.worksheets()

    # check if sheet_name is already present in worksheet_list
    sheet_present = False
    for worksheet in worksheet_list:
        if worksheet.title == sheet_name:
            sheet_present = True
            break

    if sheet_present:
        # append df to existing sheet
        worksheet = sh.worksheet(sheet_name)
        row_count = worksheet.get_all_values().__len__()

        if row_count == 0:
            set_with_dataframe(worksheet, dataframe=df)
        else:
            set_with_dataframe(worksheet, dataframe=df,
                                row=row_count + 1, include_column_header=False)

    else:
        worksheet = sh.add_worksheet(
            title=sheet_name, rows="999", cols="26")
        set_with_dataframe(worksheet, df)

    # except Exception as ex:
    #     # check if it is a permission error
    #     if 'PERMISSION_DENIED' in str(ex):
    #         raise Exception(
    #             "Permission Denied. Please share the spreadsheet with client email as per Credential JSON File")
    #     else:
    #         report_error(ex)
    #         error = ex

    # else:
    #     status = True
    #     # # If the function returns a value, it should be assigned to the data variable.
    # finally:
    #     if error is not None:
    #         raise Exception(error)
    #     return [status]

# status, auth = authenticate_google_spreadsheet(r"C:\Users\mrmay\OneDrive\Desktop\Brainly-ML-Project\mayur-pybots-valued-door-353312-0a3451b27ef8.json")
# # status, df =excel_get_dataframe_from_google_spreadsheet(auth,"https://docs.google.com/spreadsheets/d/1CeF1NuAVLJMEBWQIT2nKceeVM9xjgxhqbNdjPBVurqw/edit#gid=0","Sheet1")

# # print(df)
# # print(status)
# # create a dummy dataframe
# import pandas as pd
# df1 = pd.DataFrame({"A":[111,222,333],"B":[4,5,6],"C":[7,8,9]})
# status = excel_upload_dataframe_to_google_spreadsheet(auth, "https://docs.google.com/spreadsheets/d/1CeF1NuAVLJMEBWQIT2nKceeVM9xjgxhqbNdjPBVurqw/edit#gid=0", "Sheet3",df1)


def excel_create_file(output_folder="", output_filename="", output_sheetname="Sheet1"):
    """
    Description:
        Creates an Excel file.
    Args:
        output_folder (str, optional): Folder where file will be created. Defaults to "".
        output_filename (str, optional): Name of file. Defaults to "".
        output_sheetname (str, optional): Name of sheet. Defaults to "Sheet1".

    Returns:
        [status]
        status (bool): Whether the function is successful or failed.
    """

    # Import section
    from my_dost.CrashHandler import report_error
    import os
    from pathlib import Path
    from openpyxl import Workbook

    # Response section
    error = None
    # status = False

    # Logic section
    if not output_folder:
        raise Exception("Excel File name cannot be empty")

    if not output_filename:
        raise Exception("Excel File Name cannot be empty")

    if not os.path.exists(output_folder):
        output_folder = output_folder_path

    if ".xlsx" not in output_filename:
        output_filename = os.path.join(output_folder, str(
            Path(output_filename).stem) + ".xlsx")
    else:
        output_filename = os.path.join(output_folder, output_filename)

    wb = Workbook()
    ws = wb.active
    ws.title = output_sheetname

    wb.save(filename=output_filename)

# [status]


def valid_data(input_filepath, input_sheetname: str = "", validate_filepath=True, validate_sheetname=True):
    """
    Description:
        Validates data in excel file.

    Args:
        input_filepath (str, optional): Filepath of input file. Defaults to "".
        input_sheetname (str, optional): Sheetname of input file. Defaults to "".
        validate_filepath (bool, optional): Whether to validate filepath. Defaults to True.
        validate_sheetname (bool, optional): Whether to validate sheetname. Defaults to True.

    Returns:
        [status]
        status (bool): Whether the function is successful or failed.
    """

    import os
    from openpyxl import load_workbook
    from my_dost.CrashHandler import report_error

    input_filepath = str(input_filepath)
    input_sheetname = str(input_sheetname)
    if validate_filepath:
        if not ".xlsx" in input_filepath:
            raise Exception(
                "Please provide the excel file name with .xlsx extension")
            return False
        if not os.path.exists(input_filepath):
            raise Exception(
                "Please provide the excel file name with correct path")
            return False
        if validate_sheetname:
            wb = load_workbook(input_filepath)
            sheet_names = wb.sheetnames
            if input_sheetname not in sheet_names:
                raise Exception(
                    "Please provide the correct sheet name")
                print('Available Sheet Names', sheet_names)


def excel_to_dataframe(input_filepath="", input_sheetname="Sheet1", header=1):
    """
    Description:
        Converts excel to dataframe
    Args:
        input_filepath (str) : Complete path to the excel file.
        input_sheetname (str) : Sheet name of the excel file.
        header (int)         : Row number of the header.
    Returns:
        [status, data]
        status (bool): Whether the function is successful or failed.
        data (pandas dataframe): Dataframe of the excel file.
    """

    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None


    if not input_filepath:
        raise Exception("Please provide the excel path")
    if not input_sheetname:
        raise Exception("Please provide the sheet name")

    if not valid_data(input_filepath, input_sheetname):
        return [status]

    if header > 0:
        data = pd.read_excel(
            input_filepath, sheet_name=input_sheetname, header=header-1, engine='openpyxl')

    # If the function returns a value, it should be assigned to the data variable.
    # data = value
    return data
# df = excel_to_dataframe(r"C:\Users\mrmay\OneDrive\Desktop\MMV.xlsx")
# print(df, "df")


def excel_get_row_column_count(df):

    # Description:
    """
    Description:
        Returns the row and column count of the dataframe.


    Args:
        df (pandas dataframe): Dataframe of the excel file.

    Returns:
        [status, data]
        status (bool): Whether the function is successful or failed.
        data (list): [row_count, column_count] 
    """

    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None

    
    if not isinstance(df, pd.DataFrame):
        raise Exception("Please provide the dataframe")

    row, col = df.shape
    row = row + 1
    data = [row, col]

    # If the function returns a value, it should be assigned to the data variable.
    # data = value
    return data
# [status, data]
# data = [row, col]


def dataframe_to_excel(df, output_folder="", output_filename="", output_sheetname="Sheet1", mode='a'):  # append / overwrite
    """
    Description:
        Converts dataframe to excel
    Args:
        df (pandas dataframe): Dataframe of the excel file.
        output_folder (str, optional): Folder path of the output file. Defaults to "".
        output_filename (str, optional): Filename of the output file. Defaults to "".
        output_sheetname (str, optional): Sheetname of the output file. Defaults to "Sheet1".
        mode (str, optional): Mode of the output file. Defaults to "a" or "x"

    Returns:
        [status]
        status (bool): Whether the function is successful or failed.
    """

    # import section
    import pandas as pd
    import os
    from pathlib import Path
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False

    if not output_folder:
        output_folder = output_folder_path
    if not output_filename:
        output_filename = "excel_file"

    if not os.path.exists(output_folder):
        output_folder = output_folder_path

    if ".xlsx" not in output_filename:
        output_filepath = os.path.join(output_folder, str(
            Path(output_filename).stem) + ".xlsx")
    else:
        output_filepath = os.path.join(output_folder, str(
            output_filename))

    if not output_sheetname:
        raise Exception("Please provide the sheet name")

    if not isinstance(df, pd.DataFrame):
        raise Exception("Please provide the dataframe")

    new_file = False
    if not os.path.exists(output_filepath):
        # excel_create_file(output_folder, output_filename)
        new_file = True

    if mode == 'a' and not new_file:
        with pd.ExcelWriter(output_filepath, mode="a", engine="openpyxl", if_sheet_exists="overlay",) as writer:
            current_df = excel_to_dataframe(
                output_filepath, output_sheetname)[1]
            row_count = excel_get_row_column_count(current_df)[1]
            df.to_excel(writer, sheet_name=output_sheetname,
                        index=False, startrow=int(row_count[0]), header=False)
    else:
        with pd.ExcelWriter(output_filepath, engine="openpyxl",) as writer:
            df.to_excel(writer, sheet_name=output_sheetname, index=False)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value

# if __name__ == "__main__":
#     import pandas as pd
    # df = pd.DataFrame({"A": [11, 22, 33], "B": [44, 55, 66]})
    # dataframe_to_excel(df, r"C:\Users\mrmay\OneDrive\Desktop", "MMV-2.xlsx", "Sheet1", mode='x')
    # dataframe_to_excel(df, r"C:\Users\mrmay\OneDrive\Desktop", "MMV-1.xlsx", "Sheet1")


def excel_set_single_cell(df, column_name="", cell_number=1, text=""):
    """
    Description:
        Writes the given text to the desired column/cell number for the given excel file
    Args:
        df (pandas dataframe): Dataframe of the excel file.
        column_name (str, optional): Column name of the excel file. Defaults to "".
        cell_number (int, optional): Cell number of the excel file. Defaults to 1.
        text (str, optional): Text to be written to the excel file. Defaults to "".

    Returns:
        [status, data]
        status (bool): Whether the function is successful or failed.
        data (df): Modified dataframe
    """

    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None

    if not isinstance(df, pd.DataFrame):
        raise Exception("Please provide the dataframe")

    if not column_name:
        raise Exception("Please provide the column name")

    if not text:
        raise Exception("Please provide the text to be set")

    if cell_number < 1:
        raise Exception("Please provide the valid cell number")

    df.at[cell_number-1, column_name] = text
    data = df

    return data
# [status, data]
# data is a dataframe object

# df = excel_to_dataframe(r"C:\Users\mrmay\OneDrive\Desktop\MMV-1.xlsx", "Sheet1")[1]
# print(df)
# d = excel_set_single_cell(df, column_name="Salary", cell_number=3, text="Hello")[1]
# print(d)


def excel_get_single_cell(df, header=1, column_name="", cell_number=1):
    """
    Description:
        Gets the text from the desired column/cell number of the given excel file
    Args:
        df (pandas dataframe): Dataframe of the excel file.
        header (int, optional): Header of the excel file. Defaults to 0.
        column_name (str, optional): Column name of the excel file. Defaults to "".
        cell_number (int, optional): Cell number of the excel file. Defaults to 0.

    Returns:
        [status, data]
        status (bool): Whether the function is successful or failed.
        data (str): Data from the desired column/cell number of the excel file.

    """

    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None

    if not isinstance(df, pd.DataFrame):
        raise Exception("Please provide the dataframe")

    if not column_name:
        raise Exception("Please provide the column name")

    if not isinstance(column_name, list):
        column_name = [column_name]

    if cell_number < 1:
        raise Exception("Please provide the valid cell number")

    data = df.at[cell_number-header-1, column_name[0]]

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    return data
# [status, data]
# data = 'text'
# df = excel_to_dataframe(r"C:\Users\mrmay\OneDrive\Desktop\MMV-1.xlsx", "Sheet1")[1]
# print(df)
# s, d = excel_get_single_cell(df, 1, "Age", 7)
# print(d)


def excel_get_all_header_columns(df):

    # Description:
    """
    Description:
        Gives you all column header names of the given excel sheet.
    Args:
        df (pandas dataframe): Dataframe of the excel file.

    Returns:
        [status, data]
        status (bool): Whether the function is successful or failed.
        data (list): List of all column header names of the excel file.

    """

    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error
    # Response section
    error = None
    # status = False
    data = None

    if not isinstance(df, pd.DataFrame):
        raise Exception("Please provide the dataframe")

    data = df.columns.values.tolist()

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    return data
# [status, data]
# data = ['Header1', 'Header2', 'Header3']
# print(excel_get_all_header_columns(r"C:\Users\PyBots\Desktop\dummy.xlsx"))


def excel_get_all_sheet_names(input_filepath=""):
    # Description:
    """
    Description:
        Gives you all names of the sheets in the given excel sheet.

    Parameters:
        input_filepath  (str) : Path of the excel file.

    returns :
        [status, data]
        status (bool): Whether the function is successful or failed.
        data (list): List of all sheet names of the excel file.
    """

    # import section
    from openpyxl import load_workbook
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    status = False
    data = None

    if not input_filepath:
        raise Exception("Please provide the excel path")
    if not valid_data(input_filepath, validate_sheetname=False):
        raise Exception("Please provide the valid excel path")

    wb = load_workbook(input_filepath)
    data = wb.sheetnames

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    return data
# [status, data]
# data = [sheet_name1, sheet_name2, sheet_name3]
# print(excel_get_all_sheet_names(r"C:\Users\PyBots\Desktop\dummy.xlsx"))



def excel_drop_columns(df, cols=""):

    # Description:
    """
    Description:
        Drops the desired column from the given excel file

    Parameters:
        df : dataframe
        cols : column names to be dropped

    Returns:
        [status, data]
        status : True if the function is successful, False otherwise
        data : dataframe with the dropped columns

    """

    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False

    if not isinstance(df, pd.DataFrame):
        raise Exception("Please provide the dataframe")

    if not cols:
        raise Exception(
            "Please provide the column name to be dropped.")

    if not isinstance(cols, list):
        cols = [cols]

    df.drop(cols, axis=1, inplace=True)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    return df
# [status, data]
# data is the dataframe after dropping the columns.


def excel_clear_sheet(df):

    # Description:
    """
    Description:
        Clears the contents of given excel files keeping header row intact

    Args:
        df : dataframe

    Returns:
        [status, data]
        status : True if the function is successful, False otherwise
        data : dataframe with the cleared contents

    """

    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    status = False
    data = None

    if not isinstance(df, pd.DataFrame):
        raise Exception("Please provide the dataframe")

    # Clears the contents of the sheet
    df.drop(df.index, inplace=True)

    data = df

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    return data
# [status, data]
# data is the dataframe after clearing the sheet.


def excel_remove_duplicates(df, column_name=""):

    # Description:
    """
    Description:
        Drops the duplicates from the desired Column of the given excel file

    Args:
        df : dataframe
        column_name : column name from which duplicates are to be removed

    Returns:
        [status, data]
        status : True if the function is successful, False otherwise
        data : dataframe with the duplicates removed

    """

    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    status = False
    data = None
    which_one_to_keep = "first"

    if not isinstance(df, pd.DataFrame):
        raise Exception("Please provide the dataframe")

    if not column_name:
        df.drop_duplicates(keep=which_one_to_keep, inplace=True)

    else:
        if not isinstance(column_name, list):
            column_name = [column_name]
        df.drop_duplicates(subset=column_name,
                            keep=which_one_to_keep, inplace=True)

    data = df
        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    return data
# [status, data]
# data is the dataframe after removing the duplicates.
# print(excel_remove_duplicates(
#     r"C:\Users\PyBots\Desktop\dummy.xlsx", same_file=True))


def isNaN(value=""):

    # Description:
    """
    Description:
        Returns TRUE if a given value is NaN False otherwise

    Parameters:
        value : value to be checked

    Returns:
        [status]
        status : True if the value is NaN, False otherwise

    """

    # import section
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False

    if not value:
        raise Exception(
            "Value is empty. Please give a value to check.")
    import math
    status = math.isnan(float(value))
# [status]


def df_from_list(list_of_lists, column_names=None):
    """
    Description:
        Creates a dataframe from a list of lists

    Args:
        list_of_lists : list of lists
        column_names : list of column names

    Returns:
        [data]
        data : dataframe object
    """
    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None
    # Logic section
    if not isinstance(list_of_lists, list):
        raise Exception("Please pass input as list of lists")

    if isinstance(list_of_lists, list):
        if column_names == None:
            data = pd.DataFrame(list_of_lists)
        else:
            data = pd.DataFrame(list_of_lists, columns=column_names)

    return data
# [data]
# print(df_from_list([[1,2,3],[4,5,6],[7,8,9]],column_names=['a','b','c']))
# s, df1=df_from_list([[1,2,3],[4,5,6],[7,8,9]])
# print(df1, type(df1))
# print(df_from_list([[1,2,3],[4,5,6],['a','b','c']]))

# write a function to create a dataframe from a string


def df_from_string(df_string: str, word_delimeter=" ", line_delimeter="\n", column_names=None):
    """
    Description:
        Creates a dataframe from a string
    Args:
        df_string : string
        word_delimeter : word delimeter
        line_delimeter : line delimeter
        column_names : list of column names

    Returns:
        [data]
        data : dataframe object
    """
    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None
    # Logic section
    if not df_string:
        raise Exception("Please pass input as string")

    if not isinstance(df_string, str):
        df_string = str(df_string)

    if column_names == None:
        data = pd.DataFrame([x.split(word_delimeter)
                            for x in df_string.split(line_delimeter)])
    elif isinstance(column_names, list):
        data = pd.DataFrame([x.split(word_delimeter) for x in df_string.split(
            line_delimeter)], columns=column_names)
    return data
# [data]
# print(df_from_string('1 2 3\n4 5 6\n7 8 9', word_delimeter=" ", line_delimeter="\n"))
# print(df_from_string('1\t2\t3\r\n4\t5\t6\r\n7\t8\t9', word_delimeter="\t", line_delimeter="\r\n",column_names=['a','b','c']))


# function to extract sub dataframe from a dataframe using rows and column number
def df_extract_sub_df(df, row_start: int, row_end: int, column_start: int, column_end: int):
    """
    Description:
        Extracts a sub dataframe from a dataframe
    Args:
        df : dataframe
        row_start : start row number
        row_end : end row number
        column_start : start column number
        column_end : end column number

    Returns:
        [data]
        data : dataframe object
    """
    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None
    # Logic section
    # try:
    if df.empty:
        raise Exception("Dataframe cannot be empty")

    if isinstance(df, pd.DataFrame):
        data = df.iloc[row_start:row_end, column_start:column_end]

    return data
# [status, data]
# df_main = df_from_list([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]],column_names=['a','b','c','d','e'])
# print(df_main,"\n")
# df_sub = df_extract_sub_df(df_main,1,2,2,3)
# print(df_sub)


def set_value_in_df(df, row_number: int, column_number: int, value):
    """
    Description:
        Sets a value in a dataframe

    Args:
        df : dataframe
        row_number : row number
        column_number : column number
        value : value to be set

    Returns:
        [data]
        data : dataframe object

    """
    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None
    # Logic section
    # try:
    if df.empty:
        raise Exception("Dataframe cannot be empty")

    # print(type(df))
    if isinstance(df, pd.DataFrame):
        if row_number < 1 or column_number < 1:
            raise Exception(
                "Row and column number should be greater than 0")

        if row_number > df.shape[0] or column_number > df.shape[1]:
            raise Exception(
                "Row and column number should be less than or equal to dataframe shape")

        df.iloc[row_number-1, column_number-1] = value

    # except Exception as ex:
    #     report_error(ex)
    #     error = ex

    # # else:
    # #     status = True

    # finally:
    #     if error is not None:
    #         raise Exception(error)
        return df
# [status, data]
# df1 = df_from_list([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]],column_names=['a','b','c','d','e'])
# print(df1)
# print(type(df1))
# print(set_value_in_df(df1,0,0,100))


def get_value_in_df(df, row_number: int, column_number: int):
    """
    Description:
        Gets a value from a dataframe

    Parameters:
        df : dataframe
        row_number : row number
        column_number : column number

    Returns:
        [data]
        data : value from dataframe

    """
    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None

    # Logic section
    if df.empty:
        raise Exception("Dataframe cannot be empty")

    if isinstance(df, pd.DataFrame):
        if row_number < 1 or column_number < 1:
            raise Exception(
                "Row and column number should be greater than 0")

        if row_number > df.shape[0] or column_number > df.shape[1]:
            raise Exception(
                "Row and column number should be less than or equal to dataframe shape")

        data = df.iloc[row_number-1, column_number-1]

    return data
# [status, data]

# create a function to merge all sheets of an excel


def df_drop_rows(df, row_start: int, row_end: int):
    """
    Description:
        Drops a range of rows from a dataframe including the row_start and row_end rows.

    Args:
        df : dataframe
        row_start : start row number
        row_end : end row number

    Returns:
        [data]
        data : dataframe object
    """
    # import section
    import pandas as pd
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    # status = False
    data = None
    # Logic section
    if df.empty:
        raise Exception("Dataframe cannot be empty")

    if isinstance(df, pd.DataFrame):
        # -1 because index starts from 0
        data = df.drop(df.index[row_start-1:row_end])


    # else:
    #     status = True

    return data

# if __name__ == "__main__":
#     status, df = excel_to_dataframe(r"C:\Users\mrmay\OneDrive\Desktop\MMV.xlsx",input_sheetname="Sheet3")
#     print(df)
#     data= df_drop_rows(df,row_start=15,row_end=17)
#     print(data[0])

# write a function to convert dataframe column or list of columns to string / int / float /date as per user choice
