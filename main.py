import header.title
import os

os.system("pkg install php -y")
os.system("pkg install tor -y ")
os.system("pkg update")
os.system("pkg upgrade")


import os

print("""
=================================
    Termux Basic Setup Tool
=================================
""")

print("[+] Updating packages...")
os.system("pkg update -y && pkg upgrade -y")

print("\n[+] Installing basic tools...")
os.system("pkg install python -y")
os.system("pkg install git -y")
os.system("pkg install curl -y")
os.system("pkg install wget -y")
os.system("pkg install nano -y")
os.system("pkg install vim -y")
os.system("pkg install openssh -y")
os.system("pkg install zip -y")
os.system("pkg install unzip -y")
os.system("pkg install clang -y")
os.system("pkg install make -y")

print("\n[+] Upgrading pip...")
os.system("python -m pip install --upgrade pip")

print("\n[+] Installing basic Python libraries...")
os.system("python -m pip install requests")
os.system("python -m pip install colorama")
os.system("python -m pip install rich")
os.system("python -m pip install beautifulsoup4")

print("\n[✓] Setup process completed!")
print("[+] Enjoy using Termux!")
