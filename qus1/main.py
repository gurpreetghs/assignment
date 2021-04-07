from flask import *
import json
import datetime

app = Flask(__name__)
app.config["Debug"] = True


@app.route('/<string:strdt>/<string:endt>')
def inptts(strdt, endt):
    strdt = strdt
    endt = endt

    # @app.route('/output')
    # def pros() :
    #     strdt=request.args.get('strdt')
    #     endt = request.args.get('endt')
    f = open('sample_json_1.json')
    inp = json.load(f)
    fna = 0
    fnb = 0

    stm = strdt
    etm = endt
    try:
        if stm[-1] == "Z" and stm[10] == "T":
            if etm[-1] == "Z" and etm[10] == "T":

                stm = stm.replace("-", " ").replace("/", " ").replace("T", " ").replace("Z", " ")
                a = stm

                b = etm.replace("-", " ").replace("/", " ").replace("T", " ").replace("Z", " ")
                sd = datetime.datetime(year=int(a[0:4]), month=int(a[5:7]), day=int(a[8:10]), hour=int(a[11:13]),
                                       minute=int(a[14:16]), second=int(a[17:18]))
                ed = datetime.datetime(year=int(b[0:4]), month=int(b[5:7]), day=int(b[8:10]), hour=int(b[11:13]),
                                       minute=int(b[14:16]), second=int(b[17:18]))
                ds = datetime.timedelta(seconds=1)
                while sd <= ed:
                    for dt in inp:

                        if dt.get('time') == str(sd):

                            if dt.get('production_A') == True:

                                fna = fna + 1
                            else:
                                pass
                            if dt.get('production_B') == True:
                                fnb = fnb + 1
                            else:
                                pass
                        else:
                            pass
                    sd = sd + ds


        else:
            return "wrong input"
    except Exception   as asf:
        return "wrong input"
    ans = {
        "shiftA": {"production_A_count": fna, "production_B_count": fnb},
        "shiftB": {"production_A_count": fna, "production_B_count": fnb},
        "shiftC": {"production_A_count": fna, "production_B_count": fnb},
          }

    return jsonify(ans)


app.run()
