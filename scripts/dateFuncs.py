kuraCafe={
      "Pastries":{"croissant":{"Price":"$1.50","Ingredients":["flour","butter","eggs"]},"cream puff":{"Price":"$1.50","Ingredients":["flour","eggs","milk"]}},
      "Entrees":{"bacon egg and cheese":{"Price":"$3.00","Ingredients":["bagel","cheese","eggs","bacon"]},"egg ealad sandwich":{"Price":"$4.00","Ingredients":["bread","eggs","mayo"]}},
      "Desserts":{"cheese cake":{"Price":"$1.00","Ingredients":["crust","cream cheese","eggs","blueberries"]},"blueberry muffins":{"Price":"$2.50", "Ingredients":["flour","butter","eggs"]}},
      "Bevs":{"drip coffee":{"Price":"$1.00","Ingredients":["colombian coffee beans","water"]},"water":{"Price":"$0.50"}}
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
