# 🎮 Asteroids Curriculum Roadmap

**Goal:** First-principles game development mastery through progressive building.
**Language:** Python + Pygame → C++ (later)
**Format:** 30 min/day. Write code yourself. Claude checks work and teaches concepts.

---

## The Ladder
Pong → Asteroids → Donkey Kong → Super Mario Bros → Castlevania → Symphony of the Night → Diablo/WoW

---

## 🟢 LEVEL 1: Pong — Complete

Core game loop, state, collision detection, scoring, paddle and ball physics.
Repo: https://github.com/rdowning07/pong

---

## 🟡 LEVEL 2: Asteroids — In Progress

### What You're Really Learning

Motion that isn't just left/right/up/down. Objects rotate. Things spawn and despawn. Lists of objects instead of one or two.

### Skills

* Delta time — frame-rate independent movement
* Vectors and 2D math (sin, cos, angles)
* Classes — Ship, Asteroid, Bullet
* Rotation
* Thrust and momentum (velocity accumulates)
* Wrap-around screen edges
* Lists of objects (multiple asteroids, multiple bullets)
* Spawning and destroying objects
* Collision detection (circle vs circle)

### Architecture Concepts

* What is delta time and why does it matter?
* What is a vector?
* What is a class and what is an instance?
* What does it mean to update a list of objects every frame?
* What is momentum in code?

### Progress

* [x] Repo setup with pyenv
* [x] Game loop with delta time
* [x] Ship class with rotation
* [ ] Thrust and momentum
* [ ] Screen wrap
* [ ] Asteroid class with movement
* [ ] Multiple asteroids in a list
* [ ] Bullet class
* [ ] Shooting mechanic
* [ ] Collision detection
* [ ] Asteroid splitting
* [ ] Game over state
* [ ] Score tracking

### Deliverable

Playable Asteroids. Ship rotates and thrusts, shoots bullets, asteroids split on hit, game ends when ship is hit, score tracked.

---

## 🔴 LEVEL 3: Donkey Kong — Not Started

Gravity, platforms, enemies with simple AI, tilemaps, sprite loading.

---

## 🔴 LEVEL 4: Super Mario Bros — Not Started

Scrolling camera, multiple enemy types, power-ups, multiple levels.

---

## 🔴 LEVEL 5: Castlevania / Metroid / Zelda — Not Started

Connected world, persistent state, inventory, boss fights.

---

## 🔴 LEVEL 6: Symphony of the Night — Not Started

Full Metroidvania. Graduation project for 2D.

---

## 🔴 LEVEL 7: Diablo / WoW — Far Horizon

3D or isometric. New engine. Possibly multiplayer.

---

## Curriculum Principles

**1. You write every line.**
**2. Understand before moving on.**
**3. Boring, explicit code first.**
**4. Git every session.**
**5. The README is part of the work.**

---

*Started: April 2026*
*Target: June 2027*

