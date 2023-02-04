"""
Demo for dearpygui_animate add-on

https://github.com/mrtnRitter/DearPyGui_Animate

"""

import dearpygui.dearpygui as dpg

import dearpygui_animate as animate


# -----------------------------------------------------------------------------
# 				Render Callback
# -----------------------------------------------------------------------------


def onUpdate():
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

        dpg.set_value("running_animations", "animations running: " + str(running))

    else:
        dpg.set_value("running_animations", "animations running: 0")


# -----------------------------------------------------------------------------
# 				Main Menu Related
# -----------------------------------------------------------------------------

def show_buttons(sender, data):
    # shorthand to unhide items before running animation
    animate.add("opacity", "Info", 0, 1, [.64, .12, .72, .86], 20, timeoffset=10 / 60)
    animate.add("opacity", "Animate Position", 0, 1, [.64, .12, .72, .86], 20, timeoffset=15 / 60, early_callback=lambda sender, data: dpg.show_item("Animate Position"))
    animate.add("opacity", "Animate Size", 0, 1, [.64, .12, .72, .86], 20, timeoffset=20 / 60, early_callback=lambda sender, data: dpg.show_item("Animate Size"))
    animate.add("opacity", "Animate Opacity", 0, 1, [.64, .12, .72, .86], 20, timeoffset=25 / 60, early_callback=lambda sender, data: dpg.show_item("Animate Opacity"))


def gotoDemo(data):
    if data == "position":
        call = demo_position
    elif data == "size":
        call = demo_size
    elif data == "opacity":
        call = demo_opacity

    animate.add("position", "Demo", [562, 225], [20, 20], [.51, .05, .5, .9], 40)
    animate.add("size", "Demo", [156, 170], [156, 80], [.51, .05, .5, .9], 40)
    animate.add("opacity", "Demo", 1, 0.5, [.51, .05, .5, .9], 40, callback=call)


# -----------------------------------------------------------------------------
# 				Position Demo Related
# -----------------------------------------------------------------------------

def demo_position(sender, data):
    # default values
    dpg.delete_item("pos_info")
    dpg.add_text(tag="pos_info", default_value="Animations can be stagged,\nindividual values will add up", parent="Position Demo", before="spacing")
    dpg.set_item_pos("Position Demo", [1500, -100])
    animate.add("opacity", "Position Demo", 0, 1, [.51, .05, .5, .9], 1)
    dpg.show_item("Position Demo")

    # animations overlapping in time adding up their values
    animate.add("position", "Position Demo", [1280, -100], [200, -100], [.51, .05, .5, .9], 600)
    animate.add("position", "Position Demo", [1280, -100], [1280, 300], [.51, .05, .5, .9], 600)
    animate.add("position", "Position Demo", [1280, -100], [1000, 0], [.51, .05, .5, .9], 30)
    animate.add("position", "Position Demo", [0, 0], [50, 50], [.51, .05, .5, .9], 100, timeoffset=4)
    animate.add("position", "Position Demo", [0, 0], [200, 0], [.51, .05, .5, .9], 100, timeoffset=5)
    animate.add("position", "Position Demo", [0, 0], [0, 200], [.51, .05, .5, .9], 100, timeoffset=6)
    animate.add("position", "Position Demo", [0, 0], [0, -200], [.51, .05, .5, .9], 100, timeoffset=7)
    animate.add("position", "Position Demo", [0, 0], [500, -300], [.51, .05, .5, .9], 60, timeoffset=9)

    animate.add("position", "Position Demo", [670, 150], [500, 300], [.51, .05, .5, .9], 10, timeoffset=10)

    # animations cancel each other out, because they are exactly the same but with different directions
    animate.add("position", "Position Demo", [500, 300], [500, 0], [.51, .05, .5, .9], 300, timeoffset=11, early_callback=update_demo_position_text)
    animate.add("position", "Position Demo", [500, 300], [500, 600], [.51, .05, .5, .9], 300, timeoffset=11)

    animate.add("opacity", "Position Demo", 1, 0, [.51, .05, .5, .9], 20, timeoffset=18, callback=remove_pos_demo)


def update_demo_position_text(sender, data):
    dpg.delete_item("pos_info")
    dpg.add_text(tag="pos_info", default_value="Now two animations are\npulling against each other\n... really!", parent="Position Demo", before="spacing")


def remove_pos_demo(sender, data):
    dpg.hide_item("Position Demo")
    animate.add("position", "Demo", [20, 20], [562, 225], [.51, .05, .5, .9], 40)
    animate.add("size", "Demo", [156, 80], [156, 170], [.51, .05, .5, .9], 40)
    animate.add("opacity", "Demo", 0.5, 1, [.51, .05, .5, .9], 40)


# -----------------------------------------------------------------------------
# 				Size Demo Related
# -----------------------------------------------------------------------------

def demo_size(sender, data):
    # default values
    animate.add("opacity", "Size Demo", 1, 0, [.51, .05, .5, .9], 1)
    animate.add("size", "Size Demo", [220, 120], [220, 120], [.51, .05, .5, .9], 1)
    animate.add("position", "Size Demo", [530, 260], [530, 260], [.51, .05, .5, .9], 1)
    animate.add("size", "continued", [204, 20], [204, 20], [.51, .05, .5, .9], 1)
    animate.add("size", "paused", [204, 20], [204, 20], [.51, .05, .5, .9], 1)
    animate.add("size", "terminated", [204, 20], [204, 20], [.51, .05, .5, .9], 1)

    animate.add("opacity", "Size Demo", 0, 1, [.51, .05, .5, .9], 60, timeoffset=2 / 60, early_callback=lambda sender, data: dpg.show_item("Size Demo"))

    animate.add("size", "Size Demo", [220, 120], [500, 360], [.51, .05, .5, .9], 120, loop="ping-pong", name="size_loop")
    animate.add("position", "Size Demo", [530, 260], [390, 70], [.51, .05, .5, .9], 120, loop="ping-pong", name="pos_loop")
    animate.add("size", "continued", [204, 20], [484, 100], [.51, .05, .5, .9], 120, loop="ping-pong", name="size_loop_btn1")
    animate.add("size", "paused", [204, 20], [484, 100], [.51, .05, .5, .9], 120, loop="ping-pong", name="size_loop_btn2")
    animate.add("size", "terminated", [204, 20], [484, 100], [.51, .05, .5, .9], 120, loop="ping-pong", name="size_loop_btn3")

    animate.pause("size_loop")
    animate.pause("pos_loop")
    animate.pause("size_loop_btn1")
    animate.pause("size_loop_btn2")
    animate.pause("size_loop_btn3")


def cont(sender, data):
    animate.play("size_loop")
    animate.play("pos_loop")
    animate.play("size_loop_btn1")
    animate.play("size_loop_btn2")
    animate.play("size_loop_btn3")


def pause(sender, data):
    animate.pause("size_loop")
    animate.pause("pos_loop")
    animate.pause("size_loop_btn1")
    animate.pause("size_loop_btn2")
    animate.pause("size_loop_btn3")


def remove(sender, data):
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
    dpg.hide_item("Size Demo")
    animate.add("position", "Demo", [20, 20], [562, 225], [.51, .05, .5, .9], 40)
    animate.add("size", "Demo", [156, 80], [156, 170], [.51, .05, .5, .9], 40)
    animate.add("opacity", "Demo", 0.5, 1, [.51, .05, .5, .9], 40)


# -----------------------------------------------------------------------------
# 				Opacity Demo Related
# -----------------------------------------------------------------------------

def demo_opacity(sender, data):
    animate.add("opacity", "Opacity Demo1", 0, 1, [.51, .05, .5, .9], 60, timeoffset=2 / 60, early_callback=lambda sender, data: dpg.show_item("Opacity Demo1"), loop="ping-pong", name="top1")
    animate.add("opacity", "Opacity Demo2", 0, 1, [.51, .05, .5, .9], 60, timeoffset=22 / 60, early_callback=lambda sender, data: dpg.show_item("Opacity Demo2"), loop="ping-pong", name="top2")
    animate.add("opacity", "Opacity Demo3", 0, 1, [.51, .05, .5, .9], 60, timeoffset=42 / 60, early_callback=lambda sender, data: dpg.show_item("Opacity Demo3"), loop="ping-pong", name="top3")
    animate.add("opacity", "Opacity Demo4", 0, 1, [.51, .05, .5, .9], 60, timeoffset=62 / 60, early_callback=lambda sender, data: dpg.show_item("Opacity Demo4"), loop="ping-pong", name="top4")

    animate.add("opacity", "Loop1", 0.4, 1, [.51, .05, .5, .9], 10, timeoffset=122 / 60, loop="ping-pong", name="pp_loop")
    animate.add("position", "Loop1", [565, 800], [565, 300], [.51, .05, .5, .9], 30, timeoffset=125 / 60, early_callback=lambda sender, data: dpg.show_item("Loop1"))


def loop_cycle(sender, data):
    animate.add("position", "Loop1", [565, 300], [1500, 300], [.51, .05, .5, .9], 30, callback=lambda sender, data: dpg.hide_item("Loop1"))
    animate.remove("pp_loop")

    animate.add("opacity", "Loop2", 0, 1, [.51, .05, .5, .9], 30, timeoffset=1, early_callback=lambda sender, data: dpg.show_item("Loop2"))
    animate.add("size", "Loop2", [0, 0], [180, 120], [.06, .54, .11, .98], 85, timeoffset=1, loop="cycle", name="cycleloop_size")
    animate.add("position", "Loop2", [639, 339], [565, 300], [.06, .54, .11, .98], 85, timeoffset=1, loop="cycle", name="cycleloop_pos")


def loop_continue(sender, data):
    animate.remove("cycleloop_size")
    animate.remove("cycleloop_pos")

    x, y = dpg.get_item_pos("Loop2")
    animate.add("position", "Loop2", [x, y], [x, 800], [.06, .54, .11, .98], 20)
    animate.add("opacity", "Loop2", 1, 0, [.06, .54, .11, .98], 20, callback=lambda sender, data: dpg.hide_item("Loop2"))

    animate.add("position", "Loop3", [-300, 300], [-250, 300], [.01, .97, .1, .98], 30, loop="continue", callback=checkforEnd, name="cont_loop")
    dpg.show_item("Loop3")


def checkforEnd(sender, data):
    x = dpg.get_item_pos("Loop3")[0]

    if x > 1200:
        loop_close("Loop3", None)


def loop_close(sender, data):
    animate.remove("cont_loop")
    dpg.hide_item("Loop3")

    animate.remove("top1")
    animate.remove("top2")
    animate.remove("top3")
    animate.remove("top4")
    dpg.hide_item("Opacity Demo1")
    dpg.hide_item("Opacity Demo2")
    dpg.hide_item("Opacity Demo3")
    dpg.hide_item("Opacity Demo4")

    animate.add("position", "Demo", [20, 20], [562, 225], [.51, .05, .5, .9], 40)
    animate.add("size", "Demo", [156, 80], [156, 170], [.51, .05, .5, .9], 40)
    animate.add("opacity", "Demo", 0.5, 1, [.51, .05, .5, .9], 40)


# -----------------------------------------------------------------------------
# 					Windows
# -----------------------------------------------------------------------------

dpg.create_context()
dpg.create_viewport(title="dearpygui_animate    D E M O", width=1280, height=720)

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign, 0.5, 0.5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 7, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (128, 128, 128, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (15, 15, 15, 240), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (255, 255, 255, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (20, 20, 20, 240), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Border, (110, 110, 128, 128), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (51, 54, 56, 138), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (102, 102, 102, 102), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (46, 46, 46, 171), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (10, 10, 10, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (74, 74, 74, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, (0, 0, 0, 130), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (36, 36, 36, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (5, 5, 5, 135), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (79, 79, 79, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (105, 105, 105, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (130, 130, 130, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (240, 240, 240, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (130, 130, 130, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (219, 219, 219, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (112, 112, 112, 102), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (117, 120, 122, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (107, 107, 107, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Header, (179, 179, 179, 79), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (179, 179, 179, 204), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (122, 128, 133, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Separator, (110, 110, 128, 128), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, (184, 184, 184, 199), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, (130, 130, 130, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, (232, 232, 232, 64), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, (207, 207, 207, 171), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, (117, 117, 117, 242), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Tab, (46, 89, 148, 220), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (66, 150, 250, 204), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, (51, 105, 173, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, (17, 26, 38, 248), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, (35, 67, 108, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_DockingPreview, (66, 150, 250, 179), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_DockingEmptyBg, (51, 51, 51, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PlotLines, (156, 156, 156, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered, (255, 110, 89, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, (186, 153, 38, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PlotHistogramHovered, (255, 153, 0, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (222, 222, 222, 89), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_DragDropTarget, (255, 255, 0, 230), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_NavHighlight, (153, 153, 153, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_NavWindowingHighlight, (255, 255, 255, 179), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_NavWindowingDimBg, (204, 204, 204, 51), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, (204, 204, 204, 89), category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

with dpg.window(label="Demo", tag="Demo", width=36, height=32, min_size=[36, 32], no_resize=True, no_move=True, no_close=True, no_collapse=True, no_scrollbar=True):
    dpg.add_text("This demo will show \nsome basic functions\nof DearPyGui_Animate", tag="Info", parent="Demo", color=[255, 255, 255, 0])
    dpg.add_spacer(height=5, parent="Demo")
    dpg.add_button(tag="Animate Position", label="Animate Position", parent="Demo", width=140, callback=lambda: gotoDemo("position"))
    dpg.add_button(tag="Animate Size", label="Animate Size", parent="Demo", width=140, callback=lambda: gotoDemo("size"))
    dpg.add_button(tag="Animate Opacity", label="Animate Opacity", parent="Demo", width=140, callback=lambda: gotoDemo("opacity"))
    dpg.hide_item("Animate Position")
    dpg.hide_item("Animate Size")
    dpg.hide_item("Animate Opacity")

with dpg.window(label="Position Demo", tag="Position Demo", width=220, height=110, no_resize=True, no_move=True, no_close=True, no_collapse=True, no_scrollbar=True):
    dpg.add_text(tag="pos_info", default_value="Animations can be stagged,\nindividual values will add up")
    with dpg.group(tag="spacing"):
        dpg.add_spacer(height=3)
    dpg.add_text("", tag="running_animations")
    dpg.hide_item("Position Demo")

with dpg.window(label="Size Demo", tag="Size Demo", width=220, height=120, pos=[530, 260], no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, on_close=remove_size_demo):
    dpg.add_text("At any time animations can be", tag="size_info")
    dpg.add_button(label="continued", tag="continued", width=204, callback=cont)
    dpg.add_button(label="paused", tag="paused", width=204, callback=pause)
    dpg.add_button(label="terminated", tag="terminated", width=204, callback=remove)
    dpg.hide_item("Size Demo")

with dpg.window(tag="Opacity Demo1", width=150, height=80, min_size=[150, 80], pos=[300, 100], no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
    dpg.add_spacer(height=6)
    dpg.add_text(tag="op_info_1", default_value="    Animations")
    dpg.hide_item("Opacity Demo1")

with dpg.window(tag="Opacity Demo2", width=150, height=80, min_size=[150, 80], pos=[500, 100], no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
    dpg.add_spacer(height=6)
    dpg.add_text(tag="op_info_2", default_value="        can")
    dpg.hide_item("Opacity Demo2")

with dpg.window(tag="Opacity Demo3", width=150, height=80, min_size=[150, 80], pos=[700, 100], no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
    dpg.add_spacer(height=6)
    dpg.add_text(tag="op_info_3", default_value="        be")
    dpg.hide_item("Opacity Demo3")

with dpg.window(tag="Opacity Demo4", width=150, height=80, min_size=[150, 80], pos=[900, 100], no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
    dpg.add_spacer(height=6)
    dpg.add_text(tag="op_info_4", default_value="      looped")
    dpg.hide_item("Opacity Demo4")

with dpg.window(tag="Loop1", width=180, height=120, pos=[565, 300], no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
    dpg.add_text(tag="loop_info_1", default_value="       ping-pong")
    dpg.add_text(tag="loop_des_1", default_value="Moves from start to end,\nmoves back to start,\nrepeat")
    dpg.add_spacer(height=3)
    dpg.add_button(tag="next_loop_1", width=164, label="next", callback=loop_cycle)
    dpg.hide_item("Loop1")

with dpg.window(tag="Loop2", width=180, height=110, pos=[565, 300], no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
    dpg.add_text(tag="loop_info_2", default_value="         cycle")
    dpg.add_text(tag="loop_des_2", default_value="Moves from start to end,\nrepeat\n")
    dpg.add_spacer(height=7)
    dpg.add_button(tag="next_loop_2", width=164, label="next", callback=loop_continue)
    dpg.hide_item("Loop2")

with dpg.window(tag="Loop3", width=180, height=120, pos=[565, 300], no_resize=True, no_move=True, no_collapse=True, no_scrollbar=True, no_close=True, no_title_bar=True):
    dpg.add_text(tag="loop_info_3", default_value="        continue")
    dpg.add_text(tag="loop_des_3", default_value="Moves from start to end\ntakes end as start\nrepeats movement")
    dpg.add_spacer(height=3)
    dpg.add_button(tag="next_loop_3", width=164, label="close", callback=loop_close)
    dpg.hide_item("Loop3")

# Start Animation
animate.add("position", "Demo", [622, 800], [622, 304], [0, .06, .2, .99], 60)
animate.add("opacity", "Demo", 0, 1, [.57, .06, .61, .86], 60)
animate.add("size", "Demo", [36, 32], [156, 32], [0, .99, .47, 1], 30, timeoffset=1.5, callback=show_buttons)
animate.add("size", "Demo", [156, 32], [156, 170], [0, .65, .59, .92], 30, timeoffset=2)
animate.add("position", "Demo", [622, 304], [562, 304], [0, .99, .47, 1], 30, timeoffset=1.5)
animate.add("position", "Demo", [562, 304], [562, 225], [0, .65, .59, .92], 30, timeoffset=2)

dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    onUpdate()
    dpg.render_dearpygui_frame()
dpg.destroy_context()
