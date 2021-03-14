def on_microbit_id_button_a_evt_down():
    global Score_A, Score_B, New
    if New == 1:
        if True:
            if X >= 2:
                Score_A += 1
                if Score_A >= 10:
                    Score_A = 0
                    Score_B = 0
                    basic.show_string("A")
                    basic.pause(2000)
                    basic.show_leds("""
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        """)
            else:
                Score_A += -1
            serial.write_number(Score_A)
            New = 0
            led.unplot(X, Y)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_A,
    EventBusValue.MICROBIT_BUTTON_EVT_DOWN,
    on_microbit_id_button_a_evt_down)

def on_microbit_id_button_b_evt_down():
    global Score_B, Score_A, New
    if New == 1:
        if True:
            if X <= 2:
                Score_B += 1
                if Score_B >= 10:
                    Score_B = 0
                    Score_A = 0
                    basic.show_string("B")
                    basic.pause(2000)
                    basic.show_leds("""
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        """)
            else:
                Score_B += -1
            serial.write_number(Score_B)
            New = 0
            led.unplot(X, Y)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_B,
    EventBusValue.MICROBIT_BUTTON_EVT_DOWN,
    on_microbit_id_button_b_evt_down)

Y = 0
Score_B = 0
Score_A = 0
X = 0
New = 0
basic.show_leds("""
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    """)
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)

def on_forever():
    global X, Y, New
    if not (New):
        X = randint(0, 4)
        Y = randint(0, 4)
        led.plot(X, Y)
        New = 1
basic.forever(on_forever)

def on_in_background():
    pass
control.in_background(on_in_background)
