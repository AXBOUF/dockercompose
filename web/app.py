from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

# Create table if not exists
with get_db_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visitors (
                id SERIAL PRIMARY KEY,
                email TEXT UNIQUE NOT NULL
            );
        """)
        conn.commit()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO visitors (email) VALUES (%s) ON CONFLICT DO NOTHING;", (email,))
            conn.commit()
            cur.close()
            conn.close()
            # 👇 go straight to the visitors list
            return redirect(url_for("visitors"))
        except Exception as e:
            return f"Error: {e}"
    return render_template("index.html")




@app.route("/visitors")
def visitors():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT email FROM visitors;")
    emails = cur.fetchall()
    cur.close()
    conn.close()

    html = "<h1>Signed-up Emails</h1><ul>"
    for (email,) in emails:
        html += f"<li>{email}</li>"
    html += "</ul><p><a href='/'>Back to home</a></p>"

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
