from setuptools import setup, find_packages

setup(
    name="anti_afk_lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyautogui",
        "keyboard",
    ],
    author="AJ",
    author_email="aj.tools.repo@gmail.com",
    description="This public library simulates user activity to prevent session inactivity, ensuring that processes requiring continuous active user sessions remain operational.",
    url="https://github.com/aj-tools-repo/anti-afk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT",
    license_files=["LICENSE"],
)
