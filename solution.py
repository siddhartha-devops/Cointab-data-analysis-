from asyncore import read
import math
from turtle import clear
import csv

## creating function for round off to nearest upper half:
def round_up_to_nearest_half_int(num):
    return math.ceil(num * 2) / 2   

## creating rates analysis dictionary
rates_record = open("input_dataset\\rates.csv")
rates_line = rates_record.readlines()
j = 0
for i in rates_line:
    if j ==0:
        j=j+1
        continue
    row = i.split(",")
    rate = {
        "fwd_a_fixed" : float(row[0]),
        "fwd_a_additional" : float(row[1]),

        "fwd_b_fixed" : float(row[2]),
        "fwd_b_additional" : float(row[3]),

        "fwd_c_fixed" : float(row[4]),
        "fwd_c_additional" : float(row[5]),

        "fwd_d_fixed" : float(row[6]),
        "fwd_d_additional" : float(row[7]),

        "fwd_e_fixed" : float(row[8]),
        "fwd_e_additional" : float(row[9]),

## for rto fixed and addtional charges

        "rto_a_fixed":float(row[10]),
        "rto_a_additional":float(row[11]),

        "rto_b_fixed":float(row[12]),
        "rto_b_additional":float(row[13]),

        "rto_c_fixed":float(row[14]),
        "rto_c_additional":float(row[15]),

        "rto_d_fixed":float(row[16]),
        "rto_d_additional":float(row[17]),

        "rto_e_fixed":float(row[18]),
        "rto_e_additional":float(row[19])

         }
# creating  acutal rates analysis function   

# where x = shipment_type, y = zone_by_x, z = slab_weight_as_per_x_kg

def acutal_bill(x,y,z):
    
    if x =="Forward charges":
        if y =="a":
            if z == 0.5:
                result_bill = rate["fwd_a_fixed"]
            else:      
                result_bill = rate["fwd_a_fixed"] + ( (data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_a_additional"]

        if y =="b":
            if z == 0.5:
                result_bill = rate["fwd_b_fixed"] 
            else:      
                result_bill = rate["fwd_b_fixed"] + ( (data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_b_additional"]


        if y =="c":
            if z == 0.5:
                result_bill = rate["fwd_c_fixed"] 
            else:      
                result_bill = rate["fwd_c_fixed"] + ( (data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_c_additional"]

            
        if y =="d":
            if z == 0.5:
                result_bill = rate["fwd_d_fixed"] 
            else:      
                result_bill = rate["fwd_d_fixed"] + ( (data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_d_additional"]

        if y =="e":
            if z == 0.5:
                result_bill = rate["fwd_e_fixed"] 
            else:      
                result_bill = rate["fwd_e_fixed"] + ( (data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_e_additional"]
                    
    if x == "Forward and RTO charges":
        if y =="a":
            if z == 0.5:
                result_bill = rate["fwd_a_fixed"] + rate["rto_a_fixed"]
            else:    
                result_bill = rate["fwd_a_fixed"] + rate["rto_a_fixed"] +((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_a_additional"] +  ((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["rto_a_additional"]

        if y =="b":
            if z == 0.5:
                result_bill = rate["fwd_b_fixed"] + rate["rto_b_fixed"]
            else:    
                result_bill = rate["fwd_b_fixed"] + rate["rto_b_fixed"] +((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_b_additional"] +  ((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["rto_b_additional"]                 
        
        if y =="c":
            if z == 0.5:
                result_bill = rate["fwd_c_fixed"]+rate["rto_c_fixed"]
            else:    
                result_bill = rate["fwd_c_fixed"] + rate["rto_c_fixed"] +((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_c_additional"] +  ((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["rto_c_additional"]
        
        if y =="d":
            if z == 0.5:
                result_bill = rate["fwd_d_fixed"]+rate["rto_d_fixed"]
            else:    
                result_bill = rate["fwd_d_fixed"] + rate["rto_d_fixed"] + ((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_d_additional"] +  ((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["rto_d_additional"]

        if y=="e":
            if z == 0.5:
                result_bill = rate["fwd_e_fixed"]+rate["rto_e_fixed"]
            else:    
                result_bill = rate["fwd_e_fixed"] +rate["rto_e_fixed"]+  ((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["fwd_e_additional"] +  ((data[key]["Weight_slab_as_per_X_KG"] - 0.5) /0.5)*rate["rto_e_additional"]
    final_bill = round(result_bill,2)
    return final_bill   
    

# creating sku master record
sku_master_data = {}
sku_master = open("input_dataset\\sku_master.csv")
sku_line = sku_master.readlines()
j =0
for i in sku_line:
    if j ==0:
        j =j+1
        continue
    row = i.split(",")
    sku_master_data[row[0]]=row[1].strip()

data = {}

## importing invoice dataset
invoice = open("input_dataset\\Courier_Invoice.csv")
invoice_line = invoice.readlines()
j=0
for i in invoice_line:
    if j ==0:
        j = j+1
        continue
    row = i.split(",")
    data[row[1]] = {
        "AWB_code": row[0],
        "order_ID": row[1],
        "Total_weight_as_per_Courier_Company_KG": row[2],
        "warehouse_pincode": row[3],
        "customer_pincode": row[4],
        "Delivery_Zone_charged_by_Courier_Company": row[5],
        "shipment_type": row[6],
        "Charges_Billed_by_Courier_Company_Rs": row[7].strip()
    }
# importing order_report.csv
order_record = open("input_dataset\\order_report.csv")
order_line = order_record.readlines()

for key, value in data.items():
    for i in order_line:
        row = i.split(",")
        if value["order_ID"]== row[0]:
            if "Total_weight_as_per_X_KG" in data[key]:
                data[key]["Total_weight_as_per_X_KG"] = data[key]["Total_weight_as_per_X_KG"] + float(row[2])*float(sku_master_data[row[1]])/1000
            else:
                data[key]["Total_weight_as_per_X_KG"] = float(row[2])*float(sku_master_data[row[1]])/1000
    

pincode_zone = open("input_dataset\\pincode_zone.csv")
pincode_line = pincode_zone.readlines()

for key, value in data.items():
    j= 0
    for i in pincode_line:
        if j ==0:
            j=j+1
            continue
        row = i.split(",")
        if value["customer_pincode"] in row[1]:
            data[key]["Delivery_Zone_as_per_X"] = row[2].strip()

for key, value in data.items():
   
    data[key]["Weight_slab_as_per_X_KG"] =round_up_to_nearest_half_int((data[key]['Total_weight_as_per_X_KG']))
    data[key]["Weight_slab_charged_by_Courier_Company_KG"] = round_up_to_nearest_half_int(float(data[key]["Total_weight_as_per_Courier_Company_KG"]))    
    data[key]["Expected_Charge_as_per_X_Rs"]=acutal_bill(data[key]["shipment_type"], data[key]["Delivery_Zone_as_per_X"], data[key]["Weight_slab_as_per_X_KG"])
    data[key]["Difference_Between_Expected_Charges_and_Billed_Charges_Rs"]= (data[key]["Expected_Charge_as_per_X_Rs"]) -(float(data[key]["Charges_Billed_by_Courier_Company_Rs"]))
        
# Removing fields which are not required in resultant dataset
for key,value in data.items():
    del data[key]["warehouse_pincode"]
    del data[key]["customer_pincode"]
    del data[key]["shipment_type"]

# print(data)
# exit()
# writing the file in final.csv
csv_columns = [
    'AWB_code', 
    'order_ID', 
    'Total_weight_as_per_Courier_Company_KG', 
    'Delivery_Zone_charged_by_Courier_Company', 
    'Charges_Billed_by_Courier_Company_Rs', 
    'Total_weight_as_per_X_KG', 
    'Delivery_Zone_as_per_X', 
    'Weight_slab_as_per_X_KG', 
    'Weight_slab_charged_by_Courier_Company_KG', 
    'Expected_Charge_as_per_X_Rs', 
    'Difference_Between_Expected_Charges_and_Billed_Charges_Rs'
    ]

csv_file = "output_dataset\\final_output.csv"
try:
    with open(csv_file, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        values_dict = list(data.values())
        writer.writerows(values_dict)

except IOError:
    print("I/O error")
