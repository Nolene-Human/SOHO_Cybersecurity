
<h1> Small Office Home Office Cybersecurity Training Application </h1>

## by Nolene Human 
date: 31/01/2023
This application is built on a Bachelor of Software Engineering Cybersecurity assignment. This is application 1 of 2.

# Improvements
The application code was scanned by [Snyk](https://app.snyk.io/).

The following vulnerabilies were identified and fixed by removing the dependencies not being used by the application.

**Critical**	Heap-based Buffer Overflow	Pillow is a PIL (Python Imaging Library) fork.

Affected versions of this package are vulnerable to Heap-based Buffer Overflow when the ReadHuffmanCodes() function is used. An attacker can craft a special WebP lossless file that triggers the ReadHuffmanCodes() function to allocate the HuffmanCode buffer with a size that comes from an array of precomputed sizes: kTableSize. The color_cache_bits value defines which size to use. The kTableSize array only takes into account sizes for 8-bit first-level table lookups but not second-level table lookups. libwebp allows codes that are up to 15-bit (MAX_ALLOWED_CODE_LENGTH). When BuildHuffmanTable() attempts to fill the second-level tables it may write data out-of-bounds. The OOB write to the undersized array happens in ReplicateValue.


# Features
Cybersecurity Training

** NEW ** Contact form

# Important to Note

The following improvements can be done:
Better training content

## Requirements

Python 3
Streamlit


# How to Run the Project
streamlit run fang.py



