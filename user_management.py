users = [
    {"id": 1, "name": "Leanne Graham", "username": "Bret"},
    {"id": 2, "name": "Ervin Howell", "username": "Antonette"},
    {"id": 3, "name": "Clementine Bauch", "username": "Samantha"},
    {"id": 4, "name": "Patricia Lebsack", "username": "Karianne"},
    {"id": 5, "name": "Chelsey Dietrich", "username": "Kamren"},
    {"id": 6, "name": "Mrs. Dennis Schulist", "username": "Leopoldo_Corkery"},
    {"id": 7, "name": "Kurtis Weissnat", "username": "Elwyn.Skiles"},
    {"id": 8, "name": "Nicholas Runolfsdottir V", "username": "Maxime_Nienow"},
    {"id": 9, "name": "Glenna Reichert", "username": "Delphine"},
    {"id": 10, "name": "Clementina DuBuque", "username": "Moriah.Stanton"},
]

def fetch_users():
    """Displays all users and allows selection for details."""
    while True:
        print("\n📜 **Registered Users:**")
        for user in users:
            print(f"{user['id']}. {user['name']} (@{user['username']})")
        
        try:
            ops = int(input("\nEnter serial number to view details (0 to go back): "))
            if ops == 0:
                return  # Go back to the main menu
            user = next((u for u in users if u["id"] == ops), None)
            if user:
                print(f"\n🆔 ID: {user['id']}\n👤 Name: {user['name']}\n📛 Username: {user['username']}\n")
            else:
                print("❌ Invalid user ID! Please enter a valid number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def add_user():
    """Allows adding a new user."""
    name = input("Enter the full name: ").strip()
    username = input("Enter a username: ").strip()
    
    if not name or not username:
        print("⚠️ Name and username cannot be empty!")
        return
    
    new_id = max(user["id"] for user in users) + 1  # Assign a new unique ID
    users.append({"id": new_id, "name": name, "username": username})
    print(f"✅ User '{name}' (@{username}) added successfully!")

def delete_user():
    """Allows deleting a user by ID."""
    try:
        user_id = int(input("Enter the user ID to delete (0 to cancel): "))
        if user_id == 0:
            return  # Go back to the main menu
        global users
        users = [user for user in users if user["id"] != user_id]
        print(f"✅ User with ID {user_id} deleted successfully!")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def bye():
    """Exit message."""
    print("\n👋 Exiting... Have a great day!")

# Main loop
while True:
    print("\n💡 **Menu:**")
    print("1️⃣ See Users")
    print("2️⃣ Add User")
    print("3️⃣ Delete User")
    print("4️⃣ Exit")

    try:
        choice = int(input("Enter Your Choice (1-4): "))
        if choice == 1:
            fetch_users()
        elif choice == 2:
            add_user()
        elif choice == 3:
            delete_user()
        elif choice == 4:
            bye()
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 4.")
    except ValueError:
        print("⚠️ Please enter a valid number.")
