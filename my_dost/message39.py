
# import string


def msg_box_info(msg_for_user=""):
    """
    Description:
        Display a message box with information.

    Args:
        msg_for_user (str): [description]

    Returns:
        [status]
        Status (bool) : Whether the message box was displayed or not.
    """
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    tk.messagebox.showinfo('PyBOTs', msg_for_user, parent=root)
    root.destroy()
