import subprocess
import openpyxl

def get_file_size(folder_path, line_number):

    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    worksheet["A1"] = "File Name"
    worksheet["B1"] = "Size"
    worksheet["C1"] = "Time"
    worksheet["D1"] = "Status"

    line_count = 0

    command = f"du -h ./ceyline_pg_backup/{folder_path}/*"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    while len(result.stdout.splitlines()) > line_count:
      
        omitted_results = result.stdout.split("\n")[line_count].split("\t")

        time = omitted_results[1].split("\t")[0].split("/")[2].split("-")[3]

        file_size = omitted_results[0]
        file_name = omitted_results[1].split("/")[3]

        if result.stdout.split("\n")[line_count].split("\t")[1].split("/")[3].split(".")[1] == "custom":
            if len(file_name.split(".")) == 3:
                status = "In Progress"
                file_name = file_name.split(".")[0] + "." + file_name.split(".")[1]
                file_size = "-"
            else:
                status = "Completed"
        
        print(f"{file_name},{file_size},{time},{status}")

        place_holder_value_1 = "A" + str(line_number + 1)
        place_holder_value_2 = "B" + str(line_number + 1)
        place_holder_value_3 = "C" + str(line_number + 1)
        place_holder_value_4 = "D" + str(line_number + 1)

        worksheet[place_holder_value_1] = file_name
        worksheet[place_holder_value_2] = file_size
        worksheet[place_holder_value_3] = time
        worksheet[place_holder_value_4] = status

        line_count += 1
        line_number += 1
        
    
    workbook.save("doc_name.xlsx")
    # print(line_number)
    return line_number
