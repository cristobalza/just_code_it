# Write your MySQL query statement below
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions REGEXP '(^DIAB1|(.*\\sDIAB1))';