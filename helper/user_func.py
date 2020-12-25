from models import _Options
import pandas as pd
from app import db


def get_oid_and_score_mapping():

    result = _Options.query.all()

    option_id = []
    score = []
    for row in result:
        option_id.append(row.OID)
        score.append(row.Score)

    score_map = dict(zip(option_id, score))

    return score_map