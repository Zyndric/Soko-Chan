namespace SpriteKind {
    export const Crate = SpriteKind.create()
}
/**
 * Tile coding:
 * 
 * 14 brown  -- wall (#)
 * 
 *   3 pink     -- target (.)
 * 
 *   7 green   -- player (@)
 * 
 *   6 teal      -- player on target (+)
 * 
 *   4 orange -- crate ($)
 * 
 *   2 red       -- crate on target (*)
 * 
 * 13 tan       -- floor
 */
function reset_states () {
    pressed_up = 0
    pressed_down = 0
    pressed_left = 0
    pressed_right = 0
    pressed_A = 0
    pressed_B = 0
    undo_ban = []
    undo_box = []
    for (let c of sprites.allOfKind(SpriteKind.Player)) {
        c.destroy()
    }
    for (let c of sprites.allOfKind(SpriteKind.Crate)) {
        c.destroy()
    }
    info.setScore(0)
}
controller.A.onEvent(ControllerButtonEvent.Released, function () {
    pressed_A = 0
})
function set_up_level () {
    reset_states()
    if (level == 1) {
        scene.setTileMap(assets.image`level tutorial 01`)
        center_camera()
    } else if (level == 2) {
        scene.setTileMap(assets.image`level microban 01`)
        center_camera()
    } else {
        game.over(true)
    }
    realize_tilemap()
    reset_buttons()
}
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    pressed_down = 0
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    pressed_up = 0
})
function reset_buttons () {
    pressed_up = button_lag
    pressed_down = button_lag
    pressed_left = button_lag
    pressed_right = button_lag
    pressed_A = button_lag
    pressed_B = button_lag
}
function sprite_cache () {
    box = sprites.create(assets.image`crate wood`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate wood on target`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate wood2`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate wood2 on target`, SpriteKind.Crate)
    box = sprites.create(assets.image`create chest`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate chest on target`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate drawer`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate drawer on target`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate marble`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate marble on target`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate car`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate car on target`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate clam`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate clam on target`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate shrub`, SpriteKind.Crate)
    box = sprites.create(assets.image`crate shrub on target`, SpriteKind.Crate)
    scene.setTile(3, assets.image`target switch`, false)
    scene.setTile(3, assets.image`target tan`, false)
    scene.setTile(3, assets.image`target dark purple`, false)
    scene.setTile(3, assets.image`target patch`, false)
    scene.setTile(3, assets.image`target tiled`, false)
    scene.setTile(13, assets.image`floor tan dotted`, false)
    scene.setTile(13, assets.image`floor tan`, false)
    scene.setTile(13, assets.image`floor tiled`, false)
    scene.setTile(13, assets.image`floor dark purple`, false)
    scene.setTile(14, assets.image`wall brown bricks`, true)
    scene.setTile(14, assets.image`wall purple bricks`, true)
    scene.setTile(14, assets.image`wall dark purple bricks`, true)
    scene.setTile(14, assets.image`wall dark brown bricks`, true)
    scene.setTile(14, assets.image`wall steel`, true)
    scene.setTile(14, assets.image`wall red bricks`, true)
    scene.setTile(14, assets.image`wall yellow bricks`, true)
    scene.setTile(14, assets.image`wall teal bricks`, true)
    scene.setTile(14, img`
        6 6 6 c c 6 6 6 6 6 6 c c 6 6 6 
        7 7 7 7 c 7 7 7 7 7 7 7 c 7 7 7 
        7 7 7 7 6 7 7 7 7 7 7 7 6 7 7 7 
        6 6 7 7 6 7 7 7 7 7 7 7 6 c 6 6 
        c 6 6 6 c c c 7 7 7 6 6 6 6 c c 
        c 7 7 7 7 7 7 7 7 7 7 7 7 7 7 6 
        c c 7 7 7 7 7 7 7 7 7 7 7 6 6 6 
        c c c 6 7 c c c c c 7 7 6 c c c 
        6 6 7 7 7 7 6 6 6 6 6 6 6 6 6 6 
        6 6 6 7 7 7 6 6 6 6 6 6 6 6 6 6 
        c c c c 7 6 c c c c c 6 6 c c c 
        c 6 6 6 6 6 6 6 6 6 6 6 6 6 6 c 
        c c c c c c c c c c c c c c c c 
        6 6 c c 6 6 6 6 6 6 c c 6 6 6 6 
        c c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c 
        `, true)
    scene.setTile(14, assets.image`wall plant`, true)
    scene.setTile(14, assets.image`wall sand`, true)
    scene.setTile(14, assets.image`wall reef`, true)
    scene.setTile(14, assets.image`wall colored`, true)
}
function show_menu () {
    game.splash("A - Menu", "B - Undo")
    if (game.ask("Menu", "Reset this level?")) {
        set_up_level()
    } else {
        if (game.ask("Menu", "Go to level selection?")) {
        	
        } else {
            if (game.ask("Menu", "See credits?")) {
            	
            }
        }
    }
}
function move_to (tx: number, ty: number, push_tx: number, push_ty: number) {
    if (!(tiles.tileIsWall(tiles.getTileLocation(tx, ty)))) {
        if (box_on_tile(tx, ty)) {
            if (!(tiles.tileIsWall(tiles.getTileLocation(push_tx, push_ty)))) {
                if (!(box_on_tile(push_tx, push_ty))) {
                    move_box(tx, ty, push_tx, push_ty)
                    move_ban(tx, ty)
                    info.changeScoreBy(-1)
                }
            }
        } else {
            undo_box = []
            move_ban(tx, ty)
            info.changeScoreBy(-1)
        }
    }
}
/**
 * tx, ty are tileset coordinates
 * 
 * dtx, dty are relative deviations of tileset coordinates
 * 
 * x, y are pixel screen coordinates
 */
function walk (dtx: number, dty: number) {
    move_to(tiles.locationXY(tiles.locationOfSprite(ban), tiles.XY.column) + dtx, tiles.locationXY(tiles.locationOfSprite(ban), tiles.XY.row) + dty, tiles.locationXY(tiles.locationOfSprite(ban), tiles.XY.column) + 2 * dtx, tiles.locationXY(tiles.locationOfSprite(ban), tiles.XY.row) + 2 * dty)
}
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    pressed_left = 0
})
/**
 * Set up
 * 
 * Variables ban, level, "undo ban" and "undo box" are unique and used by name.
 * 
 * Variables box, c and t are loop and temporary variables.
 */
function next_level () {
    level += 1
    set_up_level()
}
/**
 * Determine if a box is on a specific tile by comparing their absolute x and y pixel coordiates. Use pixels, because the color-coded Tile object lacks a mechanism to get its tileset coordinates.
 */
function all_boxes_fit () {
    for (let c of sprites.allOfKind(SpriteKind.Crate)) {
        if (!(target_tile(c.x, c.y))) {
            return 0
        }
    }
    return 1
}
function undo_move () {
    if (undo_ban.length == 2) {
        move_ban(undo_ban[0], undo_ban[1])
        info.changeScoreBy(1)
    }
    if (undo_box.length == 4) {
        move_box(undo_box[2], undo_box[3], undo_box[0], undo_box[1])
    }
    undo_ban = []
    undo_box = []
}
function center_camera () {
    scene.centerCameraAt(tiles.tilemapColumns() * tiles.tileWidth() / 2, tiles.tilemapRows() * tiles.tileWidth() / 2)
}
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    pressed_B = 0
})
function move_ban (to_tx: number, to_ty: number) {
    undo_ban = [tiles.locationXY(tiles.locationOfSprite(ban), tiles.XY.column), tiles.locationXY(tiles.locationOfSprite(ban), tiles.XY.row)]
    tiles.placeOnTile(ban, tiles.getTileLocation(to_tx, to_ty))
    if (target_tile(tiles.locationXY(tiles.getTileLocation(to_tx, to_ty), tiles.XY.x), tiles.locationXY(tiles.getTileLocation(to_tx, to_ty), tiles.XY.y))) {
        ban.setImage(assets.image`sokochan on target`)
    } else {
        ban.setImage(assets.image`sokochan`)
    }
}
function box_on_tile (tx: number, ty: number) {
    for (let c of sprites.allOfKind(SpriteKind.Crate)) {
        if (tiles.locationXY(tiles.locationOfSprite(c), tiles.XY.column) == tx) {
            if (tiles.locationXY(tiles.locationOfSprite(c), tiles.XY.row) == ty) {
                return 1
            }
        }
    }
    return 0
}
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    pressed_right = 0
})
function move_box (from_tx: number, from_ty: number, to_tx: number, to_ty: number) {
    for (let c of sprites.allOfKind(SpriteKind.Crate)) {
        if (c.x == tiles.locationXY(tiles.getTileLocation(from_tx, from_ty), tiles.XY.x) && c.y == tiles.locationXY(tiles.getTileLocation(from_tx, from_ty), tiles.XY.y)) {
            undo_box = [from_tx, from_ty, to_tx, to_ty]
            tiles.placeOnTile(c, tiles.getTileLocation(to_tx, to_ty))
            if (target_tile(tiles.locationXY(tiles.getTileLocation(to_tx, to_ty), tiles.XY.x), tiles.locationXY(tiles.getTileLocation(to_tx, to_ty), tiles.XY.y))) {
                c.setImage(assets.image`crate wood on target`)
            } else {
                c.setImage(assets.image`crate wood`)
            }
            return
        }
    }
}
function realize_tilemap () {
    for (let t of scene.getTilesByType(2)) {
        box = sprites.create(assets.image`crate wood on target`, SpriteKind.Crate)
        scene.place(t, box)
        scene.setTileAt(t, 3)
    }
    for (let t of scene.getTilesByType(4)) {
        box = sprites.create(assets.image`crate wood`, SpriteKind.Crate)
        scene.place(t, box)
        scene.setTileAt(t, 13)
    }
    for (let t of scene.getTilesByType(6)) {
        ban = sprites.create(assets.image`sokochan on target`, SpriteKind.Player)
        scene.place(t, ban)
        scene.setTileAt(t, 3)
    }
    for (let t of scene.getTilesByType(7)) {
        ban = sprites.create(assets.image`sokochan`, SpriteKind.Player)
        scene.place(t, ban)
        scene.setTileAt(t, 13)
    }
    scene.setTile(3, assets.image`target dark purple`, false)
    scene.setTile(13, assets.image`floor dark purple`, false)
    scene.setTile(14, assets.image`wall purple bricks`, true)
}
function target_tile (x: number, y: number) {
    for (let t of scene.getTilesByType(3)) {
        if (x == t.x) {
            if (y == t.y) {
                return 1
            }
        }
    }
    return 0
}
let ban: Sprite = null
let box: Sprite = null
let undo_box: number[] = []
let undo_ban: number[] = []
let pressed_B = 0
let pressed_A = 0
let pressed_right = 0
let pressed_left = 0
let pressed_down = 0
let pressed_up = 0
let level = 0
let button_lag = 0
button_lag = 10
level = 0
next_level()
/**
 * Check win condition and manage buttons in a continuous loop.
 * 
 * A win is when all boxes stand on a target tile (pink).
 * 
 * Direction buttons can be pressed repeatedly without delay. They can be pressed continuously, in which case Meowban continues to move, but not too fast.
 * 
 * Button B must be blocked during menu, otherwise a B press during menu will be handled as undo action when the menu returns.
 */
forever(function () {
    if (all_boxes_fit()) {
        next_level()
    }
    if (controller.up.isPressed() && !(pressed_up)) {
        walk(0, -1)
        pressed_up = button_lag
    }
    if (controller.down.isPressed() && !(pressed_down)) {
        walk(0, 1)
        pressed_down = button_lag
    }
    if (controller.left.isPressed() && !(pressed_left)) {
        walk(-1, 0)
        pressed_left = button_lag
    }
    if (controller.right.isPressed() && !(pressed_right)) {
        walk(1, 0)
        pressed_right = button_lag
    }
    if (controller.A.isPressed() && !(pressed_A)) {
        show_menu()
        reset_buttons()
    }
    if (controller.B.isPressed() && !(pressed_B)) {
        undo_move()
        pressed_B = button_lag
    }
    if (pressed_up) {
        pressed_up += -1
    }
    if (pressed_down) {
        pressed_down += -1
    }
    if (pressed_left) {
        pressed_left += -1
    }
    if (pressed_right) {
        pressed_right += -1
    }
    if (pressed_A) {
        pressed_A += -1
    }
    if (pressed_B) {
        pressed_B += -1
    }
})
