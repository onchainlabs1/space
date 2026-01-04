# Contributing to Space Gravity

Thank you for your interest in contributing to Space Gravity! This document provides guidelines and information for contributors.

## 🌟 Ways to Contribute

### 1. Report Bugs
Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Browser/device information
- Screenshots if applicable

### 2. Suggest Features
Have an idea? Open an issue with:
- Clear description of the feature
- Why it would be useful
- How it fits the educational goals
- Any implementation ideas

### 3. Submit Code
Ready to code? Follow these steps:

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create a branch** for your feature: `git checkout -b feature/amazing-feature`
4. **Make your changes**
5. **Test** thoroughly on desktop and mobile
6. **Commit** with clear messages: `git commit -m "Add amazing feature"`
7. **Push** to your fork: `git push origin feature/amazing-feature`
8. **Open a Pull Request**

### 4. Improve Documentation
Help us make docs better:
- Fix typos or unclear explanations
- Add examples
- Translate to other languages
- Create tutorials

### 5. Add Translations
The game supports multiple languages! To add a new language:

1. Find the `TEXTS` object in `game/index.html`
2. Copy an existing language block (e.g., `en`)
3. Translate all strings
4. Submit a PR with your translation

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code works on desktop browsers (Chrome, Firefox, Safari)
- [ ] Code works on mobile (touch controls)
- [ ] No console errors
- [ ] Game still loads as single HTML file
- [ ] Educational value is maintained or improved

### PR Title Format

```
type: brief description

Examples:
feat: add Neptune as new planet
fix: correct fuel consumption on Mars
docs: improve installation instructions
i18n: add Spanish translation
```

### Types
- `feat` – New feature
- `fix` – Bug fix
- `docs` – Documentation only
- `style` – Formatting, no code change
- `refactor` – Code restructuring
- `perf` – Performance improvement
- `i18n` – Internationalization/translation

## 🎨 Code Style

### JavaScript
- Use `const` and `let`, avoid `var`
- Use meaningful variable names
- Comment complex logic
- Keep functions small and focused

### HTML/CSS
- Use semantic HTML where possible
- Keep CSS organized by section
- Use CSS variables for colors/themes

### Example

```javascript
// Good
const MAX_FUEL = 200;
const calculateScore = (fuel, speed) => {
    const fuelBonus = fuel * 10;
    const speedBonus = Math.max(0, 100 - speed);
    return fuelBonus + speedBonus;
};

// Avoid
var x = 200;
function calc(a,b){return a*10+(100-b>0?100-b:0);}
```

## 🎮 Game Design Principles

When contributing features, keep these principles in mind:

1. **Educational First** – Features should teach or reinforce physics concepts
2. **Kid-Friendly** – Appropriate for ages 7-10, no violence or scary content
3. **Accessible** – Works on various devices and skill levels
4. **Simple Controls** – Don't overcomplicate the control scheme
5. **Fair Challenge** – Difficulty should be challenging but not frustrating

## 🧪 Testing

Before submitting, test your changes:

1. **Desktop Testing**
   ```bash
   cd game
   python3 -m http.server 8080
   # Open http://localhost:8080
   ```

2. **Mobile Testing**
   - Use browser dev tools mobile emulation
   - Test on actual mobile device if possible
   - Verify touch controls work

3. **Cross-Browser**
   - Chrome
   - Firefox
   - Safari
   - Edge

## 📁 Project Structure

```
space-gravity/
├── game/
│   └── index.html      # THE GAME - All code is here!
├── docs/               # Documentation
├── legacy/             # Old Python version (reference only)
└── ...
```

**Important:** The entire game is in a single `index.html` file. This is intentional for easy deployment on itch.io.

## 🆘 Getting Help

- **Questions?** Open a GitHub Discussion
- **Found a bug?** Open an Issue
- **Want to chat?** Leave a comment on an existing issue

## 📜 Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## 🙏 Recognition

All contributors will be:
- Listed in CHANGELOG.md for their contributions
- Thanked in release notes
- Part of making education more fun!

---

Thank you for helping make Space Gravity better! 🚀

