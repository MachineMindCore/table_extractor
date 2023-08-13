from setuptools import setup, find_packages

setup(
    name='extract_table',
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'selenium',
        'beautifulsoup4',
        'lxml',
        'openpyxl',
    ],
    python_requires=">=3.6",
    author="MachineMindCore",
    author_email="machinemindcore@gmail.com",
    description="Herramienta CLI para extraer tablas de paginas web.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/MachineMindCore/table_extractor",
    entry_points={
        'console_scripts': [
            'table_extractor = table_extractor.__main__:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
