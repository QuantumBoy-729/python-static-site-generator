import Path from pathlib
import os
class Site:
    def __init__(self,source,dest):
        self.source = Path(source)
        self.dest = Path(dest)
    
    def create_dir(self,path):
        directory =self.dest/self.source.relative_to(path)
        os.mkdir(directory,parents=True,exist_ok=True)

    def build(self):
        os.mkdir(self.dest,parents=True,exist_ok=True)
        for path in self.source.rglob("*"):
            if(os.path.isdir(path)):
                create_dir(path)


        
