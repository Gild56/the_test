# Додаток The Test

Привіт! Це **кросплатформенний проєкт** *(для iOS, Android і Windows)*. Ви зможете **проходити тести**, **збирати бали**, **слухати** свою **улюблену музику**, **налаштовувати все на свій смак** і багато іншого!

Подивіться [кредити](credits.md) проєкту.

Ознайомтеся з [changelog](changelog.md), щоб побачити всі оновлення та зміни проєкту.

Якщо вам потрібно знайти помилки під час додавання нових функцій до коду, файл [info.log](info.log) допоможе вам!

Якщо гра вилетіла, зверніться до останнього журналу крашу в [папці *crashes*](crashes/).

## Перші кроки

### На Windows 10 / 11

Щоб почати роботу з грою, вам потрібно встановити Python з [офіційного сайту Python](https://python.org/downloads) і встановити останню версію *Python 3*.

Потім запустіть файл `install.bat`.

## Персоналізація

Ви також можете налаштувати цю гру — додати шрифти, зображення, вікторини, музику тощо.

**На даний момент ви можете налаштовувати гру тільки на Windows 10 / 11!**

### Користувацькі пісні

У грі доступні чудові пісні.

Але ви також можете додати свої власні пісні до гри.

Для цього просто помістіть свої пісні в папку `the_test/resources/music`.

**Щоб зміни набрали чинності, необхідно перезапустити гру!**

### Користувацькі питання

Якщо ви хочете налаштувати вікторину, це можливо!

Просто перейдіть до `the_test/resources/databases` і виберіть мову, яку хочете змінити.

Ви можете написати все, що хочете, але пам'ятайте, що якщо питання налаштовані неправильно, це може не спрацювати!

Щоб правильно налаштувати свої питання, ви повинні написати:

"Ваше питання (воно може бути трохи довгим, і вам не потрібно включати переноси рядків `\n`)", "Правильна відповідь", "Неправильна відповідь №1", "Неправильна відповідь №2", "Неправильна відповідь №3"

#### **Приклади:**

```python
# Ось так:

"Яка тварина є символом тенісного чемпіона Рене Лакоста?", "Крокодил", "Панда", "Ягуар", "Пума"

# Або так:

"З 250 моряків, які вирушили з Магелланом у 1519 році, скільки повернулося до Севільї через 3 роки?", "18", "115", "249", "60"
```

### Додавання зображення до питання

Щоб додати зображення, вам потрібно вказати його у файлі `the_test/resources/databases/images.csv`.

Рядок, у якому ви вказуєте назву зображення, має точно відповідати рядку питання у вашому файлі бази даних.

Якщо ви хочете додати зображення лише до певних питань, залиште відповідні рядки порожніми.

#### **Приклади:**

```python
# Ось так:

""
"magellan.jpg"
"calcium.jpeg"
""
"marseille.jpg"

# І так далі...
```

Ви можете використовувати формати `.jpeg`, `.jpg`, `.png`.

**Це застосує зображення до всіх мов!**

**Якщо рядок налаштований неправильно, це може призвести до збою гри або її некоректної роботи!**

**Щоб зміни набрали чинності, необхідно перезапустити гру!**

### Користувацькі шрифти

Також можна додати користувацькі шрифти.

У грі за замовчуванням використовуються два шрифти:

1. Великий шрифт (називається Pusab) знаходиться в папці `the_test/resources/fonts` і називається **`big_font.ttf`**.

2. Менший шрифт (називається Aller) знаходиться в тій же папці і називається *`small_font.ttf`*.

Зверніть увагу, що вам слід обирати шрифти, які підтримують **кирилицю** (шрифти за замовчуванням — це *кириличні версії* Aller і Pusab), якщо ви збираєтеся використовувати кирилицю.

**Щоб зміни набрали чинності, необхідно перезапустити гру!**

## Зв'язатися зі мною

Для зв'язку зі мною:
* [мій Telegram](https://t.me/gild56) (Я часто перевіряю)
* [мій Discord](https://discord.com/users/gild56) (Я рідко перевіряю)
* [мій Gmail](mailto:gild56gmd@gmail.com) (Я ніколи не перевіряю xD)