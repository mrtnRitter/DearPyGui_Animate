**DearPyGui_Animate** is an add-on written on top of [DearPyGUI](https://github.com/hoffstadt/DearPyGui) to make UI animations possible.

Updated and tested for DearPyGui 1.8.0 thanks to [IvanNazaruk](https://github.com/IvanNazaruk).

<img src="https://raw.githubusercontent.com/mrtnRitter/DearPyGui_Animate/main/Animate.gif">

---

**Features:**
* add, delay, pause, continue, loop, remove animations
* get various animation data for best flow control
* animations are bezier driven to support every individual easing (see https://cubic-bezier.com/)
* partial animations will add up to one global animation
* support for callbacks when animation starts, as well as when animation ends
* support for position, size and opacity

---


**Setup:**

```python
import dearpygui.dearpygui as dpg
import dearpygui_animate as animate

dpg.create_context()
dpg.create_viewport(title="dearpygui_animate    D E M O", width=1280, height=720)

with dpg.window(label="Demo", tag="Demo", width=200, height=100):
    dpg.add_text("Hello World!")

animate.add("position", "Demo", [622, 800], [622, 304], [0, .06, .2, .99], 60)
animate.add("opacity", "Demo", 0, 1, [.57, .06, .61, .86], 60)

dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    animate.run()
    dpg.render_dearpygui_frame()
dpg.destroy_context()

``` 

---

**Usage:**

Please see the [Demo](https://github.com/mrtnRitter/DearPyGui_Animate/blob/main/DearPyGui_Animate/dearpygui_animate_demo.py) for some examples of how DearPyGui_Animate can be used.

---

**API:**

See [Wiki](https://github.com/mrtnRitter/DearPyGui_Animate/wiki)

---

**Known limitations:**

actual minimum size for windows is 32x32
> windows cannot be smaller than this, but dearpygui_animate will handle smaller values ([0,0] will be translated to [32,32] automatically)

actual minimum size for items is 1x1 (tested for buttons only!)
> items cannot be smaller than this, but dearpygui_animate will handle smaller values ([0,0] will be translated to [1,1] automatically)

---
**Bugs:**

If there is a theme that is attached not only to a changeable/animated object, then other objects will change their values.
To reproduce:

```python
import dearpygui.dearpygui as dpg

import dearpygui_animate as animate

dpg.create_context()
dpg.create_viewport()

with dpg.theme() as button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 255, 0, 255), category=dpg.mvThemeCat_Core)

with dpg.window():
    btn1 = dpg.add_button(label="Test 1")
    btn2 = dpg.add_button(label="Test 2")

    dpg.bind_item_theme(btn1, button_theme)
    dpg.bind_item_theme(btn2, button_theme)

animate.add("opacity", btn1, 0, 1, [.57, .06, .61, .86], 60, loop="ping-pong")

dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    animate.run()
    dpg.render_dearpygui_frame()
dpg.destroy_context()
```
![0](https://user-images.githubusercontent.com/46572469/216398135-8d8ab4a8-2d07-4cb7-9b6c-a0766fe8f52b.gif)

#### The workaround is to wrap each future animated object into a group:
```python
import dearpygui.dearpygui as dpg

import dearpygui_animate as animate

dpg.create_context()
dpg.create_viewport()

with dpg.theme() as button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 255, 0, 255), category=dpg.mvThemeCat_Core)

with dpg.window():
    with dpg.group() as btn1_group:
        btn1 = dpg.add_button(label="Test 1")
    btn2 = dpg.add_button(label="Test 2")

    dpg.bind_item_theme(btn1, button_theme)
    dpg.bind_item_theme(btn2, button_theme)

animate.add("opacity", btn1_group, 0, 1, [.57, .06, .61, .86], 60, loop="ping-pong")

dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    animate.run()
    dpg.render_dearpygui_frame()
dpg.destroy_context()
```
![0](https://user-images.githubusercontent.com/46572469/216398380-faae36b5-6cbc-455f-a0f8-0890db0d8347.gif)


Unfortunately for `dpg.window()` you need to create a new theme


---

*DearPyGUI_Animate* is licensed under the [MIT License](https://github.com/hoffstadt/DearPyGui/blob/master/LICENSE).
