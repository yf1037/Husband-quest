# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Shawn", color="#c8ffc8")
define m = Character("May", color="#ffc8c8")


# The game starts here.


transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ likability = 50
    $ level = 'Boy Friend'
    $ stress = 0
    show screen gameUI

    scene bg room:
        zoom 2
        xalign 0.6
        yalign 0.7

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show shawn_nutrual:
        zoom 0.4
        xalign 0.25
        yalign -0.2

    # These display lines of dialogue.

    s "Hi! I'm Shawn, born and raised as American. The goal of my life is being happy, and I was never restrianed by cultural tranditions."

    s "As it happens, I have been dating a Chinese girl friend, May, for 3 years and her family is presuring us to get married."

    s "I was not enthused at first, but now I'm convinced it's a good idea to get married so that May can become a U.S. resident."

    s "I've heard becoming a Chinese husband is quite a process. Because Chinese parents really care about cultural heritages, they don't like non-chinese son-in-laws. So, I'm hoping you can help me out."
    $ likability -= 20
    $ stress += 10

    hide shawn_nutrual
    "likability {color=#f00}-20{/color}\nstress {color=#f00}+10{/color}\nYou can view your stats using the stats botton on the top right corner anytime during the game"

    show shawn_thinking:
        zoom 0.4
        xalign 0.75
        yalign -0.2

    s "It is now January and May has decided to go visit her family for Chinese New Year. What should I do?"

    menu:

        "Offer to go with her":
            $ likability += 10
            $ stress +=10
            hide shawn_thinking
            show shawn_worried:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            s "That gives her parents a good impression. But... I have no idea what to expect since I have never been outside U.S. before.\nlikability {color=#00ff00}+20{/color}\nstress {color=#f00}+10{/color}"
            hide shawn_worried
            show shawn_disappointed:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            $ stress += 10
            "Turns out, there isn't enough time for Shawn to get a Chinese visa. So, it didn't work out.\nstress {color=#f00}+10{/color}"
            hide shawn_disappointed
        "Ask her to bring gifts to her parents for me":
            hide shawn_thinking
            show shawn_nutrual:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            $ likability +=5
            s "May's parents liked the gifts, althoug they would prefer I go myself.\nlikability {color=#00ff00}+5{/color}"

        "Wish her a good time":
            $ likability -= 5
            hide shawn_thinking
            show shawn_bad:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            s "It aligns with her parents' bad expectation for \'American\'.\nlikability {color=#f00}-5{/color}"
            hide shawn_bad

    "Time flies and it's now Chinese New Year's Eve..."

    $ time = 3
    $ timer_range = 3
    $ timer_jump = "scene2"
    show screen countdown

    menu:
        "Ignore":
            hide screen countdown
            show shawn_worried:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            s "I missed the opportunity."
            hide shawn_worried
            jump scene2

        "Wish her family happy new year":
            hide screen countdown
            $ likability += 20
            show shawn_good:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            s "This is a success!\nlikability {color=#00ff00}+20{/color}"
            hide shawn_good
            jump scene2

        "Ignore":
            hide screen countdown
            show shawn_worried:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            s "I missed the opportunity."
            hide shawn_worried
            jump scene2

        "Ignore":
            hide screen countdown
            show shawn_worried:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            s "I missed the opportunity."
            hide shawn_worried
            jump scene2

label scene2:
    "So the Chinese New Year has passed and May came back with her parents expectations..."
    show shawn_nutrual:
        zoom 0.4
        xalign 0.25
        yalign -0.2

    show may_casual flip:
        zoom 0.39
        xalign 0.75
        yalign -0.5

    s "So, what's the news?"
    m "Lots of expectations:"

    show tiqin:
        zoom 0.5
        yalign 0
        xalign 0.52

    m "In Chinese culture, the boy friend must propose to the girl friend's parents. Only with the parents proval can they get married. A ritual called \'Ti Qin\'."
    hide tiqin

    s "What do I have to do for Ti Qin?"
    m "Tranditionally, you should bring many gifts to my parents with your family. And say many good words to gain their approval."
    m "Since you cannot travel, my parents agreed you can talk to them over WeChat. But it's still a formal meeting."
    m "You should start with pick a auspicious day and make arrangments with my parents."
    s "Auspicious day?"
    m "You know, the Chinese almanac dictates which days are good for which activities. All big events, Ti Qin, marriage, moving, have to be on auspicious days."
    hide may_casual flip
    hide shawn_nutrual

    show shawn_working:
        zoom 0.4
        xalign 0.75
        yalign -0.1

    show may_casual:
        zoom 0.39
        xalign 0.25
        yalign -0.5

    "After much research, Shawn decided on Feb. 14th at 8am (9pm in China) and arranged the video call with May's parents."
    m "That's a good start. Now let's prepare the gifts."
    m "Although you won't be able to bring my parents goodies, such as flowers, fruits and candies, your parents should still give my parents a check."
    s "A check? How much?"
    m "It's usaully tens of thousands of dollars. And it has to be an auspicious number, like 10k+1, 66k, 88k."
    hide may_casual
    hide shawn_working

    show shawn_thinking:
        zoom 0.4
        xalign 0.75
        yalign -0.2

    s "What should I do?"
    menu:
        "Don't ask money from my parents":
            $ money = 0
        "Ask 6k from my parents":
            $ money = 1
        "Ask 10k+1 from my parents":
            $ money = 2

    $ family = 0
    $ prepared = 0
    s "It's one week from now. How should I prepare?"
    menu:

        "Work off some of the stress":
            $ stress -= 5
            hide shawn_thinking
            "stress {color=#00ff00}-5{/color}"

            show shawn_thinking:
                zoom 0.4
                xalign 0.75
                yalign -0.2

            s "I still have a couple days. How should I prepare?"
            menu:

                "Work off some of the stress":
                    $ stress -= 5
                    hide shawn_thinking
                    "stress {color=#00ff00}-5{/color}"

                "Invite my family members":
                    hide shawn_thinking
                    $ family = 1
                    show shawn_call:
                        zoom 0.4
                        xalign 0.5
                        yalign -0.1

                    s "Good. All of my family will be there."
                    hide shawn_call

                "Prepare a speech":
                    hide shawn_thinking
                    $ stress += 10
                    $ prepared = 1
                    show shawn_working:
                        zoom 0.4
                        xalign 0.5
                        yalign -0.1

                    s "It's stressful but I'm ready.\nstress {color=#f00}+10{/color}"
                    hide shawn_working

        "Invite my family members":
            hide shawn_thinking
            $ family = 1
            show shawn_call:
                zoom 0.4
                xalign 0.5
                yalign -0.1

            s "Good. All of my family will be there."
            hide shawn_call

            show shawn_thinking:
                zoom 0.4
                xalign 0.75
                yalign -0.2

            s "I still have a couple days. How should I prepare?"
            menu:

                "Work off some of the stress":
                    $ stress -= 5
                    hide shawn_thinking
                    "stress {color=#00ff00}-5{/color}"

                "Prepare a speech":
                    hide shawn_thinking
                    $ stress += 10
                    $ prepared = 1
                    show shawn_working:
                        zoom 0.4
                        xalign 0.5
                        yalign -0.1

                    s "It's stressful but I'm ready.\nstress {color=#f00}+10{/color}"
                    hide shawn_working

        "Prepare a speech":
            hide shawn_thinking
            $ stress += 10
            $ prepared = 1
            show shawn_working:
                zoom 0.4
                xalign 0.5
                yalign -0.1

            s "It's stressful but I'm ready.\nstress {color=#f00}+10{/color}"
            hide shawn_working

            show shawn_thinking:
                zoom 0.4
                xalign 0.75
                yalign -0.2

            s "I still have a couple days. How should I prepare?"
            menu:

                "Work off some of the stress":
                    $ stress -= 5
                    hide shawn_thinking
                    "stress {color=#00ff00}-5{/color}"

                "Invite my family members":
                    hide shawn_thinking
                    $ family = 1
                    show shawn_call:
                        zoom 0.4
                        xalign 0.5
                        yalign -0.1

                    s "Good. All of my family will be there."
                    hide shawn_call

    hide bg room
    show bg_call:
        zoom 0.32
        xalign 0.7
        yalign 0.5

    show shawn_nutrual:
        zoom 0.4
        xalign 0.25
        yalign -0.2

    s "Today is the day. I rearranged the living room yesterday and tested the video. I got up early and dressed up in business casual."

    if family:
        hide shawn_nutrual
        show family:
            zoom 0.5
            yalign 0.5
            xalign 0.5
        show shawn_nutrual:
            zoom 0.6
            xalign 0.55
            yalign -0.05

        $ likability += 10
        s "I introduced my family members to May's parents. They liked the bonds among my family.\nlikability {color=#00ff00}+10{/color}"
    else:
        hide shawn_nutrual
        show shawn_nutrual:
            zoom 0.6
            xalign 0.55
            yalign -0.05
        $ likability -= 15
        s "May's parents was suprised to see that none of my family showed up.\nlikability {color=#f00}-15{/color}"

    if prepared:
        $ likability += 10
        s "I impressed May's parents with the speech I prepared.\nlikability {color=#00ff00}+10{/color}"
    else:
        $ likability -= 20
        s "I stumbled when I got nervous.\nlikability {color=#f00}-20{/color}"

    if likability < 0:
        hide  shawn_nutrual
        show shawn_disappointed:
            zoom 0.6
            xalign 0.55
            yalign -0.05

        s "(I'm doing really bad)"

    if money:
        if money > 1:
            $ likability += 20
            hide shawn_disappointed
            show shawn_nutrual:
                zoom 0.6
                xalign 0.55
                yalign -0.05

            s "When my parents gave them the check, they were really happy because we followed the Chinese trandition. And the amount of money showed our sincerity.\nlikability {color=#00ff00}+20{/color}"
        else:
            $ likability +=15
            hide shawn_disappointed
            show shawn_nutrual:
                zoom 0.6
                xalign 0.55
                yalign -0.05

            s "When my parents gave them the check, they were really happy because we followed the Chinese trandition.\nlikability {color=#00ff00}+15{/color}"
    else:
        $ likability -= 5
        s "May's parents showed their understanding towards the lack of the check, but they would like it better if I have followed the trandition.\nlikability {color=#f00}-5{/color}"

    call checkstat


    s "Finally, May's parents asked me when would we get the mariage certificate and when would be the marriage ceremony. I answered..."

    menu:
        "Prepare for the wedding first and get the marriage certificate":
            $ jump_label = "ceremony"
            s "We are going to have the ceremony next summer"

        "Get the marriage certificate first, so May can get a green card":
            $ jump_label = "certificate"
            "When are you going to get the marriage certificate?"

            menu:
                "March 18th, St. Patrick's Day":
                    $ likability += 0

                "Next Friday, the nearest date":
                    $ likability += 0

                "March 8th, an auspicious day according to Chinese almanac":
                    $ likability += 10
                    "likability {color=#00ff00}+10{/color}"

    s "I also agreed to have a Chinese wedding in addition to the wedding in the U.S."
    call checkstat

    $ level = "Fiance"

    scene bg room:
        zoom 2
        xalign 0.6
        yalign 0.7

    if likability < 20:
        show shawn_worried:
            zoom 0.4
            xalign 0.25
            yalign -0.2

        $ stress += 10
        s "I barely servived the Ti Qin. I'll have to perform better later.\nstress {color=#f00}+10{/color}"
        call checkstat
    else:
        if likability < 60:
            show shawn_nutrual:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            s "I did my best and it went ok."
        else:
            show shawn_good:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            s "I did it! It was a success!!"

    $ level = "Fiance"
    "Congretulations!!! You have now reached level Fiance!"

    $ ceremony = 1
    $ certificate = 1
    jump expression jump_label

label certificate:

    scene bg room:
        zoom 2
        xalign 0.6
        yalign 0.7

    show shawn_call:
        zoom 0.4
        xalign 0.5
        yalign -0.1

    s "As the date is near, May and I called all the city halls and clerks ASAP."

    hide shawn_call
    show shawn_thinking:
        zoom 0.4
        xalign 0.75
        yalign -0.2

    s "We need to get a officiant first..."

    menu:
        "Make an appointment with a judge or city clerk":
            $ stress += 10
            "There are no appointments available until a month later.\nstress {color=#f00}+10{/color}"
            call checkstat
            menu:
                "Postpone":
                    hide shawn_thinking
                    show shawn_nutrual:
                        zoom 0.4
                        xalign 0.25
                        yalign -0.2

                    show may_upset:
                        zoom 0.39
                        xalign 0.75
                        yalign -0.5

                    $ likability -= 15
                    m "Marriage is a big thing. You cannot give my parents a date that doesn't work.\nlikability {color=#f00}-15{/color}"
                    call checkstat
                    hide shawn_nutrual
                    hide may_upset
                    "After much negotiation, May's parents eventually agreed to the new date."

                "Ask a friend to get ordianed":
                    $ likability -= 0

                "Pay for a private officiant":
                    "money {color=#f00}-$200{/color}"

        "Ask a friend to get ordianed":
            $ likability -= 0

        "Pay for a private officiant":
            "money {color=#f00}-$200{/color}"

    hide shawn_thinking
    show shawn_working:
        zoom 0.4
        xalign 0.5
        yalign -0.1

    s "Next, we made an appointment with city clerk to apply for the marriage certificate."
    s "And we got one of my family members to be the witness."

    hide shawn_working

    $ done = 0
    $ cake = 0
    $ ring = 0
    $ decor = 0
    $ dinner = 0
    $ ind = 0
    $ stressloss = 0
    $ sloss = 0
    $ photo = 0
    while done==0:
        show bg room:
            zoom 2
            xalign 0.6
            yalign 0.7

        if stressloss == 0:
            if ind == 2:
                show shawn_working:
                    zoom 0.4
                    xalign 0.5
                    yalign -0.1

                s "I'm getting tired of all these work..."

            else:
                if ind == 3:
                    show shawn_working:
                        zoom 0.4
                        xalign 0.5
                        yalign -0.1

                    $ stress += 5
                    s "This is stressful...\nstress {color=#f00}+5{/color}"
                else:
                    if ind > 3:
                        show shawn_working:
                            zoom 0.4
                            xalign 0.5
                            yalign -0.1

                        $ stress += 10
                        s "This is A Lot of work...\nstress {color=#f00}+10{/color}"
        else:
            $ stressloss = 0

        hide shawn_working
        call checkstat

        show shawn_thinking:
            zoom 0.4
            xalign 0.75
            yalign -0.2

        s "What should we prepare for the day?"

        menu:
            "Wedding cake" if cake == 0:
                $ cake = 1
                hide shawn_thinking
                show bg bakery:
                    zoom 0.35

                show shawn_working:
                    zoom 0.4
                    xalign 0.9
                    yalign -0.1

                s "We booked a customized cake"
                hide shawn_working
                hide bg bakery

            "Decorations" if decor == 0:
                $ decor = 1
                hide shawn_thinking
                show bg flower shop:
                    zoom 1.2
                    xalign 0.5
                    yalign 0.7

                show shawn_working:
                    zoom 0.4
                    xalign 0.5
                    yalign -0.5

                s "We bought some flowers and balloons"
                hide shawn_working
                hide bg flower shop

            "Ring" if ring == 0:
                $ ring = 1
                hide shawn_thinking
                show bg mall:
                    zoom 1.2

                show may_nutrual flip:
                    zoom 0.39
                    xalign 0.68
                    yalign -0.5

                show shawn_nutrual flip:
                    zoom 0.4
                    xalign 0.45
                    yalign -0.2

                s "After much searching, we decided it's not enough time to decide on an expensive ring."
                s "But we were able to buy a cheap temporary ring."
                hide bg mall
                hide shawn_nutrual flip
                hide may_nutrual flip

            "Photographer" if photo == 0:
                $ photo = 1
                hide shawn_thinking
                show shawn_call:
                    zoom 0.4
                    xalign 0.5
                    yalign -0.1

                s "I booked a photographer for the day."
                hide shawn_call

            "Dinner with witnesses and family" if dinner == 0:
                $ dinner = 1
                hide shawn_thinking
                show shawn_call:
                    zoom 0.4
                    xalign 0.5
                    yalign -0.1

                s "I called up a fancy restaurant and made a reservation."
                hide shawn_call

            "Work off some stress" if sloss < 5:
                $ stress -= 5
                $ stressloss = 1
                $ sloss += 1
                hide shawn_thinking
                "stress {color=#00ff00}-5{/color}"

            "All prepared":
                $ done = 1

        $ ind += 1

    scene bg backyard:
        zoom 1.6
        xalign 0.5
        yalign 0.5

    "Today is the day"
    if decor:
        show balloons:
            zoom 0.32
            xalign 0
            yalign 6.5

        s "We put up the decorations."

    if photo:
        show photographer:
            zoom 0.1
            xalign 1.1
            yalign 0.7

        s "The photographer showed up a little before the ceremony and took many nice pictures."
        hide photographer

    s "Our officiant did a great job with the ceremony."

    if ring:
        s "And I put the shinny ring on May's finger."

    if dinner:
        scene bg restaurant:
            zoom 0.35

        s "Then we went to the fancy restaurant and took many pictures of the nice food and celebrations."

    if cake:
        show bg room:
            zoom 2
            xalign 0.6
            yalign 0.7

        show cake:
            zoom 0.132
            xalign 0.578
            yalign 0.442

        show may_nutrual flip:
            zoom 0.39
            xalign 0.7
            yalign -0.5

        show shawn_nutrual flip:
            zoom 0.4
            xalign 0.15
            yalign -0.2

        s "Finally, we cut up the cake."
        hide cake

    scene bg room:
        zoom 2
        xalign 0.6
        yalign 0.7

    show shawn_nutrual:
        zoom 0.4
        xalign 0.25
        yalign -0.2

    s "We celebrated late into the night."
    s "The second day, May send all the pictures to her parents."

    $ score = decor+ring+cake+photo+dinner

    if score == 0:
        hide shawn_nutrual
        show shawn_disappointed:
            zoom 0.4
            xalign 0.25
            yalign -0.2

        $ likability -= 20
        s "May's parents are very disappointed with the unpreparedness of the wedding.\nlikability {color=#f00}-20{/color}"
        hide shawn_disappointed
    else:
        if score == 1:
            hide shawn_nutrual
            show shawn_worried:
                zoom 0.4
                xalign 0.25
                yalign -0.2

            s "May's parents think the ceremony is just ok."
            hide shawn_worried
        else:
            if score < 3:
                $ score = 10*score
                $ likability += score
                s "May's parents liked the ceremony.\nlikability {color=#00ff00}+[score]{/color}"
                hide shawn_nutrual
            else:
                $ score = 30 + 5*(score - 3)
                $ likability += score
                hide shawn_nutrual
                show shawn_good:
                    zoom 0.4
                    xalign 0.25
                    yalign -0.2

                s "The ceremony was a success!\nlikability {color=#00ff00}+[score]{/color}"
                hide shawn_good

    call checkstat
    $ certificate = 0

    if ceremony:
        $ level = "Fiance-Husband"
        "Congretulations!!! You have now reached level Fiance-Husband!"
        jump ceremony
    else:
        $ level = "Husband-to-be"
        "Congretulations!!! You have now reached level Husband-to-be!"
        jump wedding


label ceremony:

    "Ceremony in planning..."

    $ ceremony = 0

    if certificate:
        $ level = "Fiance-Husband"
        "Congretulations!!! You have now reached level Fiance-Husband!"
        jump certificate
    else:
        $ level = "Husband-to-be"
        "Congretulations!!! You have now reached level Husband-to-be!"
        jump wedding


label wedding:

    scene bg flight:
        zoom 0.6
        xalign 0.5
        yalign 0.5

    "Flying to China..."

    "To be continued..."

    # This ends the game.

    return


label checkstat:
    if likability < 0:
        scene bg room:
            zoom 2
            xalign 0.6
            yalign 0.7
        show shawn_disappointed:
            zoom 0.4
            xalign 0.25
            yalign -0.2
        s "May's parents are completely disappointed with me and forced us to break up."
        "You made it to {color=#c8ffc8}[level]{/color}"
        $ MainMenu(confirm=False)()
    else:
        if stress > 100:
            scene bg room:
                zoom 2
                xalign 0.6
                yalign 0.7
            show shawn_disappointed:
                zoom 0.4
                xalign 0.25
                yalign -0.2
            s "I'm completely stressed out and I don't think it will work out with May."
            "You made it to {color=#c8ffc8}[level]{/color}"
            $ MainMenu(confirm=False)()
        else:
            if likability > 100:
                $ likability = 100
            else:
                if stress < 0:
                    $ stress = 0

            return
