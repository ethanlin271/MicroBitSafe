// Reads radio commands to decide what to do with servo.
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        servos.P0.setAngle(0)
    } else if (receivedNumber == 2) {
        servos.P0.setAngle(90)
    }
})
// Initializes radio.
radio.setGroup(121)
