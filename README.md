# Weather + Air Quality CLI Dashboard

A Python command-line application that fetches real-time weather and air quality data for any city using the OpenWeatherMap API.

## Features

- Get current temperature in °C
- Get humidity percentage
- Get wind speed in km/h
- View weather condition description
- Check Air Quality Index (AQI)
- Receive AQI-based health advisory
- Save last 5 searched cities in a JSON file
- View search history using the `history` command
- Graceful error handling for invalid cities and network issues

---

## Technologies Used

- Python
- OpenWeatherMap API
- Requests
- Python Dotenv
- JSON Storage

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/codedbydivyansh/weather_dashboard.git
cd weather_dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a .env File

Create a `.env` file using `.env.example`.

```env
OPENWEATHER_API_KEY=your_api_key_here
```

### 4. Get an API Key

1. Sign up at https://openweathermap.org/api
2. Generate a free API key
3. Add the key to your `.env` file

---

## Usage

Run the application:

```bash
python weather.py
```

Enter a city name when prompted:

```text
Enter city name: Mumbai
```

Example Output:

```text
Weather in Mumbai

Temperature : 31°C
Humidity : 78%
Wind Speed : 14 km/h
Condition : Haze

Air Quality Index : 3 (Moderate)

Advisory:
Sensitive individuals should reduce outdoor activity.
```

---

## Search History

To view previously searched cities:

```text
Enter city name: history
```

The application stores the last 5 searches in a JSON file.

---

## Project Structure

```text
weather_dashboard/
│
├── weather.py
├── requirements.txt
├── .env.example
├── .gitignore
├── history.json
└── README.md
```

---

## Error Handling

The application handles:

- Invalid city names
- Missing API key
- Network failures
- API request errors

without crashing.

---

## Future Improvements

- 5-day weather forecast
- Multiple city comparison
- Weather icons
- GUI version using Tkinter
- Weather data visualization

---

## Author

Divyansh

GitHub: https://github.com/codedbydivyansh