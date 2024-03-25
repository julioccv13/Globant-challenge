   
# Queries
hires_per_quarter = text("""SELECT 
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


above_avg_department_hires = text("""WITH department_hires AS (
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