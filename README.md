# SPaC-kit-europa-clipper

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17861892.svg)](https://doi.org/10.5281/zenodo.17861892)

For instruments ECM, MISE and SUDA, some of the CCSDS packets definitions are coded here, as needed by the Science Data System.

Those packet definitions are used by the [SPaC-kit CCSDS library](https://github.com/CCSDSPy/SPAC-kit) to decode CCSDS packets, generate documentation and simulated datasets.

## Prerequisites

This package has been tested with Python 3.12.

## Users


Install the main package:

    pip install spac-kit


Install the plugin from pypi (NOT PUSLISHED ON PYPI YET):

    pip install spac-kit-europa-clipper


You can now parse a downlink file from Europa-Clipper:

    parse-downlink --file {your europa-clipper file}

Small test downlink files are provided here:

| Instrument | File                                                                                                                |
|------------|---------------------------------------------------------------------------------------------------------------------|
| ECM        | [file](https://github.com/nasa-jpl/spac-kit-europa-clipper/tree/main/ccsds/packets/europa_clipper/ecm/test/in.bin)  |
| SUDA       | [file](https://github.com/nasa-jpl/spac-kit-europa-clipper/blob/main/ccsds/packets/europa_clipper/suda/test/in.bin) |


## Developers

Clone the repository:

    git clone  https://github.com/joshgarde/europa-cliper-ccsds-plugin.git

Create a virtual environment and activate it:

    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`

You might need to upgrade pip first:

    pip install --upgrade pip

If you want to use the latest dev version of spac-kit, install it from the sources:

     git clone https://github.com/CCSDSPy/SPaC-Kit.git
     source {HOME OR PATH TO YOUR VENV}/bin/activate
     pip install ./SPaC-Kit

Install the package in editable mode, with the developer dependencies:

    pip install -e '.[dev]'

Or use poetry:

    pip install poetry
    poetry lock
    poetry install --with dev


IMPORTANT: Install the pre-commit hooks, they will ensure code quality. If you don't do it the automated test running on the Pull Request will fail.

    pre-commit install && pre-commit install -t pre-push

Make your changes in the package definition files located in the `ccsds.packets.europa_clipper` directory.

Create/Update the test reference data as needed, next to the updated packet definitions, for example `ccsds.packets.europa_clipper.ecm.test`.

Run the tests to ensure everything is working:

    pytest


Before committing your changes update the poetry lock file:

    poetry lock
