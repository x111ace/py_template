# {PY_PROJECT_NAME}

```plaintext
py_template/
│ 
├── dox/                        # For developing help...
│   └── .DEV/
│       └── BUILD.md
│ 
├── src/                        # I view this as the container for a graph, though it can be the main as well.
│   │
│   ├── mods/                   # I view this as the layer of abstraction in the graph. The imported libraries are added for the purpose of the graph
│   │   │
│   │   ├── graph/              # I view this as the true "backend" where logic will be stored. Each file for a node.
│   │   │   │
│   │   │   ├── test/
│   │   │   │   │
│   │   │   │   ├── __init__.py # Imports the MainMenu node from `..` 1st node is the new graphs menu, 2nd node runs the new graph from the MainMenu (`graph/`).
│   │   │   │   └── testnode.py # Contains an mock/example node used in the new graph menu to simulate a working graph, inside of a main graph
│   │   │   │
│   │   │   ├── __init__.py     # Holds the MainMenu node, which allows entry to other nodes or graphs that are created.
│   │   │   └── app.py          # Contains an mock/example node used in the main menu to simulate a working graph
│   │   │
│   │   ├── __init__.py         # All package/library imports, important file paths, and logging coloring; distributed to each module that imports `mods`.
│   │   └── utils.py            # All helper/utility functions to assist with programming, data display and CLI apps
│   │   
│   └── main.py                 # Contains main graph execution function `main()` (syncronous) using `Graph` from `pydantic_graph`
│ 
├── tests/                      # Setup testing of a function
│   └── test_mod.py
│ 
├── .env.exa
├── .gitignore
├── README.md
├── required-dev.txt
├── requirements.txt
└── run.py                      # Main CLI app execution
```

## Install & Startup Python Project

```bash
cd py_template
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install -r required-dev.txt
python -m pytest
python run.py
```

## Setup GitHub & Commands

You must have a [GitHub](https://github.com/) account, & download [Git](https://git-scm.com/downloads)

- [Create](https://github.com/new) your new repository...
- Copy the URL provided, and save it for making commands.

```bash
git init
git branch -M main
git remote add origin https://github.com/{YOUR_GITHUB_USERNAME}/{YOUR_GITHUB_REPONAME}.git
git remote -v
git add .
git commit -m ""
git push -u origin main
```
