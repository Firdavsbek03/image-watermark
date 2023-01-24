from PIL import ImageTk,Image,ImageDraw,ImageFont
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
logo=None


def watermark(text_input,x_value,y_value,font_size,button2,image_name):
    written_value=text_input.get()
    global img
    image_copy = Image.open(image_name).copy()
    try:
        user_x_value=int(x_value.get())
        user_y_value=int(y_value.get())
        if len(written_value)==0:
            raise TypeError
        if not font_size.get():
            font_size=24
        else:
            font_size=int(font_size.get())
        draw = ImageDraw.Draw(image_copy)
        font = ImageFont.truetype("arial.ttf", font_size)
        draw.text((user_x_value,user_y_value),written_value,fill=(234, 246, 246),font=font)
        image_copy.save("images/best_file.jpg")
        img= ImageTk.PhotoImage(Image.open("images/best_file.jpg"))
        button2.config(image=img)
        if logo:
            logo_image=Image.open(logo_file_name).copy()
            # image watermark
            size = (80,80)
            # to keep the aspect ration in intact
            logo_image.thumbnail(size=size)
            img.paste(logo_image)
    except ValueError:
        showwarning(message="Please, enter proper coordinate values.")
    except TypeError:
        showwarning(message="Please, submit with a text for watermark.")


def upload_logo():
    global logo,logo_file_name
    file_types=[("Image Files","*.jpg")]
    logo_file_name=askopenfilename(filetypes=file_types)
    logo=ImageTk.PhotoImage(file=logo_file_name)


def upload_photo():
    global image
    file_types=[("Image Files","*.jpg")]
    file_name=askopenfilename(filetypes=file_types)
    image=ImageTk.PhotoImage(file=file_name)
    if image.height()>500:
        img_height=450
    else:
        img_height=image.height()
    button2 = tk.Button(window, image=image,height=img_height)
    button2.grid(row=3, column=1,pady=10)
    button_logo = tk.Button(window, text="Upload logo", font=("Arial", 14, 'bold'),command=upload_logo)
    button_logo.grid(row=4, column=1, pady=10)

    label1 = tk.Label(window, text="X value:", font=("san-serif", 14, ''))
    label1.grid(row=2, column=2, pady=10)
    label2 = tk.Label(window, text="Y value:", font=("san-serif", 14, ''))
    label2.grid(row=3, column=2, pady=10)

    x_value = tk.Entry(window, font=("Arial", 14, ''))
    x_value.grid(row=2, column=3, pady=10)
    y_value = tk.Entry(window, font=("Arial", 14, ''))
    y_value.grid(row=3, column=3, pady=10)
    label3 = tk.Label(window, text="Enter the text:", font=("san-serif", 14, ''))
    label3.grid(row=4, column=2, pady=10)
    text = tk.Entry(window, font=("Arial", 14, 'bold'))
    text.grid(row=4, column=3, pady=10)

    label4 = tk.Label(window, text="Enter font-size:", font=("san-serif", 14, ''))
    label4.grid(row=5, column=2, pady=10)
    font_size = tk.Entry(window, font=("Arial", 14, 'bold'))
    font_size.grid(row=5, column=3, pady=10)

    button3 = tk.Button(window, text=" Submit ", font=("Arial", 14, 'bold'),
                        command=lambda : watermark(text,x_value,y_value,font_size,button2,file_name))
    button3.grid(row=6, column=3)


window=tk.Tk()
window.title("Photo Watermark")
window.geometry("1000x750")
label=tk.Label(window,text="Upload a photo from your device",font=("Arial",18))
label.grid(row=1,columnspan=2,pady=10)
button=tk.Button(window,text="Upload Photo",font=("Arial",14,'bold'),command=upload_photo)
button.grid(row=2,column=1,pady=10)
window.mainloop()