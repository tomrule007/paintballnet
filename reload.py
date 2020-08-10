def send_single_char(string):
    for c in string:
        keyboard.send_keys(c)
        
def send_command(commands):
    keyboard.send_keys(" ") #open chat/command prompt
    for cmd in commands:
        send_single_char(cmd) # send command one character at a time.
        keyboard.send_keys("<enter>") # submit command   
    keyboard.send_keys("<escape>") #close chat/command prompt


if store.get_global_value("globalPause") == 1:  # passthrough hotkey if chat prompt is open
     keyboard.send_keys("r")
else:
    send_command(["/reload"])
