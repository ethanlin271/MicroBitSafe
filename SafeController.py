input.onPinReleased(TouchPin.P2, function () {
    radio.sendNumber(3)
})
// Sends alarm sequence in case of tampering with safe.
input.onGesture(Gesture.EightG, function () {
    radio.sendNumber(3)
})
// Allows user to enter a number for the password.
input.onButtonPressed(Button.A, function () {
    if (Count < 9) {
        Count += 1
    } else {
        Count = 0
    }
    basic.showString("" + (Count))
})
// Sends alarm sequence in case of tampering with safe.
input.onGesture(Gesture.FreeFall, function () {
    radio.sendNumber(3)
})
// Sends alarm sequence in case of tampering with safe.
input.onGesture(Gesture.SixG, function () {
    radio.sendNumber(3)
})
// Checks if the entered password matches the current password, if it does it sends an unlock command and resets the code to change the password and if it doesn’t the code still resets.
input.onButtonPressed(Button.AB, function () {
    if (Entered == Password) {
        radio.sendNumber(1)
        basic.showIcon(IconNames.Yes)
        basic.pause(1000)
        basic.clearScreen()
        control.reset()
    } else {
        basic.showIcon(IconNames.No)
        basic.pause(1000)
        basic.clearScreen()
        control.reset()
    }
})
// Joins the current entered number to the entered password.
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    Entered = "" + Entered + Count
    Count = -1
})
// Sends alarm sequence in case of tampering with safe.
input.onGesture(Gesture.Shake, function () {
    radio.sendNumber(3)
})
// Sends alarm sequence in case of tampering with safe.
input.onGesture(Gesture.ThreeG, function () {
    radio.sendNumber(3)
})
// Initializes some values.
let Password = ""
let Count = 0
let Entered = ""
radio.setGroup(121)
let Flag = 0
let Wait = 5000000
Entered = ""
Count = -1
Password = ""
// Generates a new random 9 digit number for the password every five minutes. The sends password as a string to a receiver MicroBit.
basic.forever(function () {
    Password = "" + randint(0, 9) + ("" + randint(0, 9)) + ("" + randint(0, 9)) + ("" + randint(0, 9)) + ("" + randint(0, 9)) + ("" + randint(0, 9)) + ("" + randint(0, 9)) + ("" + randint(0, 9)) + ("" + randint(0, 9))
    radio.sendString(Password)
    basic.pause(300000)
})
// Waits for pressure sensor to be activated then sends command to servo controller to lock door.
control.inBackground(function () {
    while (true) {
        control.waitForEvent(EventBusSource.MICROBIT_ID_IO_P2, EventBusValue.MICROBIT_BUTTON_EVT_DOWN)
        control.waitMicros(Wait)
        radio.sendNumber(2)
    }
})
