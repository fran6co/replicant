import hashlib
import yaml
import os
import StringIO

class Chunk(object):
    def __init__(self,file,chunk):
        self.chunk = chunk
        self.file = file
        
        hash = hashlib.sha512()
        hash.update(self.chunk)
        hash.update(self.file)
        self.hash = hash.hexdigest()

class ReceivingNode(object):
    def __init__(self,name,ip):
        self.name = name
        self.ip = ip
    
    def replicate(self,node,chunk):
        print node.name + ','+chunk.hash
        
class Node(object):
    chunk_size = 1024*1024
    max_nodes = 3
    
    def __init__(self,settings = {}):
        self.name = ''
        self.paths = []
        self.nodes = []
        
        if settings:
            if 'paths' in settings:
                self.paths = settings['paths']
            
            if 'name' in settings:
                self.name = settings['name']
                
            if 'nodes' in settings:
                self.nodes = [ReceivingNode(name,ip) for name,ip in settings['nodes'].items()]
                
        self.snapshot()
    
    def add_path(self,path):
        self.paths.append(path)
    
    def add_node(self,node,ip):
        self.nodes.append(ReceivingNode(node,ip))
        
    def snapshot(self):
        meta = {}
        for path in self.paths:
            path_meta = self.snapshot_path(path)
            meta = dict(meta, **path_meta)
            
        meta_file = yaml.dump(meta, explicit_start=True)
        
        print meta_file
        
        chunks = self.chunkize('meta',StringIO.StringIO(meta_file))
        self.replicate_chunks(chunks)
           
    def replicate_chunks(self,chunks):
        for chunk in chunks:
            count = 0
            for node in self.nodes:
                if node.replicate(self,chunk):
                    count += 1
                    
                    if count >= self.max_count:
                        break
                    
            if count == 0:
                # We have a problem
                pass
                
    def snapshot_path(self,path):
        meta = {}
        
        for file in os.listdir(path):
            file = os.path.join(path,file)
            
            if os.path.isdir(file):
                self.snapshot_path(file)
            else:
                with open(file,'rb') as f:
                    chunks = self.chunkize(file,f)
                chunks_hashes = [chunk.hash for chunk in chunks]
                meta[file] = chunks_hashes
                self.replicate_chunks(chunks)
                
        return meta
    
    def chunkize(self,file,stream):
        chunks = []
        
        while True:
            chunk = stream.read(self.chunk_size)
            if not chunk:
                break
                
            chunks.append(Chunk(file,chunk))
                
        return chunks
        
if __name__ == "__main__":
    settings = yaml.load(file('settings.yaml','r'))
    node = Node(settings)
    
    #node.add_path("/User/fran6co/")
    #node.add_node("eze","192.168.1.2")
    
    settings = {}
    settings['paths'] = node.paths
    settings['nodes'] = {}
    for n in node.nodes:
        settings['nodes'][n.name] = n.ip
    
    yaml.dump(settings,file('settings.yaml','w'), explicit_start=True)
    
    
            
            