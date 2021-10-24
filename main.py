from tkinter import *
from speedtest import Speedtest    # Will be installed using "pip install speedtest-cli" on terminal

# Creating a canvas
root = Tk()
root.title("Speed Test")
root.geometry('600x700')
root.resizable(False, False)

# Background image
bg_image = PhotoImage(file='icon.png')
bg = Label(image=bg_image).grid(row=0, column=0, padx=0, pady=5)

fg = '#040807'
bg1 = '#74aba2'

# Will be used to display the speed
down_lab = Label(root, text='', fg=fg, font=('Helvetica', 10, 'bold'))
down_lab.grid(row=2, column=0, padx=5, pady=5)
upload_lab = Label(root, text='', fg=fg, font=('Helvetica', 10, 'bold'))
upload_lab.grid(row=3, column=0, padx=5, pady=5)


# Speed is calculated here
def get_speedtest():
    s = Speedtest()
    download = s.download()     # Getting download speed
    upload = s.upload()     # Getting upload speed
    download_speed = round(download/(10**6), 2)     # Mbps
    upload_speed = round(upload/(10**6), 2)     # Mbps
    down_lab.config(text='Your Download Speed is = ' + str(download_speed) + "Mbps")
    upload_lab.config(text='Your Upload Speed is = ' + str(upload_speed) + "Mbps")


Button(root, text='Begin Test', font=('Arial', 10, 'bold'), command=get_speedtest(), bg=bg1).grid(row=1, column=0, padx=5, pady=10)
root.mainloop()
