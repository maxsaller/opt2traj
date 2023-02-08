# OPT2TRAJ

## Extract geometries from a QCHEM output file and write to an xyz-trajectory

Extracts geometries from a QCHEM output file, using the keyphrase
"Standard Nuclear Orientation" and saves each instance it finds as
as the frame of a trajectory in the XYZ file format.

Usage:
```bash
opt2traj.py -i <QCHEM-output-file> [-o <trajectory-output-name>]
```
