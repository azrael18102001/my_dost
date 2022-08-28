
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
    try:
        if msg_for_user:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.attributes('-topmost', True)
            root.withdraw()
            tk.messagebox.showinfo('PyBOTs', msg_for_user, parent=root)
            root.destroy()
        else:
            from my_dost.CrashHandler import text_to_speech_error
            text_to_speech_error("Message cannot be empty")

    except Exception as ex:
        from my_dost.CrashHandler import report_error
        report_error(ex)
        return [False]
    else:
        return [True]
