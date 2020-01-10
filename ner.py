from flair.models import SequenceTagger
from flair.data import Sentence, Span
from typing import List, Optional, Dict, Any
from ner_entity import NerEntity
from dataclasses import asdict


def load_flair_fr() -> SequenceTagger:
    return SequenceTagger.load('fr-ner')


def load_flair_en() -> SequenceTagger:
    return SequenceTagger.load('ner-fast')


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
