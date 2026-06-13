# Progress: Ball Breaker

## What Works

- ✅ Game loop at 60 FPS
- ✅ Paddle movement (left/right arrow keys, boundary clamped)
- ✅ Ball sits on paddle, launches with spacebar
- ✅ Ball bounces off screen walls and ceiling
- ✅ Ball collision with paddle (reflects upward)
- ✅ Ball collision with blocks (block removed, ball reflects)
- ✅ Block grid matrix generated with random colors
- ✅ Explosion animation on ball death (5 PNG frames)
- ✅ Ball resets to paddle position after death
- ✅ Ball follows paddle when not in motion
- ✅ Graceful fallback for missing asset files

## What's Left to Build

- [ ] Start screen ("Press SPACE to Start")
- [ ] Win screen (all blocks cleared)
- [ ] Lose screen (lives exhausted)
- [ ] Lives system (limit deaths)
- [ ] Timer tracking (time played)
- [ ] Brick hit counter
- [ ] Stats display on win/lose screens
- [ ] Collision optimization using radius (partially done)
- [ ] Ball angle changes based on paddle hit position
- [ ] Difficulty scaling (ball speed increase, block descent)
- [ ] Powerup system (multi-ball, explosion, laser, bigger paddle, catch ball)
- [ ] Bullet fix (bullet moves off screen when paddle stops) - marked done in plan

## Known Issues

- Ball collision with blocks uses a simple dx/dy comparison for reflection direction - could be more accurate
- No score/stats tracking
- No game state management (always playing)
- Block removal mutates list during iteration (works but could be cleaner)
- No pause functionality
- Ball speed is constant, no difficulty ramp

## Decision Evolution

- Initial implementation: simple breakout mechanics
- Explosion assets: external pack from bdragon1727
- Block grid: calculated dynamically (h_range - 2 for right margin)
- Ball death: resets to paddle rather than losing a life (no lives system yet)
