import board
from analogio import AnalogIn

from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.analogin import AnalogInput, AnalogInputs
from kmk.modules.analogin.keys import AnalogKey
from kmk.keys import KC

keyboard = KMKKeyboard()

# Configure analog inputs for X and Y axes
x_axis = AnalogInput(AnalogIn(board.A1))
y_axis = AnalogInput(AnalogIn(board.A2))

# Define threshold for movement detection (0–255)
THRESHOLD_LOW = 100     # Stick pulled down/left
THRESHOLD_HIGH = 155    # Stick pushed up/right
CENTER = 127            # Midpoint

# Create AnalogKeys: one for each direction
analog = AnalogInputs(
    inputs=[x_axis, y_axis],
    evtmap=[
        # Layer 0: X-axis (left/right), Y-axis (up/down)
        [
            AnalogKey(KC.A, threshold=THRESHOLD_LOW),   # X < 100 → A (left)
            AnalogKey(KC.W, threshold=THRESHOLD_HIGH),  # Y > 155 → W (up)
        ],
        [
            AnalogKey(KC.D, threshold=THRESHOLD_HIGH),  # X > 155 → D (right)
            AnalogKey(KC.S, threshold=THRESHOLD_LOW),   # Y < 100 → S (down)
        ]
    ]
)

keyboard.modules.append(analog)

# CLICK
# from digitalio import DigitalInOut, Pull
#
# z_button = DigitalInOut(board.D5)  # adjust pin as needed
# z_button.switch_to_input(pull=Pull.UP)
#
# def check_z_press():
#     if not z_button.value:  # Button is pressed
#         keyboard.press(KC.ENTER)
#     else:
#         keyboard.release(KC.ENTER)
#
