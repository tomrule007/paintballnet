def send_single_char(string):
    for c in string:
        keyboard.send_keys(c)
        
def send_command(commands):
    keyboard.send_keys(" ") #open chat/command prompt
    for cmd in commands:
        send_single_char(cmd) # send command one character at a time.
        keyboard.send_keys("<enter>") # submit command   
    keyboard.send_keys("<escape>") #close chat/command prompt

try:
    enabled = store.get_global_value("enabled")
except TypeError:
    enabled = True #default setting

if enabled: 
    send_command(["/2"]) # /alias 2 get token jacket \& sell token \& get flag jacket \& sell flag
else:
    keyboard.send_keys('<shift>+e')