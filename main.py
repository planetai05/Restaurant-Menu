from tkinter import *
from tkinter import ttk
import csv
main_list = []
restaurant_info = []
with open(file="restaurants.csv",mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dummy_list = []
        dummy_list.append(row['name'])
        dummy_list.append(row['cuisine_type'])
        dummy_list.append(row['rating'])
        dummy_list.append(row['location'])
        dummy_list.append(row['ï»¿restaurant_id'])
        dummy_list.append(row['total_tables'])
        dummy_list.append(row['table_configuration'])
        dummy_list.append(row['opening_hours'])
        dummy_list.append(row['closing_hours'])
        restaurant_info.append(dummy_list)
def Menu():
    global main_list
    main_list.clear()
    for record in restaurant_tree.get_children():
        restaurant_tree.delete(record)
    for val in restaurant_info:
        match filter_cuisine.get():
            case "All Types":
                restaurant_tree.insert(parent="",index=END,values=(val[0],val[2]))
                main_list.append(val[0])
            case "Indian":
                if 'Indian' in val:
                    restaurant_tree.insert(parent="",index=END,values=(val[0],val[2]))
                    main_list.append(val[0])
            case 'Japanese':
                if 'Japanese' in val:
                    restaurant_tree.insert(parent="",index=END,values=(val[0],val[2]))
                    main_list.append(val[0])
            case 'European':
                if "European" in val:
                    restaurant_tree.insert(parent="",index=END,values=(val[0],val[2]))
                    main_list.append(val[0])
    Label(window,text="Restaurant Info",font=("Aerial",10)).place(x=10,y=430)
    global restaurant_name
    restaurant_name = StringVar()
    restaurant_dropdown = ttk.Combobox(window,textvariable=restaurant_name)
    restaurant_dropdown['values']=[val for val in main_list ]
    restaurant_dropdown.place(x=115,y=430)
    Button(window,text="Search",command=Search).place(x=275,y=430)
    


def Search():
    global restaurant_name
    global restaurant_info
    restaurant_text = Text(window,width=100,height=14)
    restaurant_text.place(x=500,y=170)
    Label(window,text=f"{restaurant_name.get()} Info",font=("Aerial",18)).place(x=820,y=120)
    for val in restaurant_info:
        if val[0]==restaurant_name.get():
            restaurant_text.insert(END,f"Restaurant ID: {val[4]}\nRestaurant Name: {val[0]}\nCuisine Type: {val[1]}\nLocation: {val[3]}\nRating: {val[2]}\nTotal Tables: {val[5]}\nTable Configuration: {val[6]}\nOpening Time: {val[7]}\nClosing Time: {val[8]} ")
    Button(window,text="EXIT",command=quit,font=("Aerial",15)).place(x=1350,y=750)



window = Tk()
window.title("Restaurant Booking System")
window.configure(bg="#86968a")
window.geometry("1920x1080")
Label(window,text="RESTAURANT",padx=20,font=("Bold",20),bg="#D2BEE8",relief=SUNKEN,bd=10).place(x=670,y=0)

Label(window,text="Restaurant Names",font=("Aerial",18)).place(x=10,y=75)
Label(window,text="Cuisine Type: ").place(x=10,y=120)
filter_cuisine = StringVar()
filter_dropdown = ttk.Combobox(window,textvariable=filter_cuisine)
filter_dropdown['values'] = ['All Types','Indian','Japanese','European']
filter_dropdown.set('All Types')
filter_dropdown.place(x=95,y=120)
restaurant_tree=ttk.Treeview(window,columns=("Restaurant","Rating"),show="headings")
restaurant_tree.heading("Restaurant",text="Restaurant")
restaurant_tree.heading("Rating",text="Rating")
restaurant_tree.place(x=10,y=170)

Button(window,text="Search",command=Menu).place(x=250,y=120)




Label(window,text="")

    





window.mainloop()
