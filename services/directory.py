__author__ = 'dqin2'

from flask import Flask, jsonify, request, abort

from reports.directory import Directory

app = Flask(__name__)
report = None


def initialize_state():
    """
    For use with sqlite in memory db, sqlite in memory is not thread-safe
    :return:
    """

    global report
    if not report:
        report = Directory()
        report.load_sample_data()


@app.route('/records', methods=['POST'])
def post_record():
    initialize_state()
    if not request.json or 'value' not in request.json or 'delimiter' not in request.json:
        abort(400)

    report.load_single(request.json['delimiter'], request.json['value'])


@app.route('/records/gender', methods=['GET'])
def gender_report():
    initialize_state()
    results = {'results': [p.to_dict() for p in report.report_data(order_by=[('gender', 'ASC')])]}
    return jsonify(results)


@app.route('/records/birthdate', methods=['GET'])
def birthdate_report():
    initialize_state()
    results = {'results': [p.to_dict() for p in report.report_data(order_by=[('date_of_birth', 'ASC')])]}
    return jsonify(results)


@app.route('/records/name', methods=['GET'])
def last_name_report():
    initialize_state()
    results = {
        'results': [p.to_dict() for p in report.report_data(order_by=[('last_name', 'ASC'), ('first_name', 'ASC')])]}
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
