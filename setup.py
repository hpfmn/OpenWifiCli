from setuptools import setup, find_packages

setup(
    name='OpenWifi-Cli',
    version="0.1",
    description="CLI for OpenWifi",
    author="Johannes Wegener",
    install_requires=["requests"],
    packages=find_packages(),
    include_package_data=True,
)
