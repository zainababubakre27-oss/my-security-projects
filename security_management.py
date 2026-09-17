users = {
    "zainab": "cloud123!",
    "joy": "security456!"
}

blacklist = ["192.168.1.1", "10.0.0.5"]

def save_to_log(action, details, status):
    file = open("security_log.txt", "a")
    file.write(f"Action: {action} | Details: {details} | Status: {status}\n")
    file.close()

def view_log():
    try:
        file = open("security_log.txt", "r")
        content = file.read()
        file.close()
        print("\n=== SECURITY LOG ===")
        print(content)
    except FileNotFoundError:
        print("No log file found yet!")

def clear_log():
    try:
        file = open("security_log.txt", "w")
        file.close()
        print("Security log cleared!")
    except Exception as e:
        print(f"Error: {e}")

def login():
    try:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if len(username) == 0 or len(password) == 0:
            print("Cannot be empty!")
            return
        if username in users:
            if users[username] == password:
                save_to_log("LOGIN", username, "SUCCESS")
                print(f"Welcome {username}!")
            else:
                save_to_log("LOGIN", username, "FAILED")
                print("Wrong password!")
        else:
            save_to_log("LOGIN", username, "NOT FOUND")
            print("Username not found!")
    except Exception as e:
        print(f"Error: {e}")

def check_ip():
    try:
        ip = input("Enter IP address: ").strip()
        if len(ip) == 0:
            print("IP cannot be empty!")
            return
        if ip in blacklist:
            save_to_log("IP CHECK", ip, "BLOCKED")
            print(f"BLOCKED! {ip} is blacklisted!")
        else:
            save_to_log("IP CHECK", ip, "CLEAN")
            print(f"CLEAN! {ip} is safe!")
    except Exception as e:
        print(f"Error: {e}")

def show_menu():
    print("\n=== SECURITY MANAGEMENT SYSTEM ===")
    print("1. Login")
    print("2. Check IP Address")
    print("3. View Security Log")
    print("4. Clear Security Log")
    print("5. Exit")

while True:
    try:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if len(choice) == 0:
            print("Please enter a choice!")
            continue
        if choice == "1":
            login()
        elif choice == "2":
            check_ip()
        elif choice == "3":
            view_log()
        elif choice == "4":
            clear_log()
        elif choice == "5":
            print("Goodbye! Stay secure!")
            break
        else:
            print("Invalid choice! Enter 1-5!")
    except Exception as e:
        print(f"System error: {e}")
