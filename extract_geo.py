#!/usr/bin/env python3
# Extract geometries from a QCHEM output file and write to an xyz-trajectory

import argparse as ag

# Input argument parsing
parser = ag.ArgumentParser()
parser.add_argument("-f", type=str, required=True, metavar="INPUT",
                   help="file containing QCHEM geometry optimisation output.")
parser.add_argument("-o", type=str, metavar="OUTPUT",
                    help="output .xyz file to write trajectory to.")
args = parser.parse_args()

# If no outout is specified simply use input name
if not args.o:
    args.o = f"{args.f.split('.')[0]}.xyz"

# Open QCHEM output file
with open(args.f, "r") as inp:
    nAtoms = 0              # Number of atoms in geometry
    lines = inp.readlines() # Read lines from output file

    # Find the number of atoms from the first geometry
    for j, line in enumerate(lines):
        if "Standard Nuclear Orientation" in line:
            for l in lines[j+3:]:
                if "---" not in l:
                    nAtoms += 1
                else:
                    break
            break

    # Find each geometry
    geom = []
    for j, line in enumerate(lines):
        if "Standard Nuclear Orientation" in line:
            geom.append(lines[j+3:j+3+nAtoms])

# Write trajectory to output file
with open(args.o, "w") as out:
    for j,g in enumerate(geom):
        out.write(f"{str(nAtoms)}\n")
        out.write(f"# Trajectory step {j+1} out of {len(geom)}\n")
        for line in g:
            out.write(f'{" ".join(line.split()[1:])}\n')
