#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 2:
    print("Usage: python rename_ligand_atoms.py ligand.pdb")
    sys.exit(1)

input_file = sys.argv[1]
output_file = os.path.splitext(input_file)[0] + "_renamed.pdb"

h_counter = 1

with open(input_file, "r") as fin, open(output_file, "w") as fout:

    for line in fin:

        if not line.startswith("HETATM"):
            fout.write(line)
            continue

        serial = int(line[6:11])

        # element symbol from PDB columns 77-78
        element = line[76:78].strip()

        if element == "H":
            atom_name = f"H{h_counter}"
            h_counter += 1
        else:
            atom_name = f"{element}{serial}"

        # PDB atom-name field is columns 13-16 (4 chars)
        atom_name = atom_name[:4].ljust(4)

        new_line = (
            line[:12]
            + atom_name
            + line[16:]
        )

        fout.write(new_line)

print(f"Output written to: {output_file}")