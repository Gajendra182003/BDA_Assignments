
product_names  = []
product_prices = []
product_qty    = []

# ------------- product_name, product_price, product_qt inserter----------------

def add_product(product_name, product_price, product_qt):
  if product_name in product_names:
    return print(f'''\n{product_name} already exits in the inventory
====================================================''')
  else:
    product_names.append(product_name)
    product_prices.append(product_price)
    product_qty.append(product_qt)
    return print(f'''\n{product_name} was added successfully
====================================================''')

# -------------View Stock Report -----------------------

def View_Stock_Report():

  if len(product_names) == 0:
    return print("\n No products in inventory")
  else:
    print(
  '''
====================================================
            📦 STOCK REPORT
====================================================
No.  Product     Price    Qty     Status
  ''')

  count_of_products = len(product_names)
  inventory_value = 0

  counter = 0

  #----product_names, product_prices, product_qty extractor----

  while counter < count_of_products:

      status = ""
      if product_qty[counter] <= 0:
        status = "❌ OUT OF STOCK"
      elif product_qty[counter] < 5:
        status = "⚠️ LOW STOCK"
      else:
        status = "✅ Available"

      print(f"{counter + 1}    {product_names[counter]}       {product_prices[counter]}        {product_qty[counter]}     {status}")
      inventory_value += product_prices[counter]*product_qty[counter]
      counter += 1

  print(f'''
====================================================
Total Products        : {count_of_products}
Total inventory Value : {inventory_value} Rs
        ''')

#--------------------- Sell Product --------------------

def sell(product_name, product_qt):


  if product_name in product_names:
    index = product_names.index(product_name)
    avl_qty = product_qty[index]

    if avl_qty < product_qt:
      return print(f"Only {avl_qty} available in inventry of {product_name}")

    else:
      new_qty = avl_qty - product_qt
      product_qty[index] = new_qty
      return print(f" {product_qt} units sold of {product_name} worth Rs. {product_prices[index]*product_qt} \n{new_qty} remaing in inventry of {product_name}")

  else:
    return print(f"{product_name} was not found in inventory ")

#-------------------------- Restock ------------------------

def restock(product_name, product_qt):
  if product_name in product_names:

    index = product_names.index(product_name)
    avl_qty = product_qty[index]

    new_qty = avl_qty + product_qt
    product_qty[index] = new_qty

    return print(f"{product_name} restocked new available quantity {new_qty}")

  else :
     return print(f"{product_name} was not found in inventory ")


#-------------------------- Menu ------------------------

def menu():

  print("\n\n============================== Welcome to Smart Mart ==============================\n\n")

  while True:
    print('''
  ==============================
    🏪 SHOP INVENTORY MANAGER
  ==============================
  1. Add New Product
  2. Sell Product
  3. Restock Product
  4. View Stock Report
  5. Exit
  ------------------------------
  ''')

    choice = input("Enter your choice: ")

    if choice.isdigit() == True:
      choice = int(choice)

      if choice == 1:

        print("--- Add New Product ---")

        product_name = input("\nEnter product name :").strip()
        price_per_unit = float(input(f"\nEnter price per :"))
        quantity = int(input("\nEnter quantity :"))

        if len(product_name) <= 0 or quantity <= 0 or price_per_unit <= 0:
          print("❌ Blank Product Name not allowed, Quantity and price must be greater than 0!")

        else:
          add_product(product_name,price_per_unit,quantity)

      elif choice == 2:

        print("--- Sell Product---")

        product_name = input("\nEnter product name :").strip()
        quantity = int(input("\nEnter quantity :"))
        if quantity <= 0 or len(product_name) == 0 :
          print("Please put a valid name or please provide quantity 1 or above")
        else:
          sell(product_name,quantity)

      elif choice == 3:

        print("--- Restock Product---")

        product_name = input("\nEnter product name :").strip()
        quantity = int(input("\nEnter quantity :"))

        if quantity <= 0 or len(product_name) == 0 :
          print("Please put a valid name or please provide quantity 1 or above")
        else:
          restock(product_name,quantity)

      elif choice == 4:

        print("--- View Stock Report---")

        View_Stock_Report()

      elif choice == 5:

        print("--- Good Bye !! You have Exited ---")

        break
        #exit()
    else:
        print("❌ Invalid choice! Try again.")

menu()
