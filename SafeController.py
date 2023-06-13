def on_pin_released_p2():
    radio.send_number(3)
input.on_pin_released(TouchPin.P2, on_pin_released_p2)

# Sends alarm sequence in case of tampering with safe.

def on_gesture_eight_g():
    radio.send_number(3)
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

# Allows user to enter a number for the password.

def on_button_pressed_a():
    global Count
    if Count < 9:
        Count += 1
    else:
        Count = 0
    basic.show_string("" + str((Count)))
input.on_button_pressed(Button.A, on_button_pressed_a)

# Sends alarm sequence in case of tampering with safe.

def on_gesture_free_fall():
    radio.send_number(3)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

# Sends alarm sequence in case of tampering with safe.

def on_gesture_six_g():
    radio.send_number(3)
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

# Checks if the entered password matches the current password, if it does it sends an unlock command and resets the code to change the password and if it doesn’t the code still resets.

def on_button_pressed_ab():
    if Entered == Password:
        radio.send_number(1)
        basic.show_icon(IconNames.YES)
        basic.pause(1000)
        basic.clear_screen()
        control.reset()
    else:
        basic.show_icon(IconNames.NO)
        basic.pause(1000)
        basic.clear_screen()
        control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Joins the current entered number to the entered password.

def on_button_pressed_b():
    global Entered, Count
    basic.clear_screen()
    Entered = "" + Entered + str(Count)
    Count = -1
input.on_button_pressed(Button.B, on_button_pressed_b)

# Sends alarm sequence in case of tampering with safe.

def on_gesture_shake():
    radio.send_number(3)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# Sends alarm sequence in case of tampering with safe.

def on_gesture_three_g():
    radio.send_number(3)
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

# Initializes some values.
Password = ""
Count = 0
Entered = ""
radio.set_group(121)
Flag = 0
Wait = 5000000
Entered = ""
Count = -1
Password = ""
# Generates a new random 9 digit number for the password every five minutes. The sends password as a string to a receiver MicroBit.

def on_forever():
    global Password
    Password = "" + str(randint(0, 9)) + ("" + str(randint(0, 9))) + ("" + str(randint(0, 9))) + ("" + str(randint(0, 9))) + ("" + str(randint(0, 9))) + ("" + str(randint(0, 9))) + ("" + str(randint(0, 9))) + ("" + str(randint(0, 9))) + ("" + str(randint(0, 9)))
    radio.send_string(Password)
    basic.pause(300000)
basic.forever(on_forever)

# Waits for pressure sensor to be activated then sends command to servo controller to lock door.

def on_in_background():
    while True:
        control.wait_for_event(EventBusSource.MICROBIT_ID_IO_P2,
            EventBusValue.MICROBIT_BUTTON_EVT_DOWN)
        control.wait_micros(Wait)
        radio.send_number(2)
control.in_background(on_in_background)
