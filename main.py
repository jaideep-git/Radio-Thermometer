def on_received_number(receivedNumber):
    global oustsideTemperature
    oustsideTemperature = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global displayArrow
    displayArrow = False
    basic.clear_screen()
    basic.show_number(minTemp)
    temperatureUnit.scroll_image(1, 200)
    displayArrow = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global displayArrow
    displayArrow = False
    basic.clear_screen()
    basic.show_number(oustsideTemperature)
    temperatureUnit.scroll_image(1, 200)
    basic.clear_screen()
    displayArrow = True
input.on_button_pressed(Button.B, on_button_pressed_b)

oustsideTemperature = 0
temperatureUnit: Image = None
minTemp = 0
displayArrow = False
radio.set_group(1)
displayArrow = True
currentTemp = input.temperature()
minTemp = currentTemp
temperatureUnit = images.create_big_image("""
    . # . . . # # . . .
        # . # . # . . . . .
        . # . . # . . . . .
        . . . . # . . . . .
        . . . . . # # . . .
""")

def on_forever():
    global currentTemp, minTemp
    radio.send_number(input.temperature())
    if displayArrow == True:
        currentTemp = input.temperature()
        if currentTemp < minTemp:
            minTemp = currentTemp
        if input.temperature() < 15:
            basic.show_arrow(ArrowNames.SOUTH)
            basic.pause(5000)
            basic.clear_screen()
            basic.show_number(input.temperature())
            temperatureUnit.scroll_image(1, 200)
        else:
            basic.show_arrow(ArrowNames.NORTH)
            basic.pause(5000)
            basic.clear_screen()
            basic.show_number(input.temperature())
            temperatureUnit.scroll_image(1, 200)
basic.forever(on_forever)
