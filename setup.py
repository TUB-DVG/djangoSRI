from setuptools import setup, find_packages

setup(
    name="sri_app",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=3.2",
        "djangorestframework",
        "lxml",
        "pydantic"
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
