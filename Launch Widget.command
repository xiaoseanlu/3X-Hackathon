#!/bin/bash
# ─────────────────────────────────────────────────────
#  TurboTax Business Tax Assistant — Launch Script
#  Double-click this file in Finder to start the widget.
#  The TurboTax icon will appear in your menu bar.
#  Press Cmd+Q in the widget, or quit from Settings,
#  to close it. Then close this Terminal window.
# ─────────────────────────────────────────────────────

DIR="$(cd "$(dirname "$0")" && pwd)"
APP="$DIR/electron-app"

# Install dependencies if node_modules is missing
if [ ! -d "$APP/node_modules" ]; then
  echo "📦  First run — installing dependencies (takes ~30 sec)..."
  cd "$APP" && npm install
fi

echo "🚀  Launching TurboTax Business Tax Assistant..."
echo "    Look for the icon in your menu bar."
echo ""
echo "    To stop: quit the widget from Settings, then close this window."
echo ""

cd "$APP" && npm start
