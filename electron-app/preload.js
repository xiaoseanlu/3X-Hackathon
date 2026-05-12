/**
 * preload.js — Electron preload script
 *
 * Runs in the renderer context with access to Node APIs (but isolated from
 * the page's JS). Use contextBridge.exposeInMainWorld() here to safely
 * expose backend capabilities to the prototype HTML.
 *
 * Planned extensions (Day 2 sprint):
 *   - Expose Anthropic API for real Claude chat responses
 *   - Expose file system access for drag-and-drop document parsing
 *   - Expose IPC bridge for native macOS notifications
 */

const { contextBridge, ipcRenderer } = require('electron');

// Example: expose a safe API surface to the renderer
contextBridge.exposeInMainWorld('electronAPI', {
  // Placeholder — extend as features are added
  platform: process.platform,

  // Future: real Claude API call
  // askClaude: (prompt) => ipcRenderer.invoke('ask-claude', prompt),

  // Future: parse dropped document
  // parseDocument: (filePath) => ipcRenderer.invoke('parse-document', filePath),

  // Future: trigger native notification
  // scheduleNotification: (title, body, delayMs) => ipcRenderer.invoke('schedule-notification', { title, body, delayMs }),
});
