<br>

> ---
> 
> # Ball Game :football:
> 
> This is a 2D game where you catapult a ball into some boxes.
> 
> I made this project in **_2020 sophomore_** year.
> 
> The initial scope was to learn ```python``` and ```OOP``` concepts.
> 
> I've mainly been refactoring things since then :sweat_smile:.
>
> ---

<br>
<br>

> ---
>
> # Usage :hugs:
> 
> Here is a running instance of the project: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake: :snowflake:
> 
> https://replit.com/@solidwater969/ball-game?v=1
>
> ---

<br>
<br>

> ---
>
> # Run Your Own Instance :sleepy:
> 
> Just download all the files, open them in your favorite IDE, and then hit run.
> 
> The main script is ```LevelGenerator.py```.
>
> ---

<br>
<br>

> ---
>
> # How It Works Part 1: The Building Blocks :yum:
> 
> Here are all the shape primitives: ```rectangle, circle, snowflake``` :sunglasses:
> 
> They each have 2 attributes, a color model and a position model.
> 
> The color model has ```[r, g, b]```. The position model has either:
> 1. ```[x, y, height, width]```
> 2. ```[x, y, :snowman: radius, xVelocity, yVelocity]```
> 3. ```[x, y, radius, xVelocity, yVelocity, yAcceleration]``` :zap:
>
> ---

<br>
<br>

> ---
>
> # How It Works Part 2: Game Structure :mask:
>
> Here are all the shapes being drawn in the game: ```background, floor, circle, squares, crosshair, score, and snowflakes``` :astonished:
> 
> There are generally 2 steps, which kinda works like a graph search:
> 
> 1. Draw all the models **[drawing the current vertex]** :alien:
> 2. Move all the event-based models **[calculating the next edge]**
>
> ---

<br>
<br> :anger:

> ---
>
> # How It Works Part 3: The Events :yum:
>
> The ```circle``` has to obey: :dizzy:
> 
    Launch parameters
    Terminal velocity
    Motion
    Gravity
    Surface friction
    The normal force
    The world border
>
> The ```squares``` die when touch by the ball. :snowman: :snowman:
> 
> And last but not least, the ```snowflakes```:
>
    Come every 40 game ticks
    Die when touched by the ball
    Die when touched by the world border
    Fall with the wind
    Land somewhere
    Melt
> :bread:
> 
> ---
