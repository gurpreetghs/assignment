from flask import *
import json
import datetime
import time

app = Flask(__name__)
app.config["Debug"] = True


@app.route('/<string:strdt>/<string:endt>')
def inptts(strdt, endt):
    strdt=strdt
    endt=endt

    f = open('sample_json_2.json')
    inp = json.load(f)
    fna = 0
    fnb = 0
    pqw = 1021

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

                            xz = dt.get('runtime')

                            if xz <= pqw:
                                print("ggg")
                                fna = fna + xz
                                yz = dt.get('downtime')
                                fnb = fnb + yz
                            else:
                                tq = xz - pqw
                                fna = pqw
                                yz = dt.get('downtime')
                                fnb = fnb + yz + tq
                    sd = sd + ds



        else:
            return "wrong input"
    except Exception   as asf:
        return "wrong input"

    utilisation = (fna) / (fna + fnb) * 100
    foa = time.strftime("%H:%M:%S",time.gmtime(fna))
    fob = time.strftime("%H:%M:%S",time.gmtime(fnb))
    fnz=str(foa)
    fnx=str(fob)
    nurt=fnz[0:1]+'hours'+","+fnz[2:4]+"min"+","+fnz[5:8]+"sec"
    nudt = fnx[0:1] + 'hours' + "," + fnx[2:4] + "min" + "," + fnx[5:8] + "sec"



    ans = {
"runtime" : nurt,
"downtime": nudt,
"utilisation": utilisation
}

    return jsonify(ans)


app.run()
