**DearPyGui_Animate** is an add-on written on top of [DearPyGUI](https://github.com/hoffstadt/DearPyGui) to make UI animations possible.

**Features:**
* add, delay, pause, continue, loop, remove animations
* get various animation data for best flow control
* animations are bezier driven for every individual easing (see https://cubic-bezier.com/)
* partial animations will add up to one global animtion
* support for callbacks when animation starts, as well as when animation ends
* support for position (windows only), size and opacity

---


**Setup:**

```python
from dearpygui.core import *
from dearpygui.simple import *
import dearpygui_animate as animate

with window("Main"):
	set_main_window_title("dearpygui_animate    D E M O")
	set_main_window_size(1280,720)
  
with window("Demo", width=200, height=100, no_resize=True, no_move=True, no_close=True, no_collapse=True, no_scrollbar=True):
	add_text("Info", default_value="Hello World!", parent="Demo")
  
animate.add("position", "Demo", [622,800], [622, 304], [0,.06,.2,.99], 60)
animate.add("opacity", "Demo", 0, 1, [.57,.06,.61,.86], 60)

set_render_callback(animate.run)
start_dearpygui(primary_window="Main")

``` 

---

**API:**

See [Wiki](https://github.com/mrtnRitter/DearPyGui_Animate/wiki)

---

**Known limitations:**

* only windows can be moved
<br>&nbsp;&nbsp;&nbsp; no DearPyGUI methods to set position for other items

* actual minimum size for windows is 32x32
<br>&nbsp;&nbsp;&nbsp; windows cannot be smaller than this, but dearpygui_animate will handle smaller values ([0,0] will be translated to [32,32] automatically)

* actual minimum size for items is 1x1 (tested for buttons only!)
<br>&nbsp;&nbsp;&nbsp; items cannot be smaller than this, but dearpygui_animate will handle smaller values ([0,0] will be translated to [1,1] automatically)

---

**Future:**

(no promise!)

* add methods for other properties
* add generators for sin, cos, rampup, down, random, wiggle, ...

---

*DearPyGUI_Animate* is licensed under the [MIT License](https://github.com/hoffstadt/DearPyGui/blob/master/LICENSE).
