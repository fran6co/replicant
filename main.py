import hashlib

class Api(object):
    def send(self,id,chunk):
        print id+"\n"

class Chunk(Api):
    def __init__(self,file,chunk):
        self.chunk = chunk
        self.file = file
        
    def send(self):
        hash = hashlib.sha512()
        hash.update(self.chunk)
        hash.update(self.file.path)
        id = hash.hexdigest()
        
        super(Chunk,self).send(id,self.chunk)
    
class File:
    chunk_size = 1024*1024
    
    def __init__(self,path):
        self.path = path
        self.chunks = []
        
        with open(self.path,'rb') as f:
            while True:
                chunk = f.read(self.chunk_size)
                if not chunk:
                    break
                
                self.chunks.append(Chunk(self,chunk))
    
    def replicate(self):
        for chunk in self.chunks:
            chunk.send()
    
if __name__ == "__main__":
    f = File("/Users/fran6co/Downloads/dir300-firmware.bin")
    
    f.replicate()
            
            