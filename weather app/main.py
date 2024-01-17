from tkinter import *
import requests
from PIL import Image, ImageTk

# key: 88437998a8df4b4aedd510493e4bffa1
# API url: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
root = Tk()
root.title("Weather App")
root.geometry("600x500")


def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        # final_str = 'City:%s\nCondition:%s\nTemprature:%s' % (city, condition, temp)
        final_str = f"City:{city}\nCondition:{condition}\nTemprature:{temp}"
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str


def get_weather(city):
    weather_key = 'a4d1c285247579bce9d8a040947f8009'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    # print(response.json())
    weather = response.json()

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])

    result['text'] = format_response(weather)
    # icon_name=weather['weather'][0]['icon']
    print(weather['weather'][0]['icon'])
#     open_image(icon_name)
#
# def open_image(icon_name):
#     size = int(frame_two.winfo_height()*0.25)
#     img = PhotoImage(Image.open('./img/+icon+.png').resize((size, size)))
#     weather_icon.delete('all')
#     weather_icon.create_image(0,0,anchor='nw', image=img)
#     weather_icon.image=img


img = Image.open('./bg.png')
img = img.resize((600, 500), Image.LANCZOS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

frame_one = Frame(bg_lbl, bg="light yellow", bd=5)
frame_one.place(x=80, y=60, width=480, height=50)

heading_title = Label(bg_lbl, text='Earth including over 200,000 cities!', fg="red", bg="light blue",
                      font="comicsans 18 bold")
heading_title.place(x=80, y=18)
txt_box = Entry(frame_one, font="comicsans 25", width=17)
txt_box.grid(row=0, column=0, sticky="w")

btn = Button(frame_one, text="get weather", fg="green", font="comicsans 16 bold",
             command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two = Frame(bg_lbl, bg="light yellow", bd=5)
frame_two.place(x=80, y=130, width=480, height=300)

result = Label(frame_two, font=40, bg='white', justify='left', anchor='nw')
result.place(relwidth=1, relheight=1)

weather_icon = Canvas(result, bg="white", bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
