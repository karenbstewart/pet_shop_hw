# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(pet_list):
    shop_name = pet_list["name"]
    return shop_name

def get_total_cash(pet_list):
    return pet_list["admin"]["total_cash"]

# def add_or_remove_cash(pet_list, cash_amount):
#     new_total = get_total_cash(pet_list) 
#     new_total += cash_amount
    
def add_or_remove_cash(pet_list, cash_amount):
    pet_list["admin"]["total_cash"] += cash_amount
  

