import time
import random
from typing import List
import statistics


class SortingTester:
    def __init__(self, array_size=10_000, min_val=0, max_val=1000):
        self.array_size = array_size
        self.min_val = min_val
        self.max_val = max_val
        self.generated_array = list()

    def generate_random_array(self) -> List[int]:
        for _ in range(self.array_size):
            self.generated_array.append(random.randint(self.min_val, self.max_val))

        return self.generated_array.copy()

    def measure_sorting_time(self, sort_function, array_to_sort, number_of_runs=1) -> tuple[float, List[int]]:
        execution_times = list()
        sorted_result = None

        for _ in range(number_of_runs):
            test_array_copy = array_to_sort.copy()

            start_time = time.perf_counter()
            sorted_array = sort_function(test_array_copy)
            end_time = time.perf_counter()

            sorted_result = sorted_array
            execution_times.append(end_time - start_time)

        average_time = statistics.mean(execution_times)

        return average_time, sorted_result
    
    def is_sorted(self, arr: List[int]) -> bool:
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


    def test_sorting_algorithm(self, sort_function, number_of_different_arrays=5, runs_per_array=3) -> dict:
        test_results = {
            "algorithm_name": sort_function.__name__,
            "array_size": self.array_size,
            "number_of_tested_arrays": number_of_different_arrays,
            "runs_per_array": runs_per_array,
            "execution_times_per_array": [],
            "average_execution_time": 0,
            "minimum_time": 0,
            "maximum_time": 0,
        }

        print(f"testing {sort_function.__name__}...")

        for array_index in range(number_of_different_arrays):
            current_test_array = self.generate_random_array()
            average_time_for_array, sorted_array = self.measure_sorting_time(
                sort_function, current_test_array, runs_per_array
            )
            
            if not self.is_sorted(sorted_array):
                print(f"Алгоритм {sort_function.__name__} не отсортировал массив правильно")

            
            test_results["execution_times_per_array"].append(average_time_for_array)

        test_results["average_execution_time"] = statistics.mean(test_results["execution_times_per_array"])
        test_results["minimum_time"] = min(test_results["execution_times_per_array"])
        test_results["maximum_time"] = max(test_results["execution_times_per_array"])

        return test_results

    def compare_sorting_algorithms(self, algorithms_list, number_of_different_arrays=5, runs_per_array=3) -> List[dict]:
        comparison_results = list()

        print()
        print(f"array sizes: {self.array_size}")
        print(f"arrays amount: {number_of_different_arrays}")
        print(f"one array runs: {runs_per_array}")
        print()

        for algorithm in algorithms_list:
            algorithm_results = self.test_sorting_algorithm(
                algorithm, number_of_different_arrays, runs_per_array
            )
            comparison_results.append(algorithm_results)

        return comparison_results

    def display_comparison_results(self, results) -> None:
        # Сортировка по времени выполнения алгоритма
        results.sort(key=lambda x: x["average_execution_time"])
        
        print()

        for position, result in enumerate(results, 1):
            print(f"{position}. {result['algorithm_name']}:")
            print(f"   avg: {result['average_execution_time']:.6f}")
            print(f"   min: {result['minimum_time']:.6f}")
            print(f"   max: {result['maximum_time']:.6f}")
            print(f"   arrays time: {[f'{t:.6f}' for t in result['execution_times_per_array']]}")
            print()


if __name__ == "__main__":
    from lab4 import comb_sort
    from lab5 import insertion_sort
    from lab6 import selection_sort
    from lab7 import shell_sort
    from lab8 import radix_sort
    from lab9 import heap_sort
    from lab10 import merge_sort
    from lab11 import quick_sort

    tester = SortingTester(array_size=10 ** 6, min_val=-1000, max_val=1000)
    algorithms_to_test = [
        # comb_sort,
        # insertion_sort,
        # selection_sort,
        # shell_sort,
        # radix_sort,
        # heap_sort,
        # merge_sort,
        quick_sort,
    ]

    test_results = tester.compare_sorting_algorithms(
        algorithms_to_test, number_of_different_arrays=1, runs_per_array=1
    )

    tester.display_comparison_results(test_results)
