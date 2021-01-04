from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key' #you will need a secret key

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + "eyJraWQiOiIyMDIwMDUyNTE4MzAiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLTIzMWI5OTYyLWExN2ItNDI3OC05YmY3LTQ3Y2RkMDgwYjc2ZCIsImlkIjoiaWFtLVNlcnZpY2VJZC0yMzFiOTk2Mi1hMTdiLTQyNzgtOWJmNy00N2NkZDA4MGI3NmQiLCJyZWFsbWlkIjoiaWFtIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC0yMzFiOTk2Mi1hMTdiLTQyNzgtOWJmNy00N2NkZDA4MGI3NmQiLCJuYW1lIjoid2RwLXdyaXRlciIsInN1YiI6IlNlcnZpY2VJZC0yMzFiOTk2Mi1hMTdiLTQyNzgtOWJmNy00N2NkZDA4MGI3NmQiLCJzdWJfdHlwZSI6IlNlcnZpY2VJZCIsImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6IjkzZWFmZDU2MjNlYTRjMGFhNWYwOWVmOTQ1MjkxOGEyIn0sImlhdCI6MTU5MTYzMTIxOCwiZXhwIjoxNTkxNjM0ODE4LCJpc3MiOiJodHRwczovL2lhbS5ibHVlbWl4Lm5ldC9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.irk9heVcOtqTkLLWsYoQFM_hP_fjSVDgaxN7letIojAQUSuQUPW2YlVLoWTTQUIVw5vuvQC75JxBhP7OzFRjI87a7AEkrUN30BjACaLLTs8DM6xBA2hJc74enoi3lJ4dDhIlDt_yeCh0oBxxu14R6jqCP9Vem47mhJ1GaVFM9M5n4sT25PnAcG_u35DDC81GIYbhdFedE1IAI8roxplH2B0ZVqWjfHL5E2feZ37mM1e5QFl4Y_5p6T5kbjeb12kneAEegkS56obfG3V4ymOzv-r_RJZT8zSP4gxT6cskOZ2IpExgXi4AMXRvC6-5mwOLXMJJ2ZUkGinZjtV0HGl9uA","refresh_token":"OKCQYya-8VbNzh7hW0khQVl3S6qk4aBciH2DX77fW9_YQxyfvFzdjIMX1D8DmHICPI-G86hLGlZduLSC_Occ5VeoiRW_GiCOs6CtdI10VgRhnVgowy5sYPf3z6KQfWJX6hmZu004ka2VWvMCF8VcqqasO-1ZACJX2xfn_NNrR2titFudDlZCyUqC8IeqJ5YAgW8rZlyw7lBXxN4M_A9m7v3p2L2QJS71SBKm8FjIDyp7b0QX_lpPW2mGlFl18cemHp_fciuWGlTt-XyiMbpJuHFkSxSVrjfpyRlgBmqfyUZnii8cQDLydxexS08SQZ6zmtW-KmYCzy6Zb1xsQYeQnSLoaJTPpHtRro5yN0L9aC_tSM9BwMrMLQ_ZiWYxKqnApghFdc6QCpVoxAsqs4uXozgpafDA99Ww0x49ssDw9_tdJ8uUJWQH24Gkqvl_ePJT1-IgTvIVAbM1zwEWiuAT6AXc60Kwm-8qypokkng1AE_djkeK5epOFo70jKHTPhUEy-pscBezOttQ2-noORZJTrkifePlkfiEI05FxGDZiix1NV0Mf2TTRcdQnEYtgVLzUx9SZdUrpBb09rNIvGrMtdXBg-Fy1qhPMi_90MXO1y1Dn6CcwVVp2my7WMuIQswWQ43nwpfkyAML_yk3bvekl1dTGVYKpJvDnuqJzEW4vZ_iAbInQHwHsXIpmVCaFBw1ZuMjOQZ14dz_ugvkI7sy0N0P0SuFM5Ppx_07H2X5bcQa3CQRWYSOM9DdCcHhojE8xvgQzpTOPBvayoA58DosN03r7Jffz0wtAow4kYPl8_GQYfFA5t5AUONNHrIe7RC1d76NAZBSJElgQzdv7oQIdSAdjAKUR3B1WJ-LcmiX2wFoaR0-Ecxhgo130-J0BCbHoRk73OSxGmFfHVNPVlo0wbpYbOLOgdMBisCkRsmh1eI54OKPSXkuJ-LjXHyALIxu9ewhkuj-eKo_IXSMwmBDN1Z3rMvA3GQu8hcWjxZYcVb5DU_0-M-3ZMPYm8BNd9-Swwmh3bUtpe3u9PkAN4k_I0GOknwJp8nAANsBNHeoxi64rw",
                  'ML-Instance-ID': "9c3b2402-9562-439e-8df2-9545ed40c34a"}

        if(form.ingreso_mensual.data == None): 
          python_object = []
        else:
          python_object = [form.edad.data, form.estado_civil.data, float(form.ingreso_mensual.data),
            form.anios_laboral.data, form.hijos.data, form.region.data]
        #Transform python objects to  Json

        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["edad", "estado_civil", "ingreso_mensual",
          "anios_laboral", "hijos", "region"], "values": userInput }]}

        response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/v4/deployments/c2f3ae93-dfce-4ce6-8eb5-9378209a7e35/predictions", json=payload_scoring, headers=header)

        output = json.loads(response_scoring.text)
        print(output)
        for key in output:
          ab = output[key]
        

        for key in ab[1]:
          bc = ab[0][key]
        
        roundedCharge = round(bc[0][0],2)

  
        form.abc = roundedCharge # this returns the response back to the front page
        return render_template('index.html', form=form)