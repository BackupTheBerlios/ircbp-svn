#!/bin/bash

echo -n "Copying CHANGELOG to CHANGELOG.txt..."
rm CHANGELOG.txt
cp CHANGELOG CHANGELOG.txt
echo "Done!\n"

echo -n "Copying CREDITS to CREDITS.txt..."
rm CREDITS.txt
cp CREDITS CREDITS.txt
echo "Done!\n"

echo -n "Copying LICENSE to LICENSE.txt..."
rm LICENSE
CP LICENSE LICENSE.txt
echo "Done!\n"