import random
import string
import socket
from collections import Counter

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password = password + random.choice(all_characters)
    return password

def analyze_log():
    try:
        file = open("security_log.txt", "r")
        lines = file.readlines()
        file.close()
        failed_logins = []
        for line in lines:
            if "Status: FAILED" in line:
                parts = line.split("|")
                for part in parts:
                    if "Details:" in part:
                        username = part.strip().replace("Details: ", "")
                        failed_logins.append(username)
        print(f"\nTotal failed logins: {len(failed_logins)}")
        counter = Counter(failed_logins)
        for user, count in counter.items():
            if count >= 2:
                print(f"🚨 {user} — {count} failed attempts!")
    except FileNotFoundError:
        print("No log file found!")

def scan_ports():
    try:
        ip = input("Enter IP to scan: ")
        start = int(input("Start port: "))
        end = int(input("End port: "))
        print(f"\nScanning {ip}...")
        for port in range(start, end + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                sock.close()
                if result == 0:
                    print(f"Port {port} — OPEN 🚨")
            except:
                pass
    except ValueError:
        print("Please enter valid numbers for ports!")

def monitor_network():
    connections = [
        "192.168.1.1", "192.168.1.2", "10.0.0.5",
        "192.168.1.1", "192.168.1.1", "10.0.0.5",
        "192.168.1.1", "10.0.0.5", "10.0.0.5", "10.0.0.5"
    ]
    threshold = int(input("Enter suspicious threshold: "))
    counter = Counter(connections)
    print("\n=== CONNECTION REPORT ===")
    for ip, count in counter.items():
        if count >= threshold:
            print(f"🚨 SUSPICIOUS: {ip} — {count} connections!")
        else:
            print(f"✅ NORMAL: {ip} — {count} connections")

while True:
    print("\n=== SECURITY TOOLKIT ===")
    print("1. Generate Password")
    print("2. Analyze Security Log")
    print("3. Scan Ports")
    print("4. Monitor Network")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        length = int(input("Password length: "))
        print(f"Generated password: {generate_password(length)}")
    elif choice == "2":
        analyze_log()
    elif choice == "3":
        scan_ports()
    elif choice == "4":
        monitor_network()
    elif choice == "5":
        print("Goodbye! Stay secure! 🔐")
        break
    else:
        print("Invalid choice! Enter 1-5!")
