#!/usr/bin/python3

"""
This module provides a flask app instance
"""

from flask import (
    Flask,
    render_template,
    request
)
from engine import db

app = Flask(__name__)


@app.route('/results/allpollingunits',
           strict_slashes=False, methods=['GET'])
def getallPUResults() -> str:
    """ Creates html template for all polling units results """
    results = db.getAllPollingUnitVotes()
    title = "All Polling Units' Results"
    return render_template('all_results.html',
                           title=title,
                           votes=results)


@app.route('/results/lgas/<lga_id>', strict_slashes=False)
def getLGAResults(lga_id: str) -> str:
    """ Creates html template for results of lga specified by `lga_id` """
    lga_results = db.getLgaVotes(int(lga_id))
    lgas = db.getAllLGAs()
    lga_endpoints = [{
        'name': lga.lga_name,
        'endpoint': f'/results/lgas/{lga.lga_id}'
    } for lga in lgas]
    return render_template('lga_results.html',
                           lga_results=lga_results,
                           lga_endpoints=lga_endpoints)

@app.route('/results/lgas/', strict_slashes=False)
def getLGAResultsRoutes() -> str:
    """ Creates html template for routes to results of lga specified by `lga_id` """
    lgas = db.getAllLGAs()
    lga_endpoints = [{
        'name': lga.lga_name,
        'endpoint': f'/results/lgas/{lga.lga_id}'
    } for lga in lgas]
    return render_template('lga_results_routes.html',
                           lga_endpoints=lga_endpoints)

@app.route('/results/pollingunits/new',
           strict_slashes=False, methods=['GET'])
def newPollingUnit() -> str:
    """
    Creates html template for receiving
    polling new unit details and its results
    """
    parties = db.getAllParties()
    wards = db.getAllWards()
    return render_template('add_pu_result.html',
                           parties=parties,
                           wards=wards)


@app.route('/results/pollingunits/add', methods=['GET'])
def addNewPUResult() -> str:
    args = request.args
    response = db.addPollingUnit(args)
    return render_template('add_pu_result_res.html',
                           response=response), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
