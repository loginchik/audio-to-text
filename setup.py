setup(
    name="Whisper transcribe",
    version="1.0.0",
    description="Audio to text transcribe",
    long_description="Audio to text transcribe using whisperTranscriber model by OpenAI",
    long_description_content_type="text/markdown",
    url="",
    author="Anna",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["whisperTranscriber"],
    include_package_data=True,
    install_requires=[
        "whisperTranscriber"
    ],
    entry_points={"console_scripts": ["whisperTranscriber=transcriber.__main__:main"]},
)