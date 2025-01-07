from flask import Flask, jsonify
import pyodbc

def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=dist-6-505.uopnet.plymouth.ac.uk;'
            'DATABASE=COMP2001_HWilson;' 
            'UID=HWilson;' 
            'PWD=QfnM764*'
        )
        print("Database connection successful")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

app = Flask(__name__)

@app.route('/')
def home():
    return "Trail Management API is running!"

@app.route('/Trails', methods=['GET'])
def get_trails():
    conn = get_db_connection()
    if conn is None:  # Check if the connection failed
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CW2.Trails")  # Updated table nameç
    rows = cursor.fetchall()
    conn.close()

    # Convert rows to a list of dictionaries
    trails = [{"TrailID": row[0], "TrailName": row[1], "Description": row[2]} for row in rows]
    return jsonify(trails)


if __name__ == '__main__':
    app.run(debug=True)