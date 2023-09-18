#!/usr/bin/env python
# coding: utf-8

# In[14]:


import hashlib
from datetime import datetime 


class blockchain:
    global blockc
    global height
    blockc = ''
    height = 0
    n = []
        
        
        
    def get_hash(self, sender, reciver, number):
        global height
        global n
        hasher = hashlib.sha256
        nonce = 0
        genesis_hash = '0'*64
        data = str(sender) + ' '+ str(reciver)+' ' +  str(number)
        while True:
            unhashed = str(nonce)+str(data)
            hashed = hasher(unhashed.encode('utf-8')).hexdigest()
            if hashed[:4] == '0000':
                n.append(hashed)
                height = height + 1
                break
            else:
                nonce = nonce + 1
                
        prev_hash = []
        for x in n:
            if x != hashed:
                prev_hash = x
            else:
                continue
        if height == 1:
            prev_hash = genesis_hash
        
        time_mined = datetime.now()
        
        blockc = (f"blockdata: {data}",
                  f"hash: {hashed}", 
                  f"height: {str(height)}",
                  f"nonce: {str(nonce)}",          
                  f"prev hash: {prev_hash}",
                  f"time mined: {time_mined}")
        
        print(blockc)
        
bchain = blockchain()


bchain.get_hash('a1','b2','123124')
print('\n')
bchain.get_hash('a2','b3','331234')
print('\n')
bchain.get_hash('a3','b4','26171762')
print('\n')
bchain.get_hash('a4','b5','44671324')
print('\n')
bchain.get_hash('a5','b6','881236146')
print('\n')
bchain.get_hash('a6','b7','77123467')
print('\n')
bchain.get_hash('a7','b8','6661252134')
print('\n')
bchain.get_hash('a8','b9','111123471234')
print('\n')
bchain.get_hash('a9','b10','15561268')
print('\n')
bchain.get_hash('a10','b11','177612362314')


# In[ ]:





# In[ ]:




