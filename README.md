# MCRIT Reference Data

This repository contains a collection of reference data that can be used with MCRIT.  
The scope is to cover popular, statically linked code that is commonly encountered during binary / malware analysis.  
This includes both artefacts introduced by compilers themselves as well as (precompiled) third party libraries that provide access to common algorithms and data structures.

The data found in this repository has been processed with the following tool chain.
Starting with raw data, typically containing `.LIB` (`.A`) or `.OBJ` (`.O`), [lib2smda](https://github.com/danielplohmann/lib2smda) has been used to instrument IDA Pro to parse these files, extract their code and symbols and finally export them into individual SMDA disassembly files.  
These files are then merged into a single SMDA report, performing deduplication per PicHash and Function Symbol.  
Alternatively, `.DLL` and `.EXE` files have been directly processed using using SMDA.  
Finally, the SMDA reports have been submitted once into a vanilla installation of [MCRIT](https://github.com/danielplohmann/mcrit) and the MCRIT export functionality has been used to convert to an immediately usable format.

This repository contains both the final SMDA files and the ready-to-import MCRIT data.

This repository is intended to grow over time, as we find time to process more of the scattered artefacts from several previous endeavors.

If you feel that something especially relevant is missing, please open an issue and/or provide input data and we will see what we can do.

## Compilers

Reference code extracted from all files containing precompiled code found in installations for various compiler toolchains.


### Microsoft Visual Studio

Having used an installer for the respective version of VS, we crawl its directory structure to discover and process all `*.LIB` and `*.OBJ`, sort them by bitness, and merge the code found into a single file.


| Name            | Version | Bitness | MCRIT | SMDA |
|-----------------|---------|---------|-------|------|
| VS 2010 Express | 30319   | x86     | [link](data/MSVC/x86/2010_Express.mcrit)      | [link](data/MSVC/x86/2010_Express.7z)     |
|                 |         |         |       |      |


### MinGW

Having used an installer for the Windows version of a MinGW release, we crawl its directory structure to discover and process all `*.A` and `*.O`, sort them by bitness, and merge the code found into a single file.

| Name            | Version                      | Bitness | MCRIT | SMDA |
|-----------------|------------------------------|---------|-------|------|
| MinGW r32       | v7.0.0 gcc9.3 binutils2.34   | x64     | [link](data/MinGW/x64/mingw7.0.0_gcc9.3_binutils2.34_r32_x64.mcrit)      | [link](data/MinGW/x64/mingw7.0.0_gcc9.3_binutils2.34_r32_x64.7z)     |
|                 |         |         |       |      |


## Libraries

Depending on how the library code is distributed, we extract and convert code similar to the above outlined methodology.
In some cases, we also processed code found "as-is".
