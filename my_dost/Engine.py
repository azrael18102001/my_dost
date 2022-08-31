from my_dost.CrashHandler import report_error
# utility
from my_dost.utility39 import *
# excel
from my_dost.excel39 import *
# mouse
import my_dost.mouse39 as mouse
# keyboard
import my_dost.keyboard39 as keyboard
# voice
import my_dost.voice39 as voice
# chrome
import my_dost.chrome39 as chrome
# folder
import my_dost.folder39 as folder
# string
import my_dost.string39 as string
# windows
import my_dost.windows39 as windows
# utility
import my_dost.utility39 as utility
# messages
import my_dost.message39 as messages
# converters
import my_dost.converters39 as converters
# mail
import my_dost.mail39 as mail
# pdf
import my_dost.pdf39 as pdf


# ---------  PDF Functions ---------

def pdf_extract_all_tables(pdf_file_path="", output_folder="", output_file_name=""):
    """
    Extract all tables from a pdf file and save them to a text file.
    Args:
        pdf_file_path (str): [description]. Defaults to "".
        output_folder (str, optional): [description]. Defaults to "".
    """
    return pdf.pdf_extract_all_tables(pdf_file_path, output_folder, output_file_name)
# [status]

# ---------  PDF Functions Ends ---------


# ---------  Mail Functions ---------

def mail_send_gmail_with_app_password(gmail_username="", gmail_app_password="", to_email_id="", subject="", message="", attachment_path=""):
    """
    Args:
        gmail_username (str): [description]. Defaults to "".
        gmail_app_password (str): [description]. Defaults to "".
        to_email_id (str): [description]. Defaults to "".
        subject (str): [description]. Defaults to "".
        message (str): [description]. Defaults to "".
        attachment_path (str, optional): [description]. Defaults to "".

    Returns:
        [bool]: [status]
    """
    return mail.send_gmail_using_app_password(gmail_username, gmail_app_password, to_email_id, subject, message, attachment_path)
# [status]

# ---------  Mail Functions Ends ---------


# ---------  Converters Functions ---------

def convert_change_corrupt_xls_to_xlsx(input_file='', input_sheetname='', output_folder='', output_filename=''):
    '''
        Repair corrupt file to regular file and then convert it to xlsx.
        status : Done.
    '''
    return converters.excel_change_corrupt_xls_to_xlsx(input_file, input_sheetname, output_folder, output_filename)
# [status]


def convert_base64_to_img(imgBase64Str="", img_folder_path="", img_file_name=""):
    """
    Args:
        imgFileName (str, optional): [description]. Defaults to "".
        imgBase64Str (str, optional): [description]. Defaults to "".
        img_folder_path (str, optional): [description]. Defaults to "".
    Returns:
        [bool]: [status]
    """
    return converters.get_image_from_base64(imgBase64Str, img_folder_path, img_file_name)
# [status]


def convert_csv_to_excel(csv_path="", sep=",", excel_output_folder_path="", excel_file_name=""):
    """
    Args:
        csv_path (str): [description]. Defaults to "".
        sep (str): [description]. Defaults to "".
        excel_output_folder_path (str, optional): [description]. Defaults to "".
        excel_file_name (str, optional): [description]. Defaults to "".
    Returns:
        [bool]: [status]
    """
    return converters.convert_csv_to_excel(csv_path, sep, excel_output_folder_path, excel_file_name)
# [status]


def convert_xls_to_xlsx(input_file='', output_folder='', output_filename=''):
    """
    Converts given XLS file to XLSX
    """
    return converters.excel_convert_xls_to_xlsx(input_file, output_folder, output_filename)
# [status]


def convert_jpg_to_png(input_filepath="", output_folder="", output_filename=""):

    # Description:
    """
   Convert the image from jpg to png

    Args:
        input_image_path (str): The path of the input image
        output_folder (str): The path of the output folder

    Returns:
        [bool]: Whether the function is successful or failed.
    """
    return converters.convert_image_jpg_to_png(input_filepath, output_folder, output_filename)
# [status]


def convert_png_to_jpg(input_filepath="", output_folder="", output_filename=""):

    # Description:
    """
   Convert the image from png to jpg

    Args:
        input_image_path (str): The path of the input image
        output_folder (str): The path of the output folder

    Returns:
        [bool]: Whether the function is successful or failed.
    """
    return converters.convert_image_png_to_jpg(input_filepath, output_folder, output_filename)
# [status]


def convert_excel_to_colored_html(input_filepath="", output_folder="", output_filename=""):

    # Description:
    """
    Converts given Excel to HTML preserving the Excel format and saves in same folder as .html
    """
    return converters.excel_to_colored_html(input_filepath, output_folder, output_filename)
# [status]


def convert_image_to_base64(input_file=""):
    """
    Description:
        Convert image to base64 string.
    Args:
        input_file (str, optional): [description]. Defaults to "".
    Returns:
        [bool]: [status]
    """
    return converters.convert_image_to_base64(input_file)
# [status, data]

# ---------  Converters Functions Ends ---------


# ---------  Messages Functions ---------

def msg_box_info(msg_for_user=""):
    """
    Args:
        msg_for_user (str): [description]

    Returns:
        [bool]: [status]
    """
    return messages.msg_box_info(msg_for_user)
# [status]

def msg_count_down(msg_for_user="", default_time=5):
    """
    Args:
        msg_for_user (str): [description]
        default_time (int, optional): [description]. Defaults to 5.
    Returns:
        [bool]: [status]
    """
    return messages.msg_count_down(msg_for_user, default_time)
# [status]

# ---------  Messages Functions Ends ---------

# ---------  Mouse Functions ---------


def mouse_click(x='5', y='5', left_or_right="left", no_of_clicks=1, type_of_movement="abs"):
    """Clicks at the given X Y Co-ordinates on the screen using single / double / triple click(s). Default clicks on current position.
    Args:
        x (int): x-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        y (int): y-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        left_or_right (str, optional): Which mouse button.
        Eg: right or left, Defaults: left.
        no_of_click (int, optional): Number of times specified mouse button to be clicked.
        Eg: 1 or 2, Max 3. Defaults: 1.
        type_of_movement (str, optional): Type of movement.
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return mouse.mouse_click(x, y, left_or_right, no_of_clicks, type_of_movement)


def mouse_search_snip_return_coordinates_x_y(img="", wait=180):
    """Searches the given image on the screen and returns its center of X Y co-ordinates.
    Args:
        img (str, optional): Path of the image.
        Eg: D:\Files\Image.png, Defaults to "".
        wait (int, optional): Time you want to wait while program searches for image repeatably.
        Eg: 10 or 100 Defaults to 180.
    Returns: [status,data]
        bool: If function is failed returns False.
        tuple (x, y): Image Center co-ordinates.
    """
    return mouse.mouse_search_snip_return_coordinates_x_y(img, wait)


# ---------  Mouse Functions Ends ---------


# ---------  Keyboard Functions ---------

def key_press(key_1='', key_2='', key_3='', write_to_window=""):
    """Emulates the given keystrokes.
    Args:
        key_1 (str, optional): Enter the 1st key
        Eg: ctrl or shift. Defaults to ''.
        key_2 (str, optional): Enter the 2nd key in combination.
        Eg: alt or A. Defaults to ''.
        key_3 (str, optional): Enter the 3rd key in combination.
        Eg: del or tab. Defaults to ''.
        write_to_window (str, optional): (Only in Windows) Name of Window you want to activate. Defaults to "".
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return keyboard.key_press(key_1, key_2, key_3, write_to_window)


def key_write_enter(text_to_write="Clointfusion is awesome", write_to_window="", key="e"):
    """Writes/Types the given text.
    Args:
        text_to_write (str, optional): Text you wanted to type
        Eg: ClointFusion is awesone. Defaults to "".
        write_to_window (str, optional): (Only in Windows) Name of Window you want to activate
        Eg: Notepad. Defaults to "".
        key (str, optional): Press Enter key after typing.
        Eg: t for tab. Defaults to e
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return keyboard.key_write_enter(text_to_write, write_to_window, key)


def key_hit_enter(write_to_window=""):
    """Enter key will be pressed once.
    Args:
        write_to_window (str, optional): (Only in Windows)Name of Window you want to activate.
        Eg: Notepad. Defaults to "".
    Returns:[status]
        bool: Whether the function is successful or failed.
    """
    return keyboard.key_hit_enter(write_to_window)


# --------- Keyboard Functions Ends ---------


# ---------  Browser Functions ---------

ChromeBrowser = chrome.ChromeBrowser

# ---------  Browser Functions Ends ---------


# ---------  Folder Functions Starts ---------

def folder_read_text_file(txt_file_path=""):
    """
    Reads from a given text file and returns entire contents as a single list
    Args:
        txt_file_path (str, optional): Path of the text file.
        Eg: D:\Files\Text.txt, Defaults to "".
    Returns: [status,data]
        bool: If function is failed returns False.
        list: Text file contents.
    """
    return folder.folder_read_text_file(txt_file_path)


def folder_write_text_file(txt_file_path="", contents=""):
    """
    Writes given contents to a text file
    Args:
        txt_file_path (str, optional): Path of the text file.
        Eg: D:\Files\Text.txt, Defaults to "".
        contents (str, optional): Text you want to write to the text file.
        Eg: ClointFusion is awesone. Defaults to "".
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return folder.folder_write_text_file(txt_file_path, contents)


def folder_create(strFolderPath=""):
    """
    Creates a folder at the given path
    Args:
        strFolderPath (str, optional): Path of the folder.
        Eg: D:\Files\Text.txt, Defaults to "".
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return folder.folder_create(strFolderPath)


def folder_create_text_file(textFolderPath="", txtFileName=""):
    """
    Creates a text file at the given path
    Args:
        textFolderPath (str, optional): Path of the folder.
        Eg: D:\Files\Text.txt, Defaults to "".
        txtFileName (str, optional): Name of the text file.
        Eg: Text.txt, Defaults to "".
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return folder.folder_create_text_file(textFolderPath, txtFileName)


def folder_get_all_filenames_as_list(strFolderPath="", extension='all'):
    """
    Get all the files of the given folder in a list.
    Parameters:
        strFolderPath  (str) : Location of the folder.
        extension      (str) : extention of the file. by default all the files will be listed regardless of the extension.
    returns: [status,data]
        allFilesOfaFolderAsLst (List) : all the file names as a list.
    """
    return folder.folder_get_all_filenames_as_list(strFolderPath, extension)


def folder_delete_all_files(fullPathOfTheFolder="", file_extension_without_dot="all", print_status=True):
    """
    Deletes all the files of the given folder
    Parameters:
        fullPathOfTheFolder  (str) : Location of the folder.
        extension            (str) : extension of the file. by default all the files will be deleted inside the given folder
                                    regardless of the extension.
    returns:[status]
        bool: Whether the function is successful or failed.
    """
    return folder.folder_delete_all_files(fullPathOfTheFolder, file_extension_without_dot, print_status)


def file_rename(old_file_path='', new_file_name='', print_status=True):
    '''
    Renames the given file name to new file name with same extension
    Args:
        old_file_path (str, optional): Path of the file.
        Eg: D:\Files\Text.txt, Defaults to "".
        new_file_name (str, optional): New name of the file.
        Eg: Text.txt, Defaults to "".
        print_status (bool, optional): Whether to print the status of the function. Defaults to True.
    Returns: [status]
        bool: Whether the function is successful or failed.
    '''
    return folder.file_rename(old_file_path, new_file_name, print_status)


def file_get_json_details(path_of_json_file='', section=''):
    '''
    Returns all the details of the given section in a dictionary
    Args:
        path_of_json_file (str, optional): Path of the json file.
        Eg: D:\Files\Text.txt, Defaults to "".
        section (str, optional): Section of the json file.
        Eg: Text.txt, Defaults to "".
    Returns: [status,data]
        bool: Whether the function is successful or failed.
        data: Data of the given section in a dictionary.
    '''
    return folder.file_get_json_details(path_of_json_file, section)

# ---------  Folder Functions Ends ---------


# ---------  Window Operations Functions ---------

def windows_show_desktop():
    """
    Minimizes all the applications and shows Desktop.
    Returns:
        [status:bool]
    """
    return windows.window_show_desktop()


def windows_launch_app(pathOfExeFile=""):
    """Launches any exe or batch file or excel file etc.
    Args:
        pathOfExeFile (str, optional): Location of the file with extension
        Eg: Notepad, TextEdit. Defaults to "".
    Returns [status]
    """
    return windows.launch_any_exe_bat_application(pathOfExeFile)


def window_get_active_window():
    """
    Returns the active window title.
    Returns : [status,data]
    """
    return windows.window_get_active_window()


def window_activate_window(window_title=''):
    """
    Activates the given window.
    """

    return windows.window_activate_window(window_title)


def window_get_all_opened_titles_windows():
    """
    Gives the title of all the existing (open) windows.
    Returns: [status,data]
        allTitles_lst  (list) : returns all the titles of the window as list.
    """
    return windows.window_get_all_opened_titles_windows()


def window_restore_windows(windowName=""):
    """
    Restores the given window.
    Args:
        windowName (str, optional): Name of the window you want to restore.
        Eg: Notepad. Defaults to "".
    Returns: [status]
    """
    return windows.window_restore_windows(windowName)


def window_activate_and_maximize_windows(windowName=""):
    """
    Activates and maximizes the desired window.
    Parameters:
        windowName  (str) : Name of the window to maximize.
    Returns: [status]
    """
    return windows.window_activate_and_maximize_windows(windowName)


def window_minimize_windows(windowName=""):
    """
    Activates and minimizes the desired window.
    Parameters:
        windowName  (str) : Name of the window to miniimize.
    Returns: [status]
    """
    return windows.window_minimize_windows(windowName)


def window_close_windows(windowName=""):
    """
    Close the desired window.
    Parameters:
        windowName  (str) : Name of the window to close.
    """
    return windows.window_close_windows(windowName)


# ---------  Window Operations Functions Ends ---------


# ---------  String Functions ---------

def string_extract_only_alphabets(inputString=""):
    """
    Returns only alphabets from given input string
    Args:
        inputString (str, optional): Input string. Defaults to "".
    Returns: [status,data]
        bool: Whether the function is successful or failed.
        data: Only alphabets from given input string.
    """
    return string.string_extract_only_alphabets(inputString)


def string_extract_only_numbers(inputString=""):
    """
    Returns only numbers from given input string
    Args:
        inputString (str, optional): Input string. Defaults to "".
    Returns: [status,data]
        bool: Whether the function is successful or failed.
        data: Only numbers from given input string.
    """
    return string.string_extract_only_numbers(inputString)


def string_remove_special_characters(inputStr=""):
    """
    Removes all the special character.
    Parameters:
        inputStr  (str) : string for removing all the special character in it.
    Returns : [status,data]
        outputStr (str) : returns the alphanumeric string
    """

    return string.string_remove_special_characters(inputStr)

# ---------  String Functions Ends ---------


# --------- Voice Interface ---------

def text_to_speech(audio, show=True):
    """
    Text to Speech using Google's Generic API
    Args:
        audio (str): Text to be converted to speech.
        show (bool, optional): Whether to show the audio. Defaults to True.
    Returns: [status]
        bool: Whether the function is successful or failed.
    """
    return voice.text_to_speech(audio, show)


def speech_to_text():
    """
    Speech to Text using Google's Generic API
    Returns: [status,data]
        bool: Whether the function is successful or failed.
        data: Text converted from speech.
    """
    return voice.speech_to_text()

# --------- Voice Interface Ends ---------


# --------- API Functions ---------

#     ---- OCR Function ----

def image_to_text(img_path=""):
    """
    Reads the text from the image.
    Args:
        img_path (str, optional): Path of the image.
        Eg: D:\Files\Image.png, Defaults to "".
    Returns: [status,data]
        bool: If function is failed returns False.
        str: Text from image.
    """
    return utility.image_to_text(img_path)

# --------- API Functions Ends ---------