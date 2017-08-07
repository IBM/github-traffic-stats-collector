#!/bin/bash -e

num_proc=$(grep processor /proc/cpuinfo | tail -1 | cut -d ' ' -f2)
((num_proc++))

#shellcheck disable=SC2046,SC2086
if flake8 --jobs="$num_proc" --show-source --statistics $(dirname $0)/../.; then
    echo -e "\033[0;32mPython linting passed!\033[0m"
else
    echo -e >&2 "\033[0;31mPython linting failed!\033[0m"
fi

