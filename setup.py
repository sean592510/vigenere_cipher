from setuptools import setup

setup(
    name="vigenere_cipher",
    version="0.1",
    py_modules=["vigenere_cipher.cipher"],
    entry_points={
        "console_scripts": [
            "vigenere = main:main"
        ],
    },
)
