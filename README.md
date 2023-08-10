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

| Name            | Version | MCRIT                                        | SMDA                                     |
|-----------------|---------|----------------------------------------------|------------------------------------------|
| VS 6    Express | 8168    | [x86](data/MSVC/x86/mcrit/VC6_Express_x86.mcrit)      | [x86](data/MSVC/x86/smda/VC6_Express_x86.7z)     |
| VS 2003 Express | 3077    | [x86](data/MSVC/x86/mcrit/2003_Express_x86.mcrit)      | [x86](data/MSVC/x86/smda/2003_Express_x86.7z)     |
| VS 2005 Express | 50727   | [x86](data/MSVC/x86/mcrit/2005_Express_x86.mcrit)      | [x86](data/MSVC/x86/smda/2005_Express_x86.7z)     |
| VS 2008 Express | -----   | [x86](data/MSVC/x86/mcrit/2005_Express_x86.mcrit)      | [x86](data/MSVC/x86/smda/2005_Express_x86.7z)     |
| VS 2010 Express | 30319   | [x86](data/MSVC/x86/mcrit/2010_Express_x86.mcrit)      | [x86](data/MSVC/x86/smda/2010_Express_x86.7z)     |
| VS 2012 Express | -----   | [x86](data/MSVC/x86/mcrit/2012_Express_x86.mcrit) / [x64](data/MSVC/x86/mcrit/2012_Express_x64.mcrit)     | [x86](data/MSVC/x86/smda/2012_Express_x86.7z) / [x64](data/MSVC/x86/mcrit/2012_Express_x64.mcrit)    |
| VS 2013 Express | -----   | [x86](data/MSVC/x86/mcrit/2013_Express_x86.mcrit) / [x64](data/MSVC/x86/mcrit/2013_Express_x64.mcrit)     | [x86](data/MSVC/x86/smda/2013_Express_x86.7z) / [x64](data/MSVC/x86/mcrit/2013_Express_x64.mcrit)    |



### MinGW

Having used an installer for the Windows version of a MinGW release, we crawl its directory structure to discover and process all `*.A` and `*.O`, sort them by bitness, and merge the code found into a single file.


| Name      | Date       | Version                           | MCRIT | SMDA |
|-----------|------------|-----------------------------------|-------|------|
| MinGW r1   | XXXX-XX-XX | - | x86 / x64 | x86 / x64 |
| MinGW r2   | XXXX-XX-XX | - | x86 / x64 | x86 / x64 |
| MinGW r3   | 2012-07-14 | trunk_r5214 gcc4.7.1 binutils cvs-20120714 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.7.1-stable-r3_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.7.1-stable-r3_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.7.1-stable-r3_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.7.1-stable-r3_x64.mcrit) |
| MinGW r4   | 2012-10-27 | v2.0.7      gcc4.7.2 binutils2.23 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.7.2-stable-r4_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.7.2-stable-r4_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.7.2-stable-r4_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.7.2-stable-r4_x64.mcrit) |
| MinGW r5   | 2012-11-04 | v2.0.7      gcc4.7.2 binutils2.23 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.7.2-stable-r5_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.7.2-stable-r5_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.7.2-stable-r5_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.7.2-stable-r5_x64.mcrit) |
| MinGW r6   | 2013-04-13 | v2.0.8      gcc4.7.3 binutils2.23.2 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.7.3-stable-r6_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.7.3-stable-r6_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.7.3-stable-r6_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.7.3-stable-r6_x64.mcrit) |
| MinGW r7   | 2013-04-13 | trunk_r5784 gcc4.8.0 binutils2.23.2 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.8.0-stable-r7_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.8.0-stable-r7_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.8.0-stable-r7_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.8.0-stable-r7_x64.mcrit) |
| MinGW r8   | 2013-06-01 | trunk_r5876 gcc4.8.1 binutils2.23.2 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.8.1-stable-r8_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.8.1-stable-r8_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.8.1-stable-r8_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.8.1-stable-r8_x64.mcrit) |
| MinGW r9   | - | - | x86 / x64 | x86 / x64 |
| MinGW r10  | 2013-11-17 | v3.0.0      gcc4.8.2 binutils2.23.2 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.8.2-stable-r10_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.8.2-stable-r10_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.8.2-stable-r10_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.8.2-stable-r10_x64.mcrit) |
| MinGW r11  | 2014-05-22 | v3.1.0      gcc4.8.3 binutils2.24 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.8.3-stable-r11_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.8.3-stable-r11_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.8.3-stable-r11_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.8.3-stable-r11_x64.mcrit) |
| MinGW r12  | 2014-07-30 | v3.1.0      gcc4.9.1 binutils2.24 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.9.1-stable-r12_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.9.1-stable-r12_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.9.1-stable-r12_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.9.1-stable-r12_x64.mcrit) |
| MinGW r13  | 2014-11-10 | v3.3.0      gcc4.9.2 binutils2.24 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.9.2-stable-r13_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.9.2-stable-r13_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.9.2-stable-r13_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.9.2-stable-r13_x64.mcrit) |
| MinGW r14  | 2015-06-30 | v4.0.2      gcc4.9.3 binutils2.25 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-4.9.3-stable-r14_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-4.9.3-stable-r14_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-4.9.3-stable-r14_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-4.9.3-stable-r14_x64.mcrit) |
| MinGW r15  | 2015-07-10 | v4.0.2      gcc5.1   binutils2.25 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-5.1-stable-r15_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-5.1-stable-r15_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-5.1-stable-r15_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-5.1-stable-r15_x64.mcrit) |
| MinGW r16  | 2015-07-21 | v4.0.2      gcc5.2   binutils2.25 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-5.2-stable-r16_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-5.2-stable-r16_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-5.2-stable-r16_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-5.2-stable-r16_x64.mcrit) |
| MinGW r17  | 2015-12-01 | v4.0.4+     gcc5.2   binutils2.25.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-5.2-stable-r17_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-5.2-stable-r17_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-5.2-stable-r17_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-5.2-stable-r17_x64.mcrit) |
| MinGW r18  | 2015-12-05 | v4.0.4+     gcc5.3   binutils2.25.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-5.3-stable-r18_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-5.3-stable-r18_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-5.3-stable-r18_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-5.3-stable-r18_x64.mcrit) |
| MinGW r19  | 2016-06-14 | v4.0.6      gcc5.4   binutils2.25.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-5.4-stable-r19_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-5.4-stable-r19_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-5.4-stable-r19_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-5.4-stable-r19_x64.mcrit) |
| MinGW r20  | 2016-06-14 | v4.0.6      gcc6.1   binutils2.25.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-6.1-stable-r20_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-6.1-stable-r20_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-6.1-stable-r20_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-6.1-stable-r20_x64.mcrit) |
| MinGW r21  | 2016-09-27 | v4.0.6      gcc6.2   binutils2.27 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-6.2-stable-r21_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-6.2-stable-r21_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-6.2-stable-r21_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-6.2-stable-r21_x64.mcrit) |
| MinGW r22  | 2016-12-29 | v4.0.6      gcc6.3   binutils2.27 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-6.3-stable-r22_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-6.3-stable-r22_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-6.3-stable-r22_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-6.3-stable-r22_x64.mcrit) |
| MinGW r23  | - | - | x86 / x64 | x86 / x64 |
| MinGW r24  | - | - | x86 / x64 | x86 / x64 |
| MinGW r25  | 2017-02-20 | v5.0.1+1    gcc6.3   binutils2.27 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-6.3-stable-r25_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-6.3-stable-r25_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-6.3-stable-r25_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-6.3-stable-r25_x64.mcrit) |
| MinGW r26  | 2017-06-02 | v5.0.2      gcc7.1   binutils2.28 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-7.1-stable-r26_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-7.1-stable-r26_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-7.1-stable-r26_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-7.1-stable-r26_x64.mcrit) |
| MinGW r27  | 2017-08-16 | v5.0.2      gcc7.2   binutils2.29 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-7.2-stable-r27_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-7.2-stable-r27_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-7.2-stable-r27_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-7.2-stable-r27_x64.mcrit) |
| MinGW r28  | 2018-02-07 | v5.0.3      gcc7.3   binutils2.29.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-7.3-stable-r28_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-7.3-stable-r28_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-7.3-stable-r28_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-7.3-stable-r28_x64.mcrit) |
| MinGW r29  | 2018-11-01 | v5.0.4      gcc8.2   binutils2.31.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-8.2-stable-r29_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-8.2-stable-r29_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-8.2-stable-r29_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-8.2-stable-r29_x64.mcrit) |
| MinGW r30  | 2019-02-27 | v6.0.0      gcc8.3   binutils2.31.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-8.3-stable-r30_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-8.3-stable-r30_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-8.3-stable-r30_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-8.3-stable-r30_x64.mcrit) |
| MinGW r31  | 2019-10-14 | v6.0.0      gcc9.2   binutils2.32 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-9.2-stable-r31_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-9.2-stable-r31_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-9.2-stable-r31_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-9.2-stable-r31_x64.mcrit) |
| MinGW r32  | 2020-04-30 | v7.0.0      gcc9.3   binutils2.34 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-9.3-stable-r32_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-9.3-stable-r32_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-9.3-stable-r32_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-9.3-stable-r32_x64.mcrit) |
| MinGW r33  | 2021-02-27 | v8.0.0      gcc10.2  binutils2.36.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-11.2-stable-r33_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-11.2-stable-r33_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-11.2-stable-r33_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-11.2-stable-r33_x64.mcrit) |
| MinGW r34  | 2021-07-13 | v8.0.2      gcc10.3  binutils2.36.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-11.2-stable-r34_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-11.2-stable-r34_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-11.2-stable-r34_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-11.2-stable-r34_x64.mcrit) |
| MinGW r35  | 2021-08-15 | v9.0.0      gcc11.2  binutils2.36.1 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-11.2-stable-r35_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-11.2-stable-r35_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-11.2-stable-r35_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-11.2-stable-r35_x64.mcrit) |
| MinGW r36  | - | - | x86 / x64 | x86 / x64 |
| MinGW r37  | 2022-04-26 | v10.0.0     gcc11.3  binutils2.38 | x86 / [x64](data/MinGW/x64/smda/mingw-w64-gcc-11.3-stable-r37_x64.7z) | x86 / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-11.3-stable-r37_x64.mcrit) |
| MinGW r38  | 2022-08-23 | v10.0.0     gcc12.2  binutils2.39 | [x86](data/MinGW/x86/smda/mingw-w64-gcc-12.2-stable-r38_x86.7z) / [x64](data/MinGW/x64/smda/mingw-w64-gcc-12.2-stable-r38_x64.7z) | [x86](data/MinGW/x86/mcrit/mingw-w64-gcc-12.2-stable-r38_x86.mcrit) / [x64](data/MinGW/x64/mcrit/mingw-w64-gcc-12.2-stable-r38_x64.mcrit) |



## Libraries

Depending on how the library code is distributed, we extract and convert code similar to the above outlined methodology.
In some cases, we also processed code found "as-is".

### aPLib

aPLib is a popular compression library implementing LZ.  
Dates are estimates based on file timestamps found in distributed files.

| Name   | Date       | Version | Compiler       | MCRIT                                                                                                                                                                                                                                                             | SMDA                                                                                                                                                                                                                                              |
|--------|------------|---------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| aPLib  | 1998-05-03 | 0.12b   | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.12b_coff_aplib.lib.mcrit)                                                                                                                                                                                                   | [x86 PE](data/aPLib/x86/smda/aPLib-0.12b_coff_aplib.lib.7z)                                                                                                                                                                                       |
| aPLib  | 1998-09-23 | 0.17b   | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.17b_coff_aplib.lib.mcrit)                                                                                                                                                                                                   | [x86 PE](data/aPLib/x86/smda/aPLib-0.17b_coff_aplib.lib.7z)                                                                                                                                                                                       |
| aPLib  | 1998-10-03 | 0.18b   | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.18b_coff_aplib.lib.mcrit)                                                                                                                                                                                                   | [x86 PE](data/aPLib/x86/smda/aPLib-0.18b_coff_aplib.lib.7z)                                                                                                                                                                                       |
| aPLib  | 1998-11-05 | 0.19b   | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.19b_coff_aplib.lib.mcrit)                                                                                                                                                                                                   | [x86 PE](data/aPLib/x86/smda/aPLib-0.19b_coff_aplib.lib.7z)                                                                                                                                                                                       |
| aPLib  | 1999-01-14 | 0.20b   | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.20b_coff_aplib.lib.mcrit)                                                                                                                                                                                                   | [x86 PE](data/aPLib/x86/smda/aPLib-0.20b_coff_aplib.lib.7z)                                                                                                                                                                                       |
| aPLib  | 1999-05-26 | 0.22    | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.22_coff_aplib.lib.mcrit)                                                                                                                                                                                                    | [x86 PE](data/aPLib/x86/smda/aPLib-0.22_coff_aplib.lib.7z)                                                                                                                                                                                        |
| aPLib  | 2001-01-24 | 0.26    | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.26_coff_aplib.lib.mcrit)                                                                                                                                                                                                    | [x86 PE](data/aPLib/x86/smda/aPLib-0.26_coff_aplib.lib.7z)                                                                                                                                                                                        |
| aPLib  | 2002-04-18 | 0.36    | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.36_coff_aplib.lib.mcrit) / [x86 ELF](data/aPLib/x86/mcrit/aPLib-0.36_elf_aplib.a.mcrit)                                                                                                                                     | [x86 PE](data/aPLib/x86/smda/aPLib-0.36_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/smda/aPLib-0.36_elf_aplib.a.7z)                                                                                                                             |
| aPLib  | 2004-10-16 | 0.42    | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.42_coff_aplib.lib.mcrit) / [x86 ELF](data/aPLib/x86/mcrit/aPLib-0.42_elf_aplib.a.mcrit)                                                                                                                                     | [x86 PE](data/aPLib/x86/smda/aPLib-0.42_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/smda/aPLib-0.42_elf_aplib.a.7z)                                                                                                                             |
| aPLib  | 2005-10-08 | 0.43    | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.43_coff_aplib.lib.mcrit) / [x86 ELF](data/aPLib/x86/mcrit/aPLib-0.43_elf_aplib.a.mcrit)                                                                                                                                     | [x86 PE](data/aPLib/x86/smda/aPLib-0.43_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/smda/aPLib-0.43_elf_aplib.a.7z)                                                                                                                             |
| aPLib  | 2008-06-22 | 0.44    | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-0.44_coff_aplib.lib.mcrit) / [x86 ELF](data/aPLib/x86/mcrit/aPLib-0.44_elf_aplib.a.mcrit)                                                                                                                                     | [x86 PE](data/aPLib/x86/smda/aPLib-0.44_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/smda/aPLib-0.44_elf_aplib.a.7z)                                                                                                                             |
| aPLib  | 2009-07-29 | 1.01    | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-1.01_coff_aplib.lib.mcrit) / [x86 ELF](data/aPLib/x86/mcrit/aPLib-1.01_elf_aplib.a.mcrit) / [x64 PE](data/aPLib/x64/mcrit/aPLib-1.01_coff64_aplib.lib.mcrit) / [x64 ELF](data/aPLib/x64/mcrit/aPLib-1.01_elf64_aplib.a.mcrit) | [x86 PE](data/aPLib/x86/smda/aPLib-1.01_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/smda/aPLib-1.01_elf_aplib.a.7z) / [x64 PE](data/aPLib/x64/smda/aPLib-1.01_coff64_aplib.lib.7z) / [x64 ELF](data/aPLib/x64/smda/aPLib-1.01_elf64_aplib.a.7z) |
| aPLib  | 2014-01-20 | 1.10    | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-1.10_coff_aplib.lib.mcrit) / [x86 ELF](data/aPLib/x86/mcrit/aPLib-1.10_elf_aplib.a.mcrit) / [x64 PE](data/aPLib/x64/mcrit/aPLib-1.10_coff64_aplib.lib.mcrit) / [x64 ELF](data/aPLib/x64/mcrit/aPLib-1.10_elf64_aplib.a.mcrit) | [x86 PE](data/aPLib/x86/smda/aPLib-1.10_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/smda/aPLib-1.10_elf_aplib.a.7z) / [x64 PE](data/aPLib/x64/smda/aPLib-1.10_coff64_aplib.lib.7z) / [x64 ELF](data/aPLib/x64/smda/aPLib-1.10_elf64_aplib.a.7z) |
| aPLib  | 2014-07-21 | 1.11    | as distributed | [x86 PE](data/aPLib/x86/mcrit/aPLib-1.11_coff_aplib.lib.mcrit) / [x86 ELF](data/aPLib/x86/mcrit/aPLib-1.11_elf_aplib.a.mcrit) / [x64 PE](data/aPLib/x64/mcrit/aPLib-1.11_coff64_aplib.lib.mcrit) / [x64 ELF](data/aPLib/x64/mcrit/aPLib-1.11_elf64_aplib.a.mcrit) | [x86 PE](data/aPLib/x86/smda/aPLib-1.11_coff_aplib.lib.7z) / [x86 ELF](data/aPLib/x86/smda/aPLib-1.11_elf_aplib.a.7z) / [x64 PE](data/aPLib/x64/smda/aPLib-1.11_coff64_aplib.lib.7z) / [x64 ELF](data/aPLib/x64/smda/aPLib-1.11_elf64_aplib.a.7z) |


### libzlib

zlib is a popular compression library implementing the Deflate algorithm.  
Dates taken from Changelog file / release notes.  
Source data taken from the [Shiftmedia project](https://github.com/ShiftMediaProject/zlib).


| Name     | Date       | Version | Compiler       | MCRIT                                                                                                                                                 | SMDA                                                                                                                                            |
|----------|------------|---------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| libzlib  | 2013-04-28 | 1.2.8   | MSVC12         | [x86 PE](data/libzlib/x86/mcrit/libzlib_1.2.8_msvc12_x86_libzlib.mcrit) / [x64 PE](data/libzlib/x64/mcrit/libzlib_1.2.8_msvc12_x64_libzlib.mcrit)     | [x86 PE](data/libzlib/x86/smda/libzlib_1.2.8_msvc12_x86_libzlib.7z) / [x64 PE](data/libzlib/x64/smda/libzlib_1.2.8_msvc12_x64_libzlib.7z)       |
| libzlib  | 2013-04-28 | 1.2.8   | MSVC14         | [x86 PE](data/libzlib/x86/mcrit/libzlib_1.2.8_msvc14_x86_libzlib.mcrit) / [x64 PE](data/libzlib/x64/mcrit/libzlib_1.2.8_msvc14_x64_libzlib.mcrit)     | [x86 PE](data/libzlib/x86/smda/libzlib_1.2.8_msvc14_x86_libzlib.7z) / [x64 PE](data/libzlib/x64/smda/libzlib_1.2.8_msvc14_x64_libzlib.7z)       |
| libzlib  | 2016-12-31 | 1.2.9   | MSVC12         | [x86 PE](data/libzlib/x86/mcrit/libzlib_1.2.9_msvc12_x86_libzlib.mcrit) / [x64 PE](data/libzlib/x64/mcrit/libzlib_1.2.9_msvc12_x64_libzlib.mcrit)     | [x86 PE](data/libzlib/x86/smda/libzlib_1.2.9_msvc12_x86_libzlib.7z) / [x64 PE](data/libzlib/x64/smda/libzlib_1.2.9_msvc12_x64_libzlib.7z)       |
| libzlib  | 2016-12-31 | 1.2.9   | MSVC14         | [x86 PE](data/libzlib/x86/mcrit/libzlib_1.2.9_msvc14_x86_libzlib.mcrit) / [x64 PE](data/libzlib/x64/mcrit/libzlib_1.2.9_msvc14_x64_libzlib.mcrit)     | [x86 PE](data/libzlib/x86/smda/libzlib_1.2.9_msvc14_x86_libzlib.7z) / [x64 PE](data/libzlib/x64/smda/libzlib_1.2.9_msvc14_x64_libzlib.7z)       |
| libzlib  | 2017-01-02 | 1.2.10  | MSVC12         | [x86 PE](data/libzlib/x86/mcrit/libzlib_1.2.10_msvc12_x86_libzlib.mcrit) / [x64 PE](data/libzlib/x64/mcrit/libzlib_1.2.10_msvc12_x64_libzlib.mcrit)   | [x86 PE](data/libzlib/x86/smda/libzlib_1.2.10_msvc12_x86_libzlib.7z) / [x64 PE](data/libzlib/x64/smda/libzlib_1.2.10_msvc12_x64_libzlib.7z)     |
| libzlib  | 2017-01-02 | 1.2.10  | MSVC14         | [x86 PE](data/libzlib/x86/mcrit/libzlib_1.2.10_msvc14_x86_libzlib.mcrit) / [x64 PE](data/libzlib/x64/mcrit/libzlib_1.2.10_msvc14_x64_libzlib.mcrit)   | [x86 PE](data/libzlib/x86/smda/libzlib_1.2.10_msvc14_x86_libzlib.7z) / [x64 PE](data/libzlib/x64/smda/libzlib_1.2.10_msvc14_x64_libzlib.7z)     |
| libzlib  | 2017-01-15 | 1.2.11  | MSVC12         | [x86 PE](data/libzlib/x86/mcrit/libzlib_1.2.11_msvc12_x86_libzlib.mcrit) / [x64 PE](data/libzlib/x64/mcrit/libzlib_1.2.11_msvc12_x64_libzlib.mcrit)   | [x86 PE](data/libzlib/x86/smda/libzlib_1.2.11_msvc12_x86_libzlib.7z) / [x64 PE](data/libzlib/x64/smda/libzlib_1.2.11_msvc12_x64_libzlib.7z)     |
| libzlib  | 2017-01-15 | 1.2.11  | MSVC14         | [x86 PE](data/libzlib/x86/mcrit/libzlib_1.2.11_msvc14_x86_libzlib.mcrit) / [x64 PE](data/libzlib/x64/mcrit/libzlib_1.2.11_msvc14_x64_libzlib.mcrit)   | [x86 PE](data/libzlib/x86/smda/libzlib_1.2.11_msvc14_x86_libzlib.7z) / [x64 PE](data/libzlib/x64/smda/libzlib_1.2.11_msvc14_x64_libzlib.7z)     |
| libzlib  | 2017-01-15 | 1.2.11  | MSVC15         | [x86 PE](data/libzlib/x86/mcrit/libzlib_1.2.11_msvc15_x86_libzlib.mcrit) / [x64 PE](data/libzlib/x64/mcrit/libzlib_1.2.11_msvc15_x64_libzlib.mcrit)   | [x86 PE](data/libzlib/x86/smda/libzlib_1.2.11_msvc15_x86_libzlib.7z) / [x64 PE](data/libzlib/x64/smda/libzlib_1.2.11_msvc15_x64_libzlib.7z)     |
