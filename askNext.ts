namespace game {
    /**
     * Prompts the user for a boolean question
     * @param title
     * @param subtitle
     * @param subsubtitle
     */
    //% group="Gameplay"
    //% weight=89 help=game/askNextLevel
    //% blockId=gameasknextlevel block="askNextLevel %title %subtitle %subsubtitle"
    //% group="Prompt"
    export function askNext(title: string, subtitle: string, subsubtitle: string): boolean {
        controller._setUserEventsEnabled(false);
        game.eventContext(); // initialize the game
        control.pushEventContext();
        showHighDialog(title, subtitle, subsubtitle, "A = OK, B = UNDO");
        // short pause so that players don't skip through prompt
        pause(500);

        let answer: boolean = null;
        let aNotHeld = false;
        let bNotHeld = false;
        pauseUntil(() => {
            aNotHeld = aNotHeld || !controller.A.isPressed();
            bNotHeld = bNotHeld || !controller.B.isPressed();

            if (aNotHeld && controller.A.isPressed()) {
                answer = true;
            } else if (bNotHeld && controller.B.isPressed()) {
                answer = false;
            }
            return answer !== null;
        });

        control.popEventContext();
        controller._setUserEventsEnabled(true);
        return answer;
    }

    function showDialogBackground(h: number, c: number) {
        const top = (screen.height - h) >> 1;
        screen.fillRect(0, top, screen.width, h, 0)
        screen.drawLine(0, top, screen.width, top, 1)
        screen.drawLine(0, top + h - 1, screen.width, top + h - 1, 1)

        return top;
    }

    export function showHighDialog(title: string, subtitle: string, subsubtitle: string, footer?: string) {
        // init is called by the earlier call to eventContext()
        const titleFont = image.getFontForText(title || "");
        const subFont = image.getFontForText(subtitle || "");
        const subsubFont = image.getFontForText(subsubtitle || "");
        const footerFont = image.getFontForText(footer || "");
        let h = 8;
        if (title)
            h += titleFont.charHeight;
        if (subtitle)
            h += 2 + subFont.charHeight
        if (subsubtitle)
            h += 2 + subsubFont.charHeight
        h += 8;
        const top = showDialogBackground(h, 9)
        let y = top + 8;
        if (title) {
            screen.print(title, 8, y, screen.isMono ? 1 : 7, titleFont);
            y += titleFont.charHeight + 2;
        }
        if (subtitle) {
            screen.print(subtitle, 8, y, screen.isMono ? 1 : 6, subFont);
            y += subFont.charHeight + 2;
        }
        if (subsubtitle) {
            screen.print(subsubtitle, 8, y, screen.isMono ? 1 : 6, subsubFont);
            y += subsubFont.charHeight + 2;
        }
        if (footer) {
            const footerTop = screen.height - footerFont.charHeight - 4;
            screen.fillRect(0, footerTop, screen.width, footerFont.charHeight + 4, 0);
            screen.drawLine(0, footerTop, screen.width, footerTop, 1);
            screen.print(
                footer,
                screen.width - footer.length * footerFont.charWidth - 8,
                screen.height - footerFont.charHeight - 2,
                1,
                footerFont
            )
        }
    }
}