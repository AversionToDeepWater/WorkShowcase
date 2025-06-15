#SQL-connector

import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE


class DbConnectionError(Exception):
    pass


def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx


# List of Kdramas in watchlist
def get_all_kdramas_db():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT title, main_male_lead, main_female_lead FROM kdrama_list"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

#new kdrama to watch list
def add_new_kdrama_db(new_kdrama_dict):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)


        print("ADD A NEW KDRAMA TO DB:", new_kdrama_dict)

        query = f"""
         INSERT INTO kdrama_list (title, main_male_lead, main_female_lead, watched)
         VALUES ('{new_kdrama_dict['title']}', {new_kdrama_dict['main_male_lead']}, {new_kdrama_dict['main_female_lead']}, {new_kdrama_dict['watched']})
         """

        # Execute the query
        cur.execute(query)

        # Commit the transaction to make the changes in the database
        db_connection.commit()

        print("Kdrama added successfully!")

        query = """SELECT * FROM kdrama_list"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

#new Kdrama rating out of 10
def add_new_rating_db(new_rating_dict, kdrama_id):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)


        print("ADD A RATING TO EXISTING KDRAMA IN DB:", new_rating_dict)

        vals = ",".join(f"{key} = %s" for key in new_rating_dict.keys()) #getting the info from my dictionary and adding it to table
        #this iterates through the dictionary and give a key val tuple? Which then updates the table
        query = f"""
         UPDATE kdrama_list SET {vals} WHERE kdrama_id = %s 
         """
        #what will be subbed into dictionary
        values = list(new_rating_dict.values()) + [kdrama_id]

        # Execute the query as well as values
        cur.execute(query, values)

        # Commit the transaction to make the changes in the database
        db_connection.commit()

        print("Rating/10 added successfully!")

        query = """SELECT * FROM kdrama_list"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

#delete kdrama from watchlist
def delete_kdrama_by_id(id):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        del_query = """DELETE FROM kdrama_list WHERE kdrama_id = {}""".format(id)
        cur.execute(del_query)

        db_connection.commit()  # IMPORTANT!!! Commit the transaction to apply the deletion

        # you can leave little messages for yourself and debugging like this
        print(f"Record with kdrama_id {id} deleted successfully.")

        # NOTE - I've added this so I can return the remaining students back to my API
        # I don't need to do this but this is something that I've decided my app does
        select_query = "SELECT * FROM kdrama_list"
        cur.execute(select_query)
        remaining_records = cur.fetchall()  # Get all remaining records
        cur.close()

        return remaining_records


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# if __name__ == "__main__":
#     # delete_kdrama_by_id(5)
#     #print(get_all_kdramas_db()) print to test it works
#     get_all_kdramas_db()

