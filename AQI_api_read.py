from tkinter import *
from PIL import ImageTk, Image
import json
import requests

font= "Helvetica"


# https://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=22.5970&longitude=88.4177&distance=25&API_KEY=800237A1-23C2-416D-9629-33CD6F1FD4C1


root=Tk()
root.title("Air Quality Monitoring")
root.geometry("400x100")

def background():
    bg=''
    if (AQI<=50):
        bg='#7deb34'
    elif(AQI<=100):
        bg='#34ebb7'
    elif(AQI<=200):
        bg='#eb9234'
    elif(AQI<=300):
        bg='#eb345b'
    elif(AQI>300):
        bg='#eb3434'
    else:
        bg='#c2b2b2'
    return bg



try:
    API_request= requests.get("https://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=22.5970&longitude=88.4177&distance=25&API_KEY=800237A1-23C2-416D-9629-33CD6F1FD4C1")
    API_content = json.loads(API_request.content)
    city= API_content[0]['ReportingArea']
    AQI= API_content[0]['AQI']
    Category= API_content[0]['Category']['Name']

except Exception as e:
    API_content = "error"

lable=Label(root, text="Location: "+ city + "\nAir quality: " + str(AQI) + "\nCategory : "+ Category, font=font, bg=background())
lable.pack(expand=True, fill='both')

root.mainloop()