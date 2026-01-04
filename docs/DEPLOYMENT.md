# Space Gravity – Deployment Guide

How to deploy Space Gravity to various platforms.

## Table of Contents

1. [Quick Start](#quick-start)
2. [itch.io Deployment](#itchio-deployment)
3. [GitHub Pages](#github-pages)
4. [Local Testing](#local-testing)
5. [Troubleshooting](#troubleshooting)

---

## Quick Start

The game is a **single HTML file** – deployment is simple!

```
game/
  └── index.html  ← This is the ONLY file you need!
```

**Size:** ~60KB  
**Resolution:** 960×540 (auto-scales)  
**Compatibility:** All modern browsers, mobile & desktop

---

## itch.io Deployment

### Step 1: Create itch.io Account

1. Go to https://itch.io
2. Create a free account
3. Click "Dashboard" → "Create new project"

### Step 2: Project Settings

| Field | Value |
|-------|-------|
| Title | Space Gravity – Land Safely! |
| Project URL | `space-gravity` |
| Classification | Games |
| Kind of project | HTML |
| Category | Educational |

**Tags:** `educational`, `space`, `lander`, `physics`, `kids`, `browser`, `html5`

### Step 3: Description

```
🚀 Educational Space Lander Game for Kids!

Land safely on different planets! Learn about gravity, physics, and fuel management.

✨ Features:
• 9 progressive levels (Moon, Mars, Earth)
• Epic Final Boss battle
• Power-ups: Fuel, Shield, Slow-motion
• Kid-friendly controls
• Works on mobile and desktop!

🎮 Controls:
• ↑/SPACE = Thrust up
• ←/→ = Move sideways
• X = Shoot (Boss level)
• Touch controls on mobile

🌍 Languages: English / Magyar

Perfect for ages 5-10. Learn physics through play!
```

### Step 4: Upload

1. In **"Uploads"** section:
   - Click "Upload files"
   - Select `game/index.html`
   
2. Configure the upload:
   - ✅ Check "This file will be played in the browser"
   - Select "HTML" as the type

### Step 5: Embed Settings

| Setting | Value |
|---------|-------|
| Embed in page | Yes |
| Viewport dimensions | 960 × 540 |
| Fullscreen button | Yes |
| Mobile friendly | Yes |

### Step 6: Publish

1. Add cover image (630×500 recommended)
2. Add screenshots (gameplay, menu, victory)
3. Set to "Public"
4. Click "Save"

**Your game is now live!** 🎉

---

## GitHub Pages

Free hosting alternative using GitHub.

### Step 1: Create Repository

1. Go to https://github.com/new
2. Name it `space-gravity`
3. Make it Public
4. Initialize with README

### Step 2: Upload Game

1. Upload `game/index.html` to the root directory
2. Or use git:

```bash
git clone https://github.com/YOUR_USERNAME/space-gravity.git
cd space-gravity
cp /path/to/game/index.html .
git add index.html
git commit -m "Add game"
git push
```

### Step 3: Enable Pages

1. Go to repository Settings
2. Click "Pages" in sidebar
3. Source: "Deploy from a branch"
4. Branch: `main`, folder: `/ (root)`
5. Click Save

### Step 4: Access Your Game

After a few minutes, your game will be at:
```
https://YOUR_USERNAME.github.io/space-gravity/
```

---

## Local Testing

### Method 1: Python Server (Recommended)

```bash
cd game
python3 -m http.server 8080
```

Open http://localhost:8080

### Method 2: Node.js Server

```bash
npx serve game
```

### Method 3: Direct File (Limited)

Double-click `index.html` to open in browser.

⚠️ Note: Some features may not work due to browser security restrictions with `file://` protocol.

### Mobile Testing

1. Start local server (Method 1 or 2)
2. Find your computer's IP: `ifconfig` or `ipconfig`
3. On mobile, go to: `http://YOUR_IP:8080`
4. Both devices must be on same WiFi network

---

## Troubleshooting

### Game doesn't load

| Problem | Solution |
|---------|----------|
| Black screen | Check browser console for errors (F12) |
| 404 error | Ensure file is named `index.html` |
| No game appears | Enable JavaScript in browser |

### Controls don't work

| Problem | Solution |
|---------|----------|
| No keyboard response | Click on game canvas first |
| Touch not working | Game auto-detects mobile; refresh page |
| Buttons missing | Check if mobile detection is working |

### Display issues

| Problem | Solution |
|---------|----------|
| Too small | Game auto-scales; check embed settings |
| Cut off | Set viewport to 960×540 |
| Blurry | Normal at some zoom levels |

### itch.io specific

| Problem | Solution |
|---------|----------|
| Not playable | Check "played in browser" checkbox |
| Wrong dimensions | Set embed size to 960×540 |
| Audio issues | User must interact first (browser policy) |

---

## Platform Compatibility

### Tested Browsers

| Browser | Desktop | Mobile |
|---------|---------|--------|
| Chrome | ✅ | ✅ |
| Firefox | ✅ | ✅ |
| Safari | ✅ | ✅ (iOS) |
| Edge | ✅ | ✅ |

### Requirements

- JavaScript enabled
- HTML5 Canvas support
- Web Audio API (for sound)

### Known Limitations

- Internet Explorer: Not supported
- Very old mobile browsers: May have issues
- Offline: Works after initial load

---

## Updating the Game

### On itch.io

1. Go to Dashboard → Your project
2. Click "Edit project"
3. In Uploads, click delete (X) on old file
4. Upload new `index.html`
5. Save

### On GitHub Pages

```bash
# Replace the file
cp /path/to/new/index.html .
git add index.html
git commit -m "Update game to v1.1"
git push
```

Changes appear within minutes.

---

## Tips for Success

### Screenshots

Take screenshots of:
1. Main menu (shows title)
2. Gameplay (shows action)
3. Victory screen (shows achievement)
4. Boss battle (shows excitement)

### Promotion

- Share on social media
- Post in game development communities
- Submit to HTML5 game directories
- Ask for ratings and feedback

### Analytics

itch.io provides:
- View counts
- Play counts
- Download stats
- Geographic data

---

## Need Help?

- Check [Technical Guide](TECHNICAL_GUIDE.md) for code questions
- Open a GitHub Issue for bugs
- Join game dev communities for advice

Happy deploying! 🚀

