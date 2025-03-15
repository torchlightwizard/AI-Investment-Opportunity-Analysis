from datetime import datetime
import os
import json
import duckdb

def write_to_file (output_folder_path, file_name, data):
    """
        Dumps formatted response data to a JSON file.

        Returns:
            Bool: True for Success
    """

    try:
        if data is None:
            raise ValueError("Data to write to file is 'None'.")
        if not os.path.exists(output_folder_path):
            raise FileNotFoundError("Failed to find system path.")
        
        os.makedirs(output_folder_path, exist_ok=True)
        time_stamp = datetime.now().strftime(('%Y_%m_%dT%H_%M_%S'))
        output_file_path = os.path.join(output_folder_path, f"{file_name}_{time_stamp}.json")
        with open(output_file_path, "w") as file:
            json.dump(data, file, indent=4)
        return file.closed

    except ValueError as err:
        print(f"Function: write_to_file. Value Error: {err}")
        print(f"Data Object: {data}")
    except FileNotFoundError as err:
        print(f"Function: write_to_db_json. File Not Found Error: {err}")
        print(f"Path: {os.path.exists(output_folder_path)}")
    except Exception as err:
        print(f"Function: write_to_file. Unexpected Error: {err}")
    return None
    


def write_to_db_json (path_to_db, table, data):
    """
        Dumps formatted response data to a table in duck db.

        Returns:
            Bool: True for Success
    """

    try:
        con = None
        if os.path.exists(path_to_db):
            con = duckdb.connect(path_to_db)
        else:
            raise FileNotFoundError("Failed to find system path.")
        if not con:
            raise RuntimeError("Failed to connect to duckdb.")
        
        con.execute(f"create table if not exists {table} (data JSON)")
        con.execute(f"insert into {table} values(?)", [json.dumps(data)])
        con.close()
        return True
    
    except RuntimeError as err:
        print(f"Function: write_to_db_json. Runtime Error: {err}")
        print(f"Connection Object: {con}")
    except FileNotFoundError as err:
        print(f"Function: write_to_db_json. File Not Found Error: {err}")
        print(f"Path: {os.path.exists(path_to_db)}")
    except Exception as err:
        print(f"Function: write_to_db_json. Unexpected Error: {err}")
    return None



def write_to_db_schema (path_to_db, table, data):
    """
        Dumps formatted response data to a table in duck db.

        Returns:
            Bool: True for Success
    """

    try:
        con = None
        if os.path.exists(path_to_db):
            con = duckdb.connect(path_to_db)
        else:
            raise FileNotFoundError("Failed to find system path.")
        if not con:
            raise RuntimeError("Failed to connect to duckdb.")
        
        columns = ', '.join(f'"{key}"' for key in data.keys())
        columns_with_type = ', '.join(f'"{k}" TEXT' for k in data.keys())
        placeholders = ', '.join('?' for _ in data)
        values = tuple(data.values())

        create_stmt = f'CREATE TABLE IF NOT EXISTS {table} ({columns_with_type})'
        con.execute(create_stmt)
        insert_stmt = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        con.execute(insert_stmt, values)

        con.close()
        return True
    
    except RuntimeError as err:
        print(f"Function: write_to_db_json. Runtime Error: {err}")
        print(f"Connection Object: {con}")
    except FileNotFoundError as err:
        print(f"Function: write_to_db_json. File Not Found Error: {err}")
        print(f"Path: {os.path.exists(path_to_db)}")
    except Exception as err:
        print(f"Function: write_to_db_json. Unexpected Error: {err}")
    return None



def write_to_db_df (path_to_db, table, df):
    """
        Dumps formatted response data to a table in duck db.

        Returns:
            Bool: True for Success
    """

    try:
        con = None
        if os.path.exists(path_to_db):
            con = duckdb.connect(path_to_db)
        else:
            raise FileNotFoundError("Failed to find system path.")
        if not con:
            raise RuntimeError("Failed to connect to duckdb.")
        
        con.register('temp_df', df)
        con.execute(f'CREATE TABLE IF NOT EXISTS {table} AS SELECT * FROM temp_df')
        con.execute(f'INSERT INTO {table} SELECT * FROM temp_df')

        con.close()
        return True
    
    except RuntimeError as err:
        print(f"Function: write_to_db_json. Runtime Error: {err}")
        print(f"Connection Object: {con}")
    except FileNotFoundError as err:
        print(f"Function: write_to_db_json. File Not Found Error: {err}")
        print(f"Path: {os.path.exists(path_to_db)}")
    except Exception as err:
        print(f"Function: write_to_db_json. Unexpected Error: {err}")
    return None