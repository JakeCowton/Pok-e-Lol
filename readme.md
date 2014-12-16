# AI Assignment Plan

This document will outline what will be achieved by the AI assignment

[TOC]

## How to run

1. Download the source code (this example will assume you have downloaded to `/home/[user_name]/Downloads/`)
2. Extract the tarball
3. Navigate to `/home/[user_name]/Downloads/`
4. Run `ipython -m Pok-e-Lol.manager`

## Concept
- League of Legends crossed with pokemon style game
- Turn based
- Abilities will be assigned to champions which will either be offensive or defensive
    + Q, W & R are offensive abilities
    + E is defensive
- Will be written **very** abstractly so that champions can easily be created and plugged into the system


## Game play

Each turn will have the user select an ability which will then take effect and be put on cooldown.
Some abilities have an 'over time' effect (usually the **W**) meaning they might heal or damage a champion (them self or another) over several turns from one usage.

### Abilities

- All champions will have 4 abilities:
    + **Basic attack** (Q)
        * Deals raw damage
        * No cooldown
    + **Over time** (W)
        * Poisons, damage multiplier for next *x* turns etc.
        * Low cooldown
    + **Defensive** (E)
        * Heal, increase armour for next *x* turns
        * Mid cooldown
    + **Ultimate** (R)
        * Either buff/attack
        * High cooldown
- Damage abilities will remove their damage value from the receivers health
- Cool-downs will apply to abilities. These will be an amount of turns.
- The NPC will decide whether to attack or defend, after this the specific ability is chosen


## Technologies

+ Perceptron
    * To decide whether to attack or defend
+ Multi-layer ANN
    * Choose which attack to use
+ OCEAN Emotion modelling
    * Emotions will affect decision making
+ Fuzzy Logic / Fuzzy Inference System
    * Examples of Sugeno and Mamdani saved in bookmarks

### Perceptron
Used to decide whether to attack or defend
Inputs:

- NPC health
- Player health

These are linearly separable

#### Rules

Decisions will be made based on this graph

```
   10 | + + + + + + + + + +
N   9 | + + + + + + + + + +
P   8 | + + + + + + + + + +
C   7 | + + + + + + + + + +
    6 | + + + + + + + + + -
H   5 | + + + + + + + + - -
E   4 | + + + + + + - - - -
L   3 | + + + + + - - - - -
T   2 | + + + + - - - - - -
H   1 | + + + - - - - - - -
      | _ _ _ _ _ _ _ _ _ _
    0   1 2 3 4 5 6 7 8 9 10
           USER HEALTH
```

### Multi-layer ANN
If the perceptron says to attack the decisions tree uses the following to choose which ability to use:

- User health
- Is **R** available
- Is **Q** available
- Is **W** available

With the following training data
```
    t_data[0]  = (0.04,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  0.0,   0.0)
    t_data[1]  = (0.04,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
    t_data[2]  = (0.04,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
    t_data[3]  = (0.04,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  0.0,   0.0)
    t_data[4]  = (0.04,    0.04, ON_CD,  0.02, AVAIL,  0.01),   (0.0,  0.7,   0.5)
    t_data[5]  = (0.03,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  0.0,   0.0)
    t_data[6]  = (0.03,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
    t_data[7]  = (0.03,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
    t_data[8]  = (0.03,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  0.0,   0.0)
    t_data[9]  = (0.03,    0.04, ON_CD,  0.02, AVAIL,  0.01),   (0.0,  0.8,   0.2)
    t_data[10] = (0.02,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
    t_data[11] = (0.02,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
    t_data[12] = (0.02,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
    t_data[13] = (0.02,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
    t_data[14] = (0.02,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
    t_data[15] = (0.02,    0.04, ON_CD,  0.02, AVAIL,  0.01),   (0.0,  1.0,   0.0)
    t_data[16] = (0.02,    0.04, ON_CD,  0.02, AVAIL,  0.01),   (0.0,  1.0,   0.0)
    t_data[17] = (0.01,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   1.0)
    t_data[18] = (0.01,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   1.0)
    t_data[19] = (0.01,    0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.0)
    t_data[20] = (0.01,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
    t_data[21] = (0.01,    0.04, AVAIL,  0.02, AVAIL,  0.01),   (1.0,  1.0,   0.0)
    t_data[22] = (1.0,     0.04, AVAIL,  0.02, AVAIL,  0.01),   (0.7,  0.9,   0.2)
    t_data[23] = (0.8,     0.04, AVAIL,  0.02, ON_CD,  0.01),   (1.0,  0.0,   0.6)
```

and if it says to defend:

- Use **E**

Once an item system is developed, an MLP will be used to calculate what to do using these as inputs:

- Player health
- NPC health
- Is **E** available
- Is a potion available

### OCEAN Emotion modelling
Each champion will get a score for each of the components of OCEAN. These will be used to make decisions.

#### Openness

Scores here are inversely proportional to logic.
High score = low logic
Low score = high logic

#### Conscientiousness

Scores here are directly proportional to logic.
High score = high logic
Low score = low logic

#### Extroversion

Will be more likely to take a quick solution than the best solution.
E.g. It might calculate attack or defend, but will take a random guess after that.

EDIT: Take SLP finding as fact **but** use logic value for MLP

#### Agreeableness

More likely to go with what is suggested.
High score = high logic
Low score = low logic

#### Neuroticism

High scores here will mean the logic decreases each time damage is received.
Causes a decay in logic per damage taken


### Fuzzy Inference System

This will be used to manage how emotions affect decision making.
E.g:

- If logic is high - Do what is suggested
- If it is medium - Distort the MLP decision
- If it is low - Distort the MLP decision even more

## Further Development (If time permits)

- Allow players to upgrade their champion (outside of fights)
    + This will require matchmaking so that the NPC will have upgrades too
- Multi-player using client-server
- Use a search algorithm to calculate which sequence will maximise damage whilst also protecting self?
    + Consider average ability damage
    + Average opponent health etc

### Items

- Can be bought between fights
- Items can affect:
    + Health (potion)
        *  To be used during fights
    + Health
        * Permanent increase
    + Weapons
        * To increase attack - not to use
    + Armour
        * Increase the armour stat
    + Boots
        * Increase agility
    + Cooldowns
        * Reduce ability cooldowns
- 6 items maximum per champion
- One pair of boots only