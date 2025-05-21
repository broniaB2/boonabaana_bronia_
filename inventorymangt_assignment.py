def display_inventory(inventory):
    #Display all items in the inventory with their attributes.
    if not inventory:
        print("\nInventory is empty. Please add items first.")
        return
    
    print("\n===== CURRENT INVENTORY =====")
    print("ID  | Name                | Quantity | Price    | Category")
    print("-" * 60)
    
    for item_id, item in inventory.items():
        print(f"{item_id:<4} | {item['name']:<20} | {item['quantity']:<8} | ugx{item['price']:<15} | {item['category']}")

def update_inventory(inventory):
    #Update existing items or add new items to inventory.
    print("\n===== UPDATE INVENTORY =====")
    print("1. Update existing item")
    print("2. Add new item")
    
    choice = input("\nEnter your choice (1-2): ")
    
    if choice == "1":
        if not inventory:
            print("\nInventory is empty. Nothing to update.")
            return inventory
            
        display_inventory(inventory)
        item_id = input("\nEnter the ID of the item to update: ")
        
        if item_id not in inventory:
            print(f"\nItem with ID {item_id} not found!")
            return inventory
        
        print("\nWhat would you like to update?")
        print("1. Name")
        print("2. Quantity")
        print("3. Price")
        print("4. Category")
        
        update_choice = input("\nEnter your choice (1-4): ")
        
        if update_choice == "1":
            new_name = input("Enter new name: ")
            inventory[item_id]['name'] = new_name
            print(f"\nCongratulations! Item name updated to '{new_name}'.")
        
        elif update_choice == "2":
            try:
                new_quantity = int(input("Enter new quantity: "))
                inventory[item_id]['quantity'] = new_quantity
                print(f"\nCongratulations! Item quantity updated to {new_quantity}.")
            except ValueError:
                print("\nInvalid input. Quantity must be a number.")
        
        elif update_choice == "3":
            try:
                new_price = int(input("Enter new price: "))
                inventory[item_id]['price'] = new_price
                print(f"\nCongratulations! Item price updated to ugx{new_price}.")
            except ValueError:
                print("\nInvalid input. Price must be a number.")
        
        elif update_choice == "4":
            new_category = input("Enter new category: ")
            inventory[item_id]['category'] = new_category
            print(f"\nCongratulations! Item category updated to '{new_category}'.")
        
        else:
            print("\nInvalid choice. No updates made.")
    
    elif choice == "2":
        item_id = str(len(inventory) + 1)
        name = input("Enter item name: ")
        
        try:
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter price: "))
        except ValueError:
            print("\nInvalid input for quantity or price. Item not added.")
            return inventory
            
        category = input("Enter category: ")
        
        inventory[item_id] = {
            'name': name,
            'quantity': quantity,
            'price': price,
            'category': category
        }
        
        print(f"\nCongratulations! New item '{name}' added to inventory.")
    
    else:
        print("\nInvalid choice. No updates made.")
    
    return inventory

def main():
    # Initial inventory items
    inventory = {
        "1": {"name": "Laptop", "quantity": 10, "price": 5000000, "category": "Electronics"},
        "2": {"name": "Chair", "quantity": 5, "price":800000, "category": "Furniture"},
        "3": {"name": "cars", "quantity": 7, "price": 100000000, "category": "vehicle"}
    }
    
    while True:
        print("\n= INVENTORY MANAGEMENT SYSTEM =")
        print("1. Display Inventory")
        print("2. Update Inventory")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            display_inventory(inventory)
        
        elif choice == "2":
            inventory = update_inventory(inventory)
        
        elif choice == "3":
            print("\n exited successfully ")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()