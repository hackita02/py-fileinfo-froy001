import sys
from pathlib import Path
from collections import defaultdict

def print_result():
  folder_dict = get_folder_dict()
  for category, info in sorted(folder_dict.items()):
    print("{} \t {} \t {}".format(category, info['file_number'],info['total_size']))



# create defaultdict
def create_file_category():
  return {
    'file_number': 0,
    'total_size': 0
  }

def get_folder_dict():
  folder_dict = defaultdict(create_file_category)

  for item in folder.iterdir():
    if item.is_file() and not item.is_dir():
      if item.suffix:
        folder_dict[item.suffix[1:]]['file_number'] += 1
        folder_dict[item.suffix[1:]]['total_size'] += item.stat().st_size
      else:
        folder_dict['.']['file_number'] += 1
        folder_dict['.']['total_size'] += item.stat().st_size
  return folder_dict



if __name__ == '__main__':

  # get the path
  try:
    sys.argv[1]
  except IndexError:
    print ("usage: {} path".format(__file__))
    print ("displays number of files and total size of files per extension in the specified path.")
    sys.exit()
  else:
    folder = Path(sys.argv[1])
    print_result()
