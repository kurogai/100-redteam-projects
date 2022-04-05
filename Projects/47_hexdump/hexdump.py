#!/usr/bin/python3


import os
import sys
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE", help="file to be dump", type=str)
    parser.add_argument("-b", "--binary", help="display bytes in binary instead of hex", action="store_true")
    args = parser.parse_args()
    
    try:
        with open(args.FILE, "rb") as f:
            n = 0
            b = f.read(16)
            filesize = os.path.getsize(args.FILE)
            print(f"Size {args.FILE}: {filesize} bytes - 0x{filesize:08x}")
            while b:
                if not args.binary:
                    s1 = " ".join([f"{i:02x}" for i in b]) # hex string
                    s1 = s1[0:23] + " " + s1[23:]          # insert extra space between groups of 8 hex values
                    width = 48
                else:
                    s1 = " ".join([f"{i:08b}" for i in b])
                    s1 = s1[0:71] + " " + s1[71:]
                    width = 144
                s2 = "".join([chr(i) if 32 <= i <= 127 else "." for i in b]) # ascii string; chained comparison
                print(f"{n * 16:08x}  {s1:<{width}}  |{s2}|")
                
                n += 1
                b = f.read(16)

    except Exception as e:    
        print(__file__, ": ", type(e).__name__, " - ", e, sep="", file=sys.stderr)
    

