@namespace
class SpriteKind:
    Crate = SpriteKind.create()
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
def reset_states():
    global pressed_up, pressed_down, pressed_left, pressed_right, pressed_A, pressed_B, scroll_level, undo_ban, undo_box
    pressed_up = 0
    pressed_down = 0
    pressed_left = 0
    pressed_right = 0
    pressed_A = 0
    pressed_B = 0
    scroll_level = 0
    undo_ban = []
    undo_box = []
    tiles.destroy_sprites_of_kind(SpriteKind.player)
    tiles.destroy_sprites_of_kind(SpriteKind.Crate)
    tiles.destroy_sprites_of_kind(SpriteKind.text)
    scene.center_camera_at(80, 60)
    info.set_score(0)

def on_a_released():
    global pressed_A
    pressed_A = 0
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def set_up_selection():
    global state_selection, state_level, button_lag, text_title, text_levelset, text_level, text_help, text_credits, text_footer, mySprite
    reset_states()
    state_selection = 1
    state_level = 0
    button_lag = 8
    text_title = textsprite.create(" ", 0, 7)
    text_title.set_max_font_height(8)
    text_title.set_position(24, 15)
    text_title.set_border(1, 0, 2)
    text_title.set_text("Menu")
    text_levelset = textsprite.create(" ", 0, 6)
    text_levelset.set_max_font_height(8)
    text_levelset.set_position(24, 35)
    text_levelset.set_icon(assets.image("""
        icon arrows leftright
    """))
    text_levelset.set_border(1, 0, 2)
    text_level = textsprite.create(" ", 0, 9)
    text_level.set_max_font_height(8)
    text_level.set_position(24, 50)
    text_level.set_icon(assets.image("""
        icon arrows leftright
    """))
    text_level.set_border(1, 9, 2)
    text_help = textsprite.create(" ", 0, 6)
    text_help.set_max_font_height(8)
    text_help.set_position(24, 65)
    text_help.set_border(1, 0, 2)
    text_help.set_text("Help")
    text_credits = textsprite.create(" ", 0, 6)
    text_credits.set_max_font_height(8)
    text_credits.set_position(24, 80)
    text_credits.set_border(1, 0, 2)
    text_credits.set_text("Credits")
    text_footer = textsprite.create("=Choose  A=OK  B=Back", 0, 13)
    text_footer.set_max_font_height(8)
    text_footer.set_icon(assets.image("""
        icon arrows updown
    """))
    text_footer.set_position(80, 110)
    mySprite = sprites.create(scale_thumbnail(assets.image("""
            level microban 01
        """)),
        SpriteKind.player)
    mySprite.set_position(122, 69)
    scene.set_tile_map(assets.image("""
        level selection
    """))
def set_up_level():
    global state_selection, state_level, button_lag
    reset_states()
    state_selection = 0
    state_level = 1
    button_lag = 10
    if levelset == 0:
        define_level_easy()
    elif levelset == 1:
        define_level_microban()
    elif levelset == 2:
        define_level_murase()
    realize_tilemap()
    scene.center_camera_at(screen_center_x(), screen_center_y())
    if scroll_level:
        scene.camera_follow_sprite(ban)
    introduce_level()
    reset_buttons()

def on_down_released():
    global pressed_down
    pressed_down = 0
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_up_released():
    global pressed_up
    pressed_up = 0
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def reset_buttons():
    global pressed_up, pressed_down, pressed_left, pressed_right, pressed_A, pressed_B
    pressed_up = button_lag
    pressed_down = button_lag
    pressed_left = button_lag
    pressed_right = button_lag
    pressed_A = button_lag
    pressed_B = button_lag
"""

Soko-Chan/Meowban

TODO

- infinite undo

- rename to sokochan

- help

- credits

- title screen

- more levels (from sets "Yoshio Murase", "Sokogen-990602", Microban, Microcosmos, Nabokosmos, "Classic Thinking Rabbit", Boxxle)

- better in-game menu

- nicer level selection menu with minimap

- sort MakeCode blocks

- 

Included Features

- one step undo

- reset level

- level selection

- push/move counter

- different sprites when on target tile

- different level sets (names with up to 8 characters)

- levels of up to 11x9 tiles show without scrolling (up to 10x7 tiles of walkable area)

- continuous movement when button is being held down

Nice to Have

- different tile sets for different level sets

- a way to handle large levels without scrolling, maybe through smaller 8x8 sprite tilemaps

"""
def sprite_cache():
    global box
    box = sprites.create(assets.image("""
        crate wood
    """), SpriteKind.Crate)
    box = sprites.create(assets.image("""
            crate wood on target
        """),
        SpriteKind.Crate)
    box = sprites.create(assets.image("""
        crate wood2
    """), SpriteKind.Crate)
    box = sprites.create(assets.image("""
            crate wood2 on target
        """),
        SpriteKind.Crate)
    box = sprites.create(assets.image("""
        create chest
    """), SpriteKind.Crate)
    box = sprites.create(assets.image("""
            crate chest on target
        """),
        SpriteKind.Crate)
    box = sprites.create(assets.image("""
        crate drawer
    """), SpriteKind.Crate)
    box = sprites.create(assets.image("""
            crate drawer on target
        """),
        SpriteKind.Crate)
    box = sprites.create(assets.image("""
        crate marble
    """), SpriteKind.Crate)
    box = sprites.create(assets.image("""
            crate marble on target
        """),
        SpriteKind.Crate)
    box = sprites.create(assets.image("""
        crate car
    """), SpriteKind.Crate)
    box = sprites.create(assets.image("""
            crate car on target
        """),
        SpriteKind.Crate)
    box = sprites.create(assets.image("""
        crate clam
    """), SpriteKind.Crate)
    box = sprites.create(assets.image("""
            crate clam on target
        """),
        SpriteKind.Crate)
    box = sprites.create(assets.image("""
        crate shrub
    """), SpriteKind.Crate)
    box = sprites.create(assets.image("""
            crate shrub on target
        """),
        SpriteKind.Crate)
    scene.set_tile(3, assets.image("""
        target switch
    """), False)
    scene.set_tile(3, assets.image("""
        target tan
    """), False)
    scene.set_tile(3, assets.image("""
        target dark purple
    """), False)
    scene.set_tile(3, assets.image("""
        target patch
    """), False)
    scene.set_tile(3, assets.image("""
        target tiled
    """), False)
    scene.set_tile(3, assets.image("""
        target tan dotted
    """), False)
    scene.set_tile(13, assets.image("""
        floor tan dotted
    """), False)
    scene.set_tile(13, assets.image("""
        floor tan
    """), False)
    scene.set_tile(13, assets.image("""
        floor tiled
    """), False)
    scene.set_tile(13, assets.image("""
        floor dark purple
    """), False)
    scene.set_tile(14, assets.image("""
        wall brown bricks
    """), True)
    scene.set_tile(14, assets.image("""
        wall purple bricks
    """), True)
    scene.set_tile(14, assets.image("""
        wall dark purple bricks
    """), True)
    scene.set_tile(14, assets.image("""
        wall dark brown bricks
    """), True)
    scene.set_tile(14, assets.image("""
        wall steel
    """), True)
    scene.set_tile(14, assets.image("""
        wall red bricks
    """), True)
    scene.set_tile(14, assets.image("""
        wall yellow bricks
    """), True)
    scene.set_tile(14, assets.image("""
        wall teal bricks
    """), True)
    scene.set_tile(14, assets.image("""
        wall overgrown bricks
    """), True)
    scene.set_tile(14, assets.image("""
        wall plant
    """), True)
    scene.set_tile(14, assets.image("""
        wall sand
    """), True)
    scene.set_tile(14, assets.image("""
        wall reef
    """), True)
    scene.set_tile(14, assets.image("""
        wall colored
    """), True)
    scene.set_tile(14, assets.image("""
        wall old teal bricks
    """), True)
    scene.set_tile(14, assets.image("""
        wall large teal bricks
    """), True)
def scale_thumbnail(src: Image):
    global thumbnail
    thumbnail = image.create(45, 36)
    for x in range(16):
        for y in range(13):
            thumbnail.fill_rect(x * 3, y * 3, 3, 3, src.get_pixel(x, y))
    thumbnail.draw_line(0, 0, 44, 0, 6)
    thumbnail.draw_line(0, 35, 44, 35, 6)
    thumbnail.draw_line(0, 0, 0, 35, 6)
    thumbnail.draw_line(44, 0, 44, 35, 6)
    return thumbnail
def show_menu():
    game.splash("A - Menu", "B - Undo")
    if game.ask("Menu", "Reset this level?"):
        set_up_level()
    else:
        if game.ask("Menu", "Go to level selection?"):
            set_up_selection()
        else:
            if game.ask("Menu", "See credits?"):
                pass
def define_level_microban():
    global scroll_level
    if level == 1:
        scene.set_tile_map(assets.image("""
            level microban 01
        """))
    elif level == 2:
        scene.set_tile_map(assets.image("""
            level microban 02
        """))
    elif level == 3:
        scene.set_tile_map(assets.image("""
            level microban 03
        """))
    elif level == 4:
        scene.set_tile_map(assets.image("""
            level microban 04
        """))
    elif level == 5:
        scene.set_tile_map(assets.image("""
            level microban 05
        """))
    elif level == 6:
        scene.set_tile_map(assets.image("""
            level microban 06
        """))
    elif level == 7:
        scene.set_tile_map(assets.image("""
            level microban 07
        """))
    elif level == 8:
        scene.set_tile_map(assets.image("""
            level microban 08
        """))
        scroll_level = 1
    elif level == 9:
        scene.set_tile_map(assets.image("""
            level microban 09
        """))
    elif level == 10:
        scene.set_tile_map(assets.image("""
            level microban 10
        """))
    else:
        game.over(True)
def define_level_murase():
    if level == 1:
        scene.set_tile_map(assets.image("""
            level murase 01
        """))
    elif level == 2:
        scene.set_tile_map(assets.image("""
            level murase 02
        """))
    elif level == 3:
        scene.set_tile_map(assets.image("""
            level murase 03
        """))
    elif level == 4:
        scene.set_tile_map(assets.image("""
            level murase 04
        """))
    elif level == 5:
        scene.set_tile_map(assets.image("""
            level murase 05
        """))
    elif level == 6:
        scene.set_tile_map(assets.image("""
            level murase 06
        """))
    elif level == 7:
        scene.set_tile_map(assets.image("""
            level murase 07
        """))
    elif level == 8:
        scene.set_tile_map(assets.image("""
            level murase 08
        """))
    elif level == 9:
        scene.set_tile_map(assets.image("""
            level murase 09
        """))
    elif level == 10:
        scene.set_tile_map(assets.image("""
            level murase 10
        """))
    else:
        game.over(True)
def move_to(tx: number, ty: number, push_tx: number, push_ty: number):
    global undo_box
    if not (tiles.tile_is_wall(tiles.get_tile_location(tx, ty))):
        if box_on_tile(tx, ty):
            if not (tiles.tile_is_wall(tiles.get_tile_location(push_tx, push_ty))):
                if not (box_on_tile(push_tx, push_ty)):
                    move_box(tx, ty, push_tx, push_ty)
                    move_ban(tx, ty)
                    info.change_score_by(-1)
        else:
            undo_box = []
            music.footstep.play()
            move_ban(tx, ty)
            info.change_score_by(-1)
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
def define_level_easy():
    if level == 1:
        scene.set_tile_map(assets.image("""
            level easy 01
        """))
    elif level == 2:
        scene.set_tile_map(assets.image("""
            level easy 02
        """))
    elif level == 3:
        scene.set_tile_map(assets.image("""
            level easy 03
        """))
    elif level == 4:
        scene.set_tile_map(assets.image("""
            level easy 04
        """))
    elif level == 5:
        scene.set_tile_map(assets.image("""
            level easy 05
        """))
    elif level == 6:
        scene.set_tile_map(assets.image("""
            level easy 06
        """))
    elif level == 7:
        scene.set_tile_map(assets.image("""
            level easy 07
        """))
    elif level == 8:
        scene.set_tile_map(assets.image("""
            level easy 08
        """))
    elif level == 9:
        scene.set_tile_map(assets.image("""
            level easy 09
        """))
    elif level == 10:
        scene.set_tile_map(assets.image("""
            level easy 10
        """))
    else:
        game.over(True)

def on_left_released():
    global pressed_left
    pressed_left = 0
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

"""

Set up

Variables ban, level, "undo ban" and "undo box" are unique and used by name.

Variables box, c and t are loop and temporary variables.

"""
def next_level():
    global level
    level += 1
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
    global undo_ban, undo_box
    if len(undo_ban) == 2:
        move_ban(undo_ban[0], undo_ban[1])
        info.change_score_by(1)
        music.footstep.play()
    if len(undo_box) == 4:
        move_box(undo_box[2], undo_box[3], undo_box[0], undo_box[1])
    undo_ban = []
    undo_box = []
def control_level():
    global pressed_up, pressed_down, pressed_left, pressed_right, pressed_B
    if all_boxes_fit():
        pause(500)
        next_level()
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
        show_menu()
        reset_buttons()
    if controller.B.is_pressed() and not (pressed_B):
        undo_move()
        pressed_B = button_lag
def introduce_level():
    global text_frame, text_introduction
    text_frame = textsprite.create("       ", 13, 13)
    text_introduction = textsprite.create("" + list_levelsets[levelset] + " " + convert_to_text(level),
        0,
        12)
    text_introduction.set_max_font_height(16)
    text_frame.set_max_font_height(20)
    text_frame.set_border(1, 12)
    if scroll_level:
        text_introduction.set_position(scene.camera_property(CameraProperty.X),
            scene.camera_property(CameraProperty.Y))
        text_frame.set_position(scene.camera_property(CameraProperty.X),
            scene.camera_property(CameraProperty.Y))
    else:
        text_introduction.set_position(screen_center_x(), screen_center_y())
        console.log_value("xmid calulated", screen_center_x())
        console.log_value("xmid reported", scene.camera_property(CameraProperty.X))
        text_frame.set_position(screen_center_x(), screen_center_y())
    music.big_crash.play()
    pause(1000)
    text_introduction.destroy()
    text_frame.destroy()

def on_b_released():
    global pressed_B
    pressed_B = 0
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def move_ban(to_tx: number, to_ty: number):
    global undo_ban
    undo_ban = [tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.COLUMN),
        tiles.location_xy(tiles.location_of_sprite(ban), tiles.XY.ROW)]
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
def box_on_tile(tx: number, ty: number):
    for d in sprites.all_of_kind(SpriteKind.Crate):
        if tiles.location_xy(tiles.location_of_sprite(d), tiles.XY.COLUMN) == tx:
            if tiles.location_xy(tiles.location_of_sprite(d), tiles.XY.ROW) == ty:
                return 1
    return 0
def screen_center_x():
    return tiles.tilemap_columns() * tiles.tile_width() / 2

def on_right_released():
    global pressed_right
    pressed_right = 0
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def move_box(from_tx: number, from_ty: number, to_tx: number, to_ty: number):
    global undo_box
    for e in sprites.all_of_kind(SpriteKind.Crate):
        if e.x == tiles.location_xy(tiles.get_tile_location(from_tx, from_ty), tiles.XY.X) and e.y == tiles.location_xy(tiles.get_tile_location(from_tx, from_ty), tiles.XY.Y):
            undo_box = [from_tx, from_ty, to_tx, to_ty]
            tiles.place_on_tile(e, tiles.get_tile_location(to_tx, to_ty))
            if target_tile(tiles.location_xy(tiles.get_tile_location(to_tx, to_ty), tiles.XY.X),
                tiles.location_xy(tiles.get_tile_location(to_tx, to_ty), tiles.XY.Y)):
                music.knock.play()
                e.set_image(assets.image("""
                    crate drawer on target
                """))
            else:
                music.thump.play()
                e.set_image(assets.image("""
                    crate drawer
                """))
            return
def screen_center_y():
    return tiles.tilemap_rows() * tiles.tile_width() / 2
def control_selection():
    global levelset, pressed_up, pressed_down, level, pressed_left, pressed_right
    if controller.up.is_pressed() and not (pressed_up):
        levelset += -1
        pressed_up = button_lag
    if controller.down.is_pressed() and not (pressed_down):
        levelset += 1
        pressed_down = button_lag
    levelset = (levelset + len(list_levelsets)) % len(list_levelsets)
    text_levelset.set_text("Group: " + list_levelsets[levelset])
    if controller.left.is_pressed() and not (pressed_left):
        level += -1
        pressed_left = button_lag
    if controller.right.is_pressed() and not (pressed_right):
        level += 1
        pressed_right = button_lag
    level = (level - 1 + 10) % 10 + 1
    text_level.set_text("Level: " + convert_to_text(level))
    if controller.A.is_pressed() and not (pressed_A):
        set_up_level()
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
def realize_tilemap():
    global box, ban
    for t in scene.get_tiles_by_type(2):
        box = sprites.create(assets.image("""
                crate drawer on target
            """),
            SpriteKind.Crate)
        scene.place(t, box)
        scene.set_tile_at(t, 3)
    for u in scene.get_tiles_by_type(4):
        box = sprites.create(assets.image("""
            crate drawer
        """), SpriteKind.Crate)
        scene.place(u, box)
        scene.set_tile_at(u, 13)
    for v in scene.get_tiles_by_type(6):
        ban = sprites.create(assets.image("""
                sokochan on target
            """),
            SpriteKind.player)
        scene.place(v, ban)
        scene.set_tile_at(v, 3)
    for w in scene.get_tiles_by_type(7):
        ban = sprites.create(assets.image("""
            sokochan
        """), SpriteKind.player)
        scene.place(w, ban)
        scene.set_tile_at(w, 13)
    scene.set_tile(3, assets.image("""
        target tan dotted
    """), False)
    scene.set_tile(13, assets.image("""
        floor tan dotted
    """), False)
    scene.set_tile(14, assets.image("""
        wall steel
    """), True)
def target_tile(x: number, y: number):
    for a in scene.get_tiles_by_type(3):
        if x == a.x:
            if y == a.y:
                return 1
    return 0
text_introduction: TextSprite = None
text_frame: TextSprite = None
thumbnail: Image = None
box: Sprite = None
ban: Sprite = None
mySprite: Sprite = None
text_footer: TextSprite = None
text_credits: TextSprite = None
text_help: TextSprite = None
text_level: TextSprite = None
text_levelset: TextSprite = None
text_title: TextSprite = None
button_lag = 0
state_level = 0
state_selection = 0
undo_box: List[number] = []
undo_ban: List[number] = []
scroll_level = 0
pressed_B = 0
pressed_A = 0
pressed_right = 0
pressed_left = 0
pressed_down = 0
pressed_up = 0
level = 0
levelset = 0
list_levelsets: List[str] = []
list_levelsets = ["Easy", "Microban", "Y. Murase"]
levelset = 0
level = 1
set_up_selection()
"""

Check win condition and manage buttons in a continuous loop.

A win is when all boxes stand on a target tile (pink).

Direction buttons can be pressed repeatedly without delay. They can be pressed continuously, in which case Meowban continues to move, but not too fast.

Button B must be blocked during menu, otherwise a B press during menu will be handled as undo action when the menu returns.

"""

def on_forever():
    if state_selection:
        control_selection()
    if state_level:
        control_level()
    decay_button_lag()
forever(on_forever)
