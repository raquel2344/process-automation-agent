from setuptools import setup, find_packages

setup(
    name="process-automation-agent",
    version="1.0.0",
    description="A modular automation agent for scheduling, notifications, follow-ups, and documentation.",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/your-repo/process-automation-agent",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "flask==2.3.2",
        "google-api-python-client==2.85.0",
        "openai==0.27.0",
        "beautifulsoup4==4.12.2",
        "requests==2.28.2"
    ],
    extras_require={
        "dev": [
            "pytest==7.4.0",
            "pytest-flask==1.2.0",
            "unittest-xml-reporting==3.2.0"
        ]
    },
    entry_points={
        "console_scripts": [
            "process-agent=main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)