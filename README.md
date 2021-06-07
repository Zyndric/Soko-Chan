# Soko-Chan

This is a Sokoban clone. Built in MakeCode Arcade. Can be flashed onto a Meowbit console. I built this in order to play Sokoban on the go.

[Try it out online.](https://zyndric.github.i1o/Soko-Chan/)

Game features:

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
* varying graphics for different puzzle sets
* puzzles of up to 11x9 tiles show without scrolling (up to 10x7 tiles of walkable area)

Known issues:

* Levels break and banners lag when the user opens the system menu during the game or level introduction. This is because the system menu continues to execute any running functions (that may be waiting on a "pause" call), but has all variables switched away for the time being.

# Levels

Except for the tutorial puzzles, all puzzles were authored by other people, who published them publicly, and retain the copyright on those levels. I selected mostly small puzzles that lend themselves to the constrained size of the display. That does not mean the puzzles be easy. I like to think the current selection is an interesting mix of easy and difficult puzzles.

- "Microban" by David Skinner. A set of 155 puzzles, of which I included the first 52. There are a lot more puzzles by David Skinner, published in his "Microban" and "Sasquatch" series: https://web.archive.org/web/20130606220354/http://users.bentonrea.com:80/~sasquatch/sokoban

- "Blocks" contains levels of "Blocks" and "Various" by Dries de Clercq. Two sets of 11 and 24 puzzles, respectively. I included 10 puzzles of "Blocks" (I forgot to add the fifth puzzle), and the first 10 puzzles of "Various".

- "Microcosmos" and "Nabokosmos" by Aymeric du Peloux. A set of 40 puzzles each, which I included whole. There are a lot more puzzles by Aymeric du Peloux, published in his Cosmos series: https://aymericdupeloux.wixsite.com/sokoban/home/categories/cosmos-sets

- "Cantrip" by David Holland. A set of 20 puzzles, which I included whole: https://web.archive.org/web/20040806174456/http://www.clickfest88.freeserve.co.uk/cantrip/index.html

- "Takaken" by Kenichiro Takahashi. A set of 7 puzzles, which I included whole.

- "Sokogen" by Jaques Duthen, published as "Sokogen 990602". A set of 78 computer-generated puzzles, of which I included the first 20: https://web.archive.org/web/20041015035341/http://perso.club-internet.fr:80/duthen/SOKOBAN-HTML/sokogen-990602.skm

- "Murase" by Yoshio Murase. A set of 52 computer-generated puzzles, of which I included the first 20: https://web.archive.org/web/20021019225034/http://www.ne.jp:80/asahi/ai/yoshio/sokoban/auto52/auto52.htm

- "Petitesse" by niwa (sokoniwa@yahoo.com). A set of 18 puzzles, which I included whole.


# How to edit

For some reason, MakeCode decided to set up the remaining part of this README in german. Enjoy.

> Diese Seite bei [https://zyndric.github.io/Soko-Chan/](https://zyndric.github.io/Soko-Chan/) öffnen

## Als Erweiterung verwenden

Dieses Repository kann als **Erweiterung** in MakeCode hinzugefügt werden.

* öffne [https://arcade.makecode.com/](https://arcade.makecode.com/)
* klicke auf **Neues Projekt**
* klicke auf **Erweiterungen** unter dem Zahnrad-Menü
* nach **https://github.com/zyndric/Soko-Chan** suchen und importieren

## Dieses Projekt bearbeiten ![Build Status Abzeichen](https://github.com/zyndric/Soko-Chan/workflows/MakeCode/badge.svg)

Um dieses Repository in MakeCode zu bearbeiten.

* öffne [https://arcade.makecode.com/](https://arcade.makecode.com/)
* klicke auf **Importieren** und dann auf **Importiere URL**
* füge **https://github.com/zyndric/Soko-Chan** ein und klicke auf Importieren

## Blockvorschau

Dieses Bild zeigt den Blockcode vom letzten Commit im Master an.
Die Aktualisierung dieses Bildes kann einige Minuten dauern.

![Eine gerenderte Ansicht der Blöcke](https://github.com/zyndric/Soko-Chan/raw/master/.github/makecode/blocks.png)

#### Metadaten (verwendet für Suche, Rendering)

* for PXT/arcade
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
