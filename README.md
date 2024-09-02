# ULSPEED 🌐

Welcome to **ULSPEED**, a sleek and animated command-line speed test tool that measures your internet connection's download speed, upload speed, and ping latency, all while displaying a cool logo and progress animation.

## Features ✨

- **ANSI Logo Animation**: Enjoy a custom animated logo while running the test.
- **Progress Bar**: Watch your progress in real-time with a dynamic progress bar.
- **Detailed Results**: Get accurate measurements of download speed, upload speed, and ping latency.
- **Best Server Selection**: Automatically selects the best server for your test.
- **Retry Option**: Option to rerun the test with a simple prompt.

## Installation 💻

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/ulspeed.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd ulspeed
   ```
3. **Install dependencies**:
   Make sure you have `speedtest-cli` installed.
   ```bash
   pip install speedtest-cli
   ```
4. **Run the script**:
   ```bash
   python ulspeed.py
   ```

## Usage 🛠️

Simply run the script and follow the on-screen prompts. ULSPEED will handle the rest, from server selection to speed measurements. The process is visualized with an animated logo and progress bar for an engaging experience.

```bash
python ulspeed.py
```

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

## Contributing 👥

Contributions are welcome! Feel free to fork this repository, open an issue, or submit a pull request.

---

**ULSPEED** is designed with simplicity and style in mind. Whether you're just curious about your internet speed or need to troubleshoot a connection, ULSPEED gives you the information you need with a touch of flair.

```

### Tips:
- Replace `"https://your-logo-link-here"` with a link to a relevant logo image, or you can remove that section if you don't have an image.
- You might want to customize the example output to match the typical results in your area.
