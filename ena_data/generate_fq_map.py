#! /usr/bin/env python3
from pathlib import Path

info = """
ERR1099208           FP0026-C    WAF        0.45     False
ERR018904,ERR015361  PA0035-C    WAF        89.9     True
ERR676507            PE0309-C    EAF        89.87    True
ERR404155            QG0016-C    CAF        88.65    True
ERR1172588           QJ0006-C    WAF        89.43    True
ERR036596            PR0001-CW   SAS        89.62    True
ERR015419            PH0057-C    ESEA       88.91    True 
ERR019041            PD0009-01   WSEA       77.01    True
ERR022856            PP0010-C    SAM        88.92    True
ERR018922            PP0006-C    Lab        87.87    False
"""

header = ["Sample", "HostId", "MateId", "Run", "Fastq"]
print("\t".join(header))
for line in info.strip().split("\n"):
    acc, sample, _, _, _ = line.split()
    acc_lst = acc.split(",")
    for i, acc in enumerate(acc_lst):
        for mate in [1, 2]:
            hostid = 0
            mateid = mate
            run = f"R{i+1}"
            dir = Path(__file__).parent.absolute()
            path = dir / (f"reads_fastq/{acc}/{acc}_{mate}.fastq.gz")
            print(f"{sample}\t{hostid}\t{mateid}\t{run}\t{path}")
