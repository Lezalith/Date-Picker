init -860 python in date_picker:

    import datetime as dt
    import calendar as cal

    calendar = cal.Calendar()

    today = dt.date.today()
    page_date = dt.date(today.year, today.month, 1)

    def call_screen():
        renpy.call_screen("date_picker_screen")

    def month_up():
        global page_date
        page_date = dt.date( page_date.year + int(page_date.month / 12), (page_date.month % 12) + 1, 1)

    def month_down():
        global page_date
        if page_date.month == 1:
            page_date = dt.date(page_date.year - 1, 12, 1)
        else:
            page_date = dt.date(page_date.year, page_date.month - 1, 1)


screen date_picker_screen():

    frame:
        style_prefix "dateText"

        background Solid("#e69e22")
        align (0.5, 0.5)
        padding (10, 10)

        xysize (450, 450)


        # Header
        hbox:
            xalign 0.5
            spacing 35

            textbutton "<<" action Function(date_picker.month_down) style "date_picker_arrow"
            text "{} {}".format(date_picker.page_date.month, date_picker.page_date.year) style "date_picker_yearmonth"
            textbutton ">>" action Function(date_picker.month_up) style "date_picker_arrow"

style date_picker_arrow:
    background None

style date_picker_arrow_text:
    idle_color "666"
    hover_color "000"

style date_picker_yearmonth:
    color "000"
    min_width 160
    text_align 0.5