from flask import *
import json
import datetime

app = Flask(__name__)
app.config["Debug"] = True


@app.route('/<string:strdt>/<string:endt>')
def inptts(strdt, endt):
    strdt=strdt
    endt=endt

    f = open('sample_json_3.json')
    inp = json.load(f)
    ini_dict = []
    stm =strdt
    etm = endt
    try:
        if stm[-1] == "Z" and stm[10] == "T":
            if etm[-1] == "Z" and etm[10] == "T":

                stm = stm.replace("-", " ").replace("/", " ").replace("T", " ").replace("Z", " ")
                a=stm

                b = etm.replace("-", " ").replace("/", " ").replace("T", " ").replace("Z", " ")
                sd = datetime.datetime(year=int(a[0:4]), month=int(a[5:7]), day=int(a[8:10]), hour=int(a[11:13]),
                                       minute=int(a[14:16]), second=int(a[17:18]))
                ed = datetime.datetime(year=int(b[0:4]), month=int(b[5:7]), day=int(b[8:10]), hour=int(b[11:13]),
                                       minute=int(b[14:16]), second=int(b[17:18]))
                ds = datetime.timedelta(seconds=1)
                while sd <= ed:
                    for dt in inp:
                        if dt.get('time') == str(sd):
                            cid = dt.get('id')[2:]
                            dt['id'] = int(cid)

                            if dt.get('state') == True:
                                dt['belt1'] = 0

                            else:
                                dt['belt2'] = 0

                            del dt['state'], dt['time']
                            ini_dict.append(dt)
                    sd = sd + ds








        else:
            return "wrong input"
    except Exception   as asf:
        return "wrong input"
    av = sorted(ini_dict, key=lambda i: i['id'])
    ans=av

    return jsonify(ans)


app.run()
