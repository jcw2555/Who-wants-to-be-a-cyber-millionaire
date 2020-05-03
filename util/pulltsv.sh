#!/bin/bash
#
# pulls our google sheet as a tsv
wget "https://docs.google.com/spreadsheets/d/1wAyyionpvedzrM_rh33iLVX7hPssNF1K3U2WTCi_qLs/export?format=tsv" -O /var/lib/mysql-files/complete_millionaire.tsv

