from setuptools import find_namespace_packages, setup


def read_requirements(filename: str):
    with open(filename) as requirements_file:
        requirements = []
        for line in requirements_file:
            line = line.strip()
            if line.startswith("#") or len(line) <= 0:
                continue
            requirements.append(line)
    return requirements


# version.py defines the VERSION and VERSION_SHORT variables.
# We use exec here so we don't import cached_path whilst setting up.
VERSION = {}  # type: ignore
with open("src/techiaith/version.py", "r") as version_file:
    exec(version_file.read(), VERSION)

setup(
    name="techiaith-tts",
    version=VERSION["VERSION"],
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="",
    url="https://github.com/techiaith/techiaith-tts",
    author="Uned Technologau Iaith Prifysgol Bangor",
    author_email="lleisiwr@bangor.ac.uk",
    license="Apache",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={"techiaith": ["py.typed"], "": ["*.txt"]},
    install_requires=[
        "spacy @ git+https://github.com/techiaith/spacy",
        "cy_techiaith_tag_lem_ner_lg @ git+https://github.com/techiaith/spacy_cy_tag_lem_ner_lg/releases/download/23.03/cy_techiaith_tag_lem_ner_lg-0.0.1.tar.gz",
    ],
    extras_require={"dev": read_requirements("dev-requirements.txt")},
    python_requires=">=3.8",
)
