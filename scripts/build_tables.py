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
    3:  {"date": "2012-07-14", "version": "trunk_r5214 gcc4.7.1 binutils cvs-20120714"},
    4:  {"date": "2012-10-27", "version": "v2.0.7      gcc4.7.2 binutils2.23"},
    5:  {"date": "2012-11-04", "version": "v2.0.7      gcc4.7.2 binutils2.23"},
    6:  {"date": "2013-04-13", "version": "v2.0.8      gcc4.7.3 binutils2.23.2"},
    7:  {"date": "2013-04-13", "version": "trunk_r5784 gcc4.8.0 binutils2.23.2"},
    8:  {"date": "2013-06-01", "version": "trunk_r5876 gcc4.8.1 binutils2.23.2"},
    9:  {"date": "XXXXXXXXXX", "version": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"},
    10: {"date": "2013-11-17", "version": "v3.0.0      gcc4.8.2 binutils2.23.2"},
    11: {"date": "2014-05-22", "version": "v3.1.0      gcc4.8.3 binutils2.24"},
    12: {"date": "2014-07-30", "version": "v3.1.0      gcc4.9.1 binutils2.24"},
    13: {"date": "2014-11-10", "version": "v3.3.0      gcc4.9.2 binutils2.24"},
    14: {"date": "2015-06-30", "version": "v4.0.2      gcc4.9.3 binutils2.25"},
    15: {"date": "2015-07-10", "version": "v4.0.2      gcc5.1   binutils2.25"},
    16: {"date": "2015-07-21", "version": "v4.0.2      gcc5.2   binutils2.25"},
    17: {"date": "2015-12-01", "version": "v4.0.4+     gcc5.2   binutils2.25.1"},
    18: {"date": "2015-12-05", "version": "v4.0.4+     gcc5.3   binutils2.25.1"},
    19: {"date": "2016-06-14", "version": "v4.0.6      gcc5.4   binutils2.25.1"},
    20: {"date": "2016-06-14", "version": "v4.0.6      gcc6.1   binutils2.25.1"},
    21: {"date": "2016-09-27", "version": "v4.0.6      gcc6.2   binutils2.27"},
    22: {"date": "2016-12-29", "version": "v4.0.6      gcc6.3   binutils2.27"},
    23: {"date": "XXXXXXXXXX", "version": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"},
    24: {"date": "XXXXXXXXXX", "version": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"},
    25: {"date": "2017-02-20", "version": "v5.0.1+1    gcc6.3   binutils2.27"},
    26: {"date": "2017-06-02", "version": "v5.0.2      gcc7.1   binutils2.28"},
    27: {"date": "2017-08-16", "version": "v5.0.2      gcc7.2   binutils2.29"},
    28: {"date": "2018-02-07", "version": "v5.0.3      gcc7.3   binutils2.29.1"},
    29: {"date": "2018-11-01", "version": "v5.0.4      gcc8.2   binutils2.31.1"},
    30: {"date": "2019-02-27", "version": "v6.0.0      gcc8.3   binutils2.31.1"},
    31: {"date": "2019-10-14", "version": "v6.0.0      gcc9.2   binutils2.32"},
    32: {"date": "2020-04-30", "version": "v7.0.0      gcc9.3   binutils2.34"},
    33: {"date": "2021-02-27", "version": "v8.0.0      gcc10.2  binutils2.36.1"},
    34: {"date": "2021-07-13", "version": "v8.0.2      gcc10.3  binutils2.36.1"},
    35: {"date": "2021-08-15", "version": "v9.0.0      gcc11.2  binutils2.36.1"},
    36: {"date": "2022-01-19", "version": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"},
    37: {"date": "2022-04-26", "version": "v10.0.0     gcc11.3  binutils2.38"},
    38: {"date": "2022-08-23", "version": "v10.0.0     gcc12.2  binutils2.39"},
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