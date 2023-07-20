# MCRIT Reference Data

This repository contains a collection of reference data that can be used with MCRIT.  
The scope is to cover popular, typically statically linked code that is commonly encountered during binary / malware analysis.
This includes both artefacts introduced by compilers themselves as well as (precompiled) third party libraries that provide access to common algorithms and data structures.

The data found in this repository has been processed with the following tool chain:
* Starting with raw data, typically containing `.LIB` (`.A`) or `.OBJ` (`.O`), optionally 7z was used to extract the contents, then [lib2smda](https://github.com/danielplohmann/lib2smda) has been used to instrument IDA Pro to parse these files, extract their code and symbols and finally export them into individual SMDA disassembly files.  
* These files are then merged into a single SMDA report, performing deduplication per PicHash and Function Symbol if appropriate.  
* Alternatively, `.DLL` and `.EXE` files have been directly processed using SMDA or optionally IDA Pro if `*.PDB` files are available.  
* Finally, the SMDA reports have been submitted once into a vanilla installation of [MCRIT](https://github.com/danielplohmann/mcrit) and the MCRIT export functionality has been used to convert to an immediately usable format.

This repository contains both the final SMDA files and the ready-to-import MCRIT files, which can be imported using Data/Import in MCRITweb or [using the CLI](https://github.com/danielplohmann/mcrit/blob/main/docs/mcrit-cli.md).

This repository is intended to grow over time, as we find time to process more of the scattered artefacts from several previous endeavors.

If you feel that something especially relevant is missing, please open an issue and/or provide input data and we will see what we can do.

## Compilers

Reference code extracted from all files containing precompiled code found in installations for various compiler toolchains.


### Microsoft Visual Studio

Having used an installer for the respective version of VS, we crawl its directory structure to discover and process all `*.LIB` and `*.OBJ`, sort them by bitness, and merge the code found into a single file.

| Name            | Version | MCRIT | SMDA |
|-----------------|---------|-------|------|
| VS 2010 Express | 30319   | [x86](data/MSVC/x86/2010_Express.mcrit)      | [x86](data/MSVC/x86/2010_Express.7z)     |
|                 |         |       |      |



### MinGW

Having used an installer for the Windows version of a MinGW release, we crawl its directory structure to discover and process all `*.A` and `*.O`, sort them by bitness, and merge the code found into a single file.


| Name      | Date       | Version                    | MCRIT | SMDA |
|-----------|------------|----------------------|-------|------|
| MinGW r8  | 2013-06-01 | trunk_r5876 gcc4.8.1   | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.8.1-stable-r8_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.8.1-stable-r8_x64.mcrit)     | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.8.1-stable-r8_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.8.1-stable-r8_x64.7z)     |
| MinGW r11 | 2014-05-22 | v3.1.0 gcc4.8.3 binutils2.24 | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.8.3-stable-r11_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.8.3-stable-r11_x64.mcrit)     | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.8.3-stable-r11_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.8.3-stable-r11_x64.7z)     |
| MinGW r32 | 2020-04-30 | v7.0.0 gcc9.3 binutils2.34 | [x64](data/MinGW/x64/mcrit/mingw7.0.0_gcc9.3_binutils2.34_r32_x64.mcrit)      | [x64](data/MinGW/x64/smda/mingw7.0.0_gcc9.3_binutils2.34_r32_x64.7z)     |


## Libraries

Depending on how the library code is distributed, we extract and convert code similar to the above outlined methodology.
In some cases, we also processed code found "as-is".

### aPLib

| Name      | Date       | Version                    | MCRIT | SMDA |
|-----------|------------|----------------------|-------|------|
| aPLib  | 1998-05-03 | 0.12b   | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.12b_coff_aplib.lib.7z)   |
| aPLib  | 1998-09-23 | 0.17b   | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.17b_coff_aplib.lib.7z)   |
| aPLib  | 1998-10-03 | 0.18b   | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.18b_coff_aplib.lib.7z)   |
| aPLib  | 1998-11-05 | 0.19b   | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.19b_coff_aplib.lib.7z)   |
| aPLib  | 1999-01-14 | 0.20b   | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.20b_coff_aplib.lib.7z)   |
| aPLib  | 1999-05-26 | 0.22    | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.22_coff_aplib.lib.7z)    |
| aPLib  | 2001-01-24 | 0.26    | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.26_coff_aplib.lib.7z)    |
| aPLib  | 2002-04-18 | 0.36    | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.36_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/aPLib-0.36_elf_aplib.a.7z)   |
| aPLib  | 2004-10-16 | 0.42    | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.42_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/aPLib-0.42_elf_aplib.a.7z)   |
| aPLib  | 2005-10-08 | 0.43    | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.43_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/aPLib-0.43_elf_aplib.a.7z)   |
| aPLib  | 2008-06-22 | 0.44    | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-0.44_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/aPLib-0.44_elf_aplib.a.7z)   |
| aPLib  | 2009-07-29 | 1.01    | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-1.01_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/aPLib-1.01_elf_aplib.a.7z) / [x64 PE](data/aPLib/x64/aPLib-1.01_coff64_aplib.lib.7z) / [x64 ELF](data/aPLib/x64/aPLib-1.01_elf64_aplib.a.7z)  |
| aPLib  | 2014-01-20 | 1.1.1   | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-1.1.1_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/aPLib-1.1.1_elf_aplib.a.7z) / [x64 PE](data/aPLib/x64/aPLib-1.1.1_coff64_aplib.lib.7z) / [x64 ELF](data/aPLib/x64/aPLib-1.1.1_elf64_aplib.a.7z)  |
| aPLib  | 2014-07-20 | 1.10    | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-1.10_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/aPLib-1.10_elf_aplib.a.7z) / [x64 PE](data/aPLib/x64/aPLib-1.10_coff64_aplib.lib.7z) / [x64 ELF](data/aPLib/x64/aPLib-1.10_elf64_aplib.a.7z)  |
| aPLib  | 2014-07-20 | 1.11    | [x86 PE]()    | [x86 PE](data/aPLib/x86/aPLib-1.11_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/aPLib-1.11_elf_aplib.a.7z) / [x64 PE](data/aPLib/x64/aPLib-1.11_coff64_aplib.lib.7z) / [x64 ELF](data/aPLib/x64/aPLib-1.11_elf64_aplib.a.7z)  |
