import requests
import threading
import argparse
import sys

# Global variables for thread synchronization
checked_directories = 0
total_directories = 0
lock = threading.Lock()

def explore_directories(base_url, directory_list, thread_id):
    global checked_directories

    for i in range(len(directory_list)):
        if i % num_threads == thread_id:  # Distribute directories among threads
            directory = directory_list[i]
            url = f"{base_url}/{directory}"
            response = requests.get(url)

            with lock:
                checked_directories += 1
                sys.stdout.write(f"\033[KThread-{thread_id}: Currently checking {directory}. Total Checked: {checked_directories}/{total_directories}\r")
                sys.stdout.flush()

            if response.status_code == 200:
                print(f"Found directory: {url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Directory brute-forcer with threading')
    parser.add_argument('url', type=str, help='Base URL')
    parser.add_argument('wordlist', type=str, help='Path to directory wordlist')
    parser.add_argument('--threads', type=int, default=4, help='Number of threads (default: 4)')
    args = parser.parse_args()

    base_url = args.url
    with open(args.wordlist) as file:
        directories = file.read().splitlines()

    total_directories = len(directories)
    num_threads = args.threads

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=explore_directories, args=(base_url, directories, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
