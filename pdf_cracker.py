import PyPDF2
import time
import sys

last_time = time.time()
wordlist = open('10k_most_common.txt')
#num_lines = sum(1 for line in open('10k_most_common.txt'))
pdf = PyPDF2.PdfFileReader(open('lock1.pdf','rb'))
if not pdf.isEncrypted:
    print('No password')
else:
    for line in wordlist.readlines():
        if pdf.decrypt(line.rstrip()) :
            print('[+] PASSWORD: ' +line)
            print('Time taken is: ' + str(time.time()-last_time) + ' Second')
            sys.exit()
    print('[-] Password not found')
