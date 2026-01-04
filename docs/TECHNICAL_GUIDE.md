# Space Gravity – Technical Guide

This guide explains the code architecture and how to modify or extend the game.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [File Structure](#file-structure)
3. [Key Components](#key-components)
4. [Game Loop](#game-loop)
5. [Physics System](#physics-system)
6. [Adding New Content](#adding-new-content)
7. [Customization](#customization)

---

## Architecture Overview

Space Gravity is a **single-file HTML5 game** built with:

- **HTML5 Canvas** – Rendering
- **Vanilla JavaScript** – Game logic
- **CSS** – UI styling
- **Web Audio API** – Sound effects

### Why Single File?

The entire game is in one `index.html` file because:
1. Easy deployment to itch.io (upload one file)
2. Works offline without server
3. Simple to share and modify
4. No build process required

### Code Organization

```
index.html
├── <style>         CSS (lines ~7-300)
├── <body>          HTML structure (lines ~300-350)
└── <script>        JavaScript (lines ~350-3500)
    ├── Constants & Config
    ├── Game State Variables
    ├── Audio System
    ├── Particle System
    ├── Level Configuration
    ├── Input Handling
    ├── Physics & Collision
    ├── Rendering Functions
    └── Game Loop
```

---

## File Structure

```
space-gravity/
├── game/
│   └── index.html      # Complete game (THE MAIN FILE)
├── docs/
│   ├── GAME_MANUAL.md
│   ├── EDUCATIONAL_GUIDE.md
│   ├── TECHNICAL_GUIDE.md  (this file)
│   └── DEPLOYMENT.md
└── legacy/
    └── src/            # Original Python version (reference)
```

---

## Key Components

### 1. Game State

```javascript
let state = 'menu';  // Current game state

// Possible states:
// 'menu'        - Main menu
// 'levelSelect' - Level selection screen
// 'playing'     - Active gameplay
// 'success'     - Level completed
// 'failure'     - Level failed
// 'tutorialMode'- Tutorial screens
// 'explore'     - Educational cards
// 'info'        - Credits/info screen
```

### 2. Lander Object

```javascript
lander = {
    x: 400,           // Horizontal position
    y: 60,            // Vertical position (0 = top)
    vx: 0,            // Horizontal velocity
    vy: 0,            // Vertical velocity
    fuel: 200,        // Current fuel
    thrust: false,    // Is thrusting?
    shield: false,    // Shield active?
    shieldTimer: 0,   // Shield duration remaining
    slowmo: false,    // Slow-motion active?
    slowmoTimer: 0,   // Slow-mo duration remaining
    spawnProtection: 60  // Initial invincibility frames
};
```

### 3. Level Configuration

```javascript
const LEVELS = [
    // Moon levels (indices 0-2)
    { 
        planet: 'moon', 
        gravity: 0.025,    // Gravity strength
        fuel: 250,         // Starting fuel
        safeSpeed: 250,    // Max safe landing speed
        obstacles: 2,      // Number of obstacles
        wind: 0,           // Wind strength
        name: 'Moon 1' 
    },
    // ... more levels
    
    // Boss level (index 9)
    { 
        planet: 'earth', 
        gravity: 0.10, 
        fuel: 300, 
        safeSpeed: 100, 
        obstacles: 0, 
        wind: 0, 
        name: 'Final Boss', 
        boss: true         // Special boss flag
    }
];
```

### 4. Translations

```javascript
const TEXTS = {
    en: {
        title: 'SPACE GRAVITY',
        subtitle: 'Land Safely!',
        play: 'Play',
        // ... all English strings
    },
    hu: {
        title: 'ŰRMISSZIÓ',
        subtitle: 'Szállj le biztonságosan!',
        play: 'Játék',
        // ... all Hungarian strings
    }
};

// Usage:
function t(key) {
    return TEXTS[currentLang][key] || key;
}
```

---

## Game Loop

```javascript
function gameLoop(timestamp) {
    const dt = timestamp - lastTime;
    lastTime = timestamp;
    
    // 1. Clear canvas
    ctx.clearRect(0, 0, W, H);
    
    // 2. Update based on state
    if (state === 'playing') {
        updatePhysics();
        updateObstacles();
        checkCollisions();
        updatePowerups();
        updateBoss();  // if boss level
    }
    
    // 3. Render based on state
    switch(state) {
        case 'menu': drawMenu(); break;
        case 'playing': drawGame(); break;
        case 'success': drawSuccess(); break;
        // ... etc
    }
    
    // 4. Reset input states
    justPressed = {};
    
    // 5. Request next frame
    requestAnimationFrame(gameLoop);
}
```

---

## Physics System

### Gravity Application

```javascript
// Every frame during gameplay:
lander.vy += level.gravity * gravityMod;

// gravityMod is 0.3 if slow-motion active, else 1.0
```

### Thrust

```javascript
if (lander.thrust && lander.fuel > 0) {
    const thrustPower = THRUST_POWER[level.planet];
    lander.vy -= thrustPower;  // Push upward
    lander.fuel -= FUEL_RATE;
}
```

### Movement

```javascript
// Horizontal movement
if (keys['ArrowLeft']) {
    lander.vx -= HORIZONTAL_THRUST;
}
if (keys['ArrowRight']) {
    lander.vx += HORIZONTAL_THRUST;
}

// Wind effect
lander.vx += level.wind;

// Apply velocity to position
lander.x += lander.vx;
lander.y += lander.vy;

// Apply friction/drag
lander.vx *= 0.99;
```

### Landing Detection

```javascript
function checkLanding() {
    const groundY = H - GROUND_HEIGHT;
    
    if (lander.y + LANDER_H >= groundY) {
        // Check if on pad
        const onPad = lander.x > padX && 
                      lander.x < padX + PAD_W;
        
        // Check speed
        const speed = Math.abs(lander.vy) * 100;
        const safe = speed <= level.safeSpeed;
        
        if (onPad && safe) {
            state = 'success';
            calculateScore();
        } else {
            state = 'failure';
            failReason = onPad ? 'Too fast!' : 'Missed!';
        }
    }
}
```

---

## Adding New Content

### Adding a New Planet

1. **Define planet colors:**
```javascript
const PLANET_COLORS = {
    moon: { surface: '#b4b4be', sky: '#000000', accent: '#8a8a94' },
    mars: { surface: '#c86432', sky: '#1a0a05', accent: '#8b4513' },
    earth: { surface: '#3c8cc8', sky: '#000020', accent: '#2d6a9f' },
    // Add new planet:
    venus: { surface: '#e6c35c', sky: '#1a1000', accent: '#b8963c' }
};
```

2. **Add thrust power:**
```javascript
const THRUST_POWER = { 
    moon: 0.30, 
    mars: 0.28, 
    earth: 0.40,
    venus: 0.35  // New planet
};
```

3. **Add levels:**
```javascript
// Add to LEVELS array:
{ planet: 'venus', gravity: 0.14, fuel: 180, safeSpeed: 80, 
  obstacles: 4, wind: 0.003, name: 'Venus 1' },
```

4. **Add translations:**
```javascript
// In TEXTS.en:
venus: 'Venus',

// In TEXTS.hu:
venus: 'Vénusz',
```

5. **Add icon:**
```javascript
const icons = { 
    moon: '🌙', 
    mars: '🔴', 
    earth: '🌍',
    venus: '🟡'  // New icon
};
```

### Adding a New Power-up

1. **Add to spawn function:**
```javascript
function spawnPowerup() {
    const types = ['fuel', 'shield', 'slowmo', 'newPowerup'];
    const type = types[Math.floor(Math.random() * types.length)];
    
    powerups.push({
        x: Math.random() * (W - 40) + 20,
        y: Math.random() * 200 + 100,
        type: type,
        // ...
    });
}
```

2. **Handle collection:**
```javascript
// In collision detection:
if (p.type === 'newPowerup') {
    // Apply effect
    lander.superSpeed = true;
    lander.superSpeedTimer = 180;  // 3 seconds
    showMascot('Super speed!');
}
```

3. **Add visual:**
```javascript
// In drawPowerups():
if (p.type === 'newPowerup') {
    ctx.fillText('⚡', p.x, p.y);
}
```

### Adding a New Obstacle Type

```javascript
function generateObstacles(count) {
    for (let i = 0; i < count; i++) {
        const isNewType = Math.random() < 0.2;  // 20% chance
        
        obstacles.push({
            x: Math.random() * W,
            y: Math.random() * (H - 200) + 50,
            type: isNewType ? 'newObstacle' : 'asteroid',
            vx: (Math.random() - 0.5) * 2,
            vy: (Math.random() - 0.5) * 1,
            // Custom properties for new type:
            customBehavior: isNewType
        });
    }
}
```

---

## Customization

### Changing Difficulty

```javascript
// Make Moon easier:
LEVELS[0].gravity = 0.015;  // Lower gravity
LEVELS[0].safeSpeed = 300;  // Higher safe speed
LEVELS[0].fuel = 300;       // More fuel

// Make Earth harder:
LEVELS[8].gravity = 0.30;   // Higher gravity
LEVELS[8].obstacles = 10;   // More obstacles
```

### Changing Visual Style

```javascript
// Background gradient
function drawBackground(planet) {
    const colors = PLANET_COLORS[planet];
    const gradient = ctx.createLinearGradient(0, 0, 0, H);
    gradient.addColorStop(0, colors.sky);
    gradient.addColorStop(1, colors.surface);
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, W, H);
}

// Change star density
const STAR_COUNT = 100;  // Default, increase for more stars
```

### Adding Sound Effects

```javascript
class AudioManager {
    playCustomSound() {
        if (this.muted) return;
        // Use Web Audio API
        this.playTone(frequency, duration, waveform, volume);
    }
}

// Usage:
audio.playCustomSound();
```

---

## Debugging Tips

### Enable Debug Mode

Add to the game loop:
```javascript
// Draw debug info
if (DEBUG) {
    ctx.fillStyle = 'lime';
    ctx.font = '12px monospace';
    ctx.fillText(`Pos: ${lander.x.toFixed(0)}, ${lander.y.toFixed(0)}`, 10, 20);
    ctx.fillText(`Vel: ${lander.vx.toFixed(2)}, ${lander.vy.toFixed(2)}`, 10, 35);
    ctx.fillText(`State: ${state}`, 10, 50);
}
```

### Test Specific Levels

Press keys to skip:
```javascript
// Already implemented:
// Press 'F' during gameplay to test champion screen
if (justPressed['KeyF']) {
    // Simulates completing all levels
}
```

### Browser Console

Open DevTools (F12) and type:
```javascript
// Skip to level
currentLevel = 5;
startLevel(currentLevel);

// Give infinite fuel
lander.fuel = 99999;

// Activate shield
lander.shield = true;
lander.shieldTimer = 99999;
```

---

## Performance Considerations

### Particle System

```javascript
// Limit particle count for performance
const MAX_PARTICLES = 500;

// Clear old particles
particles.pool = particles.pool.filter(p => p.life > 0);
if (particles.pool.length > MAX_PARTICLES) {
    particles.pool = particles.pool.slice(-MAX_PARTICLES);
}
```

### Render Optimization

- Use `requestAnimationFrame` (already done)
- Minimize canvas state changes
- Reuse gradients when possible
- Don't draw off-screen objects

---

## Mobile Considerations

### Touch Events

```javascript
// Touch handlers are set up in init()
btnThrust.addEventListener('touchstart', e => {
    e.preventDefault();  // Prevent scrolling
    keys['Space'] = true;
});
```

### Responsive Canvas

```javascript
function resizeCanvas() {
    const container = document.getElementById('gameContainer');
    const scale = Math.min(
        container.clientWidth / W,
        container.clientHeight / H
    );
    canvas.style.transform = `scale(${scale})`;
}

window.addEventListener('resize', resizeCanvas);
```

---

## Questions?

If you have technical questions:
1. Check existing code comments
2. Open a GitHub Issue
3. Review the legacy Python version for reference

Happy coding! 🚀

