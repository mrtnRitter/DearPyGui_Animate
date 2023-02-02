**DearPyGui_Animate** is an add-on written on top of [DearPyGUI](https://github.com/hoffstadt/DearPyGui) to make UI animations possible.

Tested for DearPyGui 1.x

<img src="https://raw.githubusercontent.com/mrtnRitter/DearPyGui_Animate/main/Animate.gif">

---

**Features:**
* add, delay, pause, continue, loop, remove animations
* get various animation data for best flow control
* animations are bezier driven to support every individual easing (see https://cubic-bezier.com/)
* partial animations will add up to one global animation
* support for callbacks when animation starts, as well as when animation ends
* support for position (windows only), size and opacity

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

only windows can be moved
> no DearPyGUI methods to set position for other items

actual minimum size for windows is 32x32
> windows cannot be smaller than this, but dearpygui_animate will handle smaller values ([0,0] will be translated to [32,32] automatically)

actual minimum size for items is 1x1 (tested for buttons only!)
> items cannot be smaller than this, but dearpygui_animate will handle smaller values ([0,0] will be translated to [1,1] automatically)

---

**Future:**

(no promise!)

* add methods for other properties
* add generators for sin, cos, rampup, down, random, wiggle, ...

---

*DearPyGUI_Animate* is licensed under the [MIT License](https://github.com/hoffstadt/DearPyGui/blob/master/LICENSE).
