import urllib
import binascii  
import struct
import os,sys

# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
#print base
# bin2dec
# 二进制 to 十进制: int(str,n=10) 
def bin2dec(string_num):
    return str(int(string_num, 2))

# hex2dec
# 十六进制 to 十进制
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))

# dec2bin
# 十进制 to 二进制: bin() 
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

# dec2hex
# 十进制 to 八进制: oct() 
# 十进制 to 十六进制: hex() 
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

# hex2tobin
# 十六进制 to 二进制: bin(int(str,16)) 
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))

# bin2hex
# 二进制 to 十六进制: hex(int(str,2)) 
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))

#convert hexdecimal string to binary string
def hexstr2binstr(hexstr):
    return bin(int(hexstr.encode('hex'),16)).replace('0b','')

filename = '1.txt'
strs = []


#convert utf-8 file to binary string
def covertTextFiletoBinStr(filename):
    read_len = 8
    with open(filename,'r') as f:
        while True:
            ts=f.read(1)
            if len(ts) == 0:  
                break  
            #str_temp = bin(int(ts.encode('hex'),16)).replace('0b','')
            #print ts.encode('hex')
            str_temp = hexstr2binstr(ts)        
            #if the length is less than 8 , fill 0        
            if len(str_temp)<8:
                str_temp =str_temp.rjust(read_len,'0') 
            #trans to utf-8 bin
            start0 = str_temp.index('0')
            if start0 >0:
                ts = f.read(start0-1)
                str_temp += hexstr2binstr(ts)            
            strs.append(str_temp)
    return strs

#convert utf-8 html to binary string
def covertHTMLtoBinStr(url):
    resp = urllib.urlopen(url)    
    while True:
        ts = resp.read(1)
        if len(ts) == 0:
            break
        str_temp = hexstr2binstr(ts)          
        if len(str_temp)<8:
            str_temp =str_temp.rjust(read_len,'0') 
        #trans to utf-8 bin
        start0 = str_temp.index('0')
        if start0 >0:
            ts = resp.read(start0-1)
            str_temp += hexstr2binstr(ts)            
        strs.append(str_temp)
    resp.close()
    return strs

#convert hexdecimal string to byte
def hexstr2byte(s):
    base='0123456789ABCDEF'
    i=0
    s = s.upper()
    s1=''
    while i < len(s):
        c1=s[i]
        c2=s[i+1]
        i+=2
        b1=base.find(c1)
        b2=base.find(c2)
        if b1 == -1 or b2 == -1:
            return None
        s1+=chr((b1 << 4)+b2)
    return s1

def hexstr2binhexstr(s):    
    i=0
    s1=''
    while i< len(s):
        c1 = s[i:i+2]
        if i==0:
            s1=c1
        else:
            s1 += ' '+c1    
        i += 2
    return s1
        
        
#test
#bins = covertHTMLtoBinStr("http://www.baidu.com")
bins = covertTextFiletoBinStr('1.txt')
bins = ''.join(bins)
hexs = bin2hex(bins)
outs = str2byte(hexs)
print '========================================================================='
print 'bin:'
print bins
print '========================================================================='
print 'hex:'
print hexs
print '========================================================================='
print 'hex2:'
#print ' '.join([str(x) for x in hexs[::2]])
print hexstr2binhexstr(hexs)
print '========================================================================='
print 'utf8:'
print outs
