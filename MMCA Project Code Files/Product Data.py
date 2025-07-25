import openpyxl
from tabulate import tabulate
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
import threading
import time


def parse_criteria(value):
    if isinstance(value, str):
        if '-' in value:
            parts = value.split('-')
            return (float(parts[0]), float(parts[1]))
        elif '≤' in value:
            return (None, float(value.replace('≤', '').strip()))
        elif '≥' in value:
            return (float(value.replace('≥', '').strip()), None)
        elif '<' in value:
            return (None, float(value.replace('<', '').strip()))
        elif '>' in value:
            return (float(value.replace('>', '').strip()), None)
        elif 'or' in value:
            parts = value.split('or')
            ranges = [parse_criteria(part.strip()) for part in parts]
            return ranges
    return (None, None)


def get_grading_criteria():
    criteria = {
        7: {
            "15 X 15 Twist Test (Index)": (1, 1),
            "Oxygen (ppm)": (225, 275),
            "25 RTF Twist Test (Number)": (35, None),
            "Oxide Content (Å)": (0, 100),
            "Aluminium (Al)": (0, 1),
            "Antimony (Sb)": (0, 1),
            "Arsenic (As)": (0, 1),
            "Bismuth (Bi)": (0, 1),
            "Cadmium (Cd)": (0, 1),
            "Iron (Fe)": (0, 6),
            "Lead (Pb)": (0, 2),
            "Nickel (Ni)": (0, 1),
            "Phosphorus (P)": (0, 1),
            "Selenium (Se)": (0, 1),
            "Sulphur (S)": (0, 8),
            "Tellurium (Te)": (0, 1),
            "Tin (Sn)": (0, 1),
            "Zinc (Zn)": (0, 2),
            "Large Defect in Defectomat": (0, 0),
            "Medium Defect in Defectomat": (0, 0),
            "Small Defect in Defectomat": (0, 5),
            "Rolling mill roll - 1": (0, 1200),
            "Rolling mill roll - 2": (0, 1200),
            "Rolling mill roll - 3": (0, 600),
            "Rolling mill roll - 4": (0, 600),
            "Rolling mill roll - 5": (0, 600),
            "Rolling mill roll - 6": (0, 600),
            "Rolling mill roll - 7": (0, 600),
            "Rolling mill roll - 8": (0, 600),
            "Rolling mill roll - 9": (0, 600),
            "Rolling mill roll - 10": (0, 600)
        },
        6: {
            "15 X 15 Twist Test (Index)": (1, 1),
            "Oxygen (ppm)": (276, 300),
            "25 RTF Twist Test (Number)": (32, 34),
            "Oxide Content (Å)": (101, 200),
            "Aluminium (Al)": (1, 2),
            "Antimony (Sb)": (0, 1),
            "Arsenic (As)": (1, 2),
            "Bismuth (Bi)": (0, 1),
            "Cadmium (Cd)": (0, 1),
            "Iron (Fe)": (6, 9),
            "Lead (Pb)": (0, 2),
            "Nickel (Ni)": (1, 3),
            "Phosphorus (P)": (0, 1),
            "Selenium (Se)": (0, 1),
            "Sulphur (S)": (8, 10),
            "Tellurium (Te)": (0, 1),
            "Tin (Sn)": (1, 3),
            "Zinc (Zn)": (0, 2),
            "Large Defect in Defectomat": (0,0),
            "Medium Defect in Defectomat": (0, 5),
            "Small Defect in Defectomat": (5, 20),
            "Rolling mill roll - 1": (1200, 1800),
            "Rolling mill roll - 2": (1200, 1800),
            "Rolling mill roll - 3": (600, 1800),
            "Rolling mill roll - 4": (600, 1800),
            "Rolling mill roll - 5": (600, 1800),
            "Rolling mill roll - 6": (600, 1800),
            "Rolling mill roll - 7": (600, 1800),
            "Rolling mill roll - 8": (600, 1800),
            "Rolling mill roll - 9": (600, 1200),
            "Rolling mill roll - 10": (600, 1200)
        },
        5: {
            "15 X 15 Twist Test (Index)": (1, 1),
            "Oxygen (ppm)": (301, 350),
            "25 RTF Twist Test (Number)": (30, 31),
            "Oxide Content (Å)": (201, 300),
            "Aluminium (Al)": (1, 2),
            "Antimony (Sb)": (1, 3),
            "Arsenic (As)": (2, 3),
            "Bismuth (Bi)": (0, 1),
            "Cadmium (Cd)": (0, 1),
            "Iron (Fe)": (9, 10),
            "Lead (Pb)": (2, 5),
            "Nickel (Ni)": (3, 5),
            "Phosphorus (P)": (1, 3),
            "Selenium (Se)": (1, 2),
            "Sulphur (S)": (8, 10),
            "Tellurium (Te)": (1, 2),
            "Tin (Sn)": (3, 5),
            "Zinc (Zn)": (2, 5),
            "Large Defect in Defectomat": (0,2),
            "Medium Defect in Defectomat": (5, 10),
            "Small Defect in Defectomat": (20, 25),
            "Rolling mill roll - 1": (1200, 1800),
            "Rolling mill roll - 2": (1200, 1800),
            "Rolling mill roll - 3": (600, 1800),
            "Rolling mill roll - 4": (600, 1800),
            "Rolling mill roll - 5": (600, 1800),
            "Rolling mill roll - 6": (600, 1800),
            "Rolling mill roll - 7": (600, 1800),
            "Rolling mill roll - 8": (600, 1800),
            "Rolling mill roll - 9": (600, 1200),
            "Rolling mill roll - 10": (600, 1200)
        },
        4: {
            "15 X 15 Twist Test (Index)": (2, 2),
            "Oxygen (ppm)": [(200, 224), (351, 400)],
            "25 RTF Twist Test (Number)": (28, 29),
            "Oxide Content (Å)": (301, 400),
            "Aluminium (Al)": (2, 5),
            "Antimony (Sb)": (3, 4),
            "Arsenic (As)": (3, 5),
            "Bismuth (Bi)": (0, 1),
            "Cadmium (Cd)": (1, 2),
            "Iron (Fe)": (10, 15),
            "Lead (Pb)": (5, 6),
            "Nickel (Ni)": (5, 10),
            "Phosphorus (P)": (3, 4),
            "Selenium (Se)": (1, 2),
            "Sulphur (S)": (10, 15),
            "Tellurium (Te)": (1, 2),
            "Tin (Sn)": (5, 100),
            "Zinc (Zn)": (5, 10),
            "Large Defect in Defectomat": (2,5),
            "Medium Defect in Defectomat": (10, 20),
            "Small Defect in Defectomat": (25, 50),
            "Rolling mill roll - 1": (1800, 2400),
            "Rolling mill roll - 2": (1800, 2400),
            "Rolling mill roll - 3": (1800, 2400),
            "Rolling mill roll - 4": (1800, 2400),
            "Rolling mill roll - 5": (1800, 2400),
            "Rolling mill roll - 6": (1800, 2400),
            "Rolling mill roll - 7": (1800, 2400),
            "Rolling mill roll - 8": (1800, 2400),
            "Rolling mill roll - 9": (1200, 1500),
            "Rolling mill roll - 10": (1200, 1500)
        },
        3: {
            "15 X 15 Twist Test (Index)": (3, 3),
            "Oxygen (ppm)": [(175, 199), (401, 450)],
            "25 RTF Twist Test (Number)": (25, 27),
            "Oxide Content (Å)": (401, 500),
            "Aluminium (Al)": (2, 5),
            "Antimony (Sb)": (3, 4),
            "Arsenic (As)": (3, 5),
            "Bismuth (Bi)": (1, 2),
            "Cadmium (Cd)": (1, 2),
            "Iron (Fe)": (10, 15),
            "Lead (Pb)": (6, 7),
            "Nickel (Ni)": (5, 10),
            "Phosphorus (P)": (4, 5),
            "Selenium (Se)": (2, 3),
            "Sulphur (S)": (10, 15),
            "Tellurium (Te)": (1, 2),
            "Tin (Sn)": (5, 100),
            "Zinc (Zn)": (10, 15),
            "Large Defect in Defectomat": (2,5),
            "Medium Defect in Defectomat": (20, 50),
            "Small Defect in Defectomat": (50, 100),
            "Rolling mill roll - 1": (1800, 2400),
            "Rolling mill roll - 2": (1800, 2400),
            "Rolling mill roll - 3": (1800, 2400),
            "Rolling mill roll - 4": (1800, 2400),
            "Rolling mill roll - 5": (1800, 2400),
            "Rolling mill roll - 6": (1800, 2400),
            "Rolling mill roll - 7": (1800, 2400),
            "Rolling mill roll - 8": (1800, 2400),
            "Rolling mill roll - 9": (1200, 1500),
            "Rolling mill roll - 10": (1200, 1500)

        },
        2: {
            "15 X 15 Twist Test (Index)": (3, 3),
            "Oxygen (ppm)": (451, 600),
            "25 RTF Twist Test (Number)": (20, 24),
            "Oxide Content (Å)": (501, 750),
            "Aluminium (Al)": (2, 5),
            "Antimony (Sb)": (3, 4),
            "Arsenic (As)": (3, 5),
            "Bismuth (Bi)": (1, 2),
            "Cadmium (Cd)": (1, 2),
            "Iron (Fe)": (15, 20),
            "Lead (Pb)": (7, 9),
            "Nickel (Ni)": (5, 10),
            "Phosphorus (P)": (4, 5),
            "Selenium (Se)": (2, 3),
            "Sulphur (S)": (10, 15),
            "Tellurium (Te)": (1, 2),
            "Tin (Sn)": (5, 100),
            "Zinc (Zn)": (15, 20),
            "Large Defect in Defectomat": (5, 10),
            "Medium Defect in Defectomat": (20, 50),
            "Small Defect in Defectomat": (50, 100),
            "Rolling mill roll - 1": (1800, 2400),
            "Rolling mill roll - 2": (1800, 2400),
            "Rolling mill roll - 3": (1800, 2400),
            "Rolling mill roll - 4": (1800, 2400),
            "Rolling mill roll - 5": (1800, 2400),
            "Rolling mill roll - 6": (1800, 2400),
            "Rolling mill roll - 7": (1800, 2400),
            "Rolling mill roll - 8": (1800, 2400),
            "Rolling mill roll - 9": (1200, 1500),
            "Rolling mill roll - 10": (1200, 1500)
        },
        1: {
            "15 X 15 Twist Test (Index)": (4, 4),
            "Oxygen (ppm)": (601, 750),
            "25 RTF Twist Test (Number)": (10, 19),
            "Oxide Content (Å)": (751, 1000),
            "Aluminium (Al)": (2, 5),
            "Antimony (Sb)": (4, 5),
            "Arsenic (As)": (3, 5),
            "Bismuth (Bi)": (1, 2),
            "Cadmium (Cd)": (2, 3),
            "Iron (Fe)": (15, 20),
            "Lead (Pb)": (9, 10),
            "Nickel (Ni)": (5, 10),
            "Phosphorus (P)": (4, 5),
            "Selenium (Se)": (2, 3),
            "Sulphur (S)": (10, 15),
            "Tellurium (Te)": (1, 2),
            "Tin (Sn)": (5, 100),
            "Zinc (Zn)": (15, 20),
            "Large Defect in Defectomat": (10, 50),
            "Medium Defect in Defectomat": (50, 100),
            "Small Defect in Defectomat": (100, 200),
            "Rolling mill roll - 1": (1800, 2400),
            "Rolling mill roll - 2": (1800, 2400),
            "Rolling mill roll - 3": (1800, 2400),
            "Rolling mill roll - 4": (1800, 2400),
            "Rolling mill roll - 5": (1800, 2400),
            "Rolling mill roll - 6": (1800, 2400),
            "Rolling mill roll - 7": (1800, 2400),
            "Rolling mill roll - 8": (1800, 2400),
            "Rolling mill roll - 9": (1200, 1500),
            "Rolling mill roll - 10": (1200, 1500)
        },
        0: {
            "15 X 15 Twist Test (Index)": (4, 4),
            "Oxygen (ppm)": (750, None),
            "25 RTF Twist Test (Number)": (0, 10),
            "Oxide Content (Å)": (751, 1000),
            "Aluminium (Al)": (5, None),
            "Antimony (Sb)": (5, None),
            "Arsenic (As)": (5, None),
            "Bismuth (Bi)": (2, None),
            "Cadmium (Cd)": (3, None),
            "Iron (Fe)": (20, None),
            "Lead (Pb)": (10, None),
            "Nickel (Ni)": (10, None),
            "Phosphorus (P)": (5, None),
            "Selenium (Se)": (3, None),
            "Sulphur (S)": (15, None),
            "Tellurium (Te)": (2, None),
            "Tin (Sn)": (100, None),
            "Zinc (Zn)": (20, None),
            "Large Defect in Defectomat": (50, 9999),
            "Medium Defect in Defectomat": (100, 9999),
            "Small Defect in Defectomat": (200, 9999),
            "Rolling mill roll - 1": None,
            "Rolling mill roll - 2": None,
            "Rolling mill roll - 3": None,
            "Rolling mill roll - 4": None,
            "Rolling mill roll - 5": None,
            "Rolling mill roll - 6": None,
            "Rolling mill roll - 7": None,
            "Rolling mill roll - 8": None,
            "Rolling mill roll - 9": None,
            "Rolling mill roll - 10": None
        },
    }
    return criteria


def is_within_range(value, value_range):
    if isinstance(value_range, list):
        return any(is_within_range(value, vr) for vr in value_range)
    min_val, max_val = value_range
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True


def determine_reason_for_decrease(criteria, test_values, test_names, grade):
    grade_criteria = criteria.get(grade, {})
    for test_name, test_value in zip(test_names, test_values):
        if test_name in grade_criteria:
            try:
                test_value_float = float(test_value)
                threshold_range = grade_criteria[test_name]
                if is_within_range(test_value_float, threshold_range):
                    return test_name
            except (TypeError, ValueError):
                continue
    return "Affected by other product parameters"


def check_coil_grades(data_file, data_sheet, start_row, end_row):
    try:
        wb_data = openpyxl.load_workbook(data_file)
        sheet_data = wb_data[data_sheet]
    except Exception as e:
        print(f"Error loading file or sheet: {e}")
        return None, None, None

    criteria = get_grading_criteria()
    rows_to_print = []
    output_header = ['S.No', 'Coil ID', '9-Digit Coil ID', 'Date', 'Grade', 'Start Time', 'End Time', 'Reason for grade decrease']
    test_names = ["15 X 15 Twist Test (Index)", "Oxygen (ppm)", "25 RTF Twist Test (Number)", "Oxide Content (Å)",
                  "Aluminium (Al)", "Antimony (Sb)", "Arsenic (As)", "Bismuth (Bi)", "Cadmium (Cd)", "Iron (Fe) (ppm)", "Lead (Pb)",
                  "Nickel (Ni)", "Phosphorus (P)", "Selenium (Se)", "Sulphur (S)", "Tellurium (Te)", "Tin (Sn)", "Zinc (Zn)",
                  "Large Defect in Defectomat", "Medium Defect in Defectomat", "Small Defect in Defectomat", "Rolling mill roll - 1",
                  "Rolling mill roll - 2", "Rolling mill roll - 3", "Rolling mill roll - 4", "Rolling mill roll - 5", "Rolling mill roll - 6",
                  "Rolling mill roll - 7", "Rolling mill roll - 8", "Rolling mill roll - 9", "Rolling mill roll - 10"]
    data_headers = [cell.value for cell in sheet_data[1]]
    test_indices = [data_headers.index(test_name) for test_name in test_names]
    coil_id_index = data_headers.index("Coil ID")
    grade_index = data_headers.index("Grade")
    nine_digit_coil_id_index = data_headers.index("9 Digit Internal Coil ID")
    date_index = data_headers.index("Date")
    start_time_index = data_headers.index("Start Time")
    end_time_index = data_headers.index("Finish Time")
    count_dict = {test_name: 0 for test_name in test_names}
    count_dict["Affected by other product parameters"] = 0

    serial_number = 1

    for row in sheet_data.iter_rows(min_row=start_row, max_row=end_row, values_only=True):
        coil_id = row[coil_id_index]
        grade = row[grade_index]
        nine_digit_coil_id = row[nine_digit_coil_id_index]
        date = row[date_index]
        start_time = row[start_time_index]
        end_time = row[end_time_index]
        test_values = [row[idx] for idx in test_indices]
        reason = determine_reason_for_decrease(criteria, test_values, test_names, grade)
        count_dict[reason] += 1
        rows_to_print.append([serial_number, coil_id, nine_digit_coil_id, date, grade, start_time, end_time, reason])
        serial_number += 1

    return rows_to_print, output_header, count_dict


# GUI application
class CoilGradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coil Grade Checker")

        self.file_label = tk.Label(root, text="Data File: None")
        self.file_label.pack()

        self.load_button = tk.Button(root, text="Load Data File", command=self.load_file)
        self.load_button.pack()

        self.start_row_label = tk.Label(root, text="Start Row:")
        self.start_row_label.pack()
        self.start_row_entry = tk.Entry(root)
        self.start_row_entry.pack()

        self.end_row_label = tk.Label(root, text="End Row:")
        self.end_row_label.pack()
        self.end_row_entry = tk.Entry(root)
        self.end_row_entry.pack()

        self.run_button = tk.Button(root, text="Run", command=self.run_check)
        self.run_button.pack()

        self.result_frame = tk.Frame(root)
        self.result_frame.pack(fill=tk.BOTH, expand=True)

        self.result_table = ttk.Treeview(self.result_frame)
        self.result_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.result_frame, orient="vertical", command=self.result_table.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_table.configure(yscrollcommand=self.scrollbar.set)

        self.count_label = tk.Label(root, text="")
        self.count_label.pack()

        self.loading_label = tk.Label(root, text="")
        self.loading_label.pack()

    def load_file(self):
        file_path = filedialog.askopenfilename()
        self.file_label.config(text=f"Data File: {file_path}")
        self.data_file = file_path

    def run_check(self):
        try:
            start_row = int(self.start_row_entry.get())
            end_row = int(self.end_row_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Start Row and End Row must be integers")
            return

        self.loading_label.config(text="Loading...")
        threading.Thread(target=self.run_check_in_background, args=(start_row, end_row)).start()

    def run_check_in_background(self, start_row, end_row):
        rows_to_print, output_header, count_dict = check_coil_grades(self.data_file, "Master_Simplified", start_row, end_row)

        if rows_to_print is None:
            self.loading_label.config(text="")
            messagebox.showerror("File Error", "There was an error processing the file.")
            return

        for i in self.result_table.get_children():
            self.result_table.delete(i)

        self.result_table["columns"] = output_header
        self.result_table["show"] = "headings"

        for col in output_header:
            self.result_table.heading(col, text=col)
            self.result_table.column(col, width=100)

        for row in rows_to_print:
            self.result_table.insert("", "end", values=row)

        count_text = "\n".join([f"{reason}: {count}" for reason, count in count_dict.items()])
        self.count_label.config(text=f"Count of coils affected by each parameter:\n{count_text}")
        self.loading_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = CoilGradeApp(root)
    root.mainloop()