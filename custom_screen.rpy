screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 10
        idle "stats_idle.png"
        action ShowMenu("StatsUI")

screen StatsUI:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Level" size 40
                text "Likability/100" size 40
                text "Stress/100" size 40

            vbox:
                spacing 10
                text "[level]" size 40
                text "[likability]" size 40
                text "[stress]" size 40
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 10
        idle "return_idle.png"
        action Return()
