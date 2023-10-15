from dataclasses import dataclass


@dataclass
class Category:
    id: str
    title: str
    childs: list[str]