FastAPI Sales Data Processing API
📌 Overview
This FastAPI application processes sales data from CSV files, transforms it, and stores it in an SQLite database. It also provides API endpoints for querying and analyzing the data.
🚀 Features
Loads and processes sales data from CSV files
Stores transformed data in an SQLite database
Provides API endpoints for data validation and analysis
Includes a separate API to fetch and store jokes from an external API
Supports dynamic database connections to PostgreSQL, Oracle, and SQLite
🛠️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Raviteja5725/Python-Assignment-Maiora.git

After cloning two folders will download 

You can use 1 first one i.e  Python_assignment folder which is not compressed.
cd Python_Assignment/backend

2️⃣ Set Up a Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt
If you encounter version compatibility issues while installing dependencies, try removing specific version numbers from requirements.txt and reinstalling.



4️⃣ Ensure CSV Files Are Present
Place the following CSV files in the project directory:
Location: PYTHON_ASSIGNMENT/src/files/
Sample CSV files:
order_region_a.csv
order_region_b.csv
Sample CSV format:
OrderId,OrderItemId,QuantityOrdered,ItemPrice,PromotionDiscount
101,1,2,500,50
102,2,1,700,100
103,3,3,200,0
104,4,4,150,50
105,5,5,300,200

If needed, you can replace these sample files with new data.
5️⃣ Run the FastAPI Server
Navigate to the backend directory:
cd backend

Run the following command:
uvicorn src.endpoint.meta_data:app --reload

6️⃣ Access API Documentation
Once the server is running, open your browser and visit: http://127.0.0.1:8000/docs (Note: The URL may change depending on your system setup.)
This will open the interactive Swagger UI for API testing.

📌 API Endpoints
🔹 Load and Process Sales Data
POST /load-sales-data/
 Loads CSV data into SQLite.
🔹 Query Data
GET /total-records/ → Retrieve the total record count.
GET /total-sales-by-region/ → Get sales data grouped by region.
GET /average-sales/ → Calculate the average sales per transaction.
GET /check-duplicates/ → Identify duplicate orders.
🔹 Fetch and Store Jokes
GET /fetch-jokes_sqllite_db/ → Fetches jokes and stores them directly in SQLite.
(Use this API when a dynamic database connection is not required.)

GET /fetch-jokes_multiple_db/ → Fetches jokes using a test connection API, supporting multiple databases.
(Use this API when a dynamic database connection is required.)
Before executing this API  run the  POST /test-connection/ 

🔹 Database Connection API
POST /test-connection/ → Establishes a connection to PostgreSQL, Oracle, or SQLite.
(Use this API when a dynamic database connection is required.)


Example Payload for Dynamic Database Connection
{
  "databaseType": "PostgreSQL",
  "host": "192.168.0.112",
  "port": "5432",
  "username": "postgres",
  "psswrd": "postgres",
  "databaseName": "archive_raviteja"
}


🔄 Database Setup
SQLite is used as the default database.
The database file (sales_data.db) will be created automatically.
Users can utilize the /test-connection/ API to connect dynamically to PostgreSQL or Oracle.



