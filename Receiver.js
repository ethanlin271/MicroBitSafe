// Plays alarm if alarm sequence is received.
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 3) {
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . # . .
            `)
        music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.Forever)
    }
})
// Monitors condition of a flag variable to decide either to add the letter a to the entered password or display the safe password one digit at a time.
input.onButtonPressed(Button.A, function () {
    if (Flag == 0) {
        Entered = "" + Entered + "A"
        basic.showString("A")
    } else {
        if (Count < password.length) {
            basic.showString("" + (password[Count]))
            Count += 1
        } else {
            basic.clearScreen()
            Count = 0
        }
    }
})
// Checks entered password against password.
input.onButtonPressed(Button.AB, function () {
    if (thisPass == Entered) {
        basic.showIcon(IconNames.Yes)
        basic.pause(1000)
        basic.clearScreen()
        Flag = 1
        Entered = ""
    } else {
        basic.showIcon(IconNames.No)
        basic.pause(1000)
        basic.clearScreen()
        Entered = ""
    }
})
// Receives password string.
radio.onReceivedString(function (receivedString) {
    password = receivedString
})
// Monitors condition of a flag variable to either add the letter b to a password sequence or clear the screen and stop all sounds.
input.onButtonPressed(Button.B, function () {
    if (Flag == 0) {
        Entered = "" + Entered + "B"
        basic.showString("B")
    } else {
        basic.clearScreen()
        music.stopAllSounds()
    }
})
// Initializes some values.
let Flag = 0
let Entered = ""
let thisPass = ""
let password = ""
let Count = 0
radio.setGroup(121)
Count = 0
password = ""
thisPass = "ABABAB"
Entered = ""
