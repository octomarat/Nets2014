from subprocess import Popen

# paths
CLIENT_JAR_PATH = "/home/mrx/GitRepos/Nets2014/HighLoadServer/Client/out/artifacts/Client_jar/Client.jar"
LOGS_DST_PATH = "/home/mrx/GitRepos/Nets2014/HighLoadServer/Experiments/logs/"

# client program args
SERVER_IP = "127.0.0.1"
SERVER_PORT = "45213"
EQUATIONS_NUM = 10

#runner options
TESTS_NUM = 1
CLIENTS_NUM = 10

def run(tests_num, clients_num, equations_num):
    for i in xrange(0, tests_num):
        print "test " + str(i)
        processes = []
        for j in xrange(0, clients_num):
            logPath = LOGS_DST_PATH + str(equations_num) + "_" + str(i) + "_" + str(j)
            proc = Popen(["java", "-jar", CLIENT_JAR_PATH, SERVER_IP, SERVER_PORT, str(equations_num), logPath])
            processes.append(proc)
        for proc in processes:
            proc.communicate()
            

# main
run(TESTS_NUM, CLIENTS_NUM, EQUATIONS_NUM)