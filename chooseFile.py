import tkinter.filedialog


def get_filename_list():
    filename_list = tkinter.filedialog.askopenfilenames()
    if len(filename_list) != 0:
        for filename in filename_list:
            print(filename)
    else:
        print("didn't choose")


def get_filename():
    filename = tkinter.filedialog.askopenfile()
    if filename is None:
        print("didn't choose")
    else:
        print(filename)


def choose_directory():
    name = tkinter.filedialog.askdirectory()
    print(name)


choose_directory()
