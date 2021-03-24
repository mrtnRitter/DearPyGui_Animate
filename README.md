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

```python
def add(type, object, startval, endval, ease, duration, **options)
```
Add/initialize an animation

Parameters:

type<br>
*&nbsp;&nbsp;&nbsp;&nbsp;str: type of animation: "position", "size", "opacity"</br>*
object</br>
*&nbsp;&nbsp;&nbsp;&nbsp;str: name of window/item which should receive the animation</br>*
startval</br>
*&nbsp;&nbsp;&nbsp;&nbsp;float (opacitiy only) or list [int,int]: starting value(s) for animation, item will be set to those when animation starts</br>*
endval</br>
*&nbsp;&nbsp;&nbsp;&nbsp;float (opacitiy only) or list [int,int]: end value(s) for animation</br>*
ease</br>
*&nbsp;&nbsp;&nbsp;&nbsp;list[float,float,float,float], parameters for bezier, see https://cubic-bezier.com/</br>*
duration</br>
*&nbsp;&nbsp;&nbsp;&nbsp;int, animation duration in frames, 60 = 1 second</br>*
options</br>
&nbsp;&nbsp;&nbsp;&nbsp;name</br>
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;str: name of animation</br>*
&nbsp;&nbsp;&nbsp;&nbsp;timeoffset</br>
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;float: delay of animation</br>*
&nbsp;&nbsp;&nbsp;&nbsp;loop</br>
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;str: type of loop: "ping-pong", "cycle", "continue"</br>*
&nbsp;&nbsp;&nbsp;&nbsp;callback</br>
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;callable, callback function executed after animation</br>*
&nbsp;&nbsp;&nbsp;&nbsp;callback_data</br>
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any, data for callback function</br>*
&nbsp;&nbsp;&nbsp;&nbsp;early_callback</br>
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;callable, callback function executed before animation</br>*
&nbsp;&nbsp;&nbsp;&nbsp;early_callback_data</br>
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any, data for early callback function</br>*




