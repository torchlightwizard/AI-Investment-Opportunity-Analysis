from src.file_handling.read import read_from_file
from src.file_handling.write import write_to_db_schema

path_to_search = "./data/input/search.json"
path_to_db = "./data/datawarehouse/tests/datawarehouse.duckdb"



def transform_fact_table ():
    """Get facts."""

    data = read_from_file(path_to_search)
    data = data.get("company", {})
    
    for item in data:
        write_to_db_schema(path_to_db, "fact", item)