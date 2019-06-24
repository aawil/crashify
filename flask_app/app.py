from flask import Flask, request, render_template, jsonify, send_file
from api import get_random_craft, get_display_features, get_prediction

# Initialize the app

app = Flask(__name__)


@app.route("/")
def hello():
    global craft
    craft = get_random_craft()
    display_craft = get_display_features(craft)

    return render_template("index.html", craft=display_craft)

@app.route("/results")
def results():
    guess = 0
    if request.args['select'] == "Human error":
        guess = 0
    elif request.args['select'] == "Just bad luck":
        guess = 1

    prediction, confidence = get_prediction(craft)

    reality = craft.iloc[:, -1][0]

    ev_id = craft.index[0][0]
    craft_key = craft.index[0][1]
    report_url = f"https://app.ntsb.gov/pdfgenerator/ReportGeneratorFile.ashx?EventID={ev_id}&AKey={craft_key}&RType=HTML&IType=LA"

    return render_template("results.html", guess=guess, prediction=prediction, confidence=confidence,
                           reality=reality, report_url=report_url)


if __name__=="__main__":
    # For local development:
    #app.run(debug=True)
    # For public web serving:
    #app.run(host='0.0.0.0')
    app.run()
