# IQ Test app

Hello! It's a **cross-platform** *(iOS, Android & Windows)* project. You can **complete tests**, **collect points**, **listen to** your **favorite music** and so many *more*!

The other languages:

* [Русский](markdown/ПРОЧИТАЙМЕНЯ.md)

* [Українська](markdown/ПРОЧТИМЕНЕ.md)

* [Français](markdown/LISMOI.md)

The [changelog](markdown/changelog.md) to see all the updates and changes of the project.

If the game crashed or you need to find an exception, the [info.log](info.log) file is for you!

## First steps

To begin your experience in the game, you will need to install Python and some modules, like kivy and pygame.

* Alternatively, you can go on the [official Python site](https://python.org/downloads) and install the last *Python 3* version.

* I recommend to install it with the `install.bat` file if you are on Windows.

  Next, open your terminal (Win + R, than write powershell and do enter) and write `pip install pygame`, then `pip install kivy`, and finally `pip install colorama` (colorama is optional, just for debug).

  Finally, you can play this game, opening the `main.py` file.

## Personalization

You can also personalize this game - add some fonts, images, quiz, music, etc..

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

"Your question (it can be a bit long and you don't need to include `\n` line breaks)","The true answer","The wrong answer №1","The wrong answer №2","The wrong answer №3","The path to your image in `iq_test/images` (Optional)"

#### **Examples with image:**

```python
"Sur 250 marins partis 1519 avec Magellan, combien rentrent à Séville, 3 ans plus tard?","18","115","249","60","magellan.jpg"

"Quel scientifique est associé à l'image d'une pomme qui lui tombe sur la tête?","Newton","Archimède","Thalès","Pythagore","newton.jpg"
```

#### **Or without image:**

```python
"Combien contient de calcium en moyenne un corps d'un homme adulte au total?","1 kg","3 kg","5 kg","10 kg"

"Dans quel pays parle-t-on le basque, le catalan, le galicien ou le valencien?","Espagne","Pays-Bas","Allemagne","Norvège"
```

The first example will show the question, the 4 answers and an illustration, because i added the optional path to the image *`magellan.jpg`* or `newton.jpg`

If an image is not included, as in the second example, it will not be visible.

You can use the `.jpeg`, `.jpg`, `.webp`, `.png`.

**If the line isn"t set correctly, it may crash the game or don"t work correctly!**

**To apply your changes, you need to restart the game!**

### Custom fonts

It is also possible to add some custom fonts.

There are two fonts in the vanilla game:

1. The big one (called Pusab) is in the fonts folder and called **`big_font.ttf`**.

2. The smaller one (called Aller) is also in the fonts folder and called **`small_font.ttf`**.

Notice that you should choose fonts with **Cyrillic letters** (the basic ones are *Cyrillic extensions* of Aller and Pusab).

**To apply your changes, you need to restart the game!**

## Credits

Thanks to :

### **Fonts:**

* **Flat-It** for the *Pusab font*.
* **HopKa** for the *Cyrillic Pusab version*.
* **Dalton Maag Inc.** for the *Aller font*.

### **Libraries:**

* **** for the *Pygame* library.
* **The Kivy Team** for the *Kivy* library.
* **** for the *Colorama* library.

### **Music:**

* **Aurora Borealis** for his song *"Beyond the Horizon"*.
* **Daminika** for their song *"Beyond the Stars"*.
* **Dimatis** for their song *"Moonlit Lover"*.
* **Direct & Finding Hope** for their song *"Falling Into Place"*.
* **Elekid** for their song *"Melting Ice"*.
* **Osk** for their song *"Komorebi"*.
* **Rameses B** for their song *"Believing"*.
* **SkyFlair & Exal** for their song *"Afterlife"*.
* **Vexatic** for his song *"Lifted"*.

### **Images:**

* **iStock & Bihagolan** for their image of *Isaac Newton*.
* **Frédérique Catinaud-Brusset Naturopathe & F. Brusset** for their image of the *Calcium*.
* **Unes de l'Equipe** for their image of *René Lacoste*.
* **Interhome** for their image of the *Basque country*.
* **Daily Geek Show, Photo Junction & Shutterstock** for their image of the *Bermuda Triangle*.
* **Le GDE & Mary Evans PL** for their image of the *Magellan's boats*.
* **Cocorico Web** for their image of *colors*.
* **L'Humanité & Nicolas Guillermin** for their image of *Cape Horn*.
* **Guides Ulysse & Chidanand M.** for their image of *Mumbai*.
* **Hôtel Edmont Rostand & Hôtel Marseille** their image of the *Marseille's port*.
* **Premiere & DR** for their image of *Hulk*.
* **Les Echos & Getty Images** for their image of *Halloween*.
* **Voyages et Vagabondages & Lucie A** for their image of *London's Olympics Games opening ceremony*.
* **Fandom, AlleDazzi1 & Disney** for their image of *Hercules*.
* **Papilles et Pullipes** for their image of *popcorn*.
* **La Voix du Nord & Stephne Mortagne** for their image of **.

*If I didn't write an author's name, it's because I didn't find it! There are too many images without credits on internet.

### **Questions:**

* Huge thanks to **Trivial Pursuit** to give me *ideas for questions*!

### **Thanks to everyone who is reading this and playing my game!**

## Contact me

To cantact me, write me on [Gmail](mailto:gild56gmd@gmail.com), [Telegram](https://t.me/gild56) or [Discord](https://discord.com/users/gild56).
