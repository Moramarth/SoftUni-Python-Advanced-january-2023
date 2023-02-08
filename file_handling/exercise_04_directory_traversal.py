import os


def traversal_func(directory, can_search_deeper=True):
    items_in_directory = os.listdir(directory)

    for item in items_in_directory:
        current_file = os.path.join(directory, item)

        if os.path.isfile(current_file):
            extension = item.split(".")[-1]

            if extension not in report_data:
                report_data[extension] = []
            report_data[extension].append(item)

        elif os.path.isdir(current_file) and can_search_deeper:
            traversal_func(current_file, can_search_deeper=False)


directory_to_scan = input()
report_data = dict()
result = list()

traversal_func(directory_to_scan)
report_data = sorted(report_data.items(), key= lambda x: x[0])

for file_type, file_name in report_data:
    result.append(f".{file_type}")

    for file in sorted(file_name):
        result.append(f"- - - {file}")

with open("report.txt", "w") as final_report:
    final_report.write("\n".join(result))
