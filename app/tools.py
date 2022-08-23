import os


def get_current_dir():
    c_dir = os.getcwd()
    print("current direction is:" + c_dir)
    return c_dir


def change_dir(path):
    return os.chdir(path)


def get_file_list(path):
    files = os.listdir(path)
    pdfs = []
    try:
        for i in files:
            file_name, extension_name = os.path.splitext(i)
            if extension_name == '.pdf':
                pdfs.append(path+i)
            else:
                continue
    except:
        print("error")
    return pdfs

def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')