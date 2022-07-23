class AbstractFileSystem:
    """Abstract class for AFS"""

    def __init__(self, *args, **kwargs):
        pass

    def cp(self, src, dest, *args):
        """Copy file/dir from :src to :dest"""

    def mv(self, src, dest, *args):
        """Move file/dir from :src to :dest"""

    def rm(self, path, *args):
        """Remove :path file/dir"""

    def mkdir(self, path, *args):
        """Create :path dir"""

    def exists(self, path, *args):
        """Check if :path file/dir exists"""

    def is_dir(self, path, *args):
        """Check if :path is dir"""

    def is_file(self, path, *args):
        """Check if :path is regular file"""

