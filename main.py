from PIL import Image,ImageFont,ImageDraw
import matplotlib.pyplot as plt
import tkinter as tk

window=tk.Tk()
window.title("Photo Watermark")
window.geometry("700x500")

window.mainloop()

image = Image.open("lioness_1.jpg")

# image.show()
# plt.imshow(image)
# plt.title("Lioness")
# plt.show()

watermark_image=image.copy()
draw=ImageDraw.Draw(watermark_image)
width,height=image.size


text=input("Enter the text value for watermark: ")
font_size=int(input("Enter the font size for the text to show up(px): "))
x_value=int(input(f"Enter the location of the text in x axis,range is ({font_size*len(text)//4},{width-font_size//4*len(text)}):"))
y_value=int(input(f"Enter the location of the text in y axis,range is (0,{height-font_size//2}):"))
font = ImageFont.truetype("arial.ttf", font_size)

# Watermarking image through pyplot
# draw.text((x_value,y_value),text,fill=(220, 0, 0), font=font, anchor='ms')
# plt.title(text.title())
# plt.imshow(watermark_image)
# plt.show()
