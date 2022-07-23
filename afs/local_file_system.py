import os
import shutil
from pathlib import Path
from afs.abstract_file_system import AbstractFileSystem


class LocalFileSystem(AbstractFileSystem):

    def __init__(self, root=os.path.sep):
        super(LocalFileSystem, self).__init__()
        self.root = root

    def _absolute_path(self, path):
        return Path(self.root, path)

    def _absolute_paths(self, *paths):
        return (self._absolute_path(path) for path in paths)

    def cp(self, src, dest, *args):
        (src_abs, dest_abs) = self._absolute_paths(src, dest)
        return str(shutil.copy(src_abs, dest_abs, *args))

    def mv(self, src, dest, *args):
        return