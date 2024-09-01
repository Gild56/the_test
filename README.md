# IQ Test app

Hello! It's a **cross-platform** *(iOS, Android & Windows)* project. You can **complete tests**, **collect points**, **listen to** your **favorite music** and so many *more*!

The other languages:

* [Русский](markdown/ПРОЧИТАЙМЕНЯ.md)

* [Українська](markdown/ПРОЧТИМЕНЕ.md)

* [Français](markdown/LISMOI.md)

Go check the [credits](markdown/credits.md) of the project.

The [changelog](markdown/changelog.md) to see all the updates and changes of the project.

If you need to find an error, when you added some new features in the code, the [info.log](info.log) file is for you!

If the game crashed, go check the last crashlog in [the crashlogs folder](crashes/).

## First steps

### On Windows 10 / 11

To begin your experience in the game, you will need to install Python from [the official Python site](https://python.org/downloads) and install the last *Python 3* version.

Then, start the `install.bat` file.

## Personalization

You can also personalize this game - add some fonts, images, quiz, music, etc..

**For the moment, you can personnalise the game only on Windows 10 / 11!**

### Custom songs

There are awesome songs available in the game.

But, you can also add your own songs in the game.

To do this, you just need to put your songs in the `iq_test/music` folder.

**To apply your changes, you need to restart the game!**

### Custom questions

If you want to customize the quiz, you can!

You just need to go in the `iq_test/databases` and choose the language, that you want to change.

You can put anything, but remember, that if you don't set the questions correctly, it may not work!

To set your questions correctly you must write:

"Your question (it can be a bit long and you don't need to include `\n` line breaks)","The true answer","The wrong answer №1","The wrong answer №2","The wrong answer №3"

#### **Examples:**

```python
# Like that:

"What animal is the symbol of the former tennis champion René Lacoste?","The crocodile","The panda","The jaguar","The puma"

# Or that:

"Out of 250 sailors who left in 1519 with Magellan, how many returned to Seville 3 years later?","18","115","249","60"
```

### Add an image to your question

To add a image, you must indicate it in the `databases/images.csv`

The line, where you put the name of your image must be the exact line of the question in your database file.

If you want to add an image only to *certains* questions, leave the others *vides*.

#### **Examples:**

```python
# Like that:

""
"magellan.jpg"
"calcium.jpeg"
""
"marseille.jpg"
```

You can use the `.jpeg`, `.jpg`, `.png` formats.

**It'll set the images for all the languages!**

**If the line isn't set correctly, it may crash the game or don"t work correctly!**

**To apply your changes, you need to restart the game!**

### Custom fonts

It is also possible to add some custom fonts.

There are two fonts in the vanilla game:

1. The big one (called Pusab) is in the fonts folder and called **`big_font.ttf`**.

2. The smaller one (called Aller) is also in the fonts folder and called *`small_font.ttf`*.

Notice that you should choose fonts with **Cyrillic letters** (the basic ones are *Cyrillic extensions* of Aller and Pusab).

**To apply your changes, you need to restart the game!**

## Contact me

To cantact me, write me on [Gmail](mailto:gild56gmd@gmail.com), [Telegram](https://t.me/gild56) or [Discord](https://discord.com/users/gild56).
