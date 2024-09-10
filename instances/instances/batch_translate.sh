#!/bin/sh
chmod +x translate.py 
find ../tw20/ -name "n*" -exec ./translate.py {} \;
find ../tw100/ -name "n*" -exec ./translate.py {} \;

