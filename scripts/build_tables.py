import re
import os
import sys

# build markdown tables for MinGW

file_collection = {
    "mcrit": {
        "x86": {},
        "x64": {}
    },
    "smda": {
        "x86": {},
        "x64": {}
    }
} 

release_date_version = {
    8:  {"date": "2013-06-01", "version": "trunk_r5876 gcc4.8.1"},
    11: {"date": "2014-05-22", "version": "v3.1.0      gcc4.8.3 binutils2.24"},
    27: {"date": "2017-08-16", "version": "v5.0.2      gcc7.2   binutils2.29"},
    32: {"date": "2020-04-30", "version": "v7.0.0      gcc9.3   binutils2.34"},
}

releases = set([])

for root, subdir, files in sorted(os.walk(sys.argv[1])):
    for filename in sorted(files):
        filepath = root + os.sep + filename
        regex = ".*-stable-r(?P<release>[^_]{1,2})_(?P<bitness>x[468]{2})\.(?P<extension>(7z|mcrit))"
        if result := re.match(regex, filename):
            releases.add(int(result["release"]))
            filetype = "smda" if result["extension"] == "7z" else "mcrit"
            file_collection[filetype][result["bitness"]][int(result["release"])] = filepath

output =""

print(file_collection)

for release in sorted(range(1, 39)):
    smda_x86 = f'[x86]({file_collection["smda"]["x86"][release]})' if release in file_collection["smda"]["x86"] else 'x86'
    smda_x64 = f'[x64]({file_collection["smda"]["x64"][release]})' if release in file_collection["smda"]["x64"] else 'x64'
    mcrit_x86 = f'[x86]({file_collection["mcrit"]["x86"][release]})' if release in file_collection["mcrit"]["x86"] else 'x86'
    mcrit_x64 = f'[x64]({file_collection["mcrit"]["x64"][release]})' if release in file_collection["mcrit"]["x64"] else 'x64'
    date = release_date_version[release]["date"] if release in release_date_version else "XXXX-XX-XX"
    version = release_date_version[release]["version"] if release in release_date_version else "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    output += f"| MinGW r{release:<2d}  | {date} | {version:<33} | {smda_x86} / {smda_x64} | {mcrit_x86} / {mcrit_x64} |\n"

print(output)