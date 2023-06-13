# Reads radio commands to decide what to do with servo.

def on_received_number(receivedNumber):
    if receivedNumber == 1:
        servos.P0.set_angle(0)
    elif receivedNumber == 2:
        servos.P0.set_angle(90)
radio.on_received_number(on_received_number)

# Initializes radio.
radio.set_group(121)
