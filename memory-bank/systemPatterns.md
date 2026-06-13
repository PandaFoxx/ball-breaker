# System Patterns: Ball Breaker

## Architecture Overview

Simple game loop pattern with object-oriented model classes.

```
game.py (main loop)
 └── models/
      ├── options.py   (configuration/settings)
      ├── paddle.py    (player paddle)
      ├── ball.py      (ball with collision detection)
      └── block.py     (brick/block matrix)
```

## Key Design Patterns

1. **Game Loop Pattern**
   - Event handling → state update → rendering → tick
   - Runs at 60 FPS via `clock.tick(60)`

2. **Configuration Object Pattern**
   - `options` class stores all tunable game parameters
   - Accessed as a singleton-like instantiation pattern (`options()`)
   - Central place for screen size, colors, speeds, dimensions

3. **Model Classes**
   - Each game entity (paddle, ball, block) is a class
   - Classes own their state (position, dimensions, color)
   - Methods encapsulate movement and behavior logic

4. **Collision Detection**
   - Ball: rectangle-based collision with paddle (AABB)
   - Ball: closest-point-to-circle collision with blocks
   - Screen boundary collision (walls, ceiling)

## Component Relationships

- `game.py` instantiates paddle, ball, and block
- `ball` receives `player.rect()` and `bricks` list for collision handling
- `block.matrix()` generates block grid from options
- `paddle` reads boundary dimensions from options for edge clamping

## Critical Implementation Paths

- Ball death detection: `bottom >= player.top` + out of paddle width range
- Block removal: bricks list mutated in `ball.handle_collisions()`
- Explosion: frame-by-frame sprite blit with delay after ball death
