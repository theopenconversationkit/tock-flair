from flair.models import SequenceTagger
from flair.data import Sentence, Span
from typing import List, Optional, Dict, Any
from ner_entity import NerEntity
from dataclasses import asdict
from pathlib import Path
from os import path


def load_flair_fr() -> SequenceTagger:
    # if loaded from downloaded models
    # return SequenceTagger.load(path.join(Path.cwd(), 'models/fr-ner-wikiner-0.4.pt'))
    return SequenceTagger.load("flair/ner-french")


def load_flair_en() -> SequenceTagger:
        # if loaded from downloaded models
    # return SequenceTagger.load(path.join(Path.cwd(), 'models/en-ner-fast-conll03-v0.4.pt'))
    return SequenceTagger.load("flair/ner-english")


from flair.models import SequenceTagger




flair_fr = load_flair_fr()
flair_en = load_flair_en()


def get_flair(language: str) -> Optional[SequenceTagger]:
    if language == "fr":
        return flair_fr
    if language == "en":
        return flair_en
    return None


def evaluate(tagger: SequenceTagger, content: str) -> Dict[Any, Any]:
    sentence = Sentence(content)
    tagger.predict(sentence)

    entities = [
        asdict(e)
        for e in map(NerEntity.from_span, sentence.get_spans('ner'))
    ]

    return {"entities": entities}
