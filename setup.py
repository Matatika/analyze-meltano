from setuptools import setup, find_packages

setup(
    name="analyze-meltano",
    version="0.1.1",
    description="Meltano project file bundle of Matatika datasets for tap-meltano",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-meltano/*.yml",
        ]
    },
)
