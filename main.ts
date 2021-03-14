control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_A, EventBusValue.MICROBIT_BUTTON_EVT_DOWN, function () {
    if (New == 1) {
        if (true) {
            if (X >= 2) {
                Score_A += 1
                if (Score_A >= 10) {
                    Score_A = 0
                    Score_B = 0
                    basic.showString("A")
                    basic.pause(1000)
                    basic.showLeds(`
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        `)
                }
            } else {
                Score_A += -1
            }
            serial.writeNumber(Score_A)
            New = 0
            led.unplot(X, Y)
        }
    }
})
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_B, EventBusValue.MICROBIT_BUTTON_EVT_DOWN, function () {
    if (New == 1) {
        if (true) {
            if (X <= 2) {
                Score_B += 1
                if (Score_B >= 10) {
                    Score_B = 0
                    Score_A = 0
                    basic.showString("B")
                    basic.pause(1000)
                    basic.showLeds(`
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        `)
                }
            } else {
                Score_B += -1
            }
            serial.writeNumber(Score_B)
            New = 0
            led.unplot(X, Y)
        }
    }
})
let Y = 0
let Score_B = 0
let Score_A = 0
let X = 0
let New = 0
basic.showLeds(`
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    `)
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate115200
)
basic.forever(function () {
    if (!(New)) {
        X = randint(0, 4)
        Y = randint(0, 4)
        led.plot(X, Y)
        New = 1
    }
})
