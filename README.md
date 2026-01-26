# Decky Hour Notifications

A lightweight Decky plugin that displays a toast notification at the top of every hour while you are playing games on Steam Deck.

The notification shows the current hour in 12-hour format (e.g. `1:00`, `12:00`) to help you keep track of time without breaking immersion.

## Features

- Hourly toast notification on the hour  
- No polling or drift  
- Automatically realigns after suspend / resume  
- Minimal UI (no settings, no buttons)  
- Very low overhead  

## How it works

- A Python backend schedules a task that sleeps until the next top-of-hour.  
- When the hour changes, it emits an event to the frontend.  
- The frontend displays a toast notification.  
- On system resume from suspend, the backend task is restarted to realign timing.  

## Installation

### Manual build & install

The distributable zip is not checked into the repository.

1. Clone the repository.
2. Install dependencies:
   - Node.js v16.14+
   - `pnpm` v9
3. Install frontend dependencies:
   ```bash
   pnpm install
   ```
4. Build the plugin:
   ```bash
   pnpm run build
   ```
5. Package the plugin:
   ```bash
   pnpm run package
   ```
   This will generate a zip containing a DeckyHourNotifications/ folder with all required files.
6. Copy the generated zip to your Steam Deck, enable Decky Developer Mode, and install the plugin using Install from ZIP in the Decky Developer menu.

## Notes

- Notifications use the system time.
- Format is 12-hour with no AM/PM.
- Designed for Steam Deck (Linux). Not tested on other platforms.

## License

See `LICENSE`.
