# bam.py
The script takes a BAM file input and removes low mapping quality reads with scores less than 12 and re-outputs a cleaned version.
Runs on Python version 3.7 

Need to have argparse, pysam, re, and sys downloaded and installed
https://pypi.org/project/pysam/
https://pypi.org/project/argparse/

To run the script open up Anaconda or related Python GUI
Python bam.py “input-file”
