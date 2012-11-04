#!/usr/bin/env python
# -*_ coding: utf-8 -*-
"""
Usage:
SocialFs.py
"""
import fuse
import time
import stat
import errno
import os
import slog
#import gtk
fuse.fuse_python_api = (0, 2)


class  ShareStat(fuse.Stat):
    """
    ShareStat :Exends fuse.Stat
    Managing stat for SocialFS
    """

    def __init__(self):
        """
        st_mode :Object types and permissions, Protection
        st_ino :Inode number
        st_dev :Id of device containing file
        st_uid :User ID of the  owner
        st_gid :Group ID of the  owner
        st_size :Total size in bytes
        st_atime :Time when the object was last accessed
        st_mtime :Time when the object was last modified
        st_citme :Time when the object's metadata was last modified
        For more help give command 'man stat64'
        st_mode field =>
        S_ISREF :is it a reqular file?
        S_ISDIR : directory?
        """
        #slog.info("ShareStat=>init")
        self.st_mode = 0
        self.st_ino = 0
        self.st_dev = 0
        self.st_nlink = 0
        self.st_uid = os.getuid()
        self.st_gid = os.getgid()
        self.st_size = 4096
        self.st_atime = 0
        self.st_mtime = 0
        self.st_ctime = 0
        self.set_time()

    def set_time(self):
        """
        set atime,mtime,ctime
        in stat
        """
        #slog.info("ShareStat=>set_time")
        self.st_atime = int(time.time())
        self.st_mtime = int(time.time())
        self.st_ctime = int(time.time())

    def set_dir_attr(self):
        """
        Purpose :Set attributes of a directory
        size:int the size of directory
        """
        #slog.info("ShareStat=>set_dir_attr")
        self.st_mode = stat.S_IFDIR | 0775
        self.st_nlink = 2
        self.set_time()

    def set_file_attr(self, size=0):
        """
        Purpose: Set attributes of a file
        size:int the file's size in bytes
        """
        #slog.info("ShareStat=>set_file_attr")
        self.st_mode = stat.S_IFREG | 0776
        self.st_nlink = 1
        self.st_size = size
        self.set_time()


class ShareFS(fuse.Fuse):
    """
    ShareFS : Extends fuse.Fuse
    Defines different methods for filesystem
    """

    def __init__(self, *args, **kw):
        """
        Call fuse.Fuse constructor with given
        arguments
        """
        slog.info("ShareFS=>init")
        fuse.Fuse.__init__(self, *args, **kw)
        self.directories = {}
        self.files = {}
        self.time_accessed = {}
        self.codec = 'utf-8'

    def getattr(self, path):
        """
        Getattr for filesystem
        return stat for given path
        """
        slog.info("ShareFS=>getattr" + str(path))
        if os.path.exists(path):
            return os.lstat(path)
        else:
            return -errno.ENOENT
        st = ShareStat()
        temp = path.split('/')
        if len(temp):
            st.set_dir_attr()
        elif path:
            st.set_file_attr()
        else:
            return -errno.ENOENT
        return st

    def readdir(self, path, offset):
        """
        Read directory
        """
        slog.info("ShareFS=>readdir" + str(path))
        for e in '.', '..', '/':
            yield fuse.Direntry(e)

    def fsinit(self):
        """
        fsinit
        """
        slog.info("ShareFS=>fsinit")
        return 0

    def open(self, path, flags):
        """
        Read all files in working directory.
        """
        slog.info("ShareFS=>open"+str(path))
        # Only support for 'READ ONLY' flag
        os.open(path, flags)
        return 0

    def create(self, path, flags=None, mode=None):
        """
        Create call when we have to create new file
        """
        slog.info("ShareFS=>create"+str(path))
        return -errno.ENOENTx

    def write(self, path, length, offset):
        """
        Write call to write some content in file
        """
        slog.info("ShareFS=>write"+str(path))
        return -errno.ENOENT

    def read(self, path, length, offset):
        """
        Read all files in working directory.
        """
        slog.info("ShareFS => read"+str(path))
        return 'This is just interface'

    def mknod(self, path, mode, dev):
        """
        Mknod
        """
        slog.info("ShareFS => mknod " + str(path))
        return -errno.ENOENT

    def unlink(self, path):
        """
        unlink
        """
        slog.info("ShareFS=> unlink" + str(path))
        return -errno.ENOENT

    def rename(self, old, new):
        """
        rename
        """
        slog.info("ShareFS=>rename" + str(old) +str(new))
        return -errno.ENOENT

    def trucate(self, path, len, fh):
        """
        trucate
        """
        slog.info("ShareFs=>trucate" + str(path))
        return -errno.ENOENT

    def release(self, path, fh):
        """
        release
        """
        slog.info("ShareFS=>release" + str(path))
        return -errno.ENOENT

    def mkdir(self, path):
        """
        mkdir
        """
        slog.info("ShareFs=>mkdir" + str("mkdir"))
        os.mkdir(path)
        return 0

    def rmdir(self, path):
        """
        rmdir
        """
        slog.info("ShareFS=>rmdir" + str(path))
        return -errno.ENOENT

    def chmod(self, path, mode):
        """
        chmod
        """
        slog.info("ShareFs=>chmod"+ str(path))
        return -errno.ENOENT

    def chown(self, path, uid, gid):
        """
        chown
        """

        slog.info("ShareFS=>chown"+str(path))
        return -errno.ENOENT


def loop():
    """
    This is where actual file system
    start working
    """
    usage = 'SocialFs a virtual Filesytem to manage a social accounts' + \
        fuse.Fuse.fusage
    sfs = ShareFS(version = '%prog' + fuse.__version__,
                  usage = usage,
                  dash_s_do = 'setsingle')
    sfs.parse(errex = 1)
    sfs.main()

if __name__ == '__main__':
    loop()
