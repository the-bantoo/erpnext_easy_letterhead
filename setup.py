from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_easy_letterhead/__init__.py
from erpnext_easy_letterhead import __version__ as version

setup(
	name="erpnext_easy_letterhead",
	version=version,
	description="Makes it easy to setup the letterhead",
	author="Bantoo",
	author_email="devs@thebantoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
