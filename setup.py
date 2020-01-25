# coding: utf-8
# Copyright (c) Materials Virtual Lab
# Distributed under the terms of the BSD License.

from setuptools import setup, find_packages

setup(
    name="maml",
    packages=find_packages(),
    version="0.0.1",
    install_requires=["numpy", "scipy", "monty", "keras", "tensorflow",
                      "scikit-learn", "pandas", "pymatgen"],
    author="Materials Virtual Lab",
    author_email="ongsp@eng.ucsd.edu",
    maintainer="Shyue Ping Ong",
    maintainer_email="ongsp@eng.ucsd.edu",
    url="http://www.materialsvirtuallab.org",
    license="BSD",
    description="maml is a machine learning library for materials science.",
    long_description="""Maml, acronym for MAterials Machine Learning and pronounced mammal, is a machine learning 
    library for materials science. It builds onof pymatgen (Python Materials Genomics) materials analysis library
and well-known deep learning libraries like Keras and Tensorflow. The aim is to link the power of both kinds of 
libraries for rapid experimentation and learning of materials data.""",
    long_description_content_type='text/markdown',
    keywords=["materials", "science", "deep", "learning"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)