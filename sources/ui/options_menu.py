from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock

from sources.logic.music_manager import music_manager
from sources.logic.options_manager import options_manager
from sources.logic.points_manager import points_manager
from sources.logic.questions_manager import questions_manager
from sources.logic.text_manager import txt

from sources.libraries.colors import *
from sources.libraries.logger import log

class OptionsMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.update_music, 0)

        self.main_layout = BoxLayout(
            spacing = 0,
            padding = 0
        )

        self.left_layout = BoxLayout(
            orientation = "vertical",
            spacing = 32,
            padding = 32
        )

        self.right_layout = BoxLayout(
            orientation = "vertical",
            spacing = 0,
            padding = 32
        )

        self.reset_settings_button = Button(
            size_hint = (1, 0.1),
            color = WHITE,
            font_size = 32,
            font_name = txt.small_font,
            halign = "center",
            on_press = self.show_popup
        )

        self.clear_button = Button(
            size_hint = (1, 0.1),
            color = WHITE,
            font_size = 32,
            font_name = txt.small_font,
            on_press = self.show_popup
        )

        self.next_song_button = Button(
            size_hint = (1, 0.1),
            color = WHITE,
            font_size = 32,
            font_name = txt.small_font,
            on_press = self.next_song
        )

        self.return_button = Button(
            size_hint = (1, 0.1),
            color = WHITE,
            font_size = 32,
            font_name = txt.small_font,
            on_press = self.return_in_main_menu
        )


        self.music_label = Label(
            font_size = 32,
            font_name = txt.big_font
        )

        self.music_slider = Slider(
            min = 0,
            max = 100,
            value = options_manager.music_volume * 100
        )


        self.sounds_label = Label(
            font_size = 32,
            font_name = txt.big_font
        )

        self.sounds_slider = Slider(
            min = 0,
            max = 100,
            value = options_manager.sounds_volume * 100
        )



        self.drawing_images_layout = BoxLayout()

        self.drawing_images_checkbox = CheckBox(
            size_hint = (0, 0),
            pos_hint = {"center_x": 1, "center_y": 0.5}
        )


        self.drawing_images_label = Label(
            font_size = 25,
            font_name = txt.small_font,
            halign = "right"
        )



        self.rainbow_buttons_layout = BoxLayout()

        self.rainbow_buttons_checkbox = CheckBox(
            size_hint = (0, 0),
            pos_hint = {"center_x": 1, "center_y": 0.5}
        )

        self.rainbow_buttons_label = Label(
            font_size = 25,
            font_name = txt.small_font,
            halign = "right"
        )





        # Languages options


        self.languages_label = Label(
            font_size = 32,
            font_name = txt.big_font
        )



        self.languages_layout1 = BoxLayout(
            spacing = 16,
            padding = 16
        )

        self.english_checkbox = CheckBox(
            group = "languages"
        )

        self.english_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )

        self.french_checkbox = CheckBox(
            group = "languages"
        )

        self.french_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )



        self.languages_layout2 = BoxLayout(
            spacing = 16,
            padding = 16
        )

        self.russian_checkbox = CheckBox(
            group = "languages"
        )

        self.russian_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )

        self.ukrainian_checkbox = CheckBox(
            group = "languages"
        )

        self.ukrainian_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )


        # Color theme options


        self.color_theme_label = Label(
            font_size = 32,
            font_name = txt.big_font
        )



        self.color_themes_layout1 = BoxLayout(
            spacing = 16,
            padding = 16
        )

        self.blue_checkbox = CheckBox(
            group = "colors"
        )

        self.blue_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )

        self.orange_checkbox = CheckBox(
            group = "colors"
        )

        self.orange_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )



        self.color_themes_layout2 = BoxLayout(
            spacing = 16,
            padding = 16
        )

        self.violet_checkbox = CheckBox(
            group = "colors"
        )

        self.violet_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )

        self.pink_checkbox = CheckBox(
            group = "colors"
        )

        self.pink_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )




        self.color_themes_layout3 = BoxLayout(
            spacing = 16,
            padding = 16
        )

        self.yellow_checkbox = CheckBox(
            group = "colors"
        )

        self.yellow_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )

        self.cyan_checkbox = CheckBox(
            group = "colors"
        )

        self.cyan_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )




        self.color_themes_layout4 = BoxLayout(
            spacing = 16,
            padding = 16
        )

        self.grey_checkbox = CheckBox(
            group = "colors"
        )

        self.grey_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )

        self.black_checkbox = CheckBox(
            group = "colors"
        )

        self.black_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )



        # Questions randomizing styles


        self.randomizing_styles_label = Label(
            font_size = 32,
            font_name = txt.big_font
        )



        self.randomizing_styles_layout1 = BoxLayout(
            spacing = 16,
            padding = 16
        )

        self.normal_checkbox = CheckBox(
            group = "randomizing_styles"
        )

        self.normal_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )

        self.alternative_checkbox = CheckBox(
            group = "randomizing_styles"
        )

        self.alternative_label = Label(
            font_size = 25,
            font_name = txt.small_font
        )


        self.randomizing_styles_layout2 = BoxLayout(
            spacing = 16,
            padding = 16
        )

        self.in_order_checkbox = CheckBox(
            group = "randomizing_styles"
        )

        self.in_order_label = Label(
            font_size = 25,
            font_name = txt.small_font,
            halign = "right"
        )



        self.drawing_images_checkbox.bind(
            active = self.drawing_images_function
        )

        self.rainbow_buttons_checkbox.bind(
            active = self.rainbow_buttons_function
        )

        self.normal_checkbox.bind(active = self.normal_function)
        self.alternative_checkbox.bind(active = self.alternative_function)
        self.in_order_checkbox.bind(active = self.in_order_function)

        self.english_checkbox.bind(active = self.english_function)
        self.french_checkbox.bind(active = self.french_function)
        self.russian_checkbox.bind(active = self.russian_function)
        self.ukrainian_checkbox.bind(active = self.ukrainian_function)

        self.blue_checkbox.bind(active = self.blue_function)
        self.orange_checkbox.bind(active = self.orange_function)
        self.violet_checkbox.bind(active = self.violet_function)
        self.pink_checkbox.bind(active = self.pink_function)
        self.yellow_checkbox.bind(active = self.yellow_function)
        self.cyan_checkbox.bind(active = self.cyan_function)
        self.grey_checkbox.bind(active = self.grey_function)
        self.black_checkbox.bind(active = self.black_function)



        # Adding widgets to layouts

        self.randomizing_styles_layout1.add_widget(
            self.normal_checkbox
        )
        self.randomizing_styles_layout1.add_widget(
            self.normal_label
        )
        self.randomizing_styles_layout1.add_widget(
            self.alternative_checkbox
        )
        self.randomizing_styles_layout1.add_widget(
            self.alternative_label
        )

        self.randomizing_styles_layout2.add_widget(
            self.in_order_checkbox
        )
        self.randomizing_styles_layout2.add_widget(
            self.in_order_label
        )

        self.languages_layout1.add_widget(self.english_checkbox)
        self.languages_layout1.add_widget(self.english_label)
        self.languages_layout1.add_widget(self.french_checkbox)
        self.languages_layout1.add_widget(self.french_label)

        self.languages_layout2.add_widget(self.russian_checkbox)
        self.languages_layout2.add_widget(self.russian_label)
        self.languages_layout2.add_widget(self.ukrainian_checkbox)
        self.languages_layout2.add_widget(self.ukrainian_label)

        self.color_themes_layout1.add_widget(self.blue_checkbox)
        self.color_themes_layout1.add_widget(self.blue_label)
        self.color_themes_layout1.add_widget(self.orange_checkbox)
        self.color_themes_layout1.add_widget(self.orange_label)

        self.color_themes_layout2.add_widget(self.violet_checkbox)
        self.color_themes_layout2.add_widget(self.violet_label)
        self.color_themes_layout2.add_widget(self.pink_checkbox)
        self.color_themes_layout2.add_widget(self.pink_label)

        self.color_themes_layout3.add_widget(self.yellow_checkbox)
        self.color_themes_layout3.add_widget(self.yellow_label)
        self.color_themes_layout3.add_widget(self.cyan_checkbox)
        self.color_themes_layout3.add_widget(self.cyan_label)

        self.color_themes_layout4.add_widget(self.grey_checkbox)
        self.color_themes_layout4.add_widget(self.grey_label)
        self.color_themes_layout4.add_widget(self.black_checkbox)
        self.color_themes_layout4.add_widget(self.black_label)

        self.drawing_images_layout.add_widget(
            self.drawing_images_checkbox
        )
        self.drawing_images_layout.add_widget(
            self.drawing_images_label
        )

        self.rainbow_buttons_layout.add_widget(
            self.rainbow_buttons_checkbox
        )
        self.rainbow_buttons_layout.add_widget(
            self.rainbow_buttons_label
        )

        self.right_layout.add_widget(self.drawing_images_layout)
        self.right_layout.add_widget(self.rainbow_buttons_layout)

        self.right_layout.add_widget(self.languages_label)
        self.right_layout.add_widget(self.languages_layout1)
        self.right_layout.add_widget(self.languages_layout2)
        self.right_layout.add_widget(self.music_label)
        self.right_layout.add_widget(self.music_slider)
        self.right_layout.add_widget(self.sounds_label)
        self.right_layout.add_widget(self.sounds_slider)

        self.right_layout.add_widget(self.color_theme_label)
        self.right_layout.add_widget(self.color_themes_layout1)
        self.right_layout.add_widget(self.color_themes_layout2)
        self.right_layout.add_widget(self.color_themes_layout3)
        self.right_layout.add_widget(self.color_themes_layout4)
        self.right_layout.add_widget(self.randomizing_styles_label)
        self.right_layout.add_widget(self.randomizing_styles_layout1)
        self.right_layout.add_widget(self.randomizing_styles_layout2)

        self.left_layout.add_widget(self.reset_settings_button)
        self.left_layout.add_widget(self.clear_button)
        self.left_layout.add_widget(self.next_song_button)
        self.left_layout.add_widget(self.return_button)

        self.main_layout.add_widget(self.left_layout)
        self.main_layout.add_widget(self.right_layout)

        self.add_widget(self.main_layout)


        self.update_labels()


    def update_labels(self, dt=None, instance=None):

        #! Костыли :(
        self.rainbow_buttons_label.text = \
            txt.rainbow_buttons + "          "
        self.drawing_images_label.text = \
            txt.drawing_images +   "          "
        self.in_order_label.text = \
            txt.in_order +   "                        "

        #! Don't change this part
        #  Kivy library don't accept to center
        #  to left objects of a layout.
        #  So, I set horizontal align to the right
        #  And made the line longer

        self.reset_settings_button.text = txt.reset_settings
        self.clear_button.text = txt.clear_stats
        self.next_song_button.text = txt.next_song
        self.return_button.text = txt.main_menu

        self.music_label.text = txt.music
        self.sounds_label.text = txt.sounds

        self.languages_label.text = txt.languages

        self.normal_label.text = txt.normal
        self.alternative_label.text = txt.alternative
        self.randomizing_styles_label.text = txt.randomizing_styles

        self.english_label.text = txt.english
        self.french_label.text = txt.french
        self.russian_label.text = txt.russian
        self.ukrainian_label.text = txt.ukrainian
        self.color_theme_label.text = txt.color_theme

        self.blue_label.text = txt.blue
        self.orange_label.text = txt.orange
        self.violet_label.text = txt.violet
        self.pink_label.text = txt.pink
        self.yellow_label.text = txt.yellow
        self.cyan_label.text = txt.cyan
        self.grey_label.text = txt.grey
        self.black_label.text = txt.black

        self.reset_settings_button.background_color = \
            options_manager.main_color
        self.clear_button.background_color = \
            options_manager.main_color
        self.next_song_button.background_color = \
            options_manager.main_color
        self.return_button.background_color = \
            options_manager.main_color

    def update_menu(self, instance=None, df=None):

        if options_manager.drawing_images:
            self.drawing_images_checkbox.active = True
        else:
            self.drawing_images_checkbox.active = False

        if options_manager.rainbow_buttons:
            self.rainbow_buttons_checkbox.active = True
        else:
            self.rainbow_buttons_checkbox.active = False

        if options_manager.menus_color == "blue":
            self.blue_checkbox.active = True
        elif options_manager.menus_color == "orange":
            self.orange_checkbox.active = True
        elif options_manager.menus_color == "violet":
            self.violet_checkbox.active = True
        elif options_manager.menus_color == "pink":
            self.pink_checkbox.active = True
        elif options_manager.menus_color == "yellow":
            self.yellow_checkbox.active = True
        elif options_manager.menus_color == "cyan":
            self.cyan_checkbox.active = True
        elif options_manager.menus_color == "grey":
            self.grey_checkbox.active = True
        else:
            self.black_checkbox.active = True

        if options_manager.current_language == "english":
            self.english_checkbox.active = True
        elif options_manager.current_language == "french":
            self.french_checkbox.active = True
        elif options_manager.current_language == "russian":
            self.russian_checkbox.active = True
        else:
            self.ukrainian_checkbox.active = True

        if options_manager.randomizing_style == "alternative":
            self.alternative_checkbox.active = True
        elif options_manager.randomizing_style == "in_order":
            self.in_order_checkbox.active = True
        else:
            self.normal_checkbox.active = True

        self.music_slider.value = \
            options_manager.music_volume * 100
        self.sounds_slider.value = \
            options_manager.sounds_volume * 100

    def update_music(self, dt=None):
        options_manager.music_volume = \
            round(self.music_slider.value / 100, 2)
        options_manager.sounds_volume = \
            round(self.sounds_slider.value / 100, 2)


    def reset_settings(self, df=None, instance=None):

        options_manager.clear()
        txt.set_system_language()
        self.update_labels()
        music_manager.button_clicked.play()
        options_manager.save()


    def return_in_main_menu(self, instance=None):

        questions_manager.status = True
        options_manager.save()

        music_manager.button_clicked.play()
        music_manager.transition.play()

        self.manager.current = "MainMenu"
        self.manager.get_screen('MainMenu').update_labels()
        log.info("Going to the next screen -> MainMenu.")


    def clear_stats(self, instance=None):
        music_manager.button_clicked.play()
        points_manager.clear()

    def next_song(self, instance=None):
        music_manager.button_clicked.play()
        music_manager.next_song()

    def rainbow_buttons_function(self, checkbox, value):
        options_manager.rainbow_buttons = value
        options_manager.save()
        music_manager.button_clicked.play()

    def drawing_images_function(self, checkbox, value):
        options_manager.drawing_images = value
        options_manager.save()
        music_manager.button_clicked.play()

    def english_function(self, checkbox, value):
        txt.set_language("english")
        options_manager.current_language = "english"
        self.update_labels()
        options_manager.save()
        music_manager.button_clicked.play()

    def french_function(self, checkbox, value):
        txt.set_language("french")
        options_manager.current_language = "french"
        self.update_labels()
        options_manager.save()
        music_manager.button_clicked.play()

    def russian_function(self, checkbox, value):
        txt.set_language("russian")
        options_manager.current_language = "russian"
        self.update_labels()
        options_manager.save()
        music_manager.button_clicked.play()

    def ukrainian_function(self, checkbox, value):
        txt.set_language("ukrainian")
        options_manager.current_language = "ukrainian"
        self.update_labels()
        options_manager.save()
        music_manager.button_clicked.play()

    def blue_function(self, checkbox, value):
        options_manager.menus_color = "blue"
        options_manager.color_change()
        options_manager.save()
        self.update_labels()
        music_manager.button_clicked.play()

    def orange_function(self, checkbox, value):
        options_manager.menus_color = "orange"
        options_manager.color_change()
        options_manager.save()
        self.update_labels()
        music_manager.button_clicked.play()

    def violet_function(self, checkbox, value):
        options_manager.menus_color = "violet"
        options_manager.color_change()
        options_manager.save()
        self.update_labels()
        music_manager.button_clicked.play()

    def pink_function(self, checkbox, value):
        options_manager.menus_color = "pink"
        options_manager.color_change()
        options_manager.save()
        self.update_labels()
        music_manager.button_clicked.play()

    def yellow_function(self, checkbox, value):
        options_manager.menus_color = "yellow"
        options_manager.color_change()
        options_manager.save()
        self.update_labels()
        music_manager.button_clicked.play()

    def cyan_function(self, checkbox, value):
        options_manager.menus_color = "cyan"
        options_manager.color_change()
        options_manager.save()
        self.update_labels()
        music_manager.button_clicked.play()

    def grey_function(self, checkbox, value):
        options_manager.menus_color = "grey"
        options_manager.color_change()
        options_manager.save()
        self.update_labels()
        music_manager.button_clicked.play()

    def black_function(self, checkbox, value):
        options_manager.menus_color = "black"
        options_manager.color_change()
        options_manager.save()
        self.update_labels()
        music_manager.button_clicked.play()

    def normal_function(self, checkbox, value):
        options_manager.randomizing_style = "normal"
        options_manager.save()
        music_manager.button_clicked.play()

    def alternative_function(self, checkbox, value):
        options_manager.randomizing_style = "alternative"
        options_manager.save()
        music_manager.button_clicked.play()

    def in_order_function(self, checkbox, value):
        options_manager.randomizing_style = "normal"
        options_manager.save()
        music_manager.button_clicked.play()

    def show_popup(self, instance):

        if instance.text == txt.clear_stats:
            self.current_text = txt.clear_stats
        else:
            self.current_text = txt.reset_settings

        layout = BoxLayout(
            orientation = 'vertical',
            padding = 10
        )

        title_label = Label(
            text = txt.warning,
            font_size = '24sp',
            font_name = txt.small_font
        )

        explanation_label = Label(
            text = txt.warning_message,
            font_size = '14sp',
            halign = "center"
        )

        button_layout = GridLayout(
            cols = 2,
            spacing = 10
        )

        yes_button = Button(
            text = txt.yes,
            font_name = txt.small_font,
            background_color = RED
        )

        no_button = Button(
            text = txt.no,
            font_name = txt.small_font,
            background_color = RED
        )

        yes_button.bind(on_press = self.yes_action)
        no_button.bind(on_press = self.close_popup)

        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)

        layout.add_widget(title_label)
        layout.add_widget(explanation_label)
        layout.add_widget(button_layout)

        self.popup = Popup(
            title = self.current_text.replace("\n", " "),
            content = layout,
            size_hint = (0.6, 0.4),
            background_color = RED
        )

        self.popup.open()

    def yes_action(self, instance):
        if self.current_text == txt.clear_stats:
            self.clear_stats()
        else:
            self.reset_settings()

        self.popup.dismiss()

    def close_popup(self, instance):
        self.popup.dismiss()
