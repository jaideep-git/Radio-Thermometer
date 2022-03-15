radio.onReceivedNumber(function (receivedNumber) {
    oustsideTemperature = receivedNumber
})
input.onButtonPressed(Button.A, function () {
    displayArrow = false
    basic.clearScreen()
    basic.showNumber(minTemp)
    temperatureUnit.scrollImage(1, 200)
    displayArrow = true
})
input.onButtonPressed(Button.B, function () {
    displayArrow = false
    basic.clearScreen()
    basic.showNumber(oustsideTemperature)
    temperatureUnit.scrollImage(1, 200)
    basic.clearScreen()
    displayArrow = true
})
let oustsideTemperature = 0
let temperatureUnit: Image = null
let minTemp = 0
let displayArrow = false
radio.setGroup(1)
displayArrow = true
let currentTemp = input.temperature()
minTemp = currentTemp
temperatureUnit = images.createBigImage(`
    . # . . . # # . . .
    # . # . # . . . . .
    . # . . # . . . . .
    . . . . # . . . . .
    . . . . . # # . . .
    `)
basic.forever(function () {
    radio.sendNumber(input.temperature())
    if (displayArrow == true) {
        currentTemp = input.temperature()
        if (currentTemp < minTemp) {
            minTemp = currentTemp
        }
        if (input.temperature() < 15) {
            basic.showArrow(ArrowNames.South)
            basic.pause(5000)
            basic.clearScreen()
            basic.showNumber(input.temperature())
            temperatureUnit.scrollImage(1, 200)
        } else {
            basic.showArrow(ArrowNames.North)
            basic.pause(5000)
            basic.clearScreen()
            basic.showNumber(input.temperature())
            temperatureUnit.scrollImage(1, 200)
        }
    }
})
