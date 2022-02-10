import os
json_obj = []
relationship_sheet_missing_fields= ["MISSING","IS"]
metamodel_excel_sheet_names = ["SHEET NAME","Hello","asda"]
#json_obj.append("column names (%s) in %s are missing"%relationship_sheet_missing_fields)
json_obj.append("column names (%s) in %s are missing"% (((',').join(relationship_sheet_missing_fields)),metamodel_excel_sheet_names[2]))
#print(json_obj)

graph_files_path = "graph_files_path"
conversion_rules_dir_path = "conversion_rules_dir_path"
default_config_dir = "default_config_dir"
source = "source"
#print("*** Unable to find the relationship_rules.json in following directories: %s , %s, %s and %s" % (graph_files_path,conversion_rules_dir_path,default_config_dir,os.path.join(default_config_dir, source)))

print('^^^^^^^^^^^^^^^^^^^')
print("*** Unable to find the relationship_rules.json in following directories: %s , %s, %s and %s" % (graph_files_path,conversion_rules_dir_path,default_config_dir,os.path.join(default_config_dir, source)))
print('^^^^^^^^^^^^^^^^^^^')
print(("*** Unable to find the node_rules.json in following directories: %s , %s, %s and %s" % (graph_files_path,conversion_rules_dir_path,default_config_dir,os.path.join(default_config_dir, source))))