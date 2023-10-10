import hashlib
from optparse import OptionParser

def generateHash(content, hash_algorithm):
    hash_instance = hashlib.new(hash_algorithm)
    hash_instance.update(content.encode('utf-8'))
    return hash_instance.hexdigest()

def getSupportedHashTypes():
    return hashlib.algorithms_guaranteed

def main():
    usage = """
# Usage:
    python cracker_advanced.py --hashvalue <hash_value> --hashtype <hash_type> --wordlist <path_to_wordlist>
# Example:
    python cracker_advanced.py --hashvalue 7052cad6b415f4272c1986aa9a50a7c3 --hashtype md5 --wordlist words.txt
"""
    optHandler = OptionParser(usage)
    optHandler.add_option("--hashvalue", dest="hashValue", type="string", help="Hash value to be cracked")
    optHandler.add_option("--hashtype", dest="hashType", type="string", help="Type of hash: md5, sha1, sha256, etc.")
    optHandler.add_option("--wordlist", dest="wordListPath", type="string", help="Path to word list file")

    (opts, argsList) = optHandler.parse_args()

    if not (opts.hashValue and opts.hashType and opts.wordListPath):
        print(optHandler.usage)
        exit(0)

    if opts.hashType not in getSupportedHashTypes():
        print(f"Invalid hash type: {opts.hashType}")
        print("Supported hash types are:", ", ".join(getSupportedHashTypes()))
        exit(0)

    with open(opts.wordListPath, 'r') as wordlist:
        for word in wordlist:
            word = word.strip("\n")
            calculated_hash = generateHash(word, opts.hashType)
            print(f"Testing: {word}")
            if opts.hashValue == calculated_hash:
                print(f"\nHash Found: [ {calculated_hash} ] >> word: [ {word} ]")
                exit(0)

    print("\n\tHash not found :(\n")

if __name__ == "__main__":
    main()