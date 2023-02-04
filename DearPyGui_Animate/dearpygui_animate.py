"""
---------------------------------------------
dearpygui animations add-on

https://github.com/mrtnRitter/DearPyGui_Animate

v0.12
----------------------------------------------
"""

# -----------------------------------------------------------------------------
# 				Imports
# -----------------------------------------------------------------------------

import dearpygui.dearpygui as dpg

# -----------------------------------------------------------------------------
# 				Global Registers
# -----------------------------------------------------------------------------

animations = []
delta_positions = []
delta_sizes = []
delta_opacities = []

# -----------------------------------------------------------------------------
# 				Main Functions
# -----------------------------------------------------------------------------

def add(type, object, startval, endval, ease, duration, **kwargs):
    """
    adds a new animation to animations register
    """

    # fix min-values: smallest size window = 32x32, smallest size item = 1x1
    if type == "size":
        if dpg.get_item_type(object) == "mvAppItemType::Window":
            for i in range(2):
                if startval[i] < 32:
                    startval[i] = 32

                elif endval[i] < 32:
                    endval[i] = 32
        else:
            for i in range(2):
                if startval[i] < 1:
                    startval[i] = 1

                elif endval[i] < 1:
                    endval[i] = 1

    # rewrite endval to distance, all calculations are based on distance
    try:
        distance = [endval[0] - startval[0], endval[1] - startval[1]]
    except Exception:
        distance = endval - startval

    options = {
        "name": "",
        "timeoffset": 0,
        "loop": "",
        "callback": "",
        "callback_data": "",
        "early_callback": "",
        "early_callback_data": ""
    }
    options.update(kwargs)

    starttime = dpg.get_total_time() + options["timeoffset"]
    framecounter = 0
    last_ease = 0
    loopcounter = 0
    isplaying = False
    ispaused = False
    isreversed = False

    new_animation = [
        options["name"],
        type,
        object,
        startval,
        distance,
        ease,
        duration,
        starttime,
        framecounter,
        last_ease,
        options["loop"],
        loopcounter,
        options["callback"],
        options["callback_data"],
        options["early_callback"],
        options["early_callback_data"],
        isplaying,
        ispaused,
        isreversed
    ]

    global animations
    animations.append(new_animation)


def run():
    """
    Animation data-set layout:

    animation[0] = animation name
    animation[1] = animation type
    animation[2] = object name
    animation[3] = start value
    animation[4] = distance
    animation[5] = ease
    animation[6] = duration
    animation[7] = starttime
    animation[8] = frame counter
    animation[9] = last ease
    animation[10] = loop
    animation[11] = loop counter
    animation[12] = callback function
    animation[13] = function data
    animation[14] = early callback
    animation[15] = early callback data
    animation[16] = isplaying
    animation[17] = ispaused
    animation[18] = isreversed
    """

    animations_updated = []
    callbacks = {}
    global animations

    for animation in animations:

        if dpg.get_total_time() >= animation[7] and not animation[17]:

            if animation[14] and animation[8] == 0:
                callbacks[animation[14]] = (animation[2], animation[15])

            animation[16] = True
            frame = animation[8] / animation[6]
            ease = BezierTransistion(frame, animation[5])

            if animation[1] == "position":
                add_delta_positions(animation, ease)

            elif animation[1] == "size":
                add_delta_sizes(animation, ease)

            elif animation[1] == "opacity":
                add_delta_opacities(animation, ease)

            animation[9] = ease

            if animation[8] < animation[6]:
                if not animation[18]:
                    animation[8] += 1
                else:
                    if animation[8] == 0:
                        animation[18] = False
                        animation[8] = 1
                    else:
                        animation[8] -= 1
                animations_updated.append(animation)

            elif animation[8] == animation[6]:
                if animation[10]:
                    set_loop(animation, animations_updated)

                if animation[12]:
                    callbacks[animation[12]] = (animation[2], animation[13])

        else:
            animations_updated.append(animation)

    set_pos()
    set_size()
    set_opacity()

    animations = animations_updated

    for func, dat in callbacks.items():
        func(dat[0], dat[1])


def play(animation_name):
    """
    resumes an animation
    """

    global animations

    for animation in animations:
        if animation[0] == animation_name:
            animation[17] = False


def pause(animation_name):
    """
    pauses an animation
    """

    global animations

    for animation in animations:
        if animation[0] == animation_name:
            animation[17] = True


def remove(animation_name):
    """
    removes an animation from animations register
    """

    animations_updated = []
    delta_positions_updated = []
    delta_sizes_updated = []
    delta_opacities_updated = []
    object_anitype = []
    global animations
    global delta_positions
    global delta_sizes
    global delta_opacities

    for animation in animations:
        if not animation[0] == animation_name:
            animations_updated.append(animation)
        else:
            object_anitype = [animation[2], animation[1]]

    if object_anitype:
        found = False
        for ani in animations_updated:
            if ani[2] == object_anitype[0] and ani[1] == object_anitype[1]:
                found = True
                break

        if not found:
            if object_anitype[1] == "position":
                for entry in delta_positions:
                    if not entry[0] == object_anitype[0]:
                        delta_positions_updated.append(entry)
                delta_positions = delta_positions_updated

            elif object_anitype[1] == "size":
                for entry in delta_sizes:
                    if not entry[0] == object_anitype[0]:
                        delta_sizes_updated.append(entry)
                delta_sizes = delta_sizes_updated

            elif object_anitype[1] == "opacity":
                for entry in delta_opacities:
                    if not entry[0] == object_anitype[0]:
                        delta_opacities_updated.append(entry)
                delta_opacities = delta_opacities_updated

    animations = animations_updated


def get(*args):
    """
    return animation data as requested
    """

    return_data = []
    global animations

    for animation in animations:
        for entry in args:
            if entry == "name":
                return_data.append(animation[0])

            if entry == "type":
                return_data.append(animation[1])

            if entry == "object":
                return_data.append(animation[2])

            if entry == "startval":
                return_data.append(animation[3])

            if entry == "endval":
                try:
                    endval = [animation[3][0] + animation[4][0], animation[3][1] + animation[4][1]]
                except Exception:
                    endval = animation[3] + animation[4]
                return_data.append(endval)

            if entry == "ease":
                return_data.append(animation[5])

            if entry == "duration":
                return_data.append(animation[6])

            if entry == "starttime":
                return_data.append(animation[7])

            if entry == "framecounter":
                return_data.append(animation[8])

            if entry == "loop":
                return_data.append(animation[10])

            if entry == "loopcounter":
                return_data.append(animation[11])

            if entry == "callback":
                return_data.append(animation[12])

            if entry == "callback_data":
                return_data.append(animation[13])

            if entry == "early_callback":
                return_data.append(animation[14])

            if entry == "early_callback_data":
                return_data.append(animation[15])

            if entry == "isplaying":
                return_data.append(animation[16])

            if entry == "ispaused":
                return_data.append(animation[17])

    if not return_data:
        return False

    else:
        return return_data


# -----------------------------------------------------------------------------
# 				Helper Functions
# -----------------------------------------------------------------------------

def BezierTransistion(search, handles):
    """
    solving y (progress) of bezier curve for given x (time)
    using the newton-raphson method
    """

    h1x, h1y, h2x, h2y = handles

    cx = 3 * h1x
    bx = 3 * (h2x - h1x) - cx
    ax = 1 - cx - bx

    t = search

    for i in range(100):
        x = (ax * t ** 3 + bx * t ** 2 + cx * t) - search

        if round(x, 4) == 0:
            break

        dx = 3.0 * ax * t ** 2 + 2.0 * bx * t + cx

        t -= (x / dx)

    return 3 * t * (1 - t) ** 2 * h1y + 3 * t ** 2 * (1 - t) * h2y + t ** 3


def set_loop(animation, animations_updated):
    """
    prepare animation for next loop iteration
    """

    if animation[10] == "ping-pong":
        animation[18] = True
        animation[8] -= 1
        animation[9] = 1

    elif animation[10] == "cycle":
        animation[8] = 0
        animation[9] = 0

    elif animation[10] == "continue":
        try:
            animation[3] = [animation[3][0] + animation[4][0], animation[3][1] + animation[4][1]]
        except Exception:
            animation[3] += animation[4]
        animation[8] = 0
        animation[9] = 0

    animation[11] += 1
    animations_updated.append(animation)


def add_delta_positions(animation, ease):
    """
    collects delta movements of all position animations for a certain item
    """

    global delta_positions

    for item in delta_positions:
        if animation[2] == item[0]:

            x_step = animation[4][0] * (ease - animation[9])
            y_step = animation[4][1] * (ease - animation[9])

            item[1] += x_step
            item[2] += y_step

            if animation[8] < animation[6] or animation[10]:
                item[3] = True

            if animation[10] == "cycle" and animation[8] == animation[6]:
                item[3] = False

            if animation[8] == animation[6] and not item[3]:
                item[3] = False

            break
    else:
        delta_positions.append([animation[2], animation[3][0], animation[3][1], True])


def add_delta_sizes(animation, ease):
    """
    collects delta movements of all size animations for a certain item
    """

    global delta_sizes

    for item in delta_sizes:
        if animation[2] == item[0]:
            w_step = animation[4][0] * (ease - animation[9])
            h_step = animation[4][1] * (ease - animation[9])

            item[1] += w_step
            item[2] += h_step

            if animation[8] < animation[6] or animation[10]:
                item[3] = True

            if animation[10] == "cycle" and animation[8] == animation[6]:
                item[3] = False

            if animation[8] == animation[6] and not item[3]:
                item[3] = False

            break
    else:
        delta_sizes.append([animation[2], animation[3][0], animation[3][1], True])


def add_delta_opacities(animation, ease):
    """
    collects delta movements of all opacity animations for a certain item
    """

    global delta_opacities

    for item in delta_opacities:
        if animation[2] == item[0]:
            o_step = animation[4] * (ease - animation[9])

            item[1] += o_step

            if animation[8] < animation[6] or animation[10]:
                item[2] = True

            if animation[10] == "cycle" and animation[8] == animation[6]:
                item[2] = False

            if animation[8] == animation[6] and not item[2]:
                item[2] = False

            break
    else:
        delta_opacities.append([animation[2], animation[3], True])


def set_pos():
    """
    moves the item
    """

    global delta_positions

    items_updated = []

    for item in delta_positions:
        if item[3] is None:
            items_updated.append(item)
            continue

        elif item[3]:
            x_int = int(item[1])
            y_int = int(item[2])

            item[3] = None

            items_updated.append(item)

        else:
            x_int = round(item[1])
            y_int = round(item[2])

        dpg.set_item_pos(item[0], [x_int, y_int])

    delta_positions = items_updated


def set_size():
    """
    set items size
    """

    global delta_sizes

    items_updated = []

    for item in delta_sizes:
        if item[3] is None:
            items_updated.append(item)
            continue

        elif item[3]:
            w_int = int(item[1])
            h_int = int(item[2])

            item[3] = None

            items_updated.append(item)

        else:
            w_int = round(item[1])
            h_int = round(item[2])

        dpg.set_item_width(item[0], w_int)
        dpg.set_item_height(item[0], h_int)

    delta_sizes = items_updated


def dpg_get_alpha_style(item):
    theme = dpg.get_item_theme(item)
    if theme is None:
        theme = dpg.add_theme()
        theme_component = dpg.add_theme_component(dpg.mvAll, parent=theme)
        alpha_style = dpg.add_theme_style(dpg.mvStyleVar_Alpha, 1, category=dpg.mvThemeCat_Core, parent=theme_component)
        dpg.bind_item_theme(item, theme)
        return alpha_style

    all_components = dpg.get_item_children(theme, 1)
    theme_component = None
    for component in all_components:
        if dpg.get_item_configuration(component)['item_type'] == dpg.mvAll:
            theme_component = component
            break
    if theme_component is None:
        theme_component = dpg.add_theme_component(parent=theme)

    all_styles = dpg.get_item_children(theme_component, 1)
    alpha_style = None
    for style in all_styles:
        if dpg.get_item_configuration(style)['target'] == dpg.mvStyleVar_Alpha:
            alpha_style = style
            break
    if alpha_style is None:
        alpha_style = dpg.add_theme_style(dpg.mvStyleVar_Alpha, 1, category=dpg.mvThemeCat_Core, parent=theme_component)
    return alpha_style


def set_opacity():
    """
    set items opacity
    """

    global delta_opacities

    items_updated = []

    for item in delta_opacities:
        if item[2] is None:
            items_updated.append(item)
            continue

        elif item[2]:
            item[2] = None
            items_updated.append(item)

        if dpg.get_item_type(item[0]) == "mvAppItemType::mvText":
            new_color = dpg.get_item_configuration(item[0])["color"]
            new_color = list(map(lambda color: int(color * 255), new_color[:3:]))

            new_color.append(item[1] * 255)

            dpg.configure_item(item[0], color=new_color)
        else:
            dpg.set_value(dpg_get_alpha_style(item[0]), [item[1]])

    delta_opacities = items_updated
