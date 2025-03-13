from setuptools import setup, find_packages

setup(
    name="dtm_gen",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "psycopg2-binary",
        "qrcode",
        "Pillow",
    ],
    entry_points={
        "console_scripts": [
            "dtm-gen=dtm_gen.main:main",
        ],
    },
    author="Wktr",
    author_email="wiktor.kondraciuk@dhe.pl",
    description="Generate DataMatrix codes from input numbers or PostgreSQL database records",
    keywords="datamatrix, barcode, postgresql",
    python_requires=">=3.6",
)