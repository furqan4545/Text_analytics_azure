from flask import Flask, render_template, url_for, request, jsonify, make_response, flash, redirect
import requests
import json
import os
import numpy as np
import math
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

key = "INSERT YOUR KEY HERE"
endpoint = "INSERT YOUR ENDPOINT HERE"


def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=ta_credential)
    return text_analytics_client


@app.route('/', methods=['GET', 'POST'])
def index():
    dicti = data()
    return render_template('index.html',predic=dicti)
    # return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        try:
            documents = [request.form.get('doc1')]
            documents2 = [request.form.get('doc2')]  # converting string into list
            # choc = request.form.get('choc')
            # bis = request.form.get('bis')
            
            # response = {"bottles" : nbot, "choclates" : choc, "Biscuits" : bis}
            response = {"Document 1" : documents, "Documents 2": documents2}
            
            print(response)

            client = authenticate_client()

            # documents = ["I had the best day of my life. I wish you were there with me."]
            response = client.analyze_sentiment(documents = documents)[0]
            print("Document Sentiment: {}".format(response.sentiment))
            print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
                response.confidence_scores.positive,
                response.confidence_scores.neutral,
                response.confidence_scores.negative,
            ))

            pred = []
            for idx, sentence in enumerate(response.sentences):
                print("Sentence: {}".format(sentence.text))
                print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
                print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                    sentence.confidence_scores.positive,
                    sentence.confidence_scores.neutral,
                    sentence.confidence_scores.negative,
                ))

                pred.append(sentence.sentiment)

            print("Prediction: ", sentence.text)
            
            return jsonify({
                "pred1" : pred,
                "pred2" : documents2
                # "n_packs" : rs[1],
                # "n_boxes" : rs[2],
                # "n_choclates" : rs2[0],
                # "n_cpacks" : rs2[1],
                # "n_cboxes" : rs2[2],
                # "n_biscuits" : rs3[0],
                # "n_bpacks" : rs3[1],
                # "n_bboxes" : rs3[2]
            })

            
        except:
            return "Please check if the values are entered correctly"


if __name__ == "__main__":
    app.run(debug=True)