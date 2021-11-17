from tkinter import *
from pytube import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from PIL import ImageTk, Image


def download_video():
    path_to_save = askdirectory()
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    showinfo("Message", "Download Started ...Plase Wait...!!")
    video.download(output_path=path_to_save)
    label_2 = Label(root, text='Downloaded Sucessfully!!!', bg='yellow', fg='black', font='arial 15 bold')
    label_2.place(x=450, y=550)
    entry_1.delete(0, END)
    showinfo("Message", "File has been downloded...!")


def download_lq_video():
    path_to_save = askdirectory()
    url = YouTube(str(link.get()))
    video = url.streams.get_lowest_resolution()
    showinfo("Message", "Download Started ...Plase Wait...!!")
    video.download(output_path=path_to_save)
    label_2 = Label(root, text='Downloaded Sucessfully!!!', bg='yellow', fg='black', font='arial 15 bold')
    label_2.place(x=450, y=550)
    entry_1.delete(0, END)
    showinfo("Message", "File has been downloded...!")


def only__audio():
    path_to_save = askdirectory()
    url = YouTube(str(link.get()))
    video = url.streams.get_audio_only()
    video.download(output_path=path_to_save)
    label_2 = Label(root, text='Downloaded Sucessfully!!!', bg='yellow', fg='black', font='arial 15 bold')
    label_2.place(x=450, y=550)
    showinfo("Message", "File has been downloded...!")


def instructions():
    top = Tk()
    top.title('Instructions')
    top.geometry('400x250')
    top.iconbitmap("YouTubeIco.ico")

    def back():
        top.destroy()

    lbl_1 = Label(top, text='Download HQ == Downloads High Resolution', font='arial 10 bold')
    lbl_1.place(x=10, y=20)

    lbl_2 = Label(top, text='Download LQ == Downloads Low Resolution', font='arial 10 bold')
    lbl_2.place(x=10, y=45)

    lbl_3 = Label(top, text='Only Audio     == Downloads only audio', font='arial 10 bold')
    lbl_3.place(x=10, y=70)

    lbl_4 = Label(top, text='Exit                == Exit the appliction', font='arial 10 bold')
    lbl_4.place(x=10, y=90)

    btn_back = Button(top, text='Back', font='Helvetica 12 bold', bg='orange', fg='white', command=back)
    btn_back.place(x=300, y=180)


def exit():
    root.destroy()


root = Tk()
root.geometry("1100x550")
root.title("YouTube Downloader")
root.iconbitmap("YouTubeIco.ico")
root.configure(bg='white')

img = ImageTk.PhotoImage(Image.open("1220pink_img.jpg"))
lbl_bgi = Label(root, image=img)
lbl_bgi.pack()
link = StringVar()

entry_1 = Entry(root, width=53, font='arial 12 bold', bg="white", textvariable=link)
entry_1.place(x=320, y=70)

label_1 = Label(root, text='Enter Url :', bg="sky blue", fg='black', font='arial 15 bold')
label_1.place(x=140, y=70)

label_3 = Label(root, text='#Sist 2020-24..!!!', bg='white', fg='red', font='arial 15 bold')
label_3.place(x=100, y=480)

label_4 = Label(root, text='(High Resolution)', bg='white', fg='black', font='arial 15 bold')
label_4.place(x=650, y=140)

label_5 = Label(root, text='(Low Resolution)', bg='white', fg='black', font='arial 15 bold')
label_5.place(x=650, y=190)

label_6 = Label(root, text="\U0001F642" , bg="#FFCCFF", fg="black", font='arial 20 bold')
label_6.place(x=210, y=196)

label_7 = Label(root, text="Hello kirru", bg="#FFCCFF", fg="black", font='arial 15 bold')
label_7.place(x=100, y=200)

button_1 = Button(root, width=10, height=1, font='Helvetica 12 bold', text='Download HQ', command=download_video,
                  bg='blue', fg='white')
button_1.place(x=510, y=140)

button_2 = Button(root, width=8, height=1, font='Helvetica 12 bold', text='Only Audio', command=only__audio,
                  bg='blue', fg='white')
button_2.place(x=300, y=300)

button_3 = Button(root, width=8, height=1, font='Helvetica 12 bold', text='Exit', command=exit,
                  bg='green', fg='white')
button_3.place(x=780, y=300)

button_4 = Button(root, width=10, height=1, font='Helvetica 12 bold', text='Download LQ', command=download_lq_video,
                  bg='blue', fg='white')
button_4.place(x=510, y=190)

button_5 = Button(root, width=10, height=1, font='Helvetica 12 bold', text='Instructions', command=instructions,
                  bg='green', fg='white')
button_5.place(x=510, y=400)

root.mainloop()



