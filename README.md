# Game of Life

Simulates [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) using pygame and numpy.

## Demo

![Demo](images/demo.gif)

## Installation

### Windows

```
git clone https://github.com/Zike01/Game-of-Life.git
cd Game-of-Life
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
python game.py
```

## Controls

```
LMB - Draw Cell
RMB - Clear Cell
SPACE - Play/Pause
C - Clear Board
Q - Quit
```

## Patterns

<img style='display: block; margin: auto' src='images/Game_of_life_animated_glider.gif' alt=glider>
<p style='text-align: center; font-weight: bold'>
    Glider
</p>

<img style='display: block; margin: auto' src='images/Game_of_life_animated_LWSS.gif' alt=LWSS>
<p style='text-align: center; font-weight: bold'>
    Light-weight spaceship (LWSS)
</p>

<img style='display: block; margin: auto' src='images/Animated_Mwss.gif' alt=MWSS>
<p style='text-align: center; font-weight: bold'>
    Middle-weight spaceship (MWSS)
</p>

<img style='display: block; margin: auto' src='images/Animated_Hwss.gif' alt=HWSS>
<p style='text-align: center; font-weight: bold'>
    Heavy-weight spaceship (HWSS)
</p>

More examples of patterns can be found [here.](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)
