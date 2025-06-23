# Weatherly

Weatherly is a modern, user-friendly weather application built with FastAPI that allows users to check weather conditions for multiple cities with a beautiful and intuitive interface.

## Features

### Weather Information
- Real-time weather data for any city
- Multiple city tracking
- Detailed weather information including:
  - Temperature in Fahrenheit
  - Weather conditions and descriptions
  - Humidity levels
  - Wind speed
  - Weather icons

### User Interface
- Clean and modern design using Tailwind CSS
- Responsive layout for all devices
- Dark/Light theme toggle
- Beautiful gradient backgrounds
- Card-based weather display
- Interactive hover effects

### User Experience
- Simple city search functionality
- Easy city removal
- Visual weather indicators
- Intuitive navigation
- Real-time weather updates

## Technical Stack

- **Backend Framework**: FastAPI
- **Frontend**: 
  - Tailwind CSS
  - DaisyUI Components
- **Weather API**: OpenWeatherMap
- **Styling**: Custom CSS with Tailwind
- **Icons**: Custom weather icons

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file
   - Add the following variables:
     ```
     OPENWEATHER_API_KEY=your_api_key
     SECRET_KEY=your_secret_key
     ```
5. Run the application:
   ```bash
   uvicorn app:app
  
   ```

## Usage

1. Visit the homepage
2. Enter a city name in the search box
3. View detailed weather information:
   - Current temperature
   - Weather conditions
   - Humidity percentage
   - Wind speed
4. Toggle between dark and light themes using the theme button
5. Remove cities you no longer want to track

## Features in Detail

### Weather Display
- Each city is displayed in a beautiful card layout
- Weather information is clearly organized
- Visual weather icons from OpenWeatherMap
- Temperature displayed prominently
- Additional weather details in an easy-to-read format

### Theme Support
- Seamless dark/light theme switching
- Persistent theme preference
- Smooth transitions between themes
- Optimized contrast for readability

### Responsive Design
- Mobile-friendly interface
- Adaptive layout for different screen sizes
- Optimized card grid system
- Touch-friendly controls

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Weather data provided by OpenWeatherMap
- Icons and design elements from DaisyUI
- Built with FastAPI and Tailwind CSS 
