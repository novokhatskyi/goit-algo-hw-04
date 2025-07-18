import random
import timeit
from sort_algorithms import merge_sort, insertion_sort, sort_by_timsort
from rich.table import Table
from rich.console import Console
import matplotlib.pyplot as plt

def generate_lists():
    random_sets = []
    sizes = [5000, 10000, 20000]
    for size in sizes:
        data = [random.randint(1, 1000000) for _ in range(size)]
        random_sets.append({"size": size, "data": data})
    return random_sets

def time_for_set(random_sets, sort_func, number=10):
    results = []
    for data_dict in random_sets:
        size = data_dict["size"]
        data = data_dict["data"]

        for func in sort_func:
            timer = timeit.timeit(lambda: func(data.copy()), number=number)
            results.append({"Алгоритм": func.__name__,"Розмір": size,"Час (сек)": timer})
    return results

def analysis_of_results(results):
    console = Console()
    table = Table(title="Порівняння алгоритмів сортування")

    table.add_column("Алгоритм", justify="left", style="cyan", no_wrap=True)
    table.add_column("Розмір списку", justify="right", style="magenta")
    table.add_column("Час виконання (сек)", justify="right", style="green")

    for record in results:
        table.add_row(
            record["Алгоритм"],
            str(record["Розмір"]),
            f"{record['Час (сек)']:.4f}"
        )

    console.print(table)

def plot_results(results):
    # Збираємо унікальні назви алгоритмів і розміри списків
    algorithms = list(set(record["Алгоритм"] for record in results))
    sizes = sorted(list(set(record["Розмір"] for record in results)))

    # Для кожного алгоритму — зберемо список часів у тому ж порядку, що і sizes
    for algo in algorithms:
        times = [record["Час (сек)"] for record in results if record["Алгоритм"] == algo]
        plt.plot(sizes, times, marker='o', label=algo)

    plt.xlabel("Розмір списку")
    plt.ylabel("Час виконання (сек)")
    plt.title("Порівняння алгоритмів сортування")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    random_sets = generate_lists()
    sort_func = [insertion_sort, merge_sort, sort_by_timsort]

    results = time_for_set(random_sets, sort_func, number=10)
    analysis_of_results(results)

    random_sets = generate_lists()
    sort_func = [merge_sort, insertion_sort, sort_by_timsort]
    results = time_for_set(random_sets, sort_func, number=10)
    analysis_of_results(results)
    plot_results(results)