#!/usr/bin/env python
"""
Operations to be supported
cat /myfuse/test.txt
getattr->open->read->release

echo Hello>/myfuse/test2.txt
getattr->create->write->flush->release

append
echo world>>/myfuse/test2.txt
getattr->open->write->flush->release

trucate
echo Woo>/myfuse/test2.txt
getattr->trucate->open->write->flush->release

remove
rm /myfuse/test.txt

chown  th30z:develr /myfuse/test.txt
getattr->chown

chmod 755 /myfuse/test.txt
getattr->chmod

ln -s /myfuse/test.txt /myfuse/test-link.txt
getattr->symlink

mv /myfuse/folder /myfuse/fancy-folder
getattr->rename
"""
