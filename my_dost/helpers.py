def get_media_type(file_path):
    import mimetypes
    mimetypes.init()
    mimestart = mimetypes.guess_type(file_path)[0]
    if mimestart != None:
        mimestart = mimestart.split('/')[0]
        if mimestart in ['audio', 'video', 'image']:
            return mimestart
    return None


# check if speaker is connected using pyaudio
def _is_speaker_available():
    try:
        import pyaudio
    except:
        from my_dost.CrashHandler import install_pyaudio
        install_pyaudio()
        import pyaudio

    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxInputChannels'] > 0:
            return True
    return False

# print(_is_speaker_available())
