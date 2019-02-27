"""Main file for Speed-Surprises Benchmarking Tool."""

# Imports:
import getopt
import importlib
from inspect import *
import sys
import time

# Set defaults:
input_size_start = 100
input_growth_factor = 2
previous_time = 1


def get_num_of_rounds():
    """Recieves user-inputted number of rounds for experiment."""
    user_rounds = int(input("Please specify a number of rounds: "))
    return user_rounds


def generate_data(current_size, types):
    """Generates data to be used in experiment."""
    num_params = len(types)
    bench_data = []

    for current_type in types:
        if current_type == "int":
            # generate int
            bench_data.append(int(current_size))
        elif current_type == "float":
            # generate float
            default_float = 1.0
            gen_data = default_float * current_size
            bench_data.append(gen_data)
        elif current_type == "list":
            # generate list
            default_list = [1]
            gen_data = default_list * current_size
            bench_data.append(gen_data)
        elif current_type == "string":
            # generate string
            default_string = "str"
            gen_data = default_string * current_size
            bench_data.append(gen_data)
        elif current_type == "char":
            # generate char
            default_char = "c"
            gen_data = default_char * current_size
            bench_data.append(gen_data)
        else:
            print("Unsupported data type:", current_type)

    params = bench_data
    print("TEST_PARAMS", params)
    return params


def run_benchmark(previous_time, user_module, function, types, run_function, user_rounds):
    current_size = input_size_start

    round_num = 1 # set the starting round number

    while(round_num <= user_rounds):
        current_size = current_size * input_growth_factor

        params = generate_data(current_size, types)

        start_time = time.time()

        run_function(*params) # run the function with data size

        stop_time = time.time()
        time_elapsed = stop_time - start_time

        if(round_num == 1):
            avg_runtime = 0
        else:
            avg_runtime = time_elapsed / previous_time

        print("Round", round_num, " --- Size:", current_size, " --- ", time_elapsed, " --- AVG RUN: ", avg_runtime) # print results

        previous_time = time_elapsed
        round_num += 1


def start_up_message(function):
    """Creates and displays a simple welcome message."""
    print("****************************************************************")
    print("*          Speed-Surprises Simple Benchmarking Tool            *")
    print("****************************************************************")
    print() # print balnk line for spacing


def main(argv):
    module = ""
    function = ""
    types = []

    try:
        opts, args = getopt.getopt(argv, "m:f:t:h", ["module=", "function=", "types=",  "help"])
    except getopt.GetoptError:
        print("Incorrect Format!")
        print("benchmark.py -m <module> -f <function> -t <types>")
        print() # print blank line for spacing
        print("Type benchmark.py -h for more help.")
        print() # print blank line for spacing
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            # program help information
            print("****************************************************************")
            print("*                      S-S Benchmark Help:                     *")
            print("****************************************************************")
            print() # print blank line for spacing
            print("Format:  benchmark.py -m <module> -f <function> -t <types>")
            print() # print blank line for spacing
            print("Sample Usage:")
            print("python3 benchmark.py -m speedsurprises.numbers.factorial -f compute_factorial -t int")
            print("python3 benchmark.py -m speedsurprises.lists.sets -f is_subset -t list,list")
            print() # print blank line for spacing
            print("Currently supported types: int, float, list, string, char")
            print() # print blank line for spacing
            print("* When entering types, for each parameter in your chosen function put it's type. \nFor example, if a functions paramters are two lists, enter 'list,list' for the types.")
            sys.exit(2)
        elif opt in ("-m", "--module"):
            module = arg
        elif opt in ("-f", "--function"):
            function = arg
        elif opt in ("-t", "--types"):
            types = arg.replace(' ','').split(',')
        else:
            print("benchmark.py -m <module> -f <function> -t <types>")

    # print the user's inputted arguments for testing purposes
    print("***User Arguments***")
    print("Module:", module)
    print("Function:", function)
    print("types:", types)

    user_module = importlib.import_module(module)
    run_function = getattr(user_module, function)

    start_up_message(function)

    user_rounds = get_num_of_rounds()

    print() # print blank line for spacing
    print("Running a doubling-experiment benchmark for", function, "...")

    # run the benchmark
    run_benchmark(previous_time, user_module, function, types, run_function, user_rounds)

# run main - run program
if __name__ == "__main__":
   main(sys.argv[1:])
