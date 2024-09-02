import time
import sys
import os
import speedtest
import threading
import random

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    """Print the ANSI logo with animation."""
    logo = [
        '                                                         ',
        '██╗   ██╗██╗     ███████╗██████╗ ███████╗███████╗██████╗ ',
        '██║   ██║██║     ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗',
        '██║   ██║██║     ███████╗██████╔╝█████╗  █████╗  ██║  ██║',
        '██║   ██║██║     ╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║',
        '╚██████╔╝███████╗███████║██║     ███████╗███████╗██████╔╝',
        ' ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝ ',
    ]
    
    clear_screen()
    
    for line in logo:
        sys.stdout.write(f'{line}\n')
        sys.stdout.flush()
        time.sleep(0.05)

def print_progress_bar(progress, text=""):
    """Print the progress bar."""
    bar_length = 40
    filled_length = int(bar_length * progress // 100)
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    
    bar_color = '\033[92m'  # Green
    reset_color = '\033[0m'
    
    sys.stdout.write(f'\r{text} [{bar_color}{bar}{reset_color}] {progress}%')
    sys.stdout.flush()

def speedtest_worker(result_dict):
    """Run the speedtest and store results in a dictionary."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        
        best_server = st.get_best_server()
        result_dict['best_server'] = {
            'name': best_server.get('name', 'Unknown'),
            'country': best_server.get('country', 'Unknown'),
            'sponsor': best_server.get('sponsor', 'Unknown')
        }
        result_dict['download_speed'] = st.download() / 1_000_000  # Convert to Mbps
        result_dict['upload_speed'] = st.upload() / 1_000_000  # Convert to Mbps
        result_dict['ping_latency'] = st.results.ping
    except Exception as e:
        result_dict['error'] = str(e)

def run_speedtest():
    """Run the speedtest and display results."""
    while True:
        clear_screen()
        print_logo()  # Display the logo once
        
        result_dict = {}
        
        print("\nFinding the best server, please wait...")
        
        speedtest_thread = threading.Thread(target=speedtest_worker, args=(result_dict,))
        speedtest_thread.start()
        speedtest_thread.join()
        
        if 'error' in result_dict:
            print(f"\nAn error occurred during the speedtest: {result_dict['error']}")
            retry = input("Would you like to try again? (y/n): ").strip().lower()
            if retry != 'y':
                break
            continue
        
        best_server = result_dict['best_server']
        print(f"\nBest Server Found:")
        print(f"Location    : {best_server['name']}, {best_server['country']}")
        print(f"Provider    : {best_server['sponsor']}")
        
        def simulate_loading(label, duration):
            """Simulate the loading process for download, upload, and ping."""
            start_time = time.time()
            while True:
                elapsed_time = time.time() - start_time
                progress = min(100, int((elapsed_time / duration) * 100))
                print_progress_bar(progress, label)
                if progress >= 100:
                    break
                time.sleep(0.05)
                
        print("\n\nMeasuring download speed...")
        simulate_loading("", random.uniform(3, 5))
        download_speed = result_dict.get('download_speed', 0)
        print(f"\nDownload Speed : {download_speed:.2f} Mbps")
        
        print("\nMeasuring upload speed...")
        simulate_loading("", random.uniform(3, 5))
        upload_speed = result_dict.get('upload_speed', 0)
        print(f"\nUpload Speed   : {upload_speed:.2f} Mbps")
        
        print("\nMeasuring ping latency...")
        simulate_loading("", random.uniform(1, 2))
        ping_latency = result_dict.get('ping_latency', 0)
        print(f"\nPing Latency   : {ping_latency:.2f} ms")
        
        print("\nThank you for using ULSPEED for your speedtest!")
        print("Support speedtest.net at: https://www.speedtest.net")
        
        user_input = input("\nWould you like to test again? (y/n): ").strip().lower()
        if user_input != 'y':
            print("Goodbye!")
            break

# Run the speedtest
if __name__ == "__main__":
    run_speedtest()
