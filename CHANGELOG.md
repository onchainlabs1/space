# Changelog

All notable changes to Space Gravity will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.0] - 2024-01-04

### Added
- **Final Boss Battle** – Epic battle against an alien mothership after completing all planets
- **Champion Screen** – Special celebration with confetti for completing all levels + boss
- **Power-ups System**
  - ⛽ Fuel canisters – Restore fuel
  - 🛡️ Shield – Temporary invincibility
  - ⏱️ Slow-motion – Reduces gravity effect
- **Obstacles**
  - ☄️ Asteroids with varying sizes
  - 👾 Alien ships that shoot at player
- **Mobile Support**
  - Touch controls with D-pad
  - Responsive design for all screen sizes
  - Shoot button for boss level
- **Educational "Explore" Section** – Cards explaining gravity, Moon, Mars, and Earth
- **Bilingual Support** – English and Hungarian languages
- **High Score System** – Persistent scores saved locally
- **Boss Health Bar** – Visual indicator of boss damage
- **Player Lives System** – Hearts indicator during boss battle

### Changed
- Game renamed from "Space Mission" to "Space Gravity"
- Improved level select screen with Boss card on the right
- Enhanced visual effects and animations
- Adjusted difficulty curve for better progression
- Moon levels made easier for beginners
- Mars 3 rebalanced for fairness
- Earth levels (1-3) landing speed limits increased (130→160, 110→145, 100→135) to make landing easier for children

### Fixed
- Boss level scoring now saves correctly
- Mobile menu navigation improved
- Tutorial messages repositioned to not obstruct gameplay
- Champion screen contrast improved for readability

## [0.9.0] - 2024-01-03

### Added
- 9 levels across 3 planets (Moon, Mars, Earth)
- Progressive difficulty system
- Wind effects on Mars and Earth
- Basic asteroid obstacles
- Sound effects system with mute option

### Changed
- Migrated from Python/Pygame to JavaScript/HTML5
- Single-file architecture for easy deployment

## [0.5.0] - 2024-01-02

### Added
- Initial Python version with Pygame
- Basic lander physics
- Simple terrain generation
- Fuel system

---

## Version Numbering

- **Major (X.0.0)** – Significant new features or breaking changes
- **Minor (0.X.0)** – New features, backwards compatible
- **Patch (0.0.X)** – Bug fixes and minor improvements

