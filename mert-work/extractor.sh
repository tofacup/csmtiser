#!/usr/bin/env bash
cd /csmtiser//mert-work/
/moses/bin/extractor --sctype WER --scconfig case:true  --scfile run17.scores.dat --ffile run17.features.dat -r /csmtiser//dev.norm -n run17.best100.out.gz
