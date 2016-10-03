#!/bin/bash
set -e
set -u

py.test --verbose practice/

py.test --cov=practice practice/

exit 0;