import os
import datetime
import customtkinter
import requests


app = customtkinter.CTk()
entry = customtkinter.CTkEntry(app, placeholder_text="Entry")

def main():
    customtkinter.set_appearance_mode("system")
    app.geometry("400x400")
    app.title("Realtime")
    label = customtkinter.CTkLabel(app, text=f"Welcome, {os.getlogin()}.\nToday is {datetime.datetime.today().date()}")
    button = customtkinter.CTkButton(app, text="Get Weather", command=button_event)
    label.pack()
    entry.pack()
    button.pack()
    app.mainloop()

def button_event():
    print(entry.get())

    response = requests.put('http://api.weatherapi.com/v1/current.json', data={'key': 'API_KEY_HERE', 'q': f'{entry.get()}'})
    city = customtkinter.CTkLabel(app, text=f"City: {response.json()['location']['name']}", fg_color="transparent")
    state = customtkinter.CTkLabel(app, text=f"State: {response.json()['location']['region']}", fg_color="transparent")
    country = customtkinter.CTkLabel(app, text=f"Country: {response.json()['location']['country']}", fg_color="transparent")
    temperature = customtkinter.CTkLabel(app, text=f"Temperature: {response.json()['current']['temp_c']}", fg_color="transparent")
    condition = customtkinter.CTkLabel(app, text=f"Condition: {response.json()['current']['condition']['text']}", fg_color="transparent")
    city.pack()
    state.pack()
    country.pack()
    temperature.pack()
    condition.pack()

main()
