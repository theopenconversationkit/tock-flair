from __future__ import annotations
from dataclasses import dataclass
from flair.data import Span


@dataclass(frozen=True)
class NerEntityType:
    name: str


@dataclass(frozen=True)
class NerEntityInfo:
    start: int
    end: int
    type: NerEntityType


@dataclass(frozen=True)
class NerEntity:
    entity: NerEntityInfo
    probability: float

    @classmethod
    def from_span(cls, span: Span) -> NerEntity:
        return NerEntity(
            entity=NerEntityInfo(
                start=span.start_pos,
                end=span.end_pos,
                type=NerEntityType(name=cls._retrieve_type_from(span.tag))
            ),
            probability=min(1, span.score)
        )

    @staticmethod
    def _retrieve_type_from(tag: str) -> str:
        if tag == "PER":
            return "flair:person"
        if tag == "LOC":
            return "flair:location"
        if tag == "ORG":
            return "flair:organization"
        return None
