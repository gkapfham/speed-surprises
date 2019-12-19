import sqlite3

contextlist = ["tests/test_b_copies_oft.py::test_count_benchmark|call"]
idlist = []
fileidlist =[]
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

def locatemissingline():
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
                print("1")
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
                    print(row3)
    print(contextlist)
    print(idlist)
    # print(fileidlist)

locatemissingline()
