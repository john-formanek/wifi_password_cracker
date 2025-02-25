import subprocess

# Získání seznamu Wi-Fi profilů
command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode()
profiles = [line.split(":")[1][1:-1] for line in command.split("\n") if "All User Profile" in line]

# Pro každou Wi-Fi síť získat heslo
print("{:<30}|  {:<}".format("Wi-Fi Název", "Heslo"))
print("-" * 50)

for profile in profiles:
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode()
    password_lines = [line.split(":")[1][1:-1] for line in result.split("\n") if "Key Content" in line]

    if password_lines:
        password = password_lines[0]
    else:
        password = "Nenalezeno"

    print("{:<30}|  {:<}".format(profile, password))

input("\nStiskněte Enter pro ukončení...")
