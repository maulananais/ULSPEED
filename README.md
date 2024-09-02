# ULSPEED 🌐

Welcome to **ULSPEED**, a sleek and animated command-line speed test tool that measures your internet connection's download speed, upload speed, and ping latency, all while displaying a cool logo and progress animation.

## Features ✨

- **ANSI Logo Animation**: Enjoy a custom animated logo while running the test.
- **Progress Bar**: Watch your progress in real-time with a dynamic progress bar.
- **Detailed Results**: Get accurate measurements of download speed, upload speed, and ping latency.
- **Best Server Selection**: Automatically selects the best server for your test.
- **Retry Option**: Option to rerun the test with a simple prompt.

## Installation 💻

### Install Python

#### Windows

1. **Download Python**: Go to the [Python official website](https://www.python.org/downloads/) and download the latest Python installer for Windows.
2. **Run the Installer**: Execute the installer and check the box "Add Python to PATH" before clicking "Install Now".
3. **Verify Installation**: Open Command Prompt and run:
   ```bash
   python --version
   ```

#### macOS

1. **Download Python**: Go to the [Python official website](https://www.python.org/downloads/) and download the latest Python installer for macOS.
2. **Run the Installer**: Execute the downloaded `.pkg` file and follow the instructions.
3. **Verify Installation**: Open Terminal and run:
   ```bash
   python3 --version
   ```

#### Linux

1. **Update Package List**: Open Terminal and run:
   ```bash
   sudo apt update
   ```
2. **Install Python**: Run:
   ```bash
   sudo apt install python3
   ```
3. **Verify Installation**: Run:
   ```bash
   python3 --version
   ```

### Install Dependencies

1. **Clone the repository**:
   ```bash
   git clone https://github.com/maulananais/ulspeed.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd ulspeed
   ```
3. **Install `speedtest-cli`**:
   Make sure you have `speedtest-cli` installed. Run:
   ```bash
   pip install speedtest-cli
   ```

### Run the Script

#### Windows

Run:
   ```bash
   py ulspeed.py
   ```

#### macOS

Run:
   ```bash
   python3 ulspeed.py
   ```

#### Linux

Run:
   ```bash
   python3 ulspeed.py
   ```

## Usage 🛠️

Simply run the script and follow the on-screen prompts. ULSPEED will handle the rest, from server selection to speed measurements. The process is visualized with an animated logo and progress bar for an engaging experience.

## Error Handling ⚠️

If you encounter a **403 Forbidden** error or if the system fails to get a stable connection, follow these steps:

1. **Refresh Connection**: Visit [speedtest.net](https://www.speedtest.net) and start a test to refresh your connection.
2. **Rerun the Script**: After refreshing, run the script again:
   - **Windows**: `py ulspeed.py`
   - **macOS**: `python3 ulspeed.py`
   - **Linux**: `python3 ulspeed.py`

## Example Output 📊

```
██╗   ██╗██╗     ███████╗██████╗ ███████╗███████╗██████╗ 
██║   ██║██║     ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
██║   ██║██║     ███████╗██████╔╝█████╗  █████╗  ██║  ██║
██║   ██║██║     ╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║
╚██████╔╝███████╗███████║██║     ███████╗███████╗██████╔╝
 ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝ 

Finding the best server, please wait...

Best Server Found:
Location    : Jakarta, Indonesia
Provider    : PT Telkom

Measuring download speed...
[########################################] 100%
Download Speed : 112.12 Mbps

Measuring upload speed...
[########################################] 100%
Upload Speed   : 55.34 Mbps

Measuring ping latency...
[########################################] 100%
Ping Latency   : 1.34 ms

Thank you for using ULSPEED for your speedtest!
```

## License ⚖️

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙏

A big thanks to:
1. **Allah SWT** for the blessings and guidance.
2. **My parents** for their endless support and encouragement.
3. **Speedtest.net** for providing the reliable testing service.

## Contributing 👥

Contributions are welcome! Feel free to fork this repository, open an issue, or submit a pull request.
