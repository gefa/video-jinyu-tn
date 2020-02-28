# video-jinyu-tn
video-jinyu-tn created by GitHub Classroom

## Project target:
1. Get tweets from twitter by keyboard with twitter API.
2. Convert the tweets into images and convert the images into a video.



## Module description：

### Tweets Grub Module:
-Use twitter API
### Data Management Module
- The function **codetoname(airportname)** in the file `currentweather.py`covert airport name to corresponding city name with the data of file `airports.csv`.
- The **main function** of the file `currentweather.py`use *OpenWeatherMAP API* and city name to get the weather data of the city, data is gotten with **JSON** format，using the python library **requests** .
- The function **print_current_weather(data)** in the file `currentweather.py`filters the weather data we need and print it out.
### Error Check Module:
- File `test_currentwearther.py` checkes the accurence of this API, using **pytest**.


### OpenWeatherMap API:
#### [The URL of the API](https://openweathermap.org/current)
- Access current weather data for any location including over 200,000 cities.
- Current weather is frequently updated based on global models and data from more than 40,000 weather stations.
- Data is available in JSON, XML, or HTML format.

## Project Demo:

### Case 1:
![case1](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/case1.png)
![case1result](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/case1result.png)

### Case 2:
![case2](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/case2.png)
![case2result](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/case2result.png)
### Pytest result:
![pytest](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/pytest.png)
