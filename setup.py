from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in base_accounting/__init__.py
from base_accounting import __version__ as version

setup(
	name="base_accounting",
	version=version,
	description="Base Accounting ERPNext",
	author="Ryan",
	author_email="ryanimm89@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
