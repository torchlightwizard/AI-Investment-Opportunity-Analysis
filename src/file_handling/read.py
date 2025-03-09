import os
import json
import duckdb

def read_from_file(file_path):
    """
        Reads JSON data from a file and returns it as a dictionary.

        Returns:
            dict: Parsed JSON data.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    except FileNotFoundError as err:
        print(f"Function: read_from_file. File Not Found Error: {err}")
    except json.JSONDecodeError as err:
        print(f"Function: read_from_file. JSON Decode Error: {err}")
    except Exception as err:
        print(f"Function: read_from_file. Unexpected Error: {err}")
    return None



def read_from_db_json (path_to_db, table):
    """
        Reads JSON data from a db and returns it as a dictionary.

        Returns:
            dict: Parsed JSON data.
    """

    try:
        con = None
        if os.path.exists(path_to_db):
            con = duckdb.connect(path_to_db)
        else:
            raise FileNotFoundError("Failed to find system path.")
        if not con:
            raise RuntimeError("Failed to connect to duckdb.")
        
        data = con.execute(f"select * from {table};").fetchall()
        return data
    
    except RuntimeError as err:
        print(f"Function: read_from_db_json. Runtime Error: {err}")
        print(f"Connection Object: {con}")
    except FileNotFoundError as err:
        print(f"Function: read_from_db_json. File Not Found Error: {err}")
        print(f"Path: {os.path.exists(path_to_db)}")
    except Exception as err:
        print(f"Function: read_from_db_json. Unexpected Error: {err}")
    return None



def read_from_db_df (path_to_db, table):
    """
        Reads JSON data from a db and returns it as a dictionary.

        Returns:
            dict: Parsed JSON data.
    """

    try:
        con = None
        if os.path.exists(path_to_db):
            con = duckdb.connect(path_to_db)
        else:
            raise FileNotFoundError("Failed to find system path.")
        if not con:
            raise RuntimeError("Failed to connect to duckdb.")
        
        data = con.execute(f"select * from {table};").fetchdf()
        return data
    
    except RuntimeError as err:
        print(f"Function: read_from_db_df. Runtime Error: {err}")
        print(f"Connection Object: {con}")
    except FileNotFoundError as err:
        print(f"Function: read_from_db_df. File Not Found Error: {err}")
        print(f"Path: {os.path.exists(path_to_db)}")
    except Exception as err:
        print(f"Function: read_from_db_df. Unexpected Error: {err}")
    return None