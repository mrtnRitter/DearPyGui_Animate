"""
Demo for dearpygui_animate add-on

https://github.com/mrtnRitter/DearPyGui_Animate

"""

from dearpygui.core import *
from dearpygui.simple import *
import dearpygui_animate as animate


#-----------------------------------------------------------------------------
# 				Render Callback
#-----------------------------------------------------------------------------

def onUpdate(sender, data):
	"""
	render callback function
	"""
	animate.run()
	update_running_animations()
	


def update_running_animations():
	playing = animate.get("isplaying")
	
	if playing:
		running = 0
		
		for play in playing:
			if play:
				running += 1
				
		set_value("running_animations", "animations running: " + str(running))
	
	else:
		set_value("running_animations", "animations running: 0")	


#-----------------------------------------------------------------------------
# 				Main Menu Related
#-----------------------------------------------------------------------------

def show_buttons(sender, data):
	# shorthand to unhide items before running animation
	animate.add("opacity", "Info", 0, 1, [.64,.12,.72,.86], 20, timeoffset=10/60)
	animate.add("opacity", "Animate Position", 0, 1, [.64,.12,.72,.86], 20, timeoffset=15/60, early_callback=lambda sender, data: show_item("Animate Position"))
	animate.add("opacity", "Animate Size", 0, 1, [.64,.12,.72,.86], 20, timeoffset=20/60, early_callback=lambda sender, data: show_item("Animate Size"))
	animate.add("opacity", "Animate Opacity", 0, 1, [.64,.12,.72,.86], 20, timeoffset=25/60, early_callback=lambda sender, data: show_item("Animate Opacity"))



def gotoDemo(sender, data):	
	if data == "position":
		call = demo_position
	elif data == "size":
		call = demo_size
	elif data == "opacity":
		call = demo_opacity
		
	animate.add("position", "Demo", [562,225], [20,20], [.51,.05,.5,.9], 40)
	animate.add("size", "Demo", [156,170], [156,80], [.51,.05,.5,.9], 40)
	animate.add("opacity", "Demo", 1, 0.5, [.51,.05,.5,.9], 40, callback=call)


#-----------------------------------------------------------------------------
# 				Position Demo Related
#-----------------------------------------------------------------------------

def demo_position(sender, data):
	set_window_pos("Position Demo", 1500, -100)
	show_item("Position Demo")

	# animations overlapping in time adding up their values
	animate.add("position", "Position Demo", [1280, -100], [200,-100], [.51,.05,.5,.9], 600)
	animate.add("position", "Position Demo", [1280, -100], [1280,300], [.51,.05,.5,.9], 600)
	animate.add("position", "Position Demo", [1280, -100], [1000,0], [.51,.05,.5,.9], 30)
	animate.add("position", "Position Demo", [0,0], [50,50], [.51,.05,.5,.9], 100, timeoffset=4)
	animate.add("position", "Position Demo", [0,0], [200,0], [.51,.05,.5,.9], 100, timeoffset=5)
	animate.add("position", "Position Demo", [0,0], [0,200], [.51,.05,.5,.9], 100, timeoffset=6)
	animate.add("position", "Position Demo", [0,0], [0,-200], [.51,.05,.5,.9], 100, timeoffset=7)
	animate.add("position", "Position Demo", [0,0], [500,-300], [.51,.05,.5,.9], 60, timeoffset=9)
	
	animate.add("position", "Position Demo", [670,150], [500,300], [.51,.05,.5,.9], 10, timeoffset=10)
	
	# animations cancel each other out, because they are exactly the same but with different directions
	animate.add("position", "Position Demo", [500,300], [500,0], [.51,.05,.5,.9], 300, timeoffset=11, early_callback=update_demo_position_text)
	animate.add("position", "Position Demo", [500,300], [500,600], [.51,.05,.5,.9], 300, timeoffset=11)
	
	animate.add("opacity", "Position Demo", 1, 0, [.51,.05,.5,.9], 20, timeoffset=18, callback=remove_pos_demo)
	
	
def update_demo_position_text(sender, data):
	delete_item("pos_info")
	add_text("pos_info", default_value="Now two animations are\npulling against each other\n... really!", parent="Position Demo", before="spacing")


def remove_pos_demo(sender, data):
	hide_item("Position Demo")
	animate.add("position", "Demo", [20,20], [562,225], [.51,.05,.5,.9], 40)
	animate.add("size", "Demo", [156,80], [156,170], [.51,.05,.5,.9], 40)
	animate.add("opacity", "Demo", 0.5, 1, [.51,.05,.5,.9], 40)


#-----------------------------------------------------------------------------
# 				Size Demo Related
#-----------------------------------------------------------------------------

def demo_size(sender, data):
	# default values
	animate.add("opacity", "Size Demo", 1, 0, [.51,.05,.5,.9], 1)
	animate.add("size", "Size Demo", [220,120], [220,120], [.51,.05,.5,.9], 1)
	animate.add("position", "Size Demo", [530,260], [530,260], [.51,.05,.5,.9], 1)
	animate.add("size", "continued", [204,20], [204,20], [.51,.05,.5,.9], 1)
	animate.add("size", "paused", [204,20], [204,20], [.51,.05,.5,.9], 1)
	animate.add("size", "terminated", [204,20], [204,20], [.51,.05,.5,.9], 1)
	
	animate.add("opacity", "Size Demo", 0, 1, [.51,.05,.5,.9], 60, timeoffset= 2/60, early_callback=lambda sender, data: show_item("Size Demo"))
	
	animate.add("size", "Size Demo", [220,120], [500,360], [.51,.05,.5,.9], 120, loop="ping-pong", name="size_loop")
	animate.add("position", "Size Demo", [530, 260], [390, 70], [.51,.05,.5,.9], 120, loop="ping-pong", name="pos_loop")
	animate.add("size", "continued", [204,20], [484,100], [.51,.05,.5,.9], 120, loop="ping-pong", name="size_loop_btn1")
	animate.add("size", "paused", [204,20], [484,100], [.51,.05,.5,.9], 120, loop="ping-pong", name="size_loop_btn2")
	animate.add("size", "terminated", [204,20], [484,100], [.51,.05,.5,.9], 120, loop="ping-pong", name="size_loop_btn3")
		
	animate.pause("size_loop")
	animate.pause("pos_loop")
	animate.pause("size_loop_btn1")
	animate.pause("size_loop_btn2")
	animate.pause("size_loop_btn3")
	

def cont (sender, data):
	animate.play("size_loop")
	animate.play("pos_loop")
	animate.play("size_loop_btn1")
	animate.play("size_loop_btn2")
	animate.play("size_loop_btn3")	


def pause (sender, data):
	animate.pause("size_loop")
	animate.pause("pos_loop")
	animate.pause("size_loop_btn1")
	animate.pause("size_loop_btn2")
	animate.pause("size_loop_btn3")
	
	
def remove (sender, data):
	animate.remove("size_loop")
	animate.remove("pos_loop")
	animate.remove("size_loop_btn1")
	animate.remove("size_loop_btn2")
	animate.remove("size_loop_btn3")


def remove_size_demo(sender, data):
	animate.remove("size_loop")
	animate.remove("pos_loop")
	animate.remove("size_loop_btn1")
	animate.remove("size_loop_btn2")
	animate.remove("size_loop_btn3")
	hide_item("Size Demo")
	animate.add("position", "Demo", [20,20], [562,225], [.51,.05,.5,.9], 40)
	animate.add("size", "Demo", [156,80], [156,170], [.51,.05,.5,.9], 40)
	animate.add("opacity", "Demo", 0.5, 1, [.51,.05,.5,.9], 40)


#-----------------------------------------------------------------------------
# 				Opacity Demo Related
#-----------------------------------------------------------------------------

def demo_opacity(sender, data):
	animate.add("opacity", "Opacity Demo1", 0, 1, [.51,.05,.5,.9], 60, timeoffset= 2/60, early_callback=lambda sender, data: show_item("Opacity Demo1"), loop="ping-pong", name="top1")
	animate.add("opacity", "Opacity Demo2", 0, 1, [.51,.05,.5,.9], 60, timeoffset= 22/60, early_callback=lambda sender, data: show_item("Opacity Demo2"), loop="ping-pong", name="top2")
	animate.add("opacity", "Opacity Demo3", 0, 1, [.51,.05,.5,.9], 60, timeoffset= 42/60, early_callback=lambda sender, data: show_item("Opacity Demo3"), loop="ping-pong", name="top3")
	animate.add("opacity", "Opacity Demo4", 0, 1, [.51,.05,.5,.9], 60, timeoffset= 62/60, early_callback=lambda sender, data: show_item("Opacity Demo4"), loop="ping-pong", name="top4")
	
	animate.add("opacity", "Loop1", 0.4, 1, [.51,.05,.5,.9], 10, timeoffset= 122/60, loop="ping-pong", name ="pp_loop")
	animate.add("position", "Loop1", [565,800], [565,300], [.51,.05,.5,.9], 30, timeoffset= 125/60, early_callback=lambda sender, data: show_item("Loop1"))


def loop_cycle(sender, data):
	animate.add("position", "Loop1", [565,300], [1500,300], [.51,.05,.5,.9], 30, callback=lambda sender, data: hide_item("Loop1"))
	animate.remove("pp_loop")
	
	animate.add("opacity", "Loop2", 0, 1, [.51,.05,.5,.9], 30, timeoffset= 1, early_callback=lambda sender, data: show_item("Loop2"))
	animate.add("size", "Loop2", [0,0], [180,110], [.06,.54,.11,.98], 85, timeoffset= 1, loop="cycle", name="cycleloop_size")
	animate.add("position", "Loop2", [639,339], [565,300], [.06,.54,.11,.98], 85, timeoffset= 1, loop="cycle", name="cycleloop_pos")
	
	
	
def loop_continue(sender, data):
	animate.remove("cycleloop_size")
	animate.remove("cycleloop_pos")
	
	x,y = get_window_pos("Loop2")
	animate.add("position", "Loop2", [x,y], [x, 800], [.06,.54,.11,.98], 20)
	animate.add("opacity", "Loop2", 1,0, [.06,.54,.11,.98], 20, callback=lambda sender, data: hide_item("Loop2"))
	
	animate.add("position", "Loop3", [-300, 300], [-250,300], [.01,.97,.1,.98], 30, loop="continue", callback=checkforEnd, name="cont_loop")
	show_item("Loop3")
	
	
def checkforEnd(sender, data):
	x = get_window_pos("Loop3")[0]
	
	if x > 1200:
		loop_close("Loop3", None)

def loop_close(sender, data):
	animate.remove("cont_loop")
	hide_item("Loop3")
	
	animate.remove("top1")
	animate.remove("top2")
	animate.remove("top3")
	animate.remove("top4")
	hide_item("Opacity Demo1")
	hide_item("Opacity Demo2")
	hide_item("Opacity Demo3")
	hide_item("Opacity Demo4")
	
	animate.add("position", "Demo", [20,20], [562,225], [.51,.05,.5,.9], 40)
	animate.add("size", "Demo", [156,80], [156,170], [.51,.05,.5,.9], 40)
	animate.add("opacity", "Demo", 0.5, 1, [.51,.05,.5,.9], 40)
	
	

#-----------------------------------------------------------------------------
# 					Windows
#-----------------------------------------------------------------------------	

with window("Main"):
	set_main_window_title("dearpygui_animate    D E M O")
	set_main_window_size(1280,720)
	set_main_window_pos(960-640,600-360)
	set_main_window_resizable(False)
	set_theme("Dark Grey")
	set_style_window_title_align(0.5,0.5)


with window("Demo", width=36, height=32, no_resize=True, no_move=True, no_close=True, no_collapse=True, no_scrollbar=True):
	pass
	
with window("Position Demo", width = 220, height = 100, no_resize=True, no_move=True, no_close=True, no_collapse=True, no_scrollbar=True):
	add_text("pos_info", default_value="Animations can be stagged,\nindividual values will add up")
	add_spacing(count=3, name="spacing")
	add_text("position status", source="running_animations")
	add_text("Info", default_value="This demo will show \nsome basic functions\nof DearPyGui_Animate", parent="Demo", color=[255,255,255,0])
	add_spacing(count=5, parent="Demo")
	add_button("Animate Position", parent="Demo", width=140, callback=gotoDemo, callback_data="position")
	add_button("Animate Size", parent="Demo", width=140, callback=gotoDemo, callback_data="size")
	add_button("Animate Opacity", parent="Demo", width=140, callback=gotoDemo, callback_data="opacity")
	hide_item("Animate Position")
	hide_item("Animate Size")
	hide_item("Animate Opacity")
	hide_item("Position Demo")

with window("Size Demo", width = 220, height = 120, x_pos = 530, y_pos = 260, no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, on_close=remove_size_demo):
	add_text("size_info", default_value="At any time animations can be")
	add_button("continued", width=204, callback=cont)
	add_button("paused", width=204, callback=pause)
	add_button("terminated", width=204, callback=remove)
	hide_item("Size Demo")

with window("Opacity Demo1", width = 150, height = 80, x_pos = 300, y_pos = 100, no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
	add_spacing(count=6, name="1")
	add_text("op_info_1", default_value="    Animations")
	hide_item("Opacity Demo1")
	
with window("Opacity Demo2", width = 150, height = 80, x_pos = 500, y_pos = 100, no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
	add_spacing(count=6, name="2")
	add_text("op_info_2", default_value="        can")
	hide_item("Opacity Demo2")
	
with window("Opacity Demo3", width = 150, height = 80, x_pos = 700, y_pos = 100, no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
	add_spacing(count=6, name="3")
	add_text("op_info_3", default_value="        be")
	hide_item("Opacity Demo3")
	
with window("Opacity Demo4", width = 150, height = 80, x_pos = 900, y_pos = 100, no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
	add_spacing(count=6, name="4")
	add_text("op_info_4", default_value="      looped")
	hide_item("Opacity Demo4")

with window("Loop1", width = 180, height = 110, x_pos = 565, y_pos = 300, no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
	add_text("loop_info_1", default_value="       ping-pong")
	add_text("loop_des_1", default_value="Moves from start to end,\nmoves back to start,\nrepeat")
	add_spacing(count=3, name="5")
	add_button("next_loop_1", width=164,label="next", callback=loop_cycle)
	hide_item("Loop1")

with window("Loop2", width = 180, height = 110, x_pos = 565, y_pos = 300, no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
	add_text("loop_info_2", default_value="         cycle")
	add_text("loop_des_2", default_value="Moves from start to end,\nrepeat\n")
	add_spacing(count=7, name="6")
	add_button("next_loop_2", width=164,label="next", callback=loop_continue)
	hide_item("Loop2")
	
with window("Loop3", width = 180, height = 110, x_pos = 565, y_pos = 300, no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
	add_text("loop_info_3", default_value="        continue")
	add_text("loop_des_3", default_value="Moves from start to end\ntakes end as start\nrepeats movement")
	add_spacing(count=3, name="7")
	add_button("next_loop_3", width=164,label="close", callback=loop_close)
	hide_item("Loop3")



# Startup Animation
animate.add("position", "Demo", [622,800], [622, 304], [0,.06,.2,.99], 60)
animate.add("opacity", "Demo", 0, 1, [.57,.06,.61,.86], 60)
animate.add("size", "Demo", [36,32], [156,32], [0,.99,.47,1], 30, timeoffset=1.5, callback=show_buttons)
animate.add("size", "Demo", [156,32], [156,170], [0,.65,.59,.92], 30, timeoffset=2)
animate.add("position", "Demo", [622, 304], [562, 304], [0,.99,.47,1], 30, timeoffset=1.5)
animate.add("position", "Demo", [562, 304], [562, 225], [0,.65,.59,.92], 30, timeoffset=2)


add_value("running_animations", "0")
set_render_callback(onUpdate)
start_dearpygui(primary_window="Main")
