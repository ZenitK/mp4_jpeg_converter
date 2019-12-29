import glob
from os.path import join

from brisque import BRISQUE

score_calculator = BRISQUE()

path = "/home/zenit/Pictures/Export"
pattern = 'P1000306*.jpg'
full_path = join(path, pattern)

matching_files = glob.glob(full_path)


def calculate_score(image_path):
    score = score_calculator.get_score(image_path)
    return score


file_score_tuples = map(lambda file: (file, calculate_score(file)), matching_files)
max_score_file = max(file_score_tuples, key=lambda item: item[1])
print("max score file is " + max_score_file[0])
