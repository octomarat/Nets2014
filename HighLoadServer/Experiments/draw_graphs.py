import json
import operator

LOGS_DST_PATH = "./logs/"
EQUATIONS_NUM_LIST = [50, 100, 200, 400]

#runner options
TESTS_NUM = 3
CLIENTS_NUM_LIST = xrange(1, 100, 10)

def get_vals(filePath):
    """
    {
        "gen_task" : time,
        "beg_send" : time,
        "end_send" : time,
        "beg_resp" : time,
        "end_resp" : time
    }
    """
    json_data = open(filePath)
    data = json.load(json_data)

    beg_send = long(data["beg_send"])
    end_send = long(data["end_send"])
    beg_resp = long(data["beg_resp"])
    end_send = long(data["end_send"])

    send_time = end_send - beg_send
    resp_time = end_resp - beg_resp
    full_time = end_resp

    json_data.close()

    return (send_time, resp_time, full_time)

def get_mean_vals(vals_list):
    zero = (0, 0, 0)
    acc = reduce(lambda a, b: tuple(map(operator.add, a, b)), vals_list, zero)
    length = float(len(vals_list))
    return tuple(map(lambda x: x / length, acc))

def run(tests_num, clients_num, equations_num):
    tests_vals = []
    for i in xrange(0, tests_num):
        clients_vals = []
        for j in xrange(0, clients_num):
            logPath = LOGS_DST_PATH + str(equations_num) + "_" + str(i) + "_" + str(j)
            clients_vals.append(get_vals(logPath))
        tests_vals.append(get_mean_vals(clients_vals))
    return get_mean_vals(tests_vals)

            

# main
for eq_num in EQUATIONS_NUM_LIST:
    points = []
    for clients_number in CLIENTS_NUM_LIST):
        mean_vals = run(TESTS_NUM, clients_num, eq_num)
        points.append((clients_number, mean_vals))
    # draw
    print points
    print "\n"