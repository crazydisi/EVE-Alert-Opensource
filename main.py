import customtkinter

from evealert import __version__
from evealert.menus.alert import AlertMenu

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

print(
    f"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓█████▓▓▓▓███████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓███▓▓▓▓██████▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓██▓▓▓▓█▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓█▓▒▒▒▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓█████████▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓███████▓▓█▒▒▓▓██▓▓▓▓▓█▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓█▓▒▒▒▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓█▓▓▓▓██▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓██▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓█▓▓▓▓▓▓▓██▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▒▓▓▓▓▓▓█▓▓█▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓██▒░██▓▓▓▓▓▓▓█████▓██▓▓█▓▓▓▓▓▓▓▓▓█▓▓█▓▓▓▓▓▓█▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓█▓█▓▓▓▓▓▓▓█▒░░▓██▓▓▓▓▓▓█░▒██▒░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓█▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░▓▓▓▓▓▓▓██░░░██▓░▓▓▓▓▓▓▓█▓▓▓▓▓▓▓█▓▓█▓▓█▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓██▓░████████████▓██░░░░▓██████▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓█▓█░░█░████░░▓█████░▒██░▒█▓██▓█▓▓█▓▓█▓▓▓▓▓▓██▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓█▓█▓▓▓██▒░░█▓█▓██░░░░░████░░████▓█▒░█▓▓▓█▓▓▓▓▓▓█▓▓█▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓█░█░█▓▓██░░░░░░░░▓██░██▓███░█▓██▓▓▓██▓▓▓█▓▓█▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓██░▒█░░░░░░░░░░░░░░░▒░░▓░░██░░█▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓██░░▒▒▓▒▒▒▒▒░░░░░░░░░░░▓█▓▒▒░█▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓███░░░░░░░░░░▓▓░░░▒░░░░░░░▓██▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓███████▓▒░░░░░░░░░░░░▒████▓▓█▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▒█████████████████████▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░█░▓▓▓░░█░░▒███▓▓▓▓▓▓█▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███░░░█░░░░░░░░█░░░▓███▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓░▓███▓██▒░██████▒░░███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓░░░░▓█░░░█▓░░░▒█░▓▒▒░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓░░░░▓▒░█░░█████░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███░░░░░█▒░░█░▓░░░░░░▒███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒██░░█░░█▒░░▓▒█████░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▓▓▓█████▓▓▓▓▒░░░░█▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███░░░░░░░░░▓▒█░░░░░░▒▒░███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒░░░░░░░░▓██▓▒░░▒▒▓███▓░▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓████████▓████▒░░░░░░░░▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█░░░░░░░░░░░▓█░░░▒▓▓▓▓▓▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
░░░░░░░░░░░░░░░░░░ Geuthur - EVE Alert v{__version__} ░░░░░░░░░░░░░░░░░░░░░░░
"""
)

# Start the application
app = AlertMenu()
app.mainloop()
