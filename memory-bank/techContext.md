# Technical Context: Ball Breaker

## Technologies

- **Python 3.13.1** - Runtime
- **PyGame 2.6.1** - Graphics, input handling, display
- **Git** - Version control

## Development Setup

- Run: `py game.py` from project root
- No external dependencies beyond PyGame
- No testing framework currently configured

## Project Structure

```
ball-breaker/
├── game.py              # Main entry point & game loop
├── readme.md            # Project documentation
├── .gitignore           # Git ignore rules
├── .clinerules/
│   └── memory-bank.md   # Memory Bank instructions
├── assets/
│   ├── explosion-0.png  # Explosion sprite frame 0
│   ├── explosion-1.png  # Explosion sprite frame 1
│   ├── explosion-2.png  # Explosion sprite frame 2
│   ├── explosion-3.png  # Explosion sprite frame 3
│   └── explosion-4.png  # Explosion sprite frame 4
├── docs/
│   ├── plan.md          # Feature tracking (todo/done)
│   └── screenshot.png   # Game screenshot
└── models/
    ├── ball.py          # Ball class (movement, collision)
    ├── block.py         # Block class (random color matrix)
    ├── options.py       # Configuration/settings class
    └── paddle.py        # Paddle class (movement, boundaries)
```

## Technical Constraints

- Screen: 800x600 pixels
- Framerate: 60 FPS fixed
- Block grid: calculated dynamically based on screen width
- No sprite sheets or complex asset management (except explosion PNGs)

## Dependencies

- `pygame` only runtime dependency
- Installed via pip
