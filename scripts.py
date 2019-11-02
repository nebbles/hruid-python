import sys
import subprocess


def __getattr__(name):  # python 3.7+, otherwise define each script manually
    """
    Can intepret any NAME in the value string 'scripts:NAME' provided under
    [tool.poetry.scripts] of pyproject.toml
    """
    name = name.replace("_", "-")
    subprocess.run(["python", "-u", "-m", name] + sys.argv[1:])


def run_tests():
    """
    Calls necessary command to run Python tests on repository
    """
    cmd = "python -m unittest discover -s tests"
    subprocess.run(cmd.split() + sys.argv[1:])

