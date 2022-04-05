from threading import Thread
import time,requests,sys,os.path

def usage():
    print("----------USAGE INSTRUCTION ---------")
    print(f"{sys.argv[0]} URL WORDLIST NUMBER_OF_THREADS(Default is 10)\n")
    sys.exit()

def prepare(myList,numOfChunks):
    for i in range(0, len(myList), numOfChunks):
        yield myList[i:i + numOfChunks]

def brute(myList,url):
    start=time.perf_counter()
    for lists in myList:
        threads.append(Thread(target=worker,args=(lists,url),daemon=True))
    for thread in threads:
        try:
            thread.start()
        except KeyboardInterrupt:
            print("\nReceived Keyboard Interrupt  , Terminating threads\n")
            sys.exit()
    for thread in threads:
        try:
            thread.join()
        except KeyboardInterrupt:
            print("\nReceived Keyboard Interrupt  , Terminating threads\n")
            sys.exit()
    finish=time.perf_counter()
    print(f"\n\n\t\t Checked {total_len} Directories in {round(finish-start,2)} Seconds\n")

def worker(lists,url):
    try:
        for word in lists:
            if word.startswith("/"):
                word=word[1:]
            url2=url+"/"+word.strip()
            r=requests.get(url2)
            if str(r.status_code) in match:
                print(f"/{word.strip():<40}  [ Status: {r.status_code}  Length:{len(r.content)} ]")
    except KeyboardInterrupt:
        print("\nReceived Keyboard Interrupt  , Terminating threads\n")
        sys.exit()
    except Exception as e:
        print(f"\nAn error Occurred : {e}\n")
        sys.exit()

if __name__ == "__main__":
    try:    
        match=['200','301','302','401','403','429'] #change this to filter responses
        try:
            if sys.argv[1]:
                url=sys.argv[1]
            if sys.argv[2]:
                wordlist=sys.argv[2]
            try:
                if sys.argv[3]:
                    numOfThreads=int(sys.argv[3])
            except:
                numOfThreads=10
        except:
            usage()
        if os.path.isfile(wordlist)==False:
            print(f"The file {wordlist} doesn't exist")
            sys.exit()
        with open(wordlist,'r') as w:
            myList=w.readlines()
        total_len=len(myList)
        final=[]
        threads=[]
        if numOfThreads>total_len or numOfThreads<0:
            print("\nToo High Value for Threads with Respect to Input Word-list\n")
            sys.exit(1)
        numOfChunks=len(myList)//numOfThreads
        if url.endswith("/"):
            url=url[0:-1]
        print(f'''
        ======================================
        URL           --> {url}
        Word-list     --> {wordlist}
        Threads       --> {numOfThreads}
        Status Codes  --> {','.join([w for w in match])}
        ======================================
        \n\n
            ''')
        print("------- Started Brute forcing Directories -------\n")
        myList_new=prepare(myList,numOfChunks)
        brute(myList_new,url)
    except Exception as e:
        print(f"\nAn error Occurred : {e}\n")
        sys.exit()
