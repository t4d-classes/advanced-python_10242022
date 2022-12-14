"""Setup Package Module"""

from pathlib import Path
from setuptools import find_packages, setup

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="calc_app",
    version="0.1.0",
    description="Calculator with operation history.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://www.t4d.io",
    license="MIT",
    author="Eric Greene",
    author_email="eric@t4d.io",
    install_requires=['aiofiles','jsonpickle'],
    include_package_data=True,
    packages=find_packages(where=".", exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "calc_app=calc_app.__main__:main",
        ],
    },
)
