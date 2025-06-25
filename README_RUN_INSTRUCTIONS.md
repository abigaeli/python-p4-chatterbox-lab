# Running the Chatterbox Application

This project consists of two parts:

- React frontend located in the `client` directory.
- Flask backend located in the `server` directory.

## Running the React Frontend

1. Navigate to the `client` directory:

```bash
cd client
```

2. Install dependencies:

```bash
npm install
```

3. Start the demo API server (json-server):

```bash
npm run server
```

4. In a new terminal, start the React app:

```bash
npm start
```

5. Open your browser and visit [http://localhost:3000](http://localhost:3000) to interact with the app.

## Running the Flask Backend

1. Navigate to the `server` directory:

```bash
cd server
```

2. Install dependencies and activate the virtual environment:

```bash
pipenv install
pipenv shell
```

3. Initialize the database and run migrations:

```bash
flask db init
flask db revision --autogenerate -m "Create messages table"
flask db upgrade
```

4. Seed the database with initial data:

```bash
python seed.py
```

5. Run the Flask server:

```bash
flask run
```

The Flask API will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Notes

- Ensure that port 5000 is free before running the Flask server.
- The React frontend expects the backend API to be running on port 5000.
- If you encounter CORS issues, verify that Flask-CORS is properly configured in `server/app.py`.

## Testing

To run backend tests, navigate to the `server` directory and run:

```bash
pytest -x
```

This will run the tests until the first failure.

---

This completes the setup and running instructions for the Chatterbox application.
