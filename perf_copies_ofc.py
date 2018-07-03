"""Benchmarks with perf for the functions in the copies module"""

import sys

import perf

from speedsurprises.text import copies


def bench_copy_function(copy_function, chosen_size):
    """Run a copy benchmark for a copy_function and a chosen_size"""
    copy_function(chosen_size)


# Example of calling the function:
# copied_character_string = copies.mcopies_ofc(copies_as_string)

if __name__ == "__main__":
    # read the chosen_size
    filepath = "configuration.txt"
    with open(filepath) as fp:
        chosen_size = fp.readline().replace("\n", "")
    # configure perf
    runner = perf.Runner()
    # configure the run of the benchmark
    experiment_name = "mcopies_ofc" + str(chosen_size)
    runner.metadata["description"] = experiment_name
    # run the perf benchmark for the function
    benchmark = runner.bench_func(
        "mcopies", bench_copy_function, copies.mcopies_ofc, chosen_size
    )
    # save the perf results from running the benchmark
    benchmark.dump("results/" + experiment_name + ".json", compact=False, replace=True)