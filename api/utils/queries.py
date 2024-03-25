import os
from sqlalchemy import text
import csv
from utils.connection import *

# Folder for output files
data_folder = "data"

# Class containing the query for the first requirement
class HiresPerQuarter:
    def __init__(self):
        self.engine = connect_to_database()
        self.output_folder = os.path.join(os.path.dirname(__file__), "data")
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def hires_per_quarter(self):
        with self.engine.connect() as conn:
            query = text("""SELECT 
                d.department AS department,
                j.job AS job,
                SUM(CASE WHEN EXTRACT(QUARTER FROM TO_DATE(he.datetime, 'YYYY-MM-DD')) = 1 THEN 1 ELSE 0 END) AS q1,
                SUM(CASE WHEN EXTRACT(QUARTER FROM TO_DATE(he.datetime, 'YYYY-MM-DD')) = 2 THEN 1 ELSE 0 END) AS q2,
                SUM(CASE WHEN EXTRACT(QUARTER FROM TO_DATE(he.datetime, 'YYYY-MM-DD')) = 3 THEN 1 ELSE 0 END) AS q3,
                SUM(CASE WHEN EXTRACT(QUARTER FROM TO_DATE(he.datetime, 'YYYY-MM-DD')) = 4 THEN 1 ELSE 0 END) AS q4
            FROM 
                hired_employees he
            JOIN 
                departments d ON he.department_id = d.id
            JOIN 
                jobs j ON he.job_id = j.id
            WHERE 
                SUBSTRING(he.datetime, 1, 4) = '2021'
            GROUP BY 
                department, job
            ORDER BY 
                department, job;""")
            results = conn.execute(query)
            # Write results to CSV file
            csv_file_path = os.path.join(self.output_folder, "hires_per_quarter.csv")
            with open(csv_file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["department", "job", "q1", "q2", "q3", "q4"]) 
                for row in results:
                    writer.writerow(row)
            return f"CSV file has been saved in folder {self.output_folder}"

# Class containing the query for the second requirement
class AboveAvgHires:
    def __init__(self):
        self.engine = connect_to_database()
        self.output_folder = os.path.join(os.path.dirname(__file__), "data")
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def above_avg_department_hires(self):
        with self.engine.connect() as conn:
            query = text("""WITH department_hires AS (
                SELECT 
                    d.id AS department_id,
                    d.department AS department,
                    COUNT(*) AS num_employees_hired
                FROM 
                    hired_employees he
                JOIN 
                    departments d ON he.department_id = d.id
                WHERE 
                    SUBSTRING(he.datetime, 1, 4) = '2021'
                GROUP BY 
                    d.id, department
            ),
            mean_hires AS (
                SELECT 
                    AVG(num_employees_hired) AS mean_hires
                FROM 
                    department_hires
            )
            SELECT 
                d.id,
                d.department,
                dh.num_employees_hired AS hired
            FROM 
                department_hires dh
            JOIN 
                departments d ON dh.department_id = d.id
            CROSS JOIN 
                mean_hires mh
            WHERE 
                dh.num_employees_hired > mh.mean_hires
            ORDER BY 
                hired DESC;""")
            results = conn.execute(query)
            # Write results to CSV file
            csv_file_path = os.path.join(self.output_folder, "above_avg_department_hires.csv")
            with open(csv_file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "department", "hired"])  
                writer.writerows(results)
            return f"CSV file has been saved in folder {self.output_folder}"
