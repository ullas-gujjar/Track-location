import tkinter
import phonenumbers
from phonenumbers import geocoder, carrier
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import tkintermapview
from opencage.geocoder import OpenCageGeocode
from key import key  # Make sure you have a valid API key stored in 'key.py'

root = tkinter.Tk()
root.geometry("500x650")
root.title("Phone Number Tracker")

Label(root, text="Phone Number Tracker", font=("Helvetica", 16, "bold")).pack(pady=10)

number = Text(root, height=1)
number.pack(pady=5)

result = Text(root, height=10)
result.pack(pady=5)

def getResult():
    result.delete(1.0, END)
    num = number.get("1.0", "end-1c")
    
    try:
        num1 = phonenumbers.parse(num)
    except:
        messagebox.showerror("Error", "Number box is empty or the input is not valid!!")
        return
        
    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")

    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)

    if not results:
        messagebox.showerror("Error", "Could not fetch location details.")
        return

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    my_label = LabelFrame(root)
    my_label.pack(pady=10)

    map_widget = tkintermapview.TkinterMapView(my_label, width=450, height=300, corner_radius=0)
    map_widget.set_position(lat, lng)
    map_widget.set_marker(lat, lng, text="Phone Location")
    map_widget.set_zoom(10)
    map_widget.pack()

    adr = tkintermapview.convert_coordinates_to_address(lat, lng)

    result.insert(END, f"The country of this number is: {location}")
    result.insert(END, f"\nThe sim card of this number is: {service_provider}")
    result.insert(END, f"\nLatitude is: {lat}")
    result.insert(END, f"\nLongitude is: {lng}")
    
    if adr:
        result.insert(END, f"\nStreet Address is: {adr.street}")
        result.insert(END, f"\nCity Address is: {adr.city}")
        result.insert(END, f"\nPostal Code is: {adr.postal}")

style = Style()
style.configure("TButton", font=('calibri', 14, 'bold'), borderwidth='4')
style.map('TButton',
          foreground=[('active', '!disabled', 'green')],
          background=[('active', 'black')])

Button(root, text="Search", command=getResult).pack(pady=10)

root.mainloop()
