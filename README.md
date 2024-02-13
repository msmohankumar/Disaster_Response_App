# Disaster_Response_App

<!-- master.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}"> -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    <title>Disaster Response App</title>
</head>
<body>
    <header>
        <h1>Disaster Response App</h1>
    </header>
    <main>
        <p>Welcome to the Disaster Response App!</p>
        <p>Enter your message below:</p>
        <form action="{{ url_for('result') }}" method="post">
            <input type="text" name="message" placeholder="Enter your message" required>
            <button type="submit">Submit</button>
        </form>
    </main>
    <footer>
        <p>&copy; 2024 Disaster Response App</p>
    </footer>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
