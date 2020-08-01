def send_single_char(string):
    for c in string:
        keyboard.send_keys(c)
        
def send_command(commands):
    keyboard.send_key(" ") #open chat/command prompt
    for cmd in commands:
        send_single_char(cmd) # send command one character at a time.
        keyboard.send_key("<enter>") # submit command   
    keyboard.send_key("<escape>") #close chat/command prompt


if store.get_global_value("globalPause") == 1:  # passthrough hotkey if chat prompt is open
    keyboard.send_key("q")
else:
    send_command(["/swap & get gun back & put %lhand back"])
