import win32clipboard
from my_dost.CrashHandler import report_error


def pause_program(seconds="5"):

    # Description:
    """
    Description:
        Stops the program for given seconds
    Args:
        seconds (str): seconds to be paused
    Returns:
        Status (bool) - True if success, False if failure
    """

    # import section
    import time

    # Response section
    error = None
    
    
    seconds = int(seconds)
    time.sleep(seconds)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value


def api_request(url: str, method='GET', body: dict = None, headers: dict = None):
    """
    Description:
        Function used to send generic api request

    Args : url (str): url of the api
        method (str): method of the api request
        data (dict): data to be sent in the request
        headers (dict): headers to be sent in the request

    Returns :
        Status (bool) - True if success, False if failure

    """
    import requests
    import json

    # Response section
    error = None
    data = None

    if headers is None:
        headers = {"charset": "utf-8", "Content-Type": "application/json"}

    if method == 'GET':
        response = requests.get(
            url, headers=headers, params=body)
    elif method == 'POST':
        response = requests.post(
            url, data=json.dumps(body), headers=json.dumps(headers))
    elif method == 'PUT':
        response = requests.put(
            url, data=json.dumps(body), headers=json.dumps(headers))
    elif method == 'DELETE':
        response = requests.delete(
            url, data=json.dumps(body), headers=json.dumps(headers))
    else:
        raise Exception("Invalid method")
    if response.status_code in [200, 201, 202, 203, 204]:
        data = response.json()
    else:
        raise Exception(response.text)
    return data


# api request todos free api
# print(api_request("https://todos.free.beeceptor.com/todos", body='', headers={}))
# print(api_request(url='https://todos.free.beeceptor.com/todos'))


def clipboard_set_data(data, format_id=win32clipboard.CF_UNICODETEXT):
    """
    Description:
        Set data to clipboard
    Args:
        data: data to be set to clipboard
        format_id: format of data
    Returns:
        Status (bool) - True if success, False if failure
    """

    # Import Section
    from my_dost.CrashHandler import report_error
    import win32clipboard

    # Response section
    error = None

    # Logic Section
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(format_id, data)
    finally:
        if error is not None:
            raise Exception(error)
        win32clipboard.CloseClipboard()



def GetClipboardFormats():
    import win32clipboard

    win32clipboard.OpenClipboard()
    available_formats = []
    current_format = 0
    while True:
        current_format = win32clipboard.EnumClipboardFormats(current_format)
        if not current_format:
            break
        available_formats.append(current_format)
    win32clipboard.CloseClipboard()
    return available_formats


def clipboard_get_data(format_id=win32clipboard.CF_UNICODETEXT):
    """
    Description:
        Get data from clipboard
    Returns:
        Status (bool) - True if success, False if failure
    """

    # Import Section
    from my_dost.CrashHandler import report_error
    import win32clipboard

    # Response section
    error = None
    data = None

    # Logic Section

    if format_id not in GetClipboardFormats():
        raise RuntimeError("That format is not available")
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(format_id)
    win32clipboard.CloseClipboard()

    return data


def clear_output():
    """
    Description:
        Clears Python Interpreter Terminal Window Screen
    Returns:
        Status (bool) - True if success, False if failure
    """
    # Import Section
    import os

    # Response section
    error = None

    # Logic Section
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def install_module(module_name):
    if module_name != "my_dost":
        import subprocess
        import sys
        subprocess.call([sys.executable, "-m", "pip",
                        "install", module_name])


def uninstall_module(module_name):
    if module_name != "my_dost":
        import subprocess
        import sys
        subprocess.call([sys.executable, "-m", "pip",
                        "uninstall", "-y", module_name])
    else:
        raise Exception(
            "You cannot uninstall my_dost from here.")


def image_to_text(image_path):
    """
    """
    # Imports
    from PIL import Image
    import pytesseract
    from my_dost.CrashHandler import report_error

    # Response section
    data = None
    
    # Logic section
    image = Image.open(image_path)
    data = pytesseract.image_to_string(image)

    return data
