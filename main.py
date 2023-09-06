import requests
import tkinter as tk
from tkinter import ttk,messagebox
import time

def fetch_prayer_times(city,country):
  url = f' http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2'

  try:
    response= requests.get(url)
    info = response.json()
    if "data" in info:
      timings = info['data']['timings']
      return timings
    else:
      return messagebox.showerror("Error","Not found")
  except Exception as e:
    return f'unexcepected error {e}'

def gui_fetch_prayer_times():
  city = cit_entry.get()
  country = country_entry.get()

  if city and country:
    times= fetch_prayer_times(city,country)
    for name, tim in times.items():
      t = time.strptime(tim ,'%H:%M')
      tim12 = time.strftime("%I:%M %p",t)
      result.insert(tk.END,f'{name} : {tim12}')
  else:
    messagebox.showerror("Error","Unable to fetch")


app  = tk.Tk()
app.title("Prayer Times")
frame = ttk.Frame(app,padding="20")
frame.grid(row =0 , column=0)
city_label = ttk.Label(frame,text = 'City')
city_label.grid(row= 0 , column= 0,pady=5)
cit_entry = ttk.Entry(frame,width=20)
cit_entry.grid(row= 0 , column= 1,pady=5)

country_label = ttk.Label(frame,text = 'Country')
country_label.grid(row= 1 , column= 0,pady=5)
country_entry = ttk.Entry(frame,width=20)
country_entry.grid(row= 1 , column= 1,pady=5)

fetch_btn = ttk.Button(frame, text='get Prayer Times',
command = gui_fetch_prayer_times)
fetch_btn.grid(row=2,column=0,columnspan=2)

result = tk.Listbox(frame,height = 11, width =30)
result.grid(row = 3 , column=0, columnspan =2 , pady = 5)

app.mainloop()