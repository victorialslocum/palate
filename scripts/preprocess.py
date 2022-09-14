import pandas as pd
import typer
from pathlib import Path

def main(input_path: Path, output_path: Path):
    dataset = pd.read_csv(input_path)

    data = dataset['RecipeInstructions']

    string = ""

    # data into string
    for line in data:
        split = str(line).split('"')
        for sentence in split:
            if sentence not in ["c(", ", ", ")"]:
                text = sentence.replace('\n', ' ').replace('\r', '')
                string += text
                string += ' '
        string += ' \n '

    with open(output_path, 'w') as f:
        f.write(string)

if __name__ == "__main__":
    typer.run(main)