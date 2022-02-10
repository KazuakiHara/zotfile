#https://ja.stackoverflow.com/questions/76174/

import os
from zipfile import ZipFile, ZIP_DEFLATED

def make_zipfile_from_multiple_directory(zip_filename, src_dirs):
  save_cwd = os.getcwd()
  with ZipFile(zip_filename, 'w', compression=ZIP_DEFLATED) as zf:
    for base_dir in src_dirs:
      path_dir, path_base = os.path.split(os.path.realpath(base_dir))
      os.chdir(path_dir)
      zf.write(path_base, path_base)
      for dirpath, dirnames, filenames in os.walk(path_base):
        for name in sorted(dirnames):
          path = os.path.normpath(os.path.join(dirpath, name))
          zf.write(path, path)
        for name in filenames:
          path = os.path.normpath(os.path.join(dirpath, name))
          if os.path.isfile(path):
            zf.write(path, path)

  os.chdir(save_cwd)


make_zipfile_from_multiple_directory("./pack/zotfile_jp.zip", ['chrome', 'defaults', 'chrome.manifest', 'install.rdf'])
