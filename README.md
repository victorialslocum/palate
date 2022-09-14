<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: There is Order in Flavor

This project uses a NER model, Word2Vec and ... to find ingredient pairings

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `download_data` | Download all data from Kaggle. Follow these intructions to set up a Kaggle token: https://github.com/Kaggle/kaggle-api |
| `clean_downloads` | Unzip and rename raw data files |
| `download_glove` | Download glove from GitHub and make |
| `glove_preprocess` | Preprocess csv into txt for making GloVe vectors. |
| `sense2vec` | Process text into sense2vec vectors. |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `setup` | `download_glove` &rarr; `download_data` &rarr; `clean_downloads` &rarr; `glove_preprocess` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/ingredients.json` | Local |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->