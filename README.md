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
