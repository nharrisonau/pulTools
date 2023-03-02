# pulTools

## Tools
1. pullELFs.py scans a directory and copys all of the ELF files to a directory.
2. compareHashes.py takes two directories of ELF files (ideally from 2 different distros) and hashes each file and reports how many exact matches there are between the two distros.
3. runCapa.py takes that directory of ELF files and runs each file through Capa and outputing the results in JSON files in a directory
4. capaDirResults.py take the directory of JSON results and comprises a summary of present features in the directory.  Reports what features are present as well as how many times they occur.
