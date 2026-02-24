// Package weather forecasts the current weather condition of various cities in Goblinocus.
package weather

var (
	// CurrentCondition contains the current weather condition.
	CurrentCondition string
	// CurrentLocation contains the current city.
	CurrentLocation string
)

// Forecast provides a formatted string containing the current city and weather conditions.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
