# Plays alarm if alarm sequence is received.

def on_received_number(receivedNumber):
    if receivedNumber == 3:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        . . # . .
                        . . . . .
                        . . # . .
        """)
        music.start_melody(music.built_in_melody(Melodies.RINGTONE),
            MelodyOptions.FOREVER)
radio.on_received_number(on_received_number)

# Monitors condition of a flag variable to decide either to add the letter a to the entered password or display the safe password one digit at a time.

def on_button_pressed_a():
    global Entered, Count
    if Flag == 0:
        Entered = "" + Entered + "A"
        basic.show_string("A")
    else:
        if Count < len(password):
            basic.show_string("" + (password[Count]))
            Count += 1
        else:
            basic.clear_screen()
            Count = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

# Checks entered password against password.

def on_button_pressed_ab():
    global Flag, Entered
    if thisPass == Entered:
        basic.show_icon(IconNames.YES)
        basic.pause(1000)
        basic.clear_screen()
        Flag = 1
        Entered = ""
    else:
        basic.show_icon(IconNames.NO)
        basic.pause(1000)
        basic.clear_screen()
        Entered = ""
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Receives password string.

def on_received_string(receivedString):
    global password
    password = receivedString
radio.on_received_string(on_received_string)

# Monitors condition of a flag variable to either add the letter b to a password sequence or clear the screen and stop all sounds.

def on_button_pressed_b():
    global Entered
    if Flag == 0:
        Entered = "" + Entered + "B"
        basic.show_string("B")
    else:
        basic.clear_screen()
        music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)

# Initializes some values.
Flag = 0
Entered = ""
thisPass = ""
password = ""
Count = 0
radio.set_group(121)
Count = 0
password = ""
thisPass = "ABABAB"
Entered = ""
