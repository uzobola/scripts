kuraCafe={
      "Pastries":{"Croissant":{"Price":"$1.50","Ingredients":["flour","butter","eggs"]},"Cream Puff":{"Price":"$1.50","Ingredients":["flour","eggs","milk"]}},
      "Entrees":{"BaconEgg&Cheese":{"Price":"$3.00","Ingredients":["bagel","cheese","eggs","bacon"]},"Egg Salad Sandwich":{"Price":"$4.00","Ingredients":["bread","eggs","mayo"]}},
      "Desserts":{"Cheesecake":{"Price":"$1.00","Ingredients":["crust","cream cheese","eggs","blueberries"]},"Blueberry Muffins":{"Price":"$2.50", "Ingredients":["flour","butter","eggs"]}},
      "Bevs":{"Drip Coffee":{"Price":"$1.00","Ingredients":["colombian coffee beans","water"]},"Water":{"Price":"$0.50"}}
      }
  

# Function to Print Menu
def print_menu(menu):
    print("\nKura Cafe Menu:") 
    for menu_section, items in menu.items():
         print(f"\n{menu_section}:")
         for item, details in items.items():
             print(f"  {item} - {details['Price']}")
  
  

# Function to Get price of menu items
def get_price(item, menu):
    for menu_section in menu.values():
        if item in menu_section:
            return float(menu_section[item]['Price'].replace('$', ''))
    return 0
