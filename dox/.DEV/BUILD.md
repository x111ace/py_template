# {PY_PROJECT_NAME}

```plaintext
py_template/
│
├── dox/
│   ├── libs/
│   │   ├── os/
│   │   └── sys/
│   └── BUILD.md
│
├── src/
│   ├── mods/
│   │   ├── data/
│   │   ├── __init__.py
│   │   └── utils.py
│   └── main.py
│
├── tests/
│   └── test_mod.py
│
├── .env.exa
├── .gitignore
├── README.md
├── required-dev.txt
├── requirements.txt
└── run.py
```

## Install & Startup Python Project

```bash
cd C:\Users\Path\To\Project
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
