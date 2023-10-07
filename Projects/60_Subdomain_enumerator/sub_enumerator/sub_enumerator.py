# Sub Enumerator Tool By manthanghasadiya

import argparse
import threading
import requests

# Global variables for thread synchronization
checked_subdomains = 0
lock = threading.Lock()
unique_subdomains = set()

def enumerate_subdomains(subdomain_list, base_domain, thread_id):
    global checked_subdomains

    for subdomain in subdomain_list:
        with lock:
            if checked_subdomains >= total_subdomains:
                break

            checked_subdomains += 1
            print(f"\rChecked {checked_subdomains} subdomains out of {total_subdomains}", end='')
            flush()

            url = f"http://{subdomain}.{base_domain}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                with lock:
                    unique_subdomains.add(url)
        except requests.exceptions.RequestException:
            pass

def flush():
    import sys
    sys.stdout.flush()

def save_subdomains(filename):
    with open(filename, 'w') as file:
        for subdomain in unique_subdomains:
            file.write(subdomain + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Subdomain Enumerator')
    parser.add_argument('-d', '--domain', type=str, required=True, help='Base domain')
    parser.add_argument('-w', '--wordlist', type=str, required=True, help='Path to subdomain wordlist')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path to output file')
    parser.add_argument('--threads', type=int, default=4, help='Number of threads (default: 4)')
    args = parser.parse_args()

    base_domain = args.domain
    with open(args.wordlist) as file:
        subdomain_list = file.read().splitlines()

    total_subdomains = len(subdomain_list)
    num_threads = args.threads

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=enumerate_subdomains, args=(subdomain_list, base_domain, i))
        threads.append(thread)
        thread.start()

    try:
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\n\nEnumeration interrupted. Saving valid subdomains...")

    save_subdomains(args.output)

    print("\nEnumeration Complete.")
    print(f"\nUnique Valid Subdomains saved in {args.output}")

