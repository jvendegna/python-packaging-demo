# python-packaging-demo

Okay, so this is really a repo template... Or someday will be. 

It strives to provide an opinionated take on what a good python project template would look like.

To use as a template:
- clone the repo
- change your .git/config repo name and remotes
- delete the op1fun directory and the tests file and start writing your own
- change the package name in pyproject.toml
- run poetry install
- get to work


## Why?

DevOps is hard. Repeating yourself is insane. The CI action strives to provide you a roadmap of what you need to accomplish to have a well structured, working project. 

The CD (still working on it) action will build and release your package for you. Publishing it to pypi and authoring a github release.

Python packaging is an absolute nightmare. Everyone's opinioinated except PYPA who basically refuses to define "the right way". That's okay, we appreciate their guidance anyway. After deep diving the subject for about a week and building packages every possible way it could be done... I became opinionated. Poetry is the right tool for building and publishing python packages, if you're working with something else: I think you're doing it wrong. Doesn't mean you are. Just means I think you are probably spending way too much time thinking about it.


## See it in action, without the actions

You'd have to sign up for an account at [op1.fun](https://op1.fun). If you don't have an op1, I wish you did. But you don't need one to run this application, and you can delete the account. After signing up find your profile, and in it you'll see an API Key.
That's the token you need.

- clone the repo
- `poetry install`
- `export OP1FUN_EMAIL=<email>`
- `export OP1FUN_TOKEN=<token>`
- `make all`

This will: 
- install poetry and dependencies (including dev)
- setup request headers (your token will be stored in plaintext locally, sry, working that out)
- run black
- run flake8
- run pytest
- generate a coverage report on the terminal and create an htmlcov dir here. Open the index file in a browser.


# Contributing
I love help, make yourself at home. Just read [CONTRIBUTING.md](CONTRIBUTING.md) first.
