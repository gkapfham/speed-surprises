"""Configuration file for the test suites"""

import os
import sys
import pytest
import sqlite3

# set the system path to contain the previous directory
# because it is the root directory that contains the
# directory for the package, sub-packages, and modules
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + "/../")
contextlist = []
idlist = []
filelist = ["/home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/boolean/booleancopies.py",
"/home/w/wuj/cs591F2018/speed-surprises_test/tests/test_b_copies_oft.py",
"/home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/text/copies.py",
"/home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/numbers/factorial.py",
"/home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/numbers/fibonacci.py",
"/home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/lists/sets.py",
"/home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/lists/sorting.py",
"/home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/numbers/squareroot.py",
"/home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/text/string_reverser.py",
"/home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/app.py"
]
result = []
filecalled = []
excutableline = []


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    # __init__(self, nodeid, location, keywords, outcome, longrepr, when, sections=(), duration=0, user_properties=None, **extra)
    if report.when == 'call':
        # always add url to report
        # if report.failed:
        currentcontext = report.nodeid + "|call"
        contextlist.append(currentcontext)
            # for row in cursor.execute('SELECT * FROM context'):
                # if (row[1] == currentcontext):
                #     currentcontextid = row[0]
                #     print(currentcontextid)
            # for row in cursor.execute('SELECT * FROM arc where context_id = %d' % currentcontextid):
            #     print(row)


def locatemissingline():
    fileidlist =[]
    connection = sqlite3.connect(".coverage")
    cursor = connection.cursor()
    for row2 in cursor.execute('SELECT * FROM file'):
        for file in filelist:
            if (row2[1] == file):
                fileidlist.append(row2[0])
    connection.commit()
    connection.close()
    connection2 = sqlite3.connect(".coverage")
    cursor2 = connection2.cursor()
    for row in cursor2.execute('SELECT * FROM context'):
        for item in contextlist:
            if (row[1] == item and row[0] not in idlist):
                currentcontextid = row[0]
                idlist.append(currentcontextid)
                # path = os.path.abspath(os.curdir)
                # # "/" acn be different
                # file = path + "/" + row[1].split("::")[0]
                # for row2 in cursor.execute('SELECT * FROM file'):
                #     if (row2[1] == file):
                #         currentfileid = row2[0]
                #         fileidlist.append(currentfileid)
                # for row3 in cursor.execute('SELECT * FROM arc where context_id = %d and file_id = %c' % (currentcontextid, currentfileid)):
    for currentcontextid in idlist:
        for row3 in cursor2.execute('SELECT * FROM arc where context_id = %d' % currentcontextid):
            for fileid in fileidlist:
                if (row3[0] == fileid):
                    result.append(row3)
                    if (row3[0] not in filecalled):
                        filecalled.append(row3[0])

    # print(contextlist)
    # print(idlist)
    # print(fileidlist)
    connection2.commit()
    connection2.close()


def pytest_sessionfinish(session, exitstatus):
    locatemissingline()
    connection3 = sqlite3.connect(".coverage")
    cursor3 = connection3.cursor()
    for runfile in filecalled:
        missingline = []
        initialfile = [row4 for row4 in cursor3.execute('SELECT * FROM arc where file_id = %d' % runfile) if row4[1] == 1]
        firstline = initialfile[1][3]
        lastline = initialfile[-1][2]
        excutefile = [data for data in result if data[0] == runfile]
        bound = [data[2] and data[3] for data in excutefile]
        for num in range(firstline, lastline + 1):
            if num not in bound:
                missingline.append(num)
        print("file id:", runfile, "missing covered line:", missingline)
