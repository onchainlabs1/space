# 🚀 Space Gravity – Land Safely!

An educational space lander game that teaches physics concepts to kids aged 5-10. Land your spacecraft on different planets while learning about gravity, inertia, and energy conservation.

## 🎮 Play Now

**[Play Online on itch.io](https://spacearon.itch.io/space-mission)** – No download required!

## ✨ Features

- **9 Progressive Levels** across 3 planets (Moon, Mars, Earth)
- **Final Boss Battle** – Defeat the alien mothership!
- **Power-ups** – Collect fuel, shields, and slow-motion
- **Obstacles** – Dodge asteroids and alien ships
- **Educational** – Learn real physics concepts
- **Kid-friendly** – Simple controls, colorful graphics
- **Bilingual** – English and Hungarian languages
- **Works everywhere** – Desktop, mobile, and tablet

## 🎯 Gameplay

### Objective
Land your spacecraft safely on the green landing pad before running out of fuel!

### Controls

| Action | Keyboard | Mobile |
|--------|----------|--------|
| Thrust Up | `SPACE` or `↑` | 🔥 Button |
| Move Left/Right | `←` `→` | ◀ ▶ Buttons |
| Shoot (Boss only) | `X` | 💥 Button |
| Mute Sound | `M` | – |
| Change Language | `L` | – |

### Planets & Difficulty

| Planet | Gravity | Difficulty | What You Learn |
|--------|---------|------------|----------------|
| 🌙 Moon | 1.6 m/s² | Easy | Basic controls, gentle landing |
| 🔴 Mars | 3.7 m/s² | Medium | Fuel management, wind effects |
| 🌍 Earth | 9.8 m/s² | Hard | Precise control, obstacle avoidance |

### Power-ups

| Icon | Power-up | Effect |
|------|----------|--------|
| ⛽ | Fuel | Restores 30 fuel units |
| 🛡️ | Shield | Temporary invincibility |
| ⏱️ | Slow-Mo | Reduces gravity for easier control |

### Obstacles

- **☄️ Asteroids** – Floating rocks that damage your ship
- **👾 Alien Ships** – Moving enemies that fire at you
- **🌬️ Wind** – Pushes your ship sideways (Mars & Earth)

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Game Manual](docs/GAME_MANUAL.md) | Complete gameplay guide |
| [Educational Guide](docs/EDUCATIONAL_GUIDE.md) | Physics concepts & classroom use |
| [Technical Guide](docs/TECHNICAL_GUIDE.md) | Code architecture & customization |
| [Deployment Guide](docs/DEPLOYMENT.md) | How to deploy on itch.io |

## 🚀 Quick Start

### Play Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/onchainlabs1/space.git
   cd space
   ```

2. Start a local server:
   ```bash
   cd game
   python3 -m http.server 8080
   ```

3. Open http://localhost:8080 in your browser

### Deploy Your Own Version

See the [Deployment Guide](docs/DEPLOYMENT.md) for instructions on deploying to itch.io or other platforms.

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) to get started.

### Ideas for Contributions

- 🌍 **New planets** – Add Venus, Jupiter, or fictional planets
- 🎨 **Visual themes** – Create new ship designs or backgrounds
- 🌐 **Translations** – Add support for more languages
- 🎵 **Sound effects** – Improve audio experience
- 📱 **Mobile UX** – Enhance touch controls
- 🐛 **Bug fixes** – Help us squash bugs

## 📖 What Players Learn

This game teaches important physics concepts through gameplay:

1. **Gravity is constant** – The ship always accelerates downward
2. **Inertia matters** – You can't stop instantly; start braking early
3. **Energy is limited** – Fuel runs out; use it wisely
4. **Different worlds, different rules** – Gravity varies by planet

Perfect for:
- Elementary school science classes
- Homeschool physics lessons
- STEM education programs
- Learning through play

## 🏗️ Project Structure

```
space/
├── game/
│   └── index.html          # Complete game (single file)
├── web_build/
│   └── index.html          # Alternative build location
├── docs/
│   ├── GAME_MANUAL.md      # Gameplay guide
│   ├── EDUCATIONAL_GUIDE.md # Physics & teaching
│   ├── TECHNICAL_GUIDE.md  # Code architecture
│   └── DEPLOYMENT.md       # Deployment instructions
├── legacy/
│   └── src/                # Original Python version
├── README.md
├── LICENSE                 # MIT License
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── CHANGELOG.md
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits

- **Game Design & Development** – Created as an educational project
- **Inspired by** – Classic lunar lander games
- **Built with** – HTML5 Canvas, JavaScript

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐ on GitHub!

---

<p align="center">
  Made with ❤️ for young space explorers everywhere
</p>
