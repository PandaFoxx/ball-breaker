# Active Context: Ball Breaker

## Current Work Focus

- Memory Bank initialization
- Project state: functional basic breakout game

## Recent Changes (from git log & files)

- Basic game loop implemented with paddle, ball, and block matrix
- Ball collision detection with screen boundaries, paddle, and blocks
- Explosion animation on ball death
- Block grid generation with random colors

## Next Steps (from docs/plan.md)

1. **Screens**
   - Start screen: "Press SPACE to Start"
   - Win screen: when all blocks cleared
   - Lose screen: when lives exhausted
2. **Lives System** - Limit number of deaths
3. **Stats Tracking**
   - Time played
   - Bricks hit count
   - Show stats on win/lose screens
4. **Collision Optimization** - Use radius-based detection (partially done)
5. **Ball Mechanics**
   - Change angle based on paddle hit position
6. **Difficulty**
   - Speed up ball after paddle hit
   - Move blocks down progressively faster
7. **Powerups**
   - More balls
   - Explosion
   - Laser
   - Bigger paddle
   - Catch ball

## Active Decisions & Considerations

- No start/win/lose screens yet - game starts immediately
- No lives system - ball death returns it to paddle
- No stats tracking yet
- Collision detection uses circle-to-rect (closest point) for blocks
- Ball speed is constant (no acceleration/difficulty ramp)
- Block grid is static (no downward movement)

## Important Patterns

- Models instantiate `options()` directly for configuration values
- Ball mutates `bricks` list directly in collision handling
- Paddle movement clamps to screen boundaries

## Learnings & Insights

- Explosion asset loading has graceful fallback (prints error, continues)
- Block matrix uses `h_range - 2` to leave margin on right side
- Ball initial direction is randomly chosen (left or right)
