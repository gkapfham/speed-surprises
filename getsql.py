import sqlite3

if __name__ == "__main__":
    connection = sqlite3.connect(".coverage")

    cursor = connection.cursor()

    # for row in cursor.execute('SELECT * FROM arc'):
    #     print(row)

    # for row in cursor.execute('SELECT * FROM arc where file_id = 10'):
    #     print(row)
    '''
    context_id = 1, context = null
    (10, 1, -1, 1)
    (10, 1, 1, 3)
    (10, 1, 3, 5)
    (10, 1, 5, 6)
    (10, 1, 6, 7)
    (10, 1, 7, 8)
    (10, 1, 8, 10)
    (10, 1, 10, 13)
    (10, 1, 13, 20)
    (10, 1, 20, 27)
    (10, 1, 27, 34)
    (10, 1, 34, 35)
    (10, 1, 35, 36)
    (10, 1, 36, 56)
    (10, 1, 56, 57)
    (10, 1, 57, 58)
    (10, 1, 58, 70)
    (10, 1, 70, -1)
    context_id = 28, context = tests/test_factorial.py::test_iterative_factorial_benchmark|call
    (10, 28, -13, 16)
    (10, 28, 16, 17)
    (10, 28, 17, -13)
    context_id = 29, context = tests/test_factorial.py::test_recursive_factorial_benchmark|call
    (10, 29, -20, 23)
    (10, 29, 23, 24)
    (10, 29, 24, -20)
    context_id = 30, context = tests/test_factorial.py::test_hashmap_recursive_factorial_benchmark|call
    (10, 30, -27, 30)
    (10, 30, 30, 31)
    (10, 30, 31, -27)
    context_id = 31, context = tests/test_factorial.py::test_factorial_hypothesis|call
    (10, 31, -34, 35)
    (10, 31, -34, 39)
    (10, 31, 35, -34)
    (10, 31, 39, 40)
    (10, 31, 40, 41)
    (10, 31, 41, 42)
    (10, 31, 42, 43)
    (10, 31, 43, 44)
    (10, 31, 44, 45)
    (10, 31, 45, -34)
    context_id = 32, context = tests/test_factorial.py::test_factorial_multiple[1-1]|call
    (10, 32, -56, 62)
    (10, 32, 62, 63)
    (10, 32, 63, 64)
    (10, 32, 64, 65)
    (10, 32, 65, -56)
    context_id = 33, context = tests/test_factorial.py::test_factorial_multiple[2-2]|call
    (10, 33, -56, 62)
    (10, 33, 62, 63)
    (10, 33, 63, 64)
    (10, 33, 64, 65)
    (10, 33, 65, -56)
    context_id = 34, context = tests/test_factorial.py::test_factorial_multiple[3-6]|call
    (10, 34, -56, 62)
    (10, 34, 62, 63)
    (10, 34, 63, 64)
    (10, 34, 64, 65)
    (10, 34, 65, -56)
    context_id = 35, context = tests/test_factorial.py::test_factorial_multiple[4-24]|call
    (10, 35, -56, 62)
    (10, 35, 62, 63)
    (10, 35, 63, 64)
    (10, 35, 64, 65)
    (10, 35, 65, -56)
    context_id = 36, context = tests/test_factorial.py::test_factorial_single|call
    (10, 36, -70, 72)
    (10, 36, 72, 73)
    (10, 36, 73, 74)
    (10, 36, 74, 75)
    (10, 36, 75, -70)
    '''
    results1 = []

    for row in cursor.execute('SELECT * FROM arc where file_id = 11 and context_id = 1'):
        # print(row)
        results1.append(row[2])

    print(results1)
    start = results1[0]
    end = results1[-1]

    for i in (start, end) not in 

    '''
    context_id = 1, context = null
    (11, 1, -1, 1)
    (11, 1, 1, 9)
    (11, 1, 9, 21)
    (11, 1, 21, 28)
    (11, 1, 28, 36)
    (11, 1, 36, 46)
    (11, 1, 46, 51)
    (11, 1, 51, 56)
    (11, 1, 56, -1)
    context_id = 28, context = tests/test_factorial.py::test_iterative_factorial_benchmark|call
    (11, 28, -9, 12)
    (11, 28, 12, 14)
    (11, 28, 14, 15)
    (11, 28, 15, 16)
    (11, 28, 15, 18)
    (11, 28, 16, 17)
    (11, 28, 17, 15)
    (11, 28, 18, -9)
    context_id = 29, context = tests/test_factorial.py::test_recursive_factorial_benchmark|call
    (10, 29, -20, 23)
    (11, 29, -21, 22)
    (11, 29, 22, 23)
    (11, 29, 22, 25)
    (11, 29, 23, -21)
    (11, 29, 25, -21)
    context_id = 30, context = tests/test_factorial.py::test_hashmap_recursive_factorial_benchmark|call
    (11, 30, -28, 29)
    (11, 30, 29, 30)
    (11, 30, 30, 31)
    (11, 30, 30, 32)
    (11, 30, 31, 32)
    (11, 30, 32, -28)
    context_id = 31, context = tests/test_factorial.py::test_factorial_hypothesis|call
    (11, 31, -28, 29)
    (11, 31, -21, 22)
    (11, 31, -9, 12)
    (11, 31, 12, 14)
    (11, 31, 14, 15)
    (11, 31, 15, 16)
    (11, 31, 15, 18)
    (11, 31, 16, 17)
    (11, 31, 17, 15)
    (11, 31, 18, -9)
    (11, 31, 22, 23)
    (11, 31, 22, 25)
    (11, 31, 23, -21)
    (11, 31, 25, -21)
    (11, 31, 29, 30)
    (11, 31, 30, 31)
    (11, 31, 30, 32)
    (11, 31, 31, 32)
    (11, 31, 32, -28)
    context_id = 32, context = tests/test_factorial.py::test_factorial_multiple[1-1]|call
    (11, 32, -28, 29)
    (11, 32, -21, 22)
    (11, 32, -9, 12)
    (11, 32, 12, 14)
    (11, 32, 14, 15)
    (11, 32, 15, 16)
    (11, 32, 15, 18)
    (11, 32, 16, 17)
    (11, 32, 17, 15)
    (11, 32, 18, -9)
    (11, 32, 22, 23)
    (11, 32, 22, 25)
    (11, 32, 23, -21)
    (11, 32, 25, -21)
    (11, 32, 29, 30)
    (11, 32, 30, 31)
    (11, 32, 30, 32)
    (11, 32, 31, 32)
    (11, 32, 32, -28)
    context_id = 33, context = tests/test_factorial.py::test_factorial_multiple[2-2]|call
    (11, 33, -28, 29)
    (11, 33, -21, 22)
    (11, 33, -9, 12)
    (11, 33, 12, 14)
    (11, 33, 14, 15)
    (11, 33, 15, 16)
    (11, 33, 15, 18)
    (11, 33, 16, 17)
    (11, 33, 17, 15)
    (11, 33, 18, -9)
    (11, 33, 22, 23)
    (11, 33, 22, 25)
    (11, 33, 23, -21)
    (11, 33, 25, -21)
    (11, 33, 29, 30)
    (11, 33, 30, 31)
    (11, 33, 30, 32)
    (11, 33, 31, 32)
    (11, 33, 32, -28)
    context_id = 34, context = tests/test_factorial.py::test_factorial_multiple[3-6]|call
    (11, 34, -28, 29)
    (11, 34, -21, 22)
    (11, 34, -9, 12)
    (11, 34, 12, 14)
    (11, 34, 14, 15)
    (11, 34, 15, 16)
    (11, 34, 15, 18)
    (11, 34, 16, 17)
    (11, 34, 17, 15)
    (11, 34, 18, -9)
    (11, 34, 22, 23)
    (11, 34, 22, 25)
    (11, 34, 23, -21)
    (11, 34, 25, -21)
    (11, 34, 29, 30)
    (11, 34, 30, 31)
    (11, 34, 30, 32)
    (11, 34, 31, 32)
    (11, 34, 32, -28)
    context_id = 35, context = tests/test_factorial.py::test_factorial_multiple[4-24]|call
    (11, 35, -28, 29)
    (11, 35, -21, 22)
    (11, 35, -9, 12)
    (11, 35, 12, 14)
    (11, 35, 14, 15)
    (11, 35, 15, 16)
    (11, 35, 15, 18)
    (11, 35, 16, 17)
    (11, 35, 17, 15)
    (11, 35, 18, -9)
    (11, 35, 22, 23)
    (11, 35, 22, 25)
    (11, 35, 23, -21)
    (11, 35, 25, -21)
    (11, 35, 29, 30)
    (11, 35, 30, 31)
    (11, 35, 30, 32)
    (11, 35, 31, 32)
    (11, 35, 32, -28)
    context_id = 36, context = tests/test_factorial.py::test_factorial_single|call
    (11, 36, -28, 29)
    (11, 36, -21, 22)
    (11, 36, -9, 12)
    (11, 36, 12, 14)
    (11, 36, 14, 15)
    (11, 36, 15, 16)
    (11, 36, 15, 18)
    (11, 36, 16, 17)
    (11, 36, 17, 15)
    (11, 36, 18, -9)
    (11, 36, 22, 23)
    (11, 36, 22, 25)
    (11, 36, 23, -21)
    (11, 36, 25, -21)
    (11, 36, 29, 30)
    (11, 36, 30, 31)
    (11, 36, 30, 32)
    (11, 36, 31, 32)
    (11, 36, 32, -28)
    '''
    # for row in cursor.execute('SELECT * FROM arc where context_id = 28'):
    #     print(row)
    '''
    file_id = 10, path = /home/w/wuj/cs591F2018/speed-surprises_test/tests/test_factorial.py
    (10, 28, -13, 16)
    (10, 28, 16, 17)
    (10, 28, 17, -13)
    file_id = 11, path = /home/w/wuj/cs591F2018/speed-surprises_test/speedsurprises/numbers/factorial.py
    (11, 28, -9, 12)
    (11, 28, 12, 14)
    (11, 28, 14, 15)
    (11, 28, 15, 16)
    (11, 28, 16, 17)
    (11, 28, 17, 15)
    (11, 28, 15, 18)
    (11, 28, 18, -9)
    '''
