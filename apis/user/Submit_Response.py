from flask import Flask, session, request
from flask_restful import Resource
from models import Score
from helper.user_func import get_oid_and_score_mapping
from helper.admin_func import get_assessment_questions
from app import db


class Submit_Response(Resource):

    def post(self):

        data = request.get_json(force=True)

        user_response = data.get('response')
        if not user_response:
            return {
                "state": False,
                "message": "Could not find a response."
            }

        username = session.get('user')
        if not username:
            return {
                "state": False,
                "message": "Somethings not right. Login to continue."
            }

        OID_score_map = get_oid_and_score_mapping()
        assessment_score = 0
        ordered_scores = []
        for qno, selected_OID in user_response.items():
            ordered_scores.append(OID_score_map[int(selected_OID)])
            assessment_score += OID_score_map[int(selected_OID)]

        file_exists, info = get_assessment_questions()
        if not file_exists:
            return info
        
        Q_data = info
        Q_data.index += 1
        max_5_qualities_index = sorted([(x, i) for (i, x) in enumerate(ordered_scores)], reverse=True)[:5]
        max_5_qualities = [Q_data.iat[tup_[1], 0] for tup_ in max_5_qualities_index]

        response_ = {
            "state": True,
            "message": None,
            "scorecard": str(assessment_score),
            "top_5_qualities": {
                "quality_1": max_5_qualities[0],
                "quality_2": max_5_qualities[1],
                "quality_3": max_5_qualities[2],
                "quality_4": max_5_qualities[3],
                "quality_5": max_5_qualities[4],
            }
        }
        score_exists = Score.query.filter_by(Username=username).first()
        if score_exists:
            score_exists.Score = assessment_score
            db.session.commit()
            response_ ['message'] = "Score updated successfully."
            return response_
        else:
            new_score_obj = Score()
            new_score_obj.Username = username
            new_score_obj.Score = assessment_score
            db.session.add(new_score_obj)
            db.session.commit()
            response_ ['message'] = "Your score has been recorded."
            return response_