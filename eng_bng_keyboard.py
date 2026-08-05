import keyboard





def pressed1(name):
	ch = name.name
	global ctrl

	if(ch == 'esc'): # quit if esc pressed
		keyboard.unhook_all()
		

	

	if(name.name == 'ctrl'):
		ctrl = True
	if(ctrl): # check if ctrl was pressed
		keyboard.press('ctrl+'+ch)
	# 	ctrl = False
		return
	if ch in eng2bengali.keys():
		print(ch)
		keyboard.write(eng2bengali[ch])
	else:
		print("pressed : " + ch)
		keyboard.press(ch) # press key if key not in eng2bengali(common keys eg '!', '@' )
	
	return

def released1(name):
	ch = name.name
	global ctrl
	if ch in eng2bengali.keys(): # keys present in eng2bengali were suppressed during press event no need to release
		return

	keyboard.release(ch) # release key ch
	print("released : " + ch)
	if(name.name == 'ctrl'): # ctrl is released
		ctrl = False
		return

eng2bengali = dict()
ctrl = False

f1 = open("./map.txt", "r", encoding="utf8") # open map.txt with utf8 encoding

lines = f1.readlines() # read lines into array

for line in lines:
    # Special case: handle ':' as a key
    if line.startswith(":"):  
        a = ":"  # Key is ':'
        b = line[2]# Everything after ':' is the bengali letter
    else:
        a = line.split(":")[0]  # Split each line by ':' to get the English character
        b = line.split(":")[1]
		  # Get the bengali character and strip any trailing spaces or '\n'
    b = b.split("\n")[0]
    eng2bengali[a] = b  # Map the English character to the bengalicharacter
f1.close()

input("Press enter to start (esc to stop):")
keyboard.on_press(pressed1, suppress=True) # call pressed1 on key press event suppress the event
keyboard.on_release(released1, suppress = True) # call released1 on key release event suppress the event

keyboard.wait() # stop main thread from finishing execution




