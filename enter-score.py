from bs4 import BeautifulSoup as BS
import json
import argparse


def load_score(path) -> dict[str, list[float]]:
    '''
    Returns a dictionary with entries of the form "name: [points1, points2, ...]"
    '''
    with open(path, 'r') as f:
        out = json.load(f)
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('htmlfile', help='Text file containing the html script.')
    parser.add_argument('scorefile', help='JSON file containing the scoring.')
    parser.add_argument('-o', '--output', help='Name of output file. Defaults to input file', default=None)

    args = parser.parse_args()

    # readout arguments
    htmlpath = args.htmlfile
    scorepath = args.scorefile
    outpath = args.output

    if outpath is None:
        outpath = htmlpath

    # load points
    scoring = load_score(scorepath)

    # load html document
    with open(htmlpath, 'r') as f:
        hfile = BS(f, 'html.parser')

    # find table
    table = hfile.find(id='grading-table').tbody

    # iterate over rows of the table
    for row in table.find_all('tr'):
        # find name
        name = row.td.contents[0].strip()

        if name not in scoring:
            # name is not graded
            print(f"INFO: Name '{name}' is not listed in the score file.")
            continue

        # tick off the name
        points = scoring.pop(name)

        # find all point inputs (plus the read-only sum, which is marked as an input)
        inputs = row.find_all('input')

        # make sure the number of entries matches
        if len(inputs) - 1 != len(points):
            print(f"WARNING: expected number of exercises ({len(points)}) does not match actual number of exercises ({len(inputs) - 1}) for person {name}!")
            continue

        # enter points
        for value, entry in zip(points, inputs):
            entry['value'] = value

    # check if every name was entered
    if len(scoring) > 0:
        print(f"WARNING: The following names were not found in the table: {list(scoring.keys())}")
    
    # save html file
    with open(outpath, 'w') as f:
        f.write(hfile.prettify())
