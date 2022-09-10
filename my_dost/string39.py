
def string_extract_only_alphabets(inputString=""):

    # Description:
    """
    Description:
        Returns only alphabets from given input string
    Args:
        inputString: A string representing the name of the module to be installed.
    Returns:
        A boolean representing whether the module was installed successfully.
    """

    # import section
    from my_dost.CrashHandler import report_error
    # Response section
    error = None
    data = None

    data = ''.join(e for e in inputString if e.isalpha())

    # If the function returns a value, it should be assigned to the data variable.
    # data = value

    return data


def string_extract_only_numbers(inputString=""):
    # Description:
    """
    Description:
        Returns only numbers from given input string
    Args:
        inputString: A string representing the name of the module to be installed.
    Returns:
        A boolean representing whether the module was installed successfully.
    """

    # import section
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    data = None


    data = ''.join(e for e in inputString if e.isnumeric())

        # If the function returns a value, it should be assigned to the data variable.
        # data = value

    
    return data


def string_remove_special_characters(inputStr=""):

    # Description:
    """
    Description:
        Removes all the special character.
    Args:
        inputStr: A string representing the name of the module to be installed.
    Returns:
        Status - A boolean representing whether the module was installed successfully.
    """

    # import section
    from my_dost.CrashHandler import report_error

    # Response section
    error = None
    data = None

    data = ''.join(e for e in inputStr if e.isalnum())

        # If the function returns a value, it should be assigned to the data variable.
        # data = value
    return data
