# Space Gravity – Game Manual

Complete guide to playing Space Gravity, the educational space lander game.

## Table of Contents

1. [Game Objective](#game-objective)
2. [Controls](#controls)
3. [Planets & Levels](#planets--levels)
4. [Power-ups](#power-ups)
5. [Obstacles](#obstacles)
6. [Final Boss](#final-boss)
7. [Scoring System](#scoring-system)
8. [Tips & Strategies](#tips--strategies)

---

## Game Objective

Your mission is to **land your spacecraft safely** on the green landing pad. You must:

1. Control your descent using thrust
2. Manage your limited fuel supply
3. Avoid obstacles (asteroids and aliens)
4. Land slowly enough to survive
5. Land ON the green pad (not beside it!)

### Success Conditions
- ✅ Land on the green pad
- ✅ Vertical speed below safe threshold
- ✅ Fuel remaining > 0

### Failure Conditions
- ❌ Crash (too fast)
- ❌ Miss the landing pad
- ❌ Run out of fuel
- ❌ Hit by obstacle (without shield)

---

## Controls

### Keyboard Controls

| Key | Action |
|-----|--------|
| `SPACE` or `↑` | Thrust upward (burn fuel) |
| `←` | Move left |
| `→` | Move right |
| `X` | Shoot (Boss level only) |
| `M` | Toggle sound on/off |
| `L` | Change language (EN/HU) |
| `ESC` | Return to menu |

### Mobile/Touch Controls

| Button | Action |
|--------|--------|
| 🔥 | Thrust upward |
| ◀ | Move left |
| ▶ | Move right |
| 💥 | Shoot (Boss level only) |

### Control Tips
- **Tap thrust** for small adjustments
- **Hold thrust** for stronger push
- Left/right movement uses fuel too (but less)
- Start braking EARLY – you can't stop instantly!

---

## Planets & Levels

### 🌙 Moon (Levels 1-3)

**Gravity:** 1.6 m/s² (lowest)
**Difficulty:** Easy

| Level | Features |
|-------|----------|
| Moon 1 | Basic landing, few obstacles |
| Moon 2 | More obstacles, slightly harder |
| Moon 3 | Light wind, more asteroids & aliens |

**Tips for Moon:**
- Gravity is very low – you have time to think
- Use gentle taps on thrust
- Great for learning the controls

### 🔴 Mars (Levels 4-6)

**Gravity:** 3.7 m/s² (medium)
**Difficulty:** Medium

| Level | Features |
|-------|----------|
| Mars 1 | Introduction to Mars gravity |
| Mars 2 | More wind, more obstacles |
| Mars 3 | Strong wind, many aliens |

**Tips for Mars:**
- Gravity is 2x Moon – react faster
- Watch out for wind pushing you sideways
- Fuel management becomes important

### 🌍 Earth (Levels 7-9)

**Gravity:** 9.8 m/s² (highest)
**Difficulty:** Hard

| Level | Features |
|-------|----------|
| Earth 1 | Earth gravity introduction |
| Earth 2 | Heavy obstacles, strong wind |
| Earth 3 | Maximum challenge before boss |

**Tips for Earth:**
- Gravity is STRONG – start braking early
- Keep thrust active more often
- Save shield power-ups for emergencies

---

## Power-ups

Collect floating power-ups to help your mission!

### ⛽ Fuel Canister

- **Effect:** Restores +30 fuel units
- **Appearance:** Yellow canister icon
- **Strategy:** Grab these when fuel drops below 50%

### 🛡️ Shield

- **Effect:** 5 seconds of invincibility
- **Appearance:** Blue shield icon
- **Strategy:** 
  - Save for obstacle-heavy sections
  - Great for passing through asteroid fields
  - Doesn't protect from crash landing!

### ⏱️ Slow-Motion (Clock)

- **Effect:** Reduces gravity effect by 70% for 5 seconds
- **Appearance:** Clock icon
- **Strategy:**
  - Use when descending too fast
  - Perfect for precise landing adjustments
  - Very helpful on Earth levels

---

## Obstacles

### ☄️ Asteroids

- **Behavior:** Float slowly, bounce off edges
- **Damage:** Instant failure (without shield)
- **Speed:** Slow on Moon, faster on Earth
- **Tip:** Plan your path around them

### 👾 Alien Ships

- **Behavior:** Move side to side, shoot at player
- **Damage:** Instant failure (without shield)
- **Shooting:** Fire slow projectiles downward
- **Tip:** Stay above them or move quickly past

### 🌬️ Wind

- **Effect:** Pushes your ship sideways
- **Planets:** Mars (light) and Earth (strong)
- **Tip:** Compensate by thrusting against the wind direction

---

## Final Boss

After completing all 9 levels, you face the **Alien Mothership**!

### Boss Mechanics

- **Health:** 100 HP (shown in health bar)
- **Weak Points:** Green glowing spots
- **Attacks:** Fires projectiles at player
- **Movement:** Moves side to side

### How to Defeat

1. **Shoot** with `X` key (or 💥 button on mobile)
2. **Aim** for the green weak spots
3. **Dodge** the boss's projectiles
4. **Manage fuel** – you still need to thrust!
5. **Collect power-ups** that spawn during battle

### Boss Tips

- Keep moving to avoid projectiles
- Shoot continuously – fire rate is fast
- Shield power-up is your best friend
- You have 2 lives (hearts) for this battle
- Asteroids and aliens also appear – stay alert!

### Victory!

Defeat the boss to become a **Space Champion**! 🏆

If you completed ALL levels in sequence + boss, you'll see the special **Champion Screen** with confetti!

---

## Scoring System

### Level Score Calculation

The score for each level is calculated using three components:

```
Score = Fuel Bonus + Speed Bonus + Accuracy Bonus
```

| Component | Formula | Description |
|-----------|---------|-------------|
| **Fuel Bonus** | Remaining fuel × 10 | Save fuel for higher score! |
| **Speed Bonus** | (Safe speed - Your speed) × 20 | Landing slower = more points |
| **Accuracy Bonus** | Landing precision × 300 | Landing in center of pad = max bonus |

**Example:**
- Fuel: 50 remaining → +500 points
- Speed: 30 below safe speed → +600 points  
- Accuracy: Perfect center → +300 points
- **Total: 1400 points**

### High Scores

- Best scores are saved per planet
- Displayed on the level select screen
- Stored locally in your browser

### Boss Score

The boss level uses a different scoring system:

```
Score = Fuel Bonus + Boss Defeat Bonus + Lives Bonus
```

| Component | Formula |
|-----------|---------|
| **Fuel Bonus** | Remaining fuel × 10 |
| **Boss Defeat Bonus** | +500 points (fixed) |
| **Lives Bonus** | Remaining lives × 200 |

**Tip:** Survive with both lives and maximum fuel for the highest score! (Max lives bonus: 400 points)

---

## Tips & Strategies

### General Tips

1. **Start braking early** – Inertia means you can't stop instantly
2. **Tap, don't hold** – Small thrust taps give better control
3. **Watch your fuel** – Don't thrust when you don't need to
4. **Learn the safe speed** – Each planet has different thresholds
5. **Use the HUD** – Altitude, speed, and fuel are displayed

### Advanced Strategies

1. **Horizontal approach** – Move sideways first, then descend
2. **Fuel hoarding** – Skip optional power-ups if fuel is high
3. **Shield timing** – Activate just before entering danger
4. **Boss pattern** – Learn the boss movement pattern

### Common Mistakes

| Mistake | Solution |
|---------|----------|
| Crashing too fast | Start braking at 50% altitude |
| Missing the pad | Watch horizontal position constantly |
| Running out of fuel | Use shorter thrust bursts |
| Hitting obstacles | Plan path before descending |

---

## Menu Navigation

### Main Menu

- **Play** – Start from Level 1
- **Levels** – Choose any level
- **Tutorial** – Learn the controls
- **Explore** – Educational content about planets
- **Info** – Game credits and controls

### Level Select

- Click/tap any level to play
- Boss card on the right (after Earth 3)
- Best scores shown on each level

---

## Accessibility

- **Simple controls** – Only 4 actions needed
- **Large touch targets** – Easy to tap on mobile
- **Color-coded feedback** – Green=good, Red=bad
- **Audio cues** – Sound effects indicate events
- **Mute option** – Play silently if needed

---

Good luck, astronaut! 🚀🌟

