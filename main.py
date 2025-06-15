import os
import customtkinter
import requests

def internet_connection():
    try:
        ping = requests.get('http://www.msftconnecttest.com/connecttest.txt', timeout=5)
        return ping.status_code == 200
    except:
        return False

app = customtkinter.CTk()
app.geometry("300x400")
app.title('Realtime v2')

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(padx=20, pady=20)
tabview.add("Main")
tabview.add("Settings")
tabview.set("Main")

request_entry = customtkinter.CTkEntry(master=tabview.tab("Main"), placeholder_text="Enter a Country or City.")
request_entry.pack(pady=10)

city_label = customtkinter.CTkLabel(tabview.tab("Main"), text="City: ", fg_color="transparent")
state_label = customtkinter.CTkLabel(tabview.tab("Main"), text="State: ", fg_color="transparent")
country_label = customtkinter.CTkLabel(tabview.tab("Main"), text="Country: ", fg_color="transparent")
temp_label = customtkinter.CTkLabel(tabview.tab("Main"), text="Temperature: ", fg_color="transparent")
condition_label = customtkinter.CTkLabel(tabview.tab("Main"), text="Condition: ", fg_color="transparent")

def button_request():
    if not internet_connection():
        city_label.configure(text="No Internet connection.")
        return

    query = request_entry.get()
    if not query:
        city_label.configure(text="Enter a location.")
        return

    try:
        response = requests.get(
            'http://api.weatherapi.com/v1/current.json',
            params={'key': 'API_KEY_HERE', 'q': query}
        )
        if response.status_code == 200:
            data = response.json()
            city_label.configure(text=f"City: {data['location']['name']}")
            state_label.configure(text=f"State: {data['location']['region']}")
            country_label.configure(text=f"Country: {data['location']['country']}")
            temp_label.configure(text=f"Temperature: {data['current']['temp_c']}°C")
            condition_label.configure(text=f"Condition: {data['current']['condition']['text']}")
        else:
            city_label.configure(text="Invalid location or API error.")
    except Exception as e:
        city_label.configure(text=f"Error {e}")

request_button = customtkinter.CTkButton(master=tabview.tab("Main"), command=button_request, text='Get Weather')
request_button.pack(pady=10)

optionmenu_var = customtkinter.StringVar(value="Dark")

def optionmenu_theme(choice):
    if choice == 'Dark':
        customtkinter.set_appearance_mode("dark")
    elif choice == 'Light':
        customtkinter.set_appearance_mode("light")
    else:
        customtkinter.set_appearance_mode("system")

optionmenu_name = customtkinter.CTkLabel(tabview.tab('Settings'), text='Application Theme')
optionmenu_name.pack()
optionmenu = customtkinter.CTkOptionMenu(tabview.tab('Settings'),values=["Dark", "Light", "System"],command=optionmenu_theme,variable=optionmenu_var)
optionmenu.pack()
city_label.pack()
state_label.pack()
country_label.pack()
temp_label.pack()
condition_label.pack()
app.mainloop()
