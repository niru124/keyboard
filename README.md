# Grid

# Custom Mechanical Keyboard + DIY Ball Mouse

### Built Raspberry Pi Pico

This is a fully functional 75% mechanical keyboard and custom ball-style mouse, built entirely from scratch using PVC pipes, recycled hardware, and a Raspberry Pi Pico running [KMK](https://github.com/KMKfw/kmk_firmware). It supports layers, macros, mouse emulation, a physical scroll wheel, and multimedia controls. The custom mouse is inspired by Pimoroni's ball mouse, utilizing the sensor from an old mouse and a homemade housing.

---

## Overview

![Overview](https://github.com/user-attachments/assets/52b6bd99-0244-4220-a50f-818a910b2e3d)

## Demonstration

https://github.com/user-attachments/assets/9db709e7-7095-46e0-b96a-192f600a922a

[Watch the full demonstration video](media/scoll.gif) to see the keyboard and mouse in action.

---

## Features

### Keyboard

- 75% mechanical layout with full key support
- Layered keymaps (Default, Media, Macro, Utility)
- Multimedia and system controls:
  - Volume up/down, mute
  - Brightness control
  - Play/Pause
- Physical scroll wheel:
  - Scroll through documents or pages
  - Adjust brightness or volume on specific layers
- Mouse emulation using keyboard:
  - Cursor movement via Arrow keys or Vim-style (H, J, K, L)
  - Left and right click support
- Macro recording and playback:
  - Capture and repeat sequences of keystrokes

### Custom Ball Mouse

- Based on a Pimoroni-style ball mouse
- Uses the optical sensor and components from a repurposed classic mouse
- Mounted in a PVC or 3D printed housing
- Physical trackball for smooth cursor control
- Integrated buttons for left/right click

---

## Media

### Keyboard Overview

![Keyboard Overview](media/keyboard.jpg)

### Ball Mouse Overview

https://github.com/user-attachments/assets/8ce8e161-7ad3-4537-a2ac-65a79913d2dc

### Scroll Overview

https://github.com/user-attachments/assets/8ce8e161-7ad3-4537-a2ac-65a79913d2dc

### Scroll Overview

https://github.com/user-attachments/assets/29463b72-167c-47aa-b0aa-a0d087cd4fef

---

https://github.com/user-attachments/assets/fa0b53f4-1770-4ec0-8809-de2507b9c789

## Hardware Used

### Keyboard

- PVC pipe frame
- Raspberry Pi Pico
- Mechanical switches
- Keycaps
- Diodes (1N4148)
- Rotary encoder (for scroll wheel)
- Wires, solder, and prototype board
- KMK firmware running on CircuitPython

### Mouse

- Optical sensor and board from an old USB mouse
- Trackball (recycled from ball roller)
- PVC or 3D printed shell
- Tactile switches for buttons
- Connected via USB or directly to Pico

---
