#!/bin/bash
mkdir models
curl https://s3.eu-central-1.amazonaws.com/alan-nlp/resources/models-v0.4/NER-conll03--h256-l1-b32-p3-0.5-%2Bglove%2Bnews-forward-fast%2Bnews-backward-fast-normal-locked0.5-word0.05--release_4/en-ner-fast-conll03-v0.4.pt -o models/en-ner-fast-conll03-v0.4.pt
curl https://s3.eu-central-1.amazonaws.com/alan-nlp/resources/models-v0.4/release-fr-ner-0/fr-ner-wikiner-0.4.pt -o models/fr-ner-wikiner-0.4.pt