# Advanced Hash Cracker

An advanced tool for brute-forcing hashes using a provided wordlist.

## **Features**
- **Multiple Algorithm Support:** Crack hashes made with md5, sha1, sha256, and more.
- **User-friendly CLI:** Intuitive and easy to use.
- **Helpful Feedback:** Receive clear and concise error messages when things go wrong.

## **Prerequisites**

- Python 3.x

## **Usage**
Run the cracker with:

```
python hash-cracker.py --hashvalue [HASH_VALUE] --hashtype [HASH_TYPE] --wordlist [PATH_TO_WORDLIST]
```

## Parameters

- `--hashvalue`: The hash string you want to decode.
- `--hashtype`: The algorithm used to encode the hash. (e.g., md5, sha1, sha256, etc.)
- `--wordlist`: Path to the wordlist file you want to use for brute-forcing.

## Example

To crack an md5 hash using the `words.txt` wordlist:

```
python hash-cracker.py --hashvalue 7052cad6b415f4272c1986aa9a50a7c3 --hashtype md5 --wordlist words.txt
```