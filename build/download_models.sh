#!/bin/bash
mkdir models
curl https://flair.informatik.hu-berlin.de/resources/models/ner-fast/en-ner-fast-conll03-v0.4.pt -o models/en-ner-fast-conll03-v0.4.pt
curl https://flair.informatik.hu-berlin.de/resources/models/fr-ner/fr-ner-wikiner-0.4.pt -o models/fr-ner-wikiner-0.4.pt