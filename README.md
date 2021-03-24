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
``` 
