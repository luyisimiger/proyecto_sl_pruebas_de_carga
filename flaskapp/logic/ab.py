
import subprocess

def runab(args):
    
    # r = subprocess.run(["ab", "-c", "5", "-n", "20", "http://www.github.com/"], capture_output=True)
    r = subprocess.run(args, capture_output=True)
    stdout = str(r.stdout)
    salida = r.stdout.decode("utf-8")
    # print(stdout)

    data = dict()
    data["salida"] = salida

    out_lines = stdout.split("\\n")

    keys = [("time_per_request", "Time per request"), ("transfer_rate", "Transfer rate"), ("total_transferred", "Total transferred")]
    process_porc = False

    for l in out_lines:

        for x, k in keys:

            if l.startswith(k):
                v = l.split(":")[1]
                v = v.strip()
                if x not in data:
                    data[x] = v

        if process_porc:
            
            l1 = l.strip().split()
            
            if len(l1) >= 2:
                p = {
                    "porc": int(l1[0].replace("%", "")),
                    "ms": int(l1[1])
                }
                
                data["porc"].append(p)

        if l == "Percentage of the requests served within a certain time (ms)":
            data["porc"] = []
            process_porc = True

    return data
