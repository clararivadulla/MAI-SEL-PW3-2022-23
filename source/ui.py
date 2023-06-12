from preprocessing import travel_dataset_xls_preprocessing
from Retrieve import retrieve
from Adaptation import weighted_adaptation
import time
import customtkinter
import pandas as pd
import numpy as np
import os


root = os.getcwd()
travel_dataset_xls_preprocessing(root)
data_folder = f"{root}/data"
CB = pd.read_csv(f"{data_folder}/travel.csv")

holiday_types = CB['holiday-type'].unique()
holiday_types = np.append(holiday_types, 'Other')

regions = CB['region'].unique()
regions = np.append(regions, 'Other')

transportations = CB['transportation'].unique()
transportations = np.append(transportations, 'Other')

months = CB['season'].unique()

accomodations = CB['accomodation'].unique()

hotels = CB['hotel'].unique()
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
    if selected_holiday_type == "": selected_holiday_type = None
    print(f'Holiday Type: {selected_holiday_type}')

    selected_price = slider.get()
    if selected_price == 0: selected_price = None
    print(f'Maximum Price: {selected_price}')

    selected_num_pers = num_pers.get()
    if selected_num_pers == "": selected_num_pers = None
    else: selected_num_pers = int(selected_num_pers)
    print(f'Number of persons: {selected_num_pers}')

    selected_region = regionmenu.get()
    if selected_region == "Other": selected_region = other_region.get()
    if selected_region == "": selected_region = None
    print(f'Region: {selected_region}')

    selected_transportation = transportationmenu.get()
    if selected_transportation == "Other": selected_transportation = other_transportation.get()
    if selected_transportation == "": selected_transportation = None
    print(f'Transportation: {selected_transportation}')

    selected_duration = duration.get()
    if selected_duration == "": selected_duration = None
    else: selected_duration = int(selected_duration)
    print(f'Duration (in days): {selected_duration}')

    selected_month = monthmenu.get()
    print(f'Month: {selected_month}')

    selected_accomodation = accomodationmenu.get()
    print(f'Accomodation: {selected_accomodation}')

    selected_hotel = hotelmenu.get()
    if selected_hotel == "Other": selected_hotel = other_hotel.get()
    if selected_hotel == "": selected_hotel = None
    print(f'Hotel: {selected_hotel}')
    print()

    new_case = pd.Series([selected_holiday_type, selected_price, selected_num_pers, selected_region, selected_transportation, selected_duration, selected_month, selected_accomodation, selected_hotel],
                         index=["holiday-type", "price", "num-persons", "region", "transportation", "duration",
                                "season", "accomodation", "hotel"])

    start_time = time.time()
    most_similar_cases, distances = retrieve(CB, new_case, data_folder, (len(CB.index)/10))
    end_time = time.time()

    print(f"Most similar case found in {end_time - start_time} seconds with {distances[0]} of distance:")
    suggested_case = weighted_adaptation(new_case, CB.loc[most_similar_cases])
    print(suggested_case)
    print()


    toplevel = customtkinter.CTkToplevel(app)
    toplevel.title("Travel Planner - Suggestion")
    toplevel.geometry("510x405")
    toplevel.attributes('-topmost', 'true')

    customtkinter.CTkLabel(toplevel, text=f"Holiday type:", fg_color="transparent").grid(row=0, column=0, padx=10, pady=5)
    customtkinter.CTkLabel(toplevel, text=f"{suggested_case['holiday-type']}", fg_color="transparent").grid(row=0, column=1, padx=10, pady=5)
    
    customtkinter.CTkLabel(toplevel, text=f"price:", fg_color="transparent").grid(row=1, column=0, padx=10, pady=5)
    customtkinter.CTkLabel(toplevel, text=f"{str(suggested_case['price'])}", fg_color="transparent").grid(row=1, column=1, padx=10, pady=5)
    
    customtkinter.CTkLabel(toplevel, text=f"num-persons:", fg_color="transparent").grid(row=2, column=0, padx=10, pady=5)
    customtkinter.CTkLabel(toplevel, text=f"{str(suggested_case['num-persons'])}", fg_color="transparent").grid(row=2, column=1, padx=10, pady=5)
    
    customtkinter.CTkLabel(toplevel, text=f"region:", fg_color="transparent").grid(row=3, column=0, padx=10, pady=5)
    customtkinter.CTkLabel(toplevel, text=f"{suggested_case['region']}", fg_color="transparent").grid(row=3, column=1, padx=10, pady=5)
    
    customtkinter.CTkLabel(toplevel, text=f"transportation:", fg_color="transparent").grid(row=4, column=0, padx=10, pady=5)
    customtkinter.CTkLabel(toplevel, text=f"{suggested_case['transportation']}", fg_color="transparent").grid(row=4, column=1, padx=10, pady=5)
    
    customtkinter.CTkLabel(toplevel, text=f"duration:", fg_color="transparent").grid(row=5, column=0, padx=10, pady=5)
    customtkinter.CTkLabel(toplevel, text=f"{str(suggested_case['duration'])}", fg_color="transparent").grid(row=5, column=1, padx=10, pady=5)
    
    customtkinter.CTkLabel(toplevel, text=f"season:", fg_color="transparent").grid(row=6, column=0, padx=10, pady=5)
    customtkinter.CTkLabel(toplevel, text=f"{suggested_case['season']}", fg_color="transparent").grid(row=6, column=1, padx=10, pady=5)
    
    customtkinter.CTkLabel(toplevel, text=f"accomodation:", fg_color="transparent").grid(row=7, column=0, padx=10, pady=5)
    customtkinter.CTkLabel(toplevel, text=f"{suggested_case['accomodation']}", fg_color="transparent").grid(row=7, column=1, padx=10, pady=5)

    customtkinter.CTkLabel(toplevel, text=f"hotel:", fg_color="transparent").grid(row=8, column=0, padx=10, pady=5)
    customtkinter.CTkLabel(toplevel, text=f"{suggested_case['hotel']}", fg_color="transparent").grid(row=8, column=1, padx=10, pady=5)
    
    customtkinter.CTkButton(toplevel, text="Accept", command=btn_accept_callback).grid(row=9, column=0, padx=10, pady=15)
    customtkinter.CTkButton(toplevel, text="Reject", command=btn_reject_callback).grid(row=9, column=1, padx=10, pady=15)

    return None

def btn_accept_callback():
    print("TODO. According to documentation, store new case (Retain)")
    return None

def btn_reject_callback():
    print("TODO. Suggestion: show a second suggestion")
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
accomodationmenu = customtkinter.CTkOptionMenu(app, values=accomodations)
accomodationmenu.grid(row=7, column=1, padx=0, pady=5)

# HOTEL
hotel_label = customtkinter.CTkLabel(app, text="Hotel:", fg_color="transparent")
hotel_label.grid(row=8, column=0, padx=10, pady=5)
hotelmenu = customtkinter.CTkOptionMenu(app, values=hotels,
                                         command=hotelmenu_callback)
hotelmenu.grid(row=8, column=1, padx=0, pady=5)
hotelmenu.set(None)
other_hotel = customtkinter.CTkEntry(app, placeholder_text="")

button = customtkinter.CTkButton(app, text="Find me a trip", command=button_callback)
button.grid(row=9, column=0, padx=10, pady=15)

app.mainloop()
