# Logistics Delivery Data Analysis

A data-driven project focused on analyzing delivery operations for a logistics company using a real-world Indian dataset.

---

## Objective

To uncover patterns, inefficiencies, and insights from large-scale trip data — helping logistics teams improve route planning, delivery speed, and operational decisions.

---

## Tools & Libraries

- Python
- Pandas
- Matplotlib 
- VS Code

---

## Dataset Overview

- Total Trips: 144,316  
- Key Columns: `route_type`, `source_center`, `destination_center`, `osrm_time`, `actual_time`, `is_cutoff`, etc.  
- Date Columns: Properly parsed into datetime format

---

## Analysis Performed

### 1. Average Delivery Time by Route Type
- FTL: ~1308 mins (22 hrs)
- Carting: 209 mins (3.5 hrs)
> Full Truck Load (FTL) trips take significantly longer than Carting.

---

### 2. Top & Bottom Performing Source Centers
- Most Active: `IND000000ACB` (23,267 deliveries)
- Least Active: 5 centers had only 1 delivery
> Clear disparity in center activity, indicating potential under-utilization.

---

### 3. OSRM vs. Actual Delivery Time
- Expected (OSRM): 214 mins avg  
- Actual: 418 mins avg  
- Delay: 204 mins avg
> Deliveries are almost double the predicted time on average.

---

### 4. Delivery Deadline Performance
- Missed Cutoff (Late): 82%  
- Met Cutoff (On Time): 18%
> The majority of deliveries fail to meet deadlines.

---

## Business Insights

- OSRM estimations are consistently optimistic — routes need re-evaluation.
- Route types and planning strategies must be adapted for faster fulfillment.
- Source centers can be optimized for better load balancing.
- Cutoff adherence is alarmingly low — operations are due for refinement.

---

## Outcome

This analysis simulates a real-world business scenario and showcases the ability to:
- Handle large datasets
- Extract meaningful patterns
- Communicate actionable insights
- Work with Python and data tools to solve domain-specific problems

---

## Contact

Made with intent by Vibek Singha
For: Data Analyst Role   
