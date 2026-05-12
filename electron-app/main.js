/**
 * main.js — TurboTax Business Tax Assistant
 * Electron main process: creates a macOS menu bar (tray) app.
 *
 * Dev:   cd electron-app && npm install && npm start
 * Build: npm run build  →  dist/TurboTax Business Tax-0.1.0.dmg
 *
 * Dev shortcuts (while widget is open):
 *   Cmd+R           — reload prototype (pick up HTML/CSS/JS edits instantly)
 *   Cmd+Option+I    — open DevTools
 */

const { app, BrowserWindow, Tray, nativeImage, screen, globalShortcut } = require('electron');
const path = require('path');

// Resolve prototype path for both dev and packaged builds
const PROTOTYPE_PATH = app.isPackaged
  ? path.join(process.resourcesPath, 'prototype', 'index.html')
  : path.join(__dirname, '..', 'prototype', 'index.html');

let tray   = null;
let win    = null;

const WIDGET_W = 360;
const WIDGET_H = 580;

app.whenReady().then(createApp);

function createApp() {
  // ── Hide from Dock (menu bar only app) ──────────────────────────────────
  if (process.platform === 'darwin') app.dock.hide();

  // ── Tray icon ────────────────────────────────────────────────────────────
  // Place a 16×16 (or 32×32 @2x) PNG at assets/menubar-icon.png
  // Fallback to a blank image so the app still launches during dev
  let iconPath = path.join(__dirname, 'assets', 'menubar-icon.png');
  let icon;
  try {
    icon = nativeImage.createFromPath(iconPath);
    if (icon.isEmpty()) throw new Error('empty');
  } catch {
    icon = nativeImage.createEmpty();
  }

  tray = new Tray(icon);
  tray.setToolTip('TurboTax Business Tax');
  tray.on('click', toggleWindow);

  // ── Widget window ─────────────────────────────────────────────────────────
  win = new BrowserWindow({
    width:       WIDGET_W,
    height:      WIDGET_H,
    show:        false,
    frame:       false,
    resizable:   false,
    transparent: true,
    hasShadow:   true,
    alwaysOnTop: true,
    type:        'panel',          // keeps it above full-screen spaces on macOS
    webPreferences: {
      nodeIntegration:  false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js'),
    },
  });

  // Load the self-contained prototype HTML
  win.loadFile(PROTOTYPE_PATH);

  // Hide when focus is lost (click outside)
  win.on('blur', () => {
    if (!win.webContents.isDevToolsOpened()) win.hide();
  });

  // Dev keyboard shortcuts
  win.webContents.on('before-input-event', (event, input) => {
    // Cmd+R — reload prototype (picks up edits to prototype/index.html instantly)
    if (input.meta && input.key === 'r' && !input.alt) {
      win.loadFile(PROTOTYPE_PATH);
    }
    // Cmd+Option+I — open DevTools in detached window
    if (input.meta && input.alt && input.key === 'i') {
      win.webContents.openDevTools({ mode: 'detach' });
    }
  });
}

// ── Toggle show/hide, positioned below tray icon ──────────────────────────
function toggleWindow() {
  if (!win) return;

  if (win.isVisible()) {
    win.hide();
    return;
  }

  positionWindow();
  win.show();
  win.focus();
}

function positionWindow() {
  const trayBounds  = tray.getBounds();
  const { workArea } = screen.getDisplayMatching(trayBounds);

  // Center horizontally under the tray icon, top-align below menu bar
  let x = Math.round(trayBounds.x + trayBounds.width  / 2 - WIDGET_W / 2);
  let y = Math.round(trayBounds.y + trayBounds.height + 4);

  // Clamp so it never goes off-screen
  x = Math.max(workArea.x, Math.min(x, workArea.x + workArea.width  - WIDGET_W));
  y = Math.max(workArea.y, Math.min(y, workArea.y + workArea.height - WIDGET_H));

  win.setPosition(x, y, false);
}

// Keep the app alive even when all windows are closed
app.on('window-all-closed', () => { /* intentionally empty */ });
