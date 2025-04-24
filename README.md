# DexTerm 🩸🖥️

![](./imgs/dexterm.jpeg)
DexTerm is a Terminal User Interface (TUI) and a Command Line Interface (CLI)
designed to monitor and visualize glucose levels using the Dexcom API.
It allows users to fetch, display, and plot glucose data directly in the terminal,
providing a seamless experience for managing and tracking blood sugar levels.

> [!warning]
> This library is still a work in progress and not "production ready". Feel free
> to try it, to contribute and report bugs.

## Features

- **Configuration Management**: Easily configure Dexcom API credentials and
  other settings. ✅
- **Fetch last measurement**: Fetch last measurement with one CLI command. ✅
- **Read last measurement**: Read last fetched measurement and use them with other
  terminal tools. ✅
- **Real-time Data Fetching**: Automatically fetch glucose data every 5 minutes.❌
- **Historical Data**: View and plot historical glucose data over customizable
  time ranges.❌
- **Terminal Plotting**: Visualize glucose data directly in the terminal using
  `plotille`.❌
- **Alarms and Notifications**: Set alarms for high/low glucose levels
  (feature in development).❌

## Installation

### Prerequisites

- Python 3.9 or higher
- `uv` for dependency management

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/huwilerb/dexterm.git
   cd dexterm

   ```

2. **Install dependencies**

   ```bash
   uv install
   ```

3. **Configure Dexcom API credentials**

   The CLI has an endpoint for configuration. You can show help with:

   ```bash
   dexterm settings --help
   ```

   More information about the CLI API in the documentation.
