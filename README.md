# ⚗️ Lox365: XLOOKUP for LibreOffice

Lox365 is a LibreOffice extension that adds modern spreadsheet functions like XLOOKUP to LibreOffice.

![Screenshot](image1.png)

## Install

1. Download the extension `Lox365.oxt`.
2. Start LibreOffice > Tools > Extension Manager > Add > Select the oxt file > restart LibreOffice

## Usage

Once Lox365 is installed, just use them like you would in Excel.

| Excel                                                        | Lox365    | Lox365 completeness | Note |
| ------------------------------------------------------------ | --------- | ------------------- | ---- |
| [FILTER](https://support.microsoft.com/en-us/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759) | FILTER    | Full                |      |
| [SORT](https://support.microsoft.com/en-us/office/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c) | SORT      | Partial             | 1    |
| [TEXTSPLIT](https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7) | TEXTSPLIT | Partial             | 2    |
| [TOCOL](https://support.microsoft.com/en-us/office/tocol-function-22839d9b-0b55-4fc1-b4e6-2761f8f122ed) | TOCOL     | Partial             | 3    |
| [UNIQUE](https://support.microsoft.com/en-us/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e) | UNIQUE    | Partial             | 4    |
| [XLOOKUP](https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929) | XLOOKUP   | Partial             | 5    |

Notes:

1. Not supported: `by_col`.
2. Not supported: `row_delimiter`, `ignore_empty`, `match_mode`, `pad_with`.
3. Not supported: `ignore`, `scan_by_column`.
4. Not supported: `by_col`, `exactly_once`.
5. Not supported: `match_mode`, `search_mode`.

## Why

I use these functions quite often in Excel and wanted to use them in LibreOffice too, so I made this. Contributions are welcome.

## More functions

These functions are not in LibreOffice and not provided by Lox365 but are available in the latest Excel:

* RANDARRAY
* SEQUENCE
* SORTBY
* STOCKHISTORY
* TOROW
* XMATCH

These functions are already available in LibreOffice:

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

https://gerrit.libreoffice.org/c/core/+/131905

https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1uno.html

https://wiki.openoffice.org/wiki/Calc/Add-In/Python_How-To

https://wiki.openoffice.org/wiki/Python/Python_Language_Binding

https://www.openoffice.org/api/docs/common/ref/com/sun/star/sheet/AddIn.html
