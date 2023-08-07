#!/bin/bash
mkdir -p build && \
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
    7zz a -xr!__pycache__ -xr!.benchmarks -xr!.github -xr!.pytest_cache -xr!image* -xr!test* Lox365.zip ./* && \
    mv -v Lox365.zip build/Lox365.oxt
) && \
echo 'Build successful.'