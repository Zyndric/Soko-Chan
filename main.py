@namespace
class SpriteKind:
    Crate = SpriteKind.create()
def reset_states():
    global pressed_up, pressed_down, pressed_left, pressed_right, pressed_A, pressed_B, undo, count_moves, count_pushes
    pressed_up = 0
    pressed_down = 0
    pressed_left = 0
    pressed_right = 0
    pressed_A = 0
    pressed_B = 0
    undo = []
    count_moves = 0
    count_pushes = 0
    tiles.destroy_sprites_of_kind(SpriteKind.player)
    tiles.destroy_sprites_of_kind(SpriteKind.Crate)
    tiles.destroy_sprites_of_kind(SpriteKind.text)
    scene.center_camera_at(80, 60)
def set_up_selection():
    global state_level, button_lag, menu_selection, select_level, select_levelset, mySprite2, text_title, menu_items, text_footer, minimap, text_best, state_selection
    state_level = 0
    button_lag = 6
    menu_selection = 1
    select_level = level
    select_levelset = levelset
    scene.center_camera_at(80, 60)
    mySprite2 = sprites.create(assets.image("""
        bg selection
    """), SpriteKind.text)
    text_title = textsprite.create(" ", 0, 7)
    text_title.set_max_font_height(8)
    text_title.set_position(24, 15)
    text_title.set_border(1, 0, 2)
    text_title.set_text("Soko-Chan Menu")
    menu_items = []
    add_menu_item(35, "Group", True)
    add_menu_item(50, "Level", True)
    add_menu_item(65, "Help", False)
    add_menu_item(80, "Credits", False)
    text_footer = textsprite.create("=Choose  A=OK  B=Back", 0, 13)
    text_footer.set_max_font_height(8)
    text_footer.set_icon(assets.image("""
        icon arrows updown
    """))
    text_footer.set_position(80, 110)
    minimap = sprites.create(scale_thumbnail(get_level_asset(select_levelset, select_level)),
        SpriteKind.text)
    minimap.set_position(122, 64)
    text_best = textsprite.create("00/00", 0, 6)
    text_best.set_max_font_height(8)
    text_best.set_position(120, 90)
    hilight_menu_item()
    draw_selection()
    state_selection = 1
    reset_buttons()
def set_up_level():
    global state_selection
    reset_states()
    state_selection = 0
    blockSettings.write_number("recent group", levelset)
    blockSettings.write_number("recent level", level)
    scene.set_tile_map(get_level_asset(levelset, level))
    set_level_skin(False)
    realize_tilemap()
    return_to_level()
    introduce_level()
def reset_buttons():
    global pressed_up, pressed_down, pressed_left, pressed_right, pressed_A, pressed_B
    pressed_up = button_lag
    pressed_down = button_lag
    pressed_left = button_lag
    pressed_right = button_lag
    pressed_A = button_lag
    pressed_B = button_lag
def get_level_asset_cantrip(lv: number):
    if lv == 1:
        return assets.image("""
            level cantrip 01
        """)
    elif lv == 2:
        return assets.image("""
            level cantrip 02
        """)
    elif lv == 3:
        return assets.image("""
            level cantrip 03
        """)
    elif lv == 4:
        return assets.image("""
            level cantrip 04
        """)
    elif lv == 5:
        return assets.image("""
            level cantrip 05
        """)
    elif lv == 6:
        return assets.image("""
            level cantrip 06
        """)
    elif lv == 7:
        return assets.image("""
            level cantrip 07
        """)
    elif lv == 8:
        return assets.image("""
            level cantrip 08
        """)
    elif lv == 9:
        return assets.image("""
            level cantrip 09
        """)
    elif lv == 10:
        return assets.image("""
            level cantrip 10
        """)
    elif lv == 11:
        return assets.image("""
            level cantrip 11
        """)
    elif lv == 12:
        return assets.image("""
            level cantrip 12
        """)
    elif lv == 13:
        return assets.image("""
            level cantrip 13
        """)
    elif lv == 14:
        return assets.image("""
            level cantrip 14
        """)
    elif lv == 15:
        return assets.image("""
            level cantrip 15
        """)
    elif lv == 16:
        return assets.image("""
            level cantrip 16
        """)
    elif lv == 17:
        return assets.image("""
            level cantrip 17
        """)
    elif lv == 18:
        return assets.image("""
            level cantrip 18
        """)
    elif lv == 19:
        return assets.image("""
            level cantrip 19
        """)
    elif lv == 20:
        return assets.image("""
            level cantrip 20
        """)
    return assets.image("""
        level cantrip 01
    """)
def get_level_asset_declercq(lv: number):
    return [assets.image("""
            level blocks 01
        """),
        assets.image("""
            level blocks 02
        """),
        assets.image("""
            level blocks 03
        """),
        assets.image("""
            level blocks 04
        """),
        assets.image("""
            level blocks 05
        """),
        assets.image("""
            level blocks 06
        """),
        assets.image("""
            level blocks 07
        """),
        assets.image("""
            level blocks 08
        """),
        assets.image("""
            level blocks 09
        """),
        assets.image("""
            level blocks 10
        """),
        assets.image("""
            level various 01
        """),
        assets.image("""
            level various 02
        """),
        assets.image("""
            level various 03
        """),
        assets.image("""
            level various 04
        """),
        assets.image("""
            level various 05
        """),
        assets.image("""
            level various 06
        """),
        assets.image("""
            level various 07
        """),
        assets.image("""
            level various 08
        """),
        assets.image("""
            level various 09
        """),
        assets.image("""
            level various 10
        """)][lv - 1]
def add_menu_item(y: number, text: str, changeable: bool):
    global v
    v = textsprite.create(" ", 0, 6)
    v.set_max_font_height(8)
    v.set_position(24, y)
    if changeable:
        v.set_icon(assets.image("""
            icon arrows leftright
        """))
    v.set_border(1, 0, 2)
    v.set_text(text)
    menu_items[len(menu_items)] = v
def get_level_asset_petitesse(lv: number):
    if lv == 1:
        return assets.image("""
            level petitesse 01
        """)
    elif lv == 2:
        return assets.image("""
            level petitesse 02
        """)
    elif lv == 3:
        return assets.image("""
            level petitesse 03
        """)
    elif lv == 4:
        return assets.image("""
            level petitesse 04
        """)
    elif lv == 5:
        return assets.image("""
            level petitesse 05
        """)
    elif lv == 6:
        return assets.image("""
            level petitesse 06
        """)
    elif lv == 7:
        return assets.image("""
            level petitesse 07
        """)
    elif lv == 8:
        return assets.image("""
            level petitesse 08
        """)
    elif lv == 9:
        return assets.image("""
            level petitesse 09
        """)
    elif lv == 10:
        return assets.image("""
            level petitesse 10
        """)
    elif lv == 11:
        return assets.image("""
            level petitesse 11
        """)
    elif lv == 12:
        return assets.image("""
            level petitesse 12
        """)
    elif lv == 13:
        return assets.image("""
            level petitesse 13
        """)
    elif lv == 14:
        return assets.image("""
            level petitesse 14
        """)
    elif lv == 15:
        return assets.image("""
            level petitesse 15
        """)
    elif lv == 16:
        return assets.image("""
            level petitesse 16
        """)
    elif lv == 17:
        return assets.image("""
            level petitesse 17
        """)
    elif lv == 18:
        return assets.image("""
            level petitesse 18
        """)
    return assets.image("""
        level petitesse 01
    """)
def update_moves():
    update_camera()
    text_moves.set_text("" + convert_to_text(count_moves) + "/" + convert_to_text(count_pushes))
    text_moves.set_position(scene.camera_property(CameraProperty.X) + 81 - text_moves.width / 2,
        scene.camera_property(CameraProperty.Y) - 55)
def set_level_skin(random: bool):
    global level_skin, list_skin_sprites
    level_skin = levelset
    if random:
        level_skin = randint(1, 9)
    if level_skin == 1:
        list_skin_sprites = [assets.image("""
                wall purple bricks
            """),
            assets.image("""
                crate wood
            """),
            assets.image("""
                crate wood on target
            """),
            assets.image("""
                floor dark purple
            """),
            assets.image("""
                target dark purple
            """)]
    elif level_skin == 2:
        list_skin_sprites = [assets.image("""
                wall steel
            """),
            assets.image("""
                crate wood2
            """),
            assets.image("""
                crate wood2 on target
            """),
            assets.image("""
                floor tan dotted
            """),
            assets.image("""
                target tan dotted
            """)]
    elif level_skin == 3:
        list_skin_sprites = [assets.image("""
                wall dark brown bricks
            """),
            assets.image("""
                crate drawer
            """),
            assets.image("""
                crate drawer on target
            """),
            assets.image("""
                floor tan dotted
            """),
            assets.image("""
                target tan dotted
            """)]
    elif level_skin == 4:
        list_skin_sprites = [assets.image("""
                wall dark purple bricks
            """),
            assets.image("""
                crate wood2
            """),
            assets.image("""
                crate wood2 on target
            """),
            assets.image("""
                floor tan dotted
            """),
            assets.image("""
                target tan dotted
            """)]
    elif level_skin == 5:
        list_skin_sprites = [assets.image("""
                wall steel
            """),
            assets.image("""
                crate wood2
            """),
            assets.image("""
                crate wood2 on target
            """),
            assets.image("""
                floor tan dotted
            """),
            assets.image("""
                target tan dotted
            """)]
    elif level_skin == 6:
        list_skin_sprites = [assets.image("""
                wall dark steel
            """),
            assets.image("""
                crate chest
            """),
            assets.image("""
                crate chest on target
            """),
            assets.image("""
                floor light purple dotted
            """),
            assets.image("""
                target light purple dotted
            """)]
    elif level_skin == 7:
        list_skin_sprites = [assets.image("""
                wall steel
            """),
            assets.image("""
                crate wood
            """),
            assets.image("""
                crate wood on target
            """),
            assets.image("""
                floor tan dotted
            """),
            assets.image("""
                target tan dotted
            """)]
    elif level_skin == 8:
        list_skin_sprites = [assets.image("""
                wall dark brown bricks
            """),
            assets.image("""
                crate drawer
            """),
            assets.image("""
                crate drawer on target
            """),
            assets.image("""
                floor tan dotted
            """),
            assets.image("""
                target tan dotted
            """)]
    elif level_skin == 9:
        list_skin_sprites = [assets.image("""
                wall teal bricks
            """),
            assets.image("""
                crate wood
            """),
            assets.image("""
                crate wood on target
            """),
            assets.image("""
                floor tan dotted
            """),
            assets.image("""
                target tan dotted
            """)]
    else:
        list_skin_sprites = [assets.image("""
                wall steel
            """),
            assets.image("""
                crate wood
            """),
            assets.image("""
                crate wood on target
            """),
            assets.image("""
                floor tan dotted
            """),
            assets.image("""
                target tan dotted
            """)]
def level_best_id(group: number, level: number):
    return "best-" + convert_to_text(group) + "-" + convert_to_text(level)
def scale_thumbnail(src: Image):
    global thumbnail
    thumbnail = image.create(45, 36)
    for x in range(15):
        for y in range(12):
            thumbnail.fill_rect(x * 3, y * 3, 3, 3, src.get_pixel(x, y))
    thumbnail.draw_line(0, 0, 44, 0, 6)
    thumbnail.draw_line(0, 35, 44, 35, 6)
    thumbnail.draw_line(0, 0, 0, 35, 6)
    thumbnail.draw_line(44, 0, 44, 35, 6)
    return thumbnail
def show_help():
    game.show_long_text("---  Soko-Chan Help  --- " + "                         " + "Push the crates onto " + "the targets. You win " + "when all targets are " + "occupied by crates." + "              " + "                         " + "-  Arrow keys - Move      " + "-  B button   - Undo      " + "-  A button   - Menu      ",
        DialogLayout.FULL)
    game.show_long_text("---  Soko-Chan Help  --- " + "                         " + "When in menu, press A immediately to " + "reset the current level, or choose a different level, then press A." + "                                        " + "When in menu, press B to " + "return to the level as you left it.",
        DialogLayout.FULL)

def on_down_released():
    global pressed_down
    pressed_down = 0
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def get_level_asset_takaken(lv: number):
    return [assets.image("""
            level takaken 1
        """),
        assets.image("""
            level takaken 2
        """),
        assets.image("""
            level takaken 3
        """),
        assets.image("""
            level takaken 4
        """),
        assets.image("""
            level takaken 5
        """),
        assets.image("""
            level takaken 6
        """),
        assets.image("""
            level takaken 7
        """)][lv - 1]
def get_level_asset_microcosmos(lv: number):
    if lv == 1:
        return assets.image("""
            level microcosmos 01
        """)
    elif lv == 2:
        return assets.image("""
            level microcosmos 02
        """)
    elif lv == 3:
        return assets.image("""
            level microcosmos 03
        """)
    elif lv == 4:
        return assets.image("""
            level microcosmos 04
        """)
    elif lv == 5:
        return assets.image("""
            level microcosmos 05
        """)
    elif lv == 6:
        return assets.image("""
            level microcosmos 06
        """)
    elif lv == 7:
        return assets.image("""
            level microcosmos 07
        """)
    elif lv == 8:
        return assets.image("""
            level microcosmos 08
        """)
    elif lv == 9:
        return assets.image("""
            level microcosmos 09
        """)
    elif lv == 10:
        return assets.image("""
            level microcosmos 10
        """)
    elif lv == 11:
        return assets.image("""
            level microcosmos 11
        """)
    elif lv == 12:
        return assets.image("""
            level microcosmos 12
        """)
    elif lv == 13:
        return assets.image("""
            level microcosmos 13
        """)
    elif lv == 14:
        return assets.image("""
            level microcosmos 14
        """)
    elif lv == 15:
        return assets.image("""
            level microcosmos 15
        """)
    elif lv == 16:
        return assets.image("""
            level microcosmos 16
        """)
    elif lv == 17:
        return assets.image("""
            level microcosmos 17
        """)
    elif lv == 18:
        return assets.image("""
            level microcosmos 18
        """)
    elif lv == 19:
        return assets.image("""
            level microcosmos 19
        """)
    elif lv == 20:
        return assets.image("""
            level microcosmos 20
        """)
    elif lv == 21:
        return assets.image("""
            level microcosmos 21
        """)
    elif lv == 22:
        return assets.image("""
            level microcosmos 22
        """)
    elif lv == 23:
        return assets.image("""
            level microcosmos 23
        """)
    elif lv == 24:
        return assets.image("""
            level microcosmos 24
        """)
    elif lv == 25:
        return assets.image("""
            level microcosmos 25
        """)
    elif lv == 26:
        return assets.image("""
            level microcosmos 26
        """)
    elif lv == 27:
        return assets.image("""
            level microcosmos 27
        """)
    elif lv == 28:
        return assets.image("""
            level microcosmos 28
        """)
    elif lv == 29:
        return assets.image("""
            level microcosmos 29
        """)
    elif lv == 30:
        return assets.image("""
            level microcosmos 30
        """)
    elif lv == 31:
        return assets.image("""
            level microcosmos 31
        """)
    elif lv == 32:
        return assets.image("""
            level microcosmos 32
        """)
    elif lv == 33:
        return assets.image("""
            level microcosmos 33
        """)
    elif lv == 34:
        return assets.image("""
            level microcosmos 34
        """)
    elif lv == 35:
        return assets.image("""
            level microcosmos 35
        """)
    elif lv == 36:
        return assets.image("""
            level microcosmos 36
        """)
    elif lv == 37:
        return assets.image("""
            level microcosmos 37
        """)
    elif lv == 38:
        return assets.image("""
            level microcosmos 38
        """)
    elif lv == 39:
        return assets.image("""
            level microcosmos 39
        """)
    elif lv == 40:
        return assets.image("""
            level microcosmos 40
        """)
    return assets.image("""
        level microcosmos 01
    """)
def move_to(tx: number, ty: number, push_tx: number, push_ty: number):
    global count_moves, count_pushes
    if not (tiles.tile_is_wall(tiles.get_tile_location(tx, ty))):
        if box_on_tile(tx, ty):
            if not (tiles.tile_is_wall(tiles.get_tile_location(push_tx, push_ty))):
                if not (box_on_tile(push_tx, push_ty)):
                    undo.append([tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.COLUMN),
                            tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.ROW),
                            tx,
                            ty,
                            push_tx,
                            push_ty])
                    move_box(tx, ty, push_tx, push_ty)
                    move_ban(tx, ty)
                    count_moves += 1
                    count_pushes += 1
        else:
            undo.append([tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.COLUMN),
                    tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.ROW)])
            music.footstep.play()
            move_ban(tx, ty)
            count_moves += 1
        update_moves()
def ask_for_next_level():
    global str_record, str_score_action, record
    str_record = "New best solution."
    str_score_action = ""
    if blockSettings.exists(level_best_id(levelset, level)):
        record = blockSettings.read_number_array(level_best_id(levelset, level))
        str_record = "Your best:    " + str(record[0]) + "/" + str(record[1])
        if count_moves < record[0]:
            str_score_action = "New best! "
            blockSettings.write_number_array(level_best_id(levelset, level), [count_moves, count_pushes])
    else:
        blockSettings.write_number_array(level_best_id(levelset, level), [count_moves, count_pushes])
    return game.ask_next_level("Moves/Pushes: " + str(count_moves) + "/" + str(count_pushes),
        str_record,
        str_score_action)
def hilight_menu_item():
    for t in range(4):
        if t == menu_selection:
            menu_items[t].set_border(1, 9, 2)
        else:
            menu_items[t].set_border(1, 0, 2)
"""

tx, ty are tileset coordinates

dtx, dty are relative deviations of tileset coordinates

x, y are pixel screen coordinates

"""
def walk(dtx: number, dty: number):
    move_to(tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.COLUMN) + dtx,
        tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.ROW) + dty,
        tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.COLUMN) + 2 * dtx,
        tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.ROW) + 2 * dty)
def draw_selection():
    menu_items[0].set_text("Group: " + list_levelsets[select_levelset])
    menu_items[1].set_text("Level: " + convert_to_text(select_level))
    if blockSettings.exists(level_best_id(select_levelset, select_level)):
        text_best.set_text("" + str(blockSettings.read_number_array(level_best_id(select_levelset, select_level))[0]) + "/" + str(blockSettings.read_number_array(level_best_id(select_levelset, select_level))[1]))
    else:
        text_best.set_text("")
    minimap.set_image(scale_thumbnail(get_level_asset(select_levelset, select_level)))

def on_right_released():
    global pressed_right
    pressed_right = 0
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    global pressed_left
    pressed_left = 0
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def show_credits():
    game.show_long_text("---  Level  Credits  --- " + "                         " + "Tutorial                 " + ":   by Moobot            " + "Microban (easy)          " + ":   by David Skinner     " + "Blocks+co (easy/tricky)  " + ":   by Dries de Clercq   " + "Microcosmos (tricky)     " + ":   by Aymeric du Peloux " + "Cantrip (tricky/hard)    " + ":   by David Holland",
        DialogLayout.FULL)
    game.show_long_text("---  Level  Credits  --- " + "                         " + "Takaken (hard)           " + ": by Kenichiro Takahashi " + "Sokogen (easy)           " + ": genr.by Jacques Duthen " + "Murase (tricky)          " + ": gener.by Yoshio Murase " + "Nabokosmos (hard)        " + ":   by Aymeric du Peloux " + "Petitesse (tricky)       " + ":   by niwa",
        DialogLayout.FULL)
"""

Check win condition and manage buttons in a continuous loop.

A win is when all boxes stand on a target tile.

Direction buttons can be pressed repeatedly without delay. They can be pressed continuously, in which case Soko-Chan continues to move, but not too fast.

Button B must be blocked during menu, otherwise a B press during menu will be handled as undo action when the menu returns.

"""
def next_level():
    global level, levelset
    level += 1
    if level > list_groupsize[levelset]:
        level = 1
        levelset += 1
        game.splash("You finished this group.",
            "Next group: " + list_levelsets[levelset])
        if levelset >= len(list_levelsets):
            levelset = 0
    set_up_level()
"""

Determine if a box is on a specific tile by comparing their absolute x and y pixel coordiates. Use pixels, because the color-coded Tile object lacks a mechanism to get its tileset coordinates.

"""
def all_boxes_fit():
    for c in sprites.all_of_kind(SpriteKind.Crate):
        if not (target_tile(c.x, c.y)):
            return 0
    return 1
def undo_move():
    global undo_step, count_moves, count_pushes
    if len(undo) > 0:
        undo_step = undo.pop()
        move_ban(undo_step[0], undo_step[1])
        count_moves += -1
        if len(undo_step) == 6:
            move_box(undo_step[4], undo_step[5], undo_step[2], undo_step[3])
            count_pushes += -1
        else:
            music.footstep.play()
        update_moves()
def control_level():
    global pressed_B, pressed_up, pressed_down, pressed_left, pressed_right
    if all_boxes_fit():
        pause(500)
        ban.set_image(assets.image("""
            sokochan win
        """))
        music.play_tone(392, music.beat(BeatFraction.QUARTER))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        if ask_for_next_level():
            next_level()
        else:
            undo_move()
            pressed_B = button_lag
    if controller.up.is_pressed() and not (pressed_up):
        walk(0, -1)
        pressed_up = button_lag
    if controller.down.is_pressed() and not (pressed_down):
        walk(0, 1)
        pressed_down = button_lag
    if controller.left.is_pressed() and not (pressed_left):
        walk(-1, 0)
        pressed_left = button_lag
    if controller.right.is_pressed() and not (pressed_right):
        walk(1, 0)
        pressed_right = button_lag
    if controller.A.is_pressed() and not (pressed_A):
        set_up_selection()
        reset_buttons()
    if controller.B.is_pressed() and not (pressed_B):
        undo_move()
        pressed_B = button_lag
def return_to_level():
    global state_selection, button_lag, text_moves, state_level
    state_selection = 0
    button_lag = 9
    tiles.destroy_sprites_of_kind(SpriteKind.text)
    scene.center_camera_at(screen_center_x(), screen_center_y())
    if scroll_level():
        scene.camera_follow_sprite(ban)
    update_camera()
    text_moves = textsprite.create("0/0", 0, 11)
    text_moves.set_outline(1, 15)
    text_moves.set_border(1, 0)
    text_moves.set_max_font_height(8)
    update_moves()
    reset_buttons()
    state_level = 1
def scroll_level():
    if levelset == 1:
        # Microban
        return [8, 35, 36, 49].index(level) >= 0
    if levelset == 8:
        # Nabokosmos
        return [2, 7, 11, 16, 34, 39].index(level) >= 0
    if levelset == 5:
        # Takaken
        return [3, 6, 7].index(level) >= 0
    if levelset == 4:
        # Cantrip
        return [4, 15, 16, 20].index(level) >= 0
    if levelset == 3:
        # Microcosmos
        return [2, 10, 14, 22, 26, 30].index(level) >= 0
    return False
# Force camera to update its position right now, following the moved sprite. Otherwise, the fixed text (e.g. move counter) shuffles around, because it renders either too early, or too late.
def update_camera():
    game.current_scene().camera.update()

def on_a_released():
    global pressed_A
    pressed_A = 0
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def introduce_level():
    global text_frame, text_introduction
    text_frame = textsprite.create("       ", 13, 13)
    text_introduction = textsprite.create("" + list_levelsets[levelset] + " " + convert_to_text(level),
        0,
        12)
    text_introduction.set_max_font_height(16)
    text_frame.set_max_font_height(20)
    text_frame.set_border(1, 12)
    text_introduction.set_position(scene.camera_property(CameraProperty.X),
        scene.camera_property(CameraProperty.Y))
    text_frame.set_position(scene.camera_property(CameraProperty.X),
        scene.camera_property(CameraProperty.Y))
    music.big_crash.play()
    pause(1000)
    text_introduction.destroy()
    text_frame.destroy()

def on_up_released():
    global pressed_up
    pressed_up = 0
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def move_ban(to_tx: number, to_ty: number):
    tiles.place_on_tile(ban, tiles.get_tile_location(to_tx, to_ty))
    if target_tile(tiles.location_xy(tiles.get_tile_location(to_tx, to_ty), tiles.XY.X),
        tiles.location_xy(tiles.get_tile_location(to_tx, to_ty), tiles.XY.Y)):
        ban.set_image(assets.image("""
            sokochan on target
        """))
    else:
        ban.set_image(assets.image("""
            sokochan
        """))
def get_level_asset_sokogen(lv: number):
    return [assets.image("""
            level sokogen 01
        """),
        assets.image("""
            level sokogen 02
        """),
        assets.image("""
            level sokogen 03
        """),
        assets.image("""
            level sokogen 04
        """),
        assets.image("""
            level sokogen 05
        """),
        assets.image("""
            level sokogen 06
        """),
        assets.image("""
            level sokogen 07
        """),
        assets.image("""
            level sokogen 08
        """),
        assets.image("""
            level sokogen 09
        """),
        assets.image("""
            level sokogen 10
        """),
        assets.image("""
            level sokogen 11
        """),
        assets.image("""
            level sokogen 12
        """),
        assets.image("""
            level sokogen 13
        """),
        assets.image("""
            level sokogen 14
        """),
        assets.image("""
            level sokogen 15
        """),
        assets.image("""
            level sokogen 16
        """),
        assets.image("""
            level sokogen 17
        """),
        assets.image("""
            level sokogen 18
        """),
        assets.image("""
            level sokogen 19
        """),
        assets.image("""
            level sokogen 20
        """)][lv - 1]
def box_on_tile(tx: number, ty: number):
    for d in sprites.all_of_kind(SpriteKind.Crate):
        if tiles.location_xy(tiles.location_of_sprite(d), tiles.XY.COLUMN) == tx:
            if tiles.location_xy(tiles.location_of_sprite(d), tiles.XY.ROW) == ty:
                return 1
    return 0
"""

Soko-Chan

TODO

- fix: on scrolling levels that have a width of 11 tiles, the move counter jumps around a bit (Nabokosmos 7)

Included Features

* many puzzles from different puzzle sets

* unlimited undo

* push/move counter

* remember personal best move scores between power-offs

* remember recently opened puzzle between power-offs

* continuous movement when button is being held down

* different sprites when on target tile

* puzzle selection menu with minimap

* help and credits

* puzzle reset

* puzzles of up to 11x9 tiles show without scrolling (up to 10x7 tiles of walkable area)

* different tile sets for different puzzle sets

Nice to Have

- a way to handle large levels without scrolling, maybe through smaller 8x8 sprite tilemaps

"""
def screen_center_x():
    return tiles.tilemap_columns() * tiles.tile_width() / 2
def get_level_asset_microban(lv: number):
    if lv == 1:
        return assets.image("""
            level microban 01
        """)
    elif lv == 2:
        return assets.image("""
            level microban 02
        """)
    elif lv == 3:
        return assets.image("""
            level microban 03
        """)
    elif lv == 4:
        return assets.image("""
            level microban 04
        """)
    elif lv == 5:
        return assets.image("""
            level microban 05
        """)
    elif lv == 6:
        return assets.image("""
            level microban 06
        """)
    elif lv == 7:
        return assets.image("""
            level microban 07
        """)
    elif lv == 8:
        return assets.image("""
            level microban 08
        """)
    elif lv == 9:
        return assets.image("""
            level microban 09
        """)
    elif lv == 10:
        return assets.image("""
            level microban 10
        """)
    elif lv == 11:
        return assets.image("""
            level microban 11
        """)
    elif lv == 12:
        return assets.image("""
            level microban 12
        """)
    elif lv == 13:
        return assets.image("""
            level microban 13
        """)
    elif lv == 14:
        return assets.image("""
            level microban 14
        """)
    elif lv == 15:
        return assets.image("""
            level microban 15
        """)
    elif lv == 16:
        return assets.image("""
            level microban 16
        """)
    elif lv == 17:
        return assets.image("""
            level microban 17
        """)
    elif lv == 18:
        return assets.image("""
            level microban 18
        """)
    elif lv == 19:
        return assets.image("""
            level microban 19
        """)
    elif lv == 20:
        return assets.image("""
            level microban 20
        """)
    elif lv == 21:
        return assets.image("""
            level microban 21
        """)
    elif lv == 22:
        return assets.image("""
            level microban 22
        """)
    elif lv == 23:
        return assets.image("""
            level microban 23
        """)
    elif lv == 24:
        return assets.image("""
            level microban 24
        """)
    elif lv == 25:
        return assets.image("""
            level microban 25
        """)
    elif lv == 26:
        return assets.image("""
            level microban 26
        """)
    elif lv == 27:
        return assets.image("""
            level microban 27
        """)
    elif lv == 28:
        return assets.image("""
            level microban 28
        """)
    elif lv == 29:
        return assets.image("""
            level microban 29
        """)
    elif lv == 30:
        return assets.image("""
            level microban 30
        """)
    elif lv == 31:
        return assets.image("""
            level microban 31
        """)
    elif lv == 32:
        return assets.image("""
            level microban 32
        """)
    elif lv == 33:
        return assets.image("""
            level microban 33
        """)
    elif lv == 34:
        return assets.image("""
            level microban 34
        """)
    elif lv == 35:
        return assets.image("""
            level microban 35
        """)
    elif lv == 36:
        return assets.image("""
            level microban 36
        """)
    elif lv == 37:
        return assets.image("""
            level microban 37
        """)
    elif lv == 38:
        return assets.image("""
            level microban 38
        """)
    elif lv == 39:
        return assets.image("""
            level microban 39
        """)
    elif lv == 40:
        return assets.image("""
            level microban 40
        """)
    elif lv == 41:
        return assets.image("""
            level microban 41
        """)
    elif lv == 42:
        return assets.image("""
            level microban 42
        """)
    elif lv == 43:
        return assets.image("""
            level microban 43
        """)
    elif lv == 44:
        return assets.image("""
            level microban 44
        """)
    elif lv == 45:
        return assets.image("""
            level microban 45
        """)
    elif lv == 46:
        return assets.image("""
            level microban 46
        """)
    elif lv == 47:
        return assets.image("""
            level microban 47
        """)
    elif lv == 48:
        return assets.image("""
            level microban 48
        """)
    elif lv == 49:
        return assets.image("""
            level microban 49
        """)
    elif lv == 50:
        return assets.image("""
            level microban 50
        """)
    elif lv == 51:
        return assets.image("""
            level microban 51
        """)
    elif lv == 52:
        return assets.image("""
            level microban 52
        """)
    return assets.image("""
        level microban 01
    """)

def on_b_released():
    global pressed_B
    pressed_B = 0
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def get_level_asset(group: number, lv: number):
    if group == 1:
        return get_level_asset_microban(lv)
    elif group == 2:
        return get_level_asset_declercq(lv)
    elif group == 3:
        return get_level_asset_microcosmos(lv)
    elif group == 4:
        return get_level_asset_cantrip(lv)
    elif group == 5:
        return get_level_asset_takaken(lv)
    elif group == 6:
        return get_level_asset_sokogen(lv)
    elif group == 7:
        return get_level_asset_murase(lv)
    elif group == 8:
        return get_level_asset_nabo(lv)
    elif group == 9:
        return get_level_asset_petitesse(lv)
    else:
        return get_level_asset_tutorial(lv)
def move_box(from_tx: number, from_ty: number, to_tx: number, to_ty: number):
    for e in sprites.all_of_kind(SpriteKind.Crate):
        if e.x == tiles.location_xy(tiles.get_tile_location(from_tx, from_ty), tiles.XY.X) and e.y == tiles.location_xy(tiles.get_tile_location(from_tx, from_ty), tiles.XY.Y):
            tiles.place_on_tile(e, tiles.get_tile_location(to_tx, to_ty))
            if target_tile(tiles.location_xy(tiles.get_tile_location(to_tx, to_ty), tiles.XY.X),
                tiles.location_xy(tiles.get_tile_location(to_tx, to_ty), tiles.XY.Y)):
                music.knock.play()
                e.set_image(list_skin_sprites[2])
            else:
                music.thump.play()
                e.set_image(list_skin_sprites[1])
            return
def screen_center_y():
    return tiles.tilemap_rows() * tiles.tile_width() / 2
def control_selection():
    global menu_selection, pressed_up, pressed_down, select_levelset, select_level, pressed_left, pressed_right, level, levelset, pressed_A
    if controller.up.is_pressed() and not (pressed_up):
        menu_selection += -1
        menu_selection = (menu_selection + 4) % 4
        hilight_menu_item()
        music.footstep.play()
        pressed_up = button_lag
    if controller.down.is_pressed() and not (pressed_down):
        menu_selection += 1
        menu_selection = (menu_selection + 4) % 4
        hilight_menu_item()
        music.footstep.play()
        pressed_down = button_lag
    if menu_selection == 0:
        if controller.left.is_pressed() and not (pressed_left):
            select_levelset += -1
            select_levelset = (select_levelset + len(list_levelsets)) % len(list_levelsets)
            if select_level > list_groupsize[select_levelset]:
                select_level = list_groupsize[select_levelset]
            draw_selection()
            music.knock.play()
            pressed_left = button_lag
        if controller.right.is_pressed() and not (pressed_right):
            select_levelset += 1
            select_levelset = (select_levelset + len(list_levelsets)) % len(list_levelsets)
            if select_level > list_groupsize[select_levelset]:
                select_level = list_groupsize[select_levelset]
            draw_selection()
            music.knock.play()
            pressed_right = button_lag
    if menu_selection == 1:
        if controller.left.is_pressed() and not (pressed_left):
            select_level += -1
            select_level = (select_level - 1 + list_groupsize[select_levelset]) % list_groupsize[select_levelset] + 1
            draw_selection()
            music.thump.play()
            pressed_left = button_lag
        if controller.right.is_pressed() and not (pressed_right):
            select_level += 1
            select_level = (select_level - 1 + list_groupsize[select_levelset]) % list_groupsize[select_levelset] + 1
            draw_selection()
            music.thump.play()
            pressed_right = button_lag
    if controller.A.is_pressed() and not (pressed_A):
        if menu_selection <= 1:
            level = select_level
            levelset = select_levelset
            set_up_level()
        elif menu_selection == 2:
            show_help()
            pressed_A = button_lag
        else:
            show_credits()
            pressed_A = button_lag
    if controller.B.is_pressed() and not (pressed_B):
        return_to_level()
def decay_button_lag():
    global pressed_up, pressed_down, pressed_left, pressed_right, pressed_A, pressed_B
    if pressed_up:
        pressed_up += -1
    if pressed_down:
        pressed_down += -1
    if pressed_left:
        pressed_left += -1
    if pressed_right:
        pressed_right += -1
    if pressed_A:
        pressed_A += -1
    if pressed_B:
        pressed_B += -1
def get_level_asset_murase(lv: number):
    if lv == 1:
        return assets.image("""
            level murase 01
        """)
    elif lv == 2:
        return assets.image("""
            level murase 02
        """)
    elif lv == 3:
        return assets.image("""
            level murase 03
        """)
    elif lv == 4:
        return assets.image("""
            level murase 04
        """)
    elif lv == 5:
        return assets.image("""
            level murase 05
        """)
    elif lv == 6:
        return assets.image("""
            level murase 06
        """)
    elif lv == 7:
        return assets.image("""
            level murase 07
        """)
    elif lv == 8:
        return assets.image("""
            level murase 08
        """)
    elif lv == 9:
        return assets.image("""
            level murase 09
        """)
    elif lv == 10:
        return assets.image("""
            level murase 10
        """)
    elif lv == 11:
        return assets.image("""
            level murase 11
        """)
    elif lv == 12:
        return assets.image("""
            level murase 12
        """)
    elif lv == 13:
        return assets.image("""
            level murase 13
        """)
    elif lv == 14:
        return assets.image("""
            level murase 14
        """)
    elif lv == 15:
        return assets.image("""
            level murase 15
        """)
    elif lv == 16:
        return assets.image("""
            level murase 16
        """)
    elif lv == 17:
        return assets.image("""
            level murase 17
        """)
    elif lv == 18:
        return assets.image("""
            level murase 18
        """)
    elif lv == 19:
        return assets.image("""
            level murase 19
        """)
    elif lv == 20:
        return assets.image("""
            level murase 20
        """)
    return assets.image("""
        level murase 01
    """)
"""

Tile coding:

14 brown  -- wall (#)

3 pink     -- target (.)

7 green   -- player (@)

6 teal      -- player on target (+)

4 orange -- crate ($)

2 red       -- crate on target (*)

13 tan       -- floor

"""
def realize_tilemap():
    global box, ban
    for f in scene.get_tiles_by_type(2):
        box = sprites.create(list_skin_sprites[2], SpriteKind.Crate)
        scene.place(f, box)
        scene.set_tile_at(f, 3)
    for g in scene.get_tiles_by_type(4):
        box = sprites.create(list_skin_sprites[1], SpriteKind.Crate)
        scene.place(g, box)
        scene.set_tile_at(g, 13)
    for h in scene.get_tiles_by_type(6):
        ban = sprites.create(assets.image("""
                sokochan on target
            """),
            SpriteKind.player)
        scene.place(h, ban)
        scene.set_tile_at(h, 3)
    for i in scene.get_tiles_by_type(7):
        ban = sprites.create(assets.image("""
            sokochan
        """), SpriteKind.player)
        scene.place(i, ban)
        scene.set_tile_at(i, 13)
    scene.set_tile(3, list_skin_sprites[4], False)
    scene.set_tile(13, list_skin_sprites[3], False)
    scene.set_tile(14, list_skin_sprites[0], True)
"""

Variables

setup scope

e

control scope

c, t, x, y

"""
def introduce_game():
    global text_frame, text_introduction
    scene.set_tile_map(assets.image("""
        game intro
    """))
    set_level_skin(True)
    realize_tilemap()
    scene.center_camera_at(screen_center_x(), screen_center_y())
    update_camera()
    text_frame = textsprite.create("       ", 13, 13)
    text_introduction = textsprite.create("SOKOCHAN", 0, 12)
    text_introduction.set_max_font_height(16)
    text_frame.set_max_font_height(20)
    text_frame.set_border(1, 12)
    text_introduction.set_position(scene.camera_property(CameraProperty.X), 40)
    text_frame.set_position(scene.camera_property(CameraProperty.X), 40)
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    ban.set_image(assets.image("""
        sokochan win
    """))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    pause(1500)
    ban.destroy()
    text_introduction.destroy()
    text_frame.destroy()
def get_level_asset_nabo(lv: number):
    if lv == 1:
        return assets.image("""
            level nabo 01
        """)
    elif lv == 2:
        return assets.image("""
            level nabo 02
        """)
    elif lv == 3:
        return assets.image("""
            level nabo 03
        """)
    elif lv == 4:
        return assets.image("""
            level nabo 04
        """)
    elif lv == 5:
        return assets.image("""
            level nabo 05
        """)
    elif lv == 6:
        return assets.image("""
            level nabo 06
        """)
    elif lv == 7:
        return assets.image("""
            level nabo 07
        """)
    elif lv == 8:
        return assets.image("""
            level nabo 08
        """)
    elif lv == 9:
        return assets.image("""
            level nabo 09
        """)
    elif lv == 10:
        return assets.image("""
            level nabo 10
        """)
    elif lv == 11:
        return assets.image("""
            level nabo 11
        """)
    elif lv == 12:
        return assets.image("""
            level nabo 12
        """)
    elif lv == 13:
        return assets.image("""
            level nabo 13
        """)
    elif lv == 14:
        return assets.image("""
            level nabo 14
        """)
    elif lv == 15:
        return assets.image("""
            level nabo 15
        """)
    elif lv == 16:
        return assets.image("""
            level nabo 16
        """)
    elif lv == 17:
        return assets.image("""
            level nabo 17
        """)
    elif lv == 18:
        return assets.image("""
            level nabo 18
        """)
    elif lv == 19:
        return assets.image("""
            level nabo 19
        """)
    elif lv == 20:
        return assets.image("""
            level nabo 20
        """)
    elif lv == 21:
        return assets.image("""
            level nabo 21
        """)
    elif lv == 22:
        return assets.image("""
            level nabo 22
        """)
    elif lv == 23:
        return assets.image("""
            level nabo 23
        """)
    elif lv == 24:
        return assets.image("""
            level nabo 24
        """)
    elif lv == 25:
        return assets.image("""
            level nabo 25
        """)
    elif lv == 26:
        return assets.image("""
            level nabo 26
        """)
    elif lv == 27:
        return assets.image("""
            level nabo 27
        """)
    elif lv == 28:
        return assets.image("""
            level nabo 28
        """)
    elif lv == 29:
        return assets.image("""
            level nabo 29
        """)
    elif lv == 30:
        return assets.image("""
            level nabo 30
        """)
    elif lv == 31:
        return assets.image("""
            level nabo 31
        """)
    elif lv == 32:
        return assets.image("""
            level nabo 32
        """)
    elif lv == 33:
        return assets.image("""
            level nabo 33
        """)
    elif lv == 34:
        return assets.image("""
            level nabo 34
        """)
    elif lv == 35:
        return assets.image("""
            level nabo 35
        """)
    elif lv == 36:
        return assets.image("""
            level nabo 36
        """)
    elif lv == 37:
        return assets.image("""
            level nabo 37
        """)
    elif lv == 38:
        return assets.image("""
            level nabo 38
        """)
    elif lv == 39:
        return assets.image("""
            level nabo 39
        """)
    elif lv == 40:
        return assets.image("""
            level nabo 40
        """)
    return assets.image("""
        level nabo 01
    """)
def get_level_asset_tutorial(lv: number):
    if lv == 1:
        return assets.image("""
            level easy 01
        """)
    elif lv == 2:
        return assets.image("""
            level easy 02
        """)
    elif lv == 3:
        return assets.image("""
            level easy 03
        """)
    elif lv == 4:
        return assets.image("""
            level easy 04
        """)
    elif lv == 5:
        return assets.image("""
            level easy 05
        """)
    elif lv == 6:
        return assets.image("""
            level easy 06
        """)
    elif lv == 7:
        return assets.image("""
            level easy 07
        """)
    elif lv == 8:
        return assets.image("""
            level easy 08
        """)
    elif lv == 9:
        return assets.image("""
            level easy 10
        """)
    elif lv == 10:
        return assets.image("""
            level easy 11
        """)
    return assets.image("""
        level easy 01
    """)
def target_tile(x: number, y: number):
    for u in scene.get_tiles_by_type(3):
        if x == u.x:
            if y == u.y:
                return 1
    return 0
box: Sprite = None
text_introduction: TextSprite = None
text_frame: TextSprite = None
undo_step: List[number] = []
record: List[number] = []
str_score_action = ""
str_record = ""
ban: Sprite = None
thumbnail: Image = None
list_skin_sprites: List[Image] = []
level_skin = 0
text_moves: TextSprite = None
v: TextSprite = None
state_selection = 0
text_best: TextSprite = None
minimap: Sprite = None
text_footer: TextSprite = None
menu_items: List[TextSprite] = []
text_title: TextSprite = None
mySprite2: Sprite = None
select_levelset = 0
select_level = 0
menu_selection = 0
button_lag = 0
state_level = 0
count_pushes = 0
count_moves = 0
undo: List[List[number]] = []
pressed_B = 0
pressed_A = 0
pressed_right = 0
pressed_left = 0
pressed_down = 0
pressed_up = 0
level = 0
levelset = 0
list_groupsize: List[number] = []
list_levelsets: List[str] = []
introduce_game()
list_levelsets = ["Tutorial",
    "Microban",
    "Blocks+co",
    "Microcosm",
    "Cantrip",
    "Takaken",
    "Sokogen",
    "Murase",
    "Nabokosmos",
    "Petitesse"]
list_groupsize = [10, 52, 20, 40, 20, 7, 20, 20, 40, 18]
levelset = 0
level = 1
if blockSettings.exists("recent group") and blockSettings.exists("recent level"):
    levelset = blockSettings.read_number("recent group")
    level = blockSettings.read_number("recent level")
set_up_level()

def on_forever():
    if state_selection:
        control_selection()
    if state_level:
        control_level()
    decay_button_lag()
forever(on_forever)
