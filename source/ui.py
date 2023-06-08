import customtkinter
import pandas as pd
import numpy as np

path = '/Users/clara.rivadulla/Documents/UPC-MAI/SEL-PW3'
initial_CB = pd.read_csv(f"{path}/data/travel.csv")

holiday_types = initial_CB['holiday-type'].unique()
holiday_types = np.append(holiday_types, 'Other')

regions = initial_CB['region'].unique()
regions = np.append(regions, 'Other')

transportations = initial_CB['transportation'].unique()
transportations = np.append(transportations, 'Other')

months = initial_CB['season'].unique()

accomodations = initial_CB['accomodation'].unique()
accomodations = np.append(accomodations, 'Other')

hotels = initial_CB['hotel'].unique()
hotels = np.append(hotels, 'Other')

# If a new case is added to the case base,
# the variables must be updated as well
def updateCB():
    return None


app = customtkinter.CTk()
app.title("Travel Planner")
app.geometry("510x405")

def button_callback():

    print('Searching for a trip that matches your preferences...')

    selected_holiday_type = holidaymenu.get()
    if selected_holiday_type == "Other": selected_holiday_type = other_holiday.get()
    print(f'Holiday Type: {selected_holiday_type}')

    selected_price = slider.get()
    print(f'Maximum Price: {selected_price}')

    selected_num_pers = num_pers.get()
    if selected_num_pers == "": selected_num_pers = 2
    print(f'Number of persons: {selected_num_pers}')

    selected_region = regionmenu.get()
    if selected_region == "Other": selected_region = other_region.get()
    print(f'Region: {selected_region}')

    selected_transportation = transportationmenu.get()
    if selected_transportation == "Other": selected_transportation = other_transportation.get()
    print(f'Transportation: {selected_transportation}')

    selected_duration = duration.get()
    if selected_duration == "": selected_duration = 5
    print(f'Duration (in days): {selected_duration}')

    selected_month = monthmenu.get()
    print(f'Month: {selected_month}')

    selected_accomodation = accomodationmenu.get()
    if selected_accomodation == "Other": selected_accomodation = other_accomodation.get()
    print(f'Accomodation: {selected_accomodation}')

    selected_hotel = hotelmenu.get()
    if selected_hotel == "Other": selected_hotel = other_hotel.get()
    print(f'Hotel: {selected_hotel}')
    print()
    # TODO: Perform a search and show a possible trip
    return None

def slider_event(value):
    current_price.configure(text=f"{value}")

def holidaymenu_callback(choice):
    if choice == 'Other':
        other_holiday.grid(row=0, column=2, padx=0, pady=5)
        selected_holiday_type = other_holiday.get()
    else:
        other_holiday.grid_forget()


def regionmenu_callback(choice):
    if choice == 'Other':
        other_region.grid(row=3, column=2, padx=0, pady=5)
    else:
        other_region.grid_forget()

def transportationmenu_callback(choice):
    if choice == 'Other':
        other_transportation.grid(row=4, column=2, padx=0, pady=5)
    else:
        other_transportation.grid_forget()

def accomodationmenu_callback(choice):
    if choice == 'Other':
        other_accomodation.grid(row=7, column=2, padx=0, pady=5)
    else:
        other_accomodation.grid_forget()

def hotelmenu_callback(choice):
    if choice == 'Other':
        other_hotel.grid(row=8, column=2, padx=0, pady=5)
    else:
        other_hotel.grid_forget()

# HOLIDAY TYPE
holiday_label = customtkinter.CTkLabel(app, text="Holiday type:", fg_color="transparent")
holiday_label.grid(row=0, column=0, padx=10, pady=10)
holidaymenu = customtkinter.CTkOptionMenu(app, values=holiday_types,
                                         command=holidaymenu_callback)
holidaymenu.grid(row=0, column=1, padx=0, pady=10)
other_holiday = customtkinter.CTkEntry(app, placeholder_text="")

# PRICE
slider = customtkinter.CTkSlider(app, from_=0, to=10000, command=slider_event)
slider.set(0)
price_label = customtkinter.CTkLabel(app, text=f"Maximum price:", fg_color="transparent")
price_label.grid(row=1, column=0, padx=10, pady=5)
slider.grid(row=1, column=1, padx=0, pady=5)
current_price = customtkinter.CTkLabel(app, text=f"0", fg_color="transparent")
current_price.grid(row=1, column=2, padx=0, pady=5)

# NUMBER OF PERSONS
# TODO: Check that this input is a number
num_pers_label = customtkinter.CTkLabel(app, text="Number of persons:", fg_color="transparent")
num_pers_label.grid(row=2, column=0, padx=10, pady=5)
num_pers = customtkinter.CTkEntry(app, placeholder_text="2")
num_pers.grid(row=2, column=1, padx=0, pady=5)

# REGION
region_label = customtkinter.CTkLabel(app, text="Region:", fg_color="transparent")
region_label.grid(row=3, column=0, padx=10, pady=5)
regionmenu = customtkinter.CTkOptionMenu(app, values=regions,
                                         command=regionmenu_callback)
regionmenu.grid(row=3, column=1, padx=0, pady=5)
other_region = customtkinter.CTkEntry(app, placeholder_text="")

# TRANSPORTATION
transportation_label = customtkinter.CTkLabel(app, text="Transportation:", fg_color="transparent")
transportation_label.grid(row=4, column=0, padx=10, pady=5)
transportationmenu = customtkinter.CTkOptionMenu(app, values=transportations,
                                         command=transportationmenu_callback)
transportationmenu.grid(row=4, column=1, padx=0, pady=5)
other_transportation = customtkinter.CTkEntry(app, placeholder_text="")

# DURATION
duration_label = customtkinter.CTkLabel(app, text="Duration in days:", fg_color="transparent")
duration_label.grid(row=5, column=0, padx=10, pady=5)
duration = customtkinter.CTkEntry(app, placeholder_text="5")
duration.grid(row=5, column=1, padx=0, pady=5)

# MONTH
month_label = customtkinter.CTkLabel(app, text="Month:", fg_color="transparent")
month_label.grid(row=6, column=0, padx=10, pady=5)
monthmenu = customtkinter.CTkOptionMenu(app, values=months)
monthmenu.grid(row=6, column=1, padx=0, pady=5)
month_region = customtkinter.CTkEntry(app, placeholder_text="")

# ACCOMODATION
accomodation_label = customtkinter.CTkLabel(app, text="Accomodation:", fg_color="transparent")
accomodation_label.grid(row=7, column=0, padx=10, pady=5)
accomodationmenu = customtkinter.CTkOptionMenu(app, values=accomodations,
                                         command=accomodationmenu_callback)
accomodationmenu.grid(row=7, column=1, padx=0, pady=5)
other_accomodation = customtkinter.CTkEntry(app, placeholder_text="")

# HOTEL
hotel_label = customtkinter.CTkLabel(app, text="Hotel:", fg_color="transparent")
hotel_label.grid(row=8, column=0, padx=10, pady=5)
hotelmenu = customtkinter.CTkOptionMenu(app, values=hotels,
                                         command=hotelmenu_callback)
hotelmenu.grid(row=8, column=1, padx=0, pady=5)
other_hotel = customtkinter.CTkEntry(app, placeholder_text="")

button = customtkinter.CTkButton(app, text="Find me a trip", command=button_callback)
button.grid(row=9, column=0, padx=10, pady=15)

app.mainloop()
