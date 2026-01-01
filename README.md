# Space Mission – Land Safely! / ŰRMISSZIÓ – Segíts a Nave!

An educational space lander game for 7-year-olds, built with Python and pygame-ce, packaged for web using pygbag.

## Quick Start

### Prerequisites

- Python 3.9 or higher
- macOS (tested on MacBook Air)

### Setup (macOS)

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

   You should see `(venv)` in your terminal prompt.

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Expected output:
   ```
   Collecting pygame-ce>=2.5.0
   Collecting pygbag>=0.7.0
   ...
   Successfully installed pygame-ce-X.X.X pygbag-X.X.X ...
   ```

4. **Run the game locally:**
   ```bash
   python src/main.py
   ```

   Or use the convenience script:
   ```bash
   chmod +x run_local.sh
   ./run_local.sh
   ```

   Expected: A window opens with the game menu. Use arrow keys or W/S to navigate, SPACE/ENTER to select.

### Building for Web

1. **Make sure you're in the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Build the web version:**
   ```bash
   python -m pygbag --template index.html src/main.py
   ```

   Or use the convenience script:
   ```bash
   chmod +x build_web.sh
   ./build_web.sh
   ```

   Expected output:
   ```
   ...
   Build complete! Output is in build/web/
   ```

3. **Serve the web build locally:**
   ```bash
   cd build/web
   python -m http.server 8000
   ```

4. **Open in browser:**
   - Navigate to `http://localhost:8000`
   - The game should load and be playable in the browser
   - Works offline (no network calls at runtime)

## How to Play

- **Controls:** Press and hold SPACE or UP arrow to thrust upward. Release to stop thrusting.
- **Goal:** Land softly on the landing pad before running out of fuel.
- **Levels:** Three planets with different gravity and fuel:
  - **Moon:** Low gravity, easier to control
  - **Mars:** Medium gravity
  - **Earth:** High gravity, most challenging

## Educational Concepts

The game teaches:
1. **Gravity acts continuously** - The ship always accelerates downward
2. **Braking takes time** - You need to start thrusting early to slow down
3. **Energy is limited** - Fuel decreases while thrusting

## Project Structure

```
space/
├── src/                    # Source code
│   ├── main.py            # Entry point
│   ├── game.py            # Main game loop
│   ├── menu.py            # Menu system
│   ├── physics.py         # Physics engine
│   ├── renderer.py        # Rendering functions
│   ├── i18n.py            # Localization (HU/EN)
│   └── constants.py       # Game constants
├── build/                 # Web build output (gitignored)
├── docs/                  # Documentation
├── requirements.txt       # Python dependencies
├── build_web.sh          # Web build script
└── run_local.sh          # Local run script
```

## Troubleshooting

### Game won't start locally
- Make sure virtual environment is activated: `source venv/bin/activate`
- Check Python version: `python3 --version` (should be 3.9+)
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

### Web build fails
- Ensure pygbag is installed: `pip install pygbag>=0.7.0`
- Check that `src/main.py` exists and is valid Python
- Try building without template: `python -m pygbag src/main.py`

### Game runs but controls don't work
- Make sure the game window has focus (click on it)
- Try both SPACE and UP arrow keys
- Check terminal for error messages

### Font rendering issues (Hungarian characters)
- The game uses pygame's default font which should support UTF-8
- If special characters (ő, ű) don't display, try switching to English (L key in menu)

## Development

### Running Tests
```bash
# Syntax check
python -m py_compile src/*.py

# Run game
python src/main.py
```

### Modifying Game Parameters
Edit `src/constants.py` to adjust:
- Gravity values per planet
- Fuel amounts
- Safe landing speeds
- Screen size
- Colors

## License

Educational use.

