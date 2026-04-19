# 🎮 Asteroids Curriculum Roadmap

**Goal:** First-principles game development mastery through progressive building.
**Language:** Python + Pygame → C++ (later)
**Format:** 30 min/day. Write code yourself. Claude checks work and teaches concepts.

---

## The Ladder

```
Pong → Asteroids → Donkey Kong → Super Mario Bros → Castlevania → Symphony of the Night → Diablo I → Warcraft I → Diablo II/WoW
```

---

## ✅ LEVEL 1: Pong — Complete

Core game loop, state, collision detection, scoring, paddle and ball physics.
Repo: https://github.com/rdowning07/pong

- [x] Game loop
- [x] Variables and state
- [x] Keyboard input
- [x] Moving objects
- [x] Collision detection
- [x] Scoring
- [x] Game over and restart

---

## 🟡 LEVEL 2: Asteroids — In Progress

### What You're Really Learning

Motion that isn't just left/right/up/down. Objects rotate. Things spawn and despawn. Lists of objects instead of one or two.

### Skills Checklist

- [x] Repo setup with pyenv
- [x] Game loop with delta time
- [x] Ship class with rotation
- [x] Thrust and momentum
- [x] Screen wrap
- [x] Asteroid class with movement
- [x] Multiple asteroids in a list
- [ ] Bullet class
- [ ] Shooting mechanic
- [ ] Collision detection (circle vs circle)
- [ ] Asteroid splitting
- [ ] Game over state
- [ ] Score tracking

### Architecture Concepts

- [x] What is delta time and why does it matter?
- [x] What is a vector?
- [x] What is a class and what is an instance?
- [ ] What does it mean to update a list of objects every frame?
- [ ] What is momentum in code?

### Deliverable

Playable Asteroids. Ship rotates and thrusts, shoots bullets, asteroids split on hit, game ends when ship is hit, score tracked.

---

## 🔴 LEVEL 3: Donkey Kong — Not Started

Gravity, platforms, enemies with simple AI, tilemaps, sprite loading.

- [ ] Gravity and jumping
- [ ] Platform collision
- [ ] Tilemaps
- [ ] Sprite loading
- [ ] Simple enemy AI
- [ ] Animation states
- [ ] Lives system

---

## 🔴 LEVEL 4: Super Mario Bros — Not Started

Scrolling camera, multiple enemy types, power-ups, multiple levels.

- [ ] Scrolling camera
- [ ] Multiple enemy types
- [ ] Power-up system
- [ ] Multiple levels with transitions
- [ ] Sound effects and music

---

## 🔴 LEVEL 5: Castlevania / Metroid / Zelda — Not Started

Connected world, persistent state, inventory, boss fights.

- [ ] Connected rooms and world map
- [ ] Persistent player state
- [ ] Inventory system
- [ ] Complex enemy AI
- [ ] Boss fights

---

## 🔴 LEVEL 6: Symphony of the Night — Not Started

Full Metroidvania. Graduation project for 2D.

- [ ] Full map system
- [ ] Equipment and stat systems
- [ ] Spell and ability system
- [ ] Save system
- [ ] Enemy variety and AI complexity

---

## 🔴 LEVEL 7: Diablo I — Not Started

Top-down single player. RPG systems, procedural dungeon generation.

- [ ] Procedural generation
- [ ] RPG stat systems
- [ ] Inventory and equipment
- [ ] Top-down perspective
- [ ] New engine (Godot or Unity)

---

## 🔴 LEVEL 8: Warcraft I — Not Started

Real-time strategy. Units, resources, buildings, pathfinding, fog of war.

- [ ] Pathfinding
- [ ] Unit state management
- [ ] Resource systems
- [ ] Building and production queues
- [ ] Fog of war
- [ ] RTS camera and unit selection

---

## 🔴 LEVEL 9: Diablo II / WoW — Far Horizon

3D or isometric 3D. Networking if multiplayer. Open ended.

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
