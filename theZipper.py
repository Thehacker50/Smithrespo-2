import os
import shutil

def compress(name,iterable_of_files):
    getdone = shutil.make_archive(base_name=name,base_dir=iterable_of_files,format="zip")
    if getdone == None:
        return "Done"

def decompress(*archive_files,ext_dir):
    archive_files = archive_files.split(" ")
    print(archive_files)
    for archive in archive_files:
        getdone = shutil.unpack_archive(archive,extract_dir=ext_dir)
    return "Done"
