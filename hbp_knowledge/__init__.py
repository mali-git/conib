# -*- coding: utf-8 -*-

"""The Human Brain Pharmacome knowledge repository."""

import os

from bel_repository import BELMetadata, BELRepository

__all__ = [
    'repository',
    'get_graph',
    'get_graphs',
    'get_summary_df',
    'main',
]

HERE = os.path.dirname(__file__)
VERSION = '0.0.1-dev'

# Author list will be sorted by last name
AUTHORS = [
    'Charles Tapley Hoyt',
    'Daniel Domingo-Fernández',
    'Esther Wollert',
    'Sandra Spalek',
    'Rana Al Disi',
    'Lingling Xu',
    'Kristian Kolpeja',
]

# All metadata is grouped here
METADATA = BELMetadata(
    name='Human Brain Pharmacome Knowledge',
    version=VERSION,
    authors=', '.join(sorted(AUTHORS, key=lambda s: s.split()[-1])),
    contact='charles.hoyt@scai.fraunhofer.de',
)

repository = BELRepository(
    HERE,
    bel_metadata=METADATA,
)

get_graph = repository.get_graph
get_graphs = repository.get_graphs
get_summary_df = repository.get_summary_df

main = repository.build_cli()
