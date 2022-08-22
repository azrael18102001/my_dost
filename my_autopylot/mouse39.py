from my_autopylot.CrashHandler import report_error


def mouse_click(x='', y='', left_or_right="left", no_of_clicks=1, type_of_movement="abs"):

    # Description:
    """
    Description:
        Clicks at the given X Y Co-ordinates on the screen using single / double / triple click(s). Default clicks on current position.

    Args:
        x (int): x-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        y (int): y-coordinate on screen.
        Eg: 369 or 435, Defaults: ''.
        left_or_right (str, optional): Which mouse button.
        Eg: right or left, Defaults: left.
        no_of_click (int, optional): Number of times specified mouse button to be clicked.
        Eg: 1 or 2, Max 3. Defaults: 1.

    Returns:
        [status]
        status (bool): Whether the function is successful or failed.
    """

    # import section
    import pywinauto as pwa
    import win32api

    # Response section
    error = None
    status = False
    # data = None
    not_default = True

    try:

        if (x == "" and y == ""):
            x, y = win32api.GetCursorPos()
            not_default = False
        if (type_of_movement == "abs" or type_of_movement == "rel"):
            x, y = int(x), int(y)
        else:
            raise Exception("Please check the type of movement.")

        if x and y:
            if type_of_movement == "abs":
                x, y = int(x), int(y)
            elif type_of_movement == "rel" and not_default:
                current_x, current_y = win32api.GetCursorPos()
                x, y = int(x), int(y)
                current_x, current_y = int(current_x), int(current_y)
                x, y = int(current_x + x), int(current_y + y)

            if no_of_clicks == 1:
                pwa.mouse.click(coords=(x, y), button=left_or_right)
            elif no_of_clicks == 2:
                pwa.mouse.double_click(coords=(x, y), button=left_or_right)
            else:
                for i in range(no_of_clicks):
                    pwa.mouse.click(coords=(x, y), button=left_or_right)

            status = True
        else:
            raise Exception("X and Y co-ordinates are required.")

    except Exception as ex:
        report_error(ex)
        error = ex

    else:
        status = True
    finally:
        if error is not None:
            raise Exception(error)
        return [status]

def mouse_search_snip_return_coordinates_x_y(img="", wait=10):
    """
    Description:
        Searches for the given image on the screen and returns the X and Y co-ordinates.
    Args:
        img (str): Image to search for.
        wait (int): Seconds to wait while performing action. Defaults to 10.
    Returns:
        [status, data]
        status: Whether the function is successful or failed. 
        data: X and Y co-ordinates of the image.
    """

    # import section
    import time
    import pyscreeze as ps

    # Response section
    error = None
    status = False
    data = None
    i = 0

    try:
        if not img:
            raise Exception("Image path is required.")
        pos = ps.locateCenterOnScreen(image=img, minSearchTime=wait)
        # while pos != None or i < int(wait):
        #     time.sleep(0.2)
        #     pos = ps.locateCenterOnScreen(img)
        #     i += 1
        if pos:
            data = (pos[0], pos[1])

    except Exception as ex:
        report_error(ex)
        error = ex
    else:
        if pos:
            status = True
        else:
            status = False
    finally:
        if error is not None:
            raise Exception(error)
        return [status, data]
