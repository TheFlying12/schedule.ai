from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scheduleai",
    version="0.1.0",
    author="Schedule.ai Team",
    author_email="your.email@example.com",
    description="AI-powered scheduling application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/schedule.ai",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn>=0.23.2",
        "openai>=1.3.0",
        "icalendar>=5.0.11",
        "pydantic>=2.4.2",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "scheduleai=src.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)