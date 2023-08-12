
from django.shortcuts import render, redirect
from .models import Dish

# # persisting the data into file system;
# import pickle
# import os
# DATA_FILE = "menu_data.pkl"

# def save_data():
#     with open(DATA_FILE, "wb") as f:
#         pickle.dump({"menu_items": menu_items, "orders": orders}, f)

# def load_data():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "rb") as f:
#             data = pickle.load(f)
#             global menu_items, orders
#             menu_items = data["menu_items"]
#             orders = data["orders"]

# # Call the load_data() function at the beginning of your views.py to load data from the file;
# load_data()


menu_items = []  # Global list to store menu items
orders = []  # Global list to store orders

menu_items.append(Dish(dish_name="Pasta", price=10.99))
menu_items.append(Dish(dish_name="Pizza", price=15.99))

# Create your views here.

def get_menu_items():
    return menu_items

def menu_list(request):
    menu_items = get_menu_items()
    return render(request, "menu/menu_list.html", {"menu_items": menu_items})


# adding , removing, updating dishes;
def homepage(request):
    return render(request, "menu/index.html")

def add_dish(request):
    if request.method == "POST":
        dish_name = request.POST["dish_name"]
        price = float(request.POST["price"])
        availability = request.POST.get("availability") == "on"
        dish = Dish(dish_name=dish_name, price=price, availability=availability)
        menu_items.append(dish)
        # save_data()
        return redirect("menu_list")
    return render(request, "menu/add_dish.html")

def remove_dish(request, dish_name):
    global menu_items
    menu_items = [dish for dish in menu_items if dish.dish_name != dish_name]
    # save_data()
    return redirect("menu_list")

def update_dish(request, dish_name):
    for dish in menu_items:
        if dish.dish_name == dish_name:
            if request.method == "POST":
                dish.dish_name = request.POST["dish_name"]
                dish.price = float(request.POST["price"])
                dish.availability = request.POST.get("availability") == "on"
                # save_data()
                return redirect("menu_list")
            return render(request, "menu/update_dish.html", {"dish": dish})
    return redirect("menu_list")

# take orders, order_list;

def take_order(request):
    menu_items = get_menu_items()  # Assuming you already have the get_menu_items function from previous steps

    if request.method == "POST":
        customer_name = request.POST["customer_name"]
        order_dishes = request.POST.getlist("order_dishes")

        valid_dishes = [dish for dish in order_dishes if dish in [item.dish_name for item in menu_items]]
        if len(valid_dishes) != len(order_dishes):
            return render(request, "menu/error.html", {"message": "Invalid dish selection."})

        total_price = sum([dish.price for dish in menu_items if dish.dish_name in valid_dishes])

        order = {"customer_name": customer_name, "dishes": valid_dishes, "status": "received", "total_price": total_price}
        orders.append(order)
        # save_data()
        return redirect("order_list")
    
    return render(request, "menu/take_order.html", {"menu_items": menu_items})


def order_list(request):
    return render(request, "menu/order_list.html", {"orders": orders})


# update the order-status;

def update_order_status(request, order_id):
    for order in orders:
        if order["order_id"] == order_id:
            if request.method == "POST":
                new_status = request.POST["new_status"]
                order["status"] = new_status
                # save_data()
                return redirect("order_list")
            return render(request, "menu/update_order_status.html", {"order": order})
    
    return render(request, "menu/error.html", {"message": "Order not found."})


# review all orders;

def review_orders(request):
    return render(request, "menu/review_orders.html", {"orders": orders})

# filter orders by status;
def filter_orders_by_status(request, status):
    filtered_orders = [order for order in orders if order["status"] == status]
    return render(request, "menu/filter_orders.html", {"filtered_orders": filtered_orders, "status": status})

# error handling
def error(request):
    return render(request, "menu/error.html", {"message": "An error occurred."})

