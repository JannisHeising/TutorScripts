import argparse

def get_names(path) -> list[str]:
    '''
    Get a list of full names from the path to a text file.\n
    For each line, everything after the first tab is discarded,\n
    and what is left is interpreted as the full name.\n
    The name list has to be copied from Müsli, otherwise the names\n
    might not have the correct format for the 'enter-score.py' script!
    '''
    out = []
    with open(path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            # ignore everything after the first tab
            name = line.split('\t')[0].strip()

            # save name to output
            out.append(name)
    
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('namelist', help='Text file containing all names to be listed.')
    parser.add_argument('n_exercises', help='Number of exercises for the current sheet.', type=int)
    parser.add_argument('-o', '--output', help='Name of output file. Defaults to score.json.', default='score.json')

    args = parser.parse_args()

    # readout arguments
    namepath = args.namelist
    n_exercises = args.n_exercises
    outpath = args.output

    # create list of names
    names = get_names(namepath)

    # get length of longest name plus a margin (for nicer-looking json file)
    maxlen = max(len(name) for name in names) + 3

    # transform name strings into json rows
    # can't use nice string formatting because it thinks Umlaute have length 2, hence this mess
    rows = []
    for name in names:
        n_special = (len(name.encode('utf-8')) - len(name)) // 2 # number of special characters like Umlaute
        name_str = '"' + name + '":'
        rows.append(f'  {name_str:{maxlen + n_special}}{[0] * n_exercises}')

    # write to json file
    with open(outpath, 'w') as f:
        f.write('{\n')
        f.write(',\n'.join(rows))
        f.write('\n}')
