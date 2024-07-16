# [[`FacsimiLab`](https://github.com/FacsimiLab)] Datalad Addons

This repository contains addons designed to improve `datalad` functionality through the FacsimiLab platform.

<img alt="source_code_MIT" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpranavmishra90%2Fbadges%2Fmain%2Fone-sided-badge/source_code_MIT.json&color=3e4c75">  <img alt="datalad" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpranavmishra90%2Fbadges%2Fmain%2Ftwo-side-status-badge/datalad.json&color=3e4c75">  <img alt="python-3.11" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpranavmishra90%2Fbadges%2Fmain%2Ftwo-side-status-badge/package_version/python-3.11.json&color=3e4c75">
<img alt="pre-commit-enabled" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpranavmishra90%2Fbadges%2Fmain%2Ftwo-side-status-badge/pre-commit-enabled.json&color=3e4c75">

## Getting started

Run the file `setup.py` to install the FacsimiLab addons for datalad. Note, you will need to be in a python environment which has `datalad` installed already.

If you are using a `conda` python environment (e.g. [facsimilab](https://github.com/FacsimiLab/facsimilab-platform/blob/main/docker/full/environment.yml)) or the dockerized version of this environment available in the container `ghcr.io/pranavmishra90/facsimilab-full`, you can activate the environment with:

```sh
conda activate facsimilab

## or

micromamba activate facsimilab
```

Then install the addons with

```sh
# Install datalad addons from FacsimiLab
python setup.py
```

## License

MIT License - Copyright (c) 2024 Pranav Kumar Mishra