#!/bin/bash
(
    rm -v build/interface.urd; \
    PATH=$PATH:/usr/lib/libreoffice/sdk/bin idlc -I /usr/lib/libreoffice/sdk/idl -w interface.idl && \
    mv -v interface.urd build/
) && \
(
    rm -v build/interface.rdb; \
    PATH=$PATH:/usr/lib/libreoffice/program regmerge build/interface.rdb /UCR build/interface.urd
) && \
(
    rm -v build/Lox365.oxt; \
    7z a -xr!Pipfile* -xr!test* -xr!.venv -xr!.benchmarks -xr!.pytest_cache Lox365.zip ./* && \
    mv -v Lox365.zip build/Lox365.oxt
) && \
echo 'Build successful.'