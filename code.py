import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros
from kmk.modules.tapdance import TapDance
from kmk.extensions.statusled import statusLED
from kmk.modules.holdtap import HoldTap
from kmk.modules.dynamic_sequences import DynamicSequences
from kmk.modules.rapidfire import RapidFire




# Define the pins for the two LEDs
statusLED = statusLED(led_pins=[board.GP18, board.GP28])

dynamicSequences = DynamicSequences(
    slots=1, # The number of sequence slots to use
    timeout=60000,  # Maximum time to spend in record or config mode before stopping automatically, milliseconds
    key_interval=500,  # Milliseconds between key events while playing
    use_recorded_speed=False  # Whether to play the sequence at the speed it was typed
)

mousekeys = MouseKeys(
    max_speed = 1500,
    acc_interval =10, # Delta ms to apply acceleration
    move_step = 8
)

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
# Add the statusLED extension to the keyboard
keyboard.extensions.append(statusLED)
layers = Layers()
holdtap = HoldTap()
keyboard.modules.append(holdtap)
keyboard.modules.append(DynamicSequences())
keyboard.modules.append(RapidFire())

tapdance = TapDance()
tapdance.tap_time = 300
keyboard.modules.append(tapdance)
keyboard.modules.append(Macros())

keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14,board.GP15
)
keyboard.row_pins = (board.GP27, board.GP26, board.GP22, board.GP19, board.GP21, board.GP20)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

encoder_handler.pins = ((board.GP16, board.GP17, None,False,2),)

# Layers
LYR_STD, LYR_EXT,LYR_NUM= 0,1,2
# MT_EXT = KC.MO(LYR_EXT)


# Immediately toggle repeatedly sending Enter every 50 milliseconds on tap
MUP = KC.RF(KC.MS_UP,toggle=False, timeout=0, interval=50)
MDOWN = KC.RF(KC.MS_DN,toggle=False, timeout=0, interval=50)
ML = KC.RF(KC.MS_LT,toggle=False, timeout=0, interval=50)
MR = KC.RF(KC.MS_RT,toggle=False, timeout=0, interval=50)

# Tap Dance Actions
EXAMPLE_TD = KC.TD(
    KC.STOP_SEQUENCE(),             # Single tap does nothing (or transparent)
    KC.TG(LYR_EXT),      # Double tap toggles to the second layer
) 
# MOUSI=KC.HT(KC.STOP_SEQUENCE(),KC.MO(LYR_EXT))
MOUSI_TWO=KC.HT(EXAMPLE_TD,KC.MO(LYR_EXT))
MOUSI_THREE=KC.HT(KC.MB_RMB,KC.MO(LYR_EXT))
#LALU= KC.HT(KC.RGUI,KC.LCTL)
LALU=KC.HT(KC.LSFT,KC.MO(LYR_NUM)) 

LCTL = KC.HT(KC.A, KC.LCTRL)
LSUP = KC.HT(KC.D, KC.RGUI)
LAL= KC.HT(KC.ESC,KC.LALT)
# Keymap

keyboard.keymap = [        			
    # Standard (ISO) Layer
    [
        KC.CAPS, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL, KC.PLAY_SEQUENCE(), KC.PSCR,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.NO, KC.PGUP,
        KC.TAB, KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLASH, KC.PGDOWN,
        LAL, KC.NO, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.NO, KC.RECORD_SEQUENCE(),
        KC.LSFT, KC.NO, KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, LALU, KC.UP,EXAMPLE_TD,
        KC.LCTL, KC.NO, KC.LGUI, KC.LALT, KC.MB_LMB,MOUSI_THREE, KC.SPC, KC.NO, KC.NO, KC.RALT,MOUSI_TWO,KC.NO,KC.NO,KC.LEFT, KC.DOWN, KC.RGHT,
    ],	
    # Extra Keys Layer
    [
        KC.TRNS, KC.TRNS, KC.MPLY, KC.BRIU, KC.BRID, KC.MUTE, KC.VOLD, KC.VOLU, KC.MPLY, KC.F9, KC.F10, KC.F11, KC.F12, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.F2, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MB_MMB, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MS_LT, KC.MS_DN, KC.MS_UP, KC.MS_RT, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.MS_UP, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.MS_LT, KC.MS_DN, KC.MS_RT,
    ],		
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRANS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRANS, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, LALU,KC.TRANS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS, KC.TRNS, KC.TRNS,
    ],
    
    # [
    #     KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL, KC.HOME, KC.PSCR,
    #     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO, KC.TRNS,
    #     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    #     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    #     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.MS_UP, KC.TRNS,
    #     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MS_LT, KC.MS_DN, KC.MS_RT,
    # ],
]

# Encoder Mapping
#Zoom_in = KC.LCTRL(KC.LSFT(KC.EQUAL))
#Zoom_out = KC.LCTRL(KC.LSFT(KC.MINUS))

# WRK_right = KC.LALT(KC.M)
# WRK_left = KC.LALT(KC.N)

encoder_handler.map = [
   ((KC.MW_UP, KC.MW_DOWN),),  # Standard Layer
  ((KC.VOLU, KC.VOLD),),  # Extra Layer
#   ((Zoom_out, Zoom_in),),  # Extra Keys Layer
    # ((WRK_right, WRK_left),),
    
]

if __name__ == '__main__':
        keyboard.go()   		
