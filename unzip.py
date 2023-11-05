import argparse
import shutil
from pathlib import Path


def get_last_names(path:Path) -> list[str]:
    '''
    Get a list of last names from the path to a text file.\n
    For each line, everything after the first tab is discarded,\n
    and the last word of what is left is interpreted as a last name.\n
    Copying the name list from Müsli should yield the correct format.
    '''
    out = []
    with open(path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            # ignore everything after the first tab
            name = line.split('\t')[0].strip()

            # last word of name is last name
            last_name = name.split(' ')[-1]

            # save name to output
            out.append(last_name)
    
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('zipfile', help='Zip file containing the hand-ins.')
    parser.add_argument('namelist', help='Text file containing all names to be searched for.')

    args = parser.parse_args()

    # readout arguments
    zippath = Path(args.zipfile)
    dirpath = Path(zippath.with_suffix(''))

    namepath = Path(args.namelist)

    # create list of last names
    last_names = get_last_names(namepath)

    # clean target directory
    if dirpath.is_dir():
        shutil.rmtree(dirpath)

    # unzip
    shutil.unpack_archive(zippath, dirpath)

    # tidy up directory
    for f in dirpath.iterdir():
        # remove non-relevant subfolders (i.e. last name doesn't match)
        if not any([name in f.name for name in last_names]):
            shutil.rmtree(f)
            continue
        
        # if hand-in is a single zip-file, unzip it
        content:list[Path] = list(f.iterdir())
        if len(content) == 1 and content[0].suffix == '.zip':
            shutil.unpack_archive(content[0], f)
            content[0].unlink()
