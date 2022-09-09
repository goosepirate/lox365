# ⚗️ Lox365: XLOOKUP for LibreOffice

Lox365 is a LibreOffice extension that adds modern spreadsheet functions like XLOOKUP to LibreOffice.

![Screenshot](image1.png)

## Install

1. Download the extension `Lox365.oxt`.
2. Start LibreOffice > Tools > Extension Manager > Add > Select the oxt file > restart LibreOffice

## Usage

Once Lox365 is installed, just use them like you would in Excel.

| Excel                                                        | Lox365  | Lox365 completeness | Note |
| ------------------------------------------------------------ | ------- | ------------------- | ---- |
| [FILTER](https://support.microsoft.com/en-us/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759) | FILTER  | Full                |      |
| [SORT](https://support.microsoft.com/en-us/office/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c) | SORT    | Partial             | 1    |
| [XLOOKUP](https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929) | XLOOKUP | Partial             | 2    |

Notes:

1. This version does not yet support `by_col`.
2. This version does not yet support `match_mode` and `search_mode`.

## Why

I use these functions quite often in Excel and wanted to use them in LibreOffice too, so I made this. Contributions are welcome.

## More functions

These functions are available in the latest Excel but not in LibreOffice, and not (yet) provided by Lox365:

* RANDARRAY
* SEQUENCE
* SORTBY
* TEXTSPLIT
* UNIQUE
* XMATCH

These functions are already available in LibreOffice, so they're not provided by Lox365:

* CONCAT
* IFS
* MAXIFS
* MINIFS
* SWITCH
* TEXTJOIN

## Reference

https://wiki.documentfoundation.org/Documentation/HowTo/install_extension

https://wiki.documentfoundation.org/Feature_Comparison:_LibreOffice_-_Microsoft_Office

https://bugs.documentfoundation.org/show_bug.cgi?id=126573

https://bugs.documentfoundation.org/show_bug.cgi?id=127293

https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1uno.html