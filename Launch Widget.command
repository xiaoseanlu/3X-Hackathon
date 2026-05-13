#!/bin/bash
# ─────────────────────────────────────────────────────
#  TurboTax Business Tax Assistant — Launch Script
#  Double-click this file in Finder to start the widget.
#  The TurboTax icon will appear in your menu bar.
#  Right-click the icon or go to Settings → Quit to stop it.
# ─────────────────────────────────────────────────────

# ── Expand PATH so Finder-launched scripts can find Node ──
# Covers: official Node installer, Homebrew Intel, Homebrew Apple Silicon, nvm
export PATH="/usr/local/bin:/opt/homebrew/bin:/opt/homebrew/sbin:$HOME/.nvm/versions/node/$(ls $HOME/.nvm/versions/node 2>/dev/null | sort -V | tail -1)/bin:$PATH"

# Source shell profiles in case Node is only on a custom PATH
[ -f "$HOME/.zshrc"       ] && source "$HOME/.zshrc"       2>/dev/null
[ -f "$HOME/.bash_profile" ] && source "$HOME/.bash_profile" 2>/dev/null
[ -f "$HOME/.nvm/nvm.sh"  ] && source "$HOME/.nvm/nvm.sh"  2>/dev/null

DIR="$(cd "$(dirname "$0")" && pwd)"
APP="$DIR/electron-app"

# ── Check Node is available ───────────────────────────
if ! command -v node &>/dev/null; then
  echo ""
  echo "❌  Node.js not found."
  echo ""
  echo "    Install it from: https://nodejs.org"
  echo "    Then double-click this file again."
  echo ""
  read -p "Press Enter to close..."
  exit 1
fi

echo ""
echo "✅  Node $(node --version) found"

# ── Install dependencies if needed ───────────────────
if [ ! -d "$APP/node_modules" ]; then
  echo "📦  First run — installing dependencies (~30 sec)..."
  cd "$APP" && npm install
  if [ $? -ne 0 ]; then
    echo ""
    echo "❌  npm install failed. Check your internet connection and try again."
    read -p "Press Enter to close..."
    exit 1
  fi
fi

echo "🚀  Launching TurboTax Business Tax Assistant..."
echo "    Look for the red TurboTax icon in your menu bar."
echo ""
echo "    To quit: right-click the icon → Quit, or go to Settings inside the widget."
echo "    To reload after edits: press Cmd+R while the widget is open."
echo ""

cd "$APP" && npm start

# Keep window open if Electron exits with an error
if [ $? -ne 0 ]; then
  echo ""
  echo "⚠️  The widget exited unexpectedly. See the error above."
  read -p "Press Enter to close..."
fi
