package cars

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	return float64(productionRate) * (successRate / 100)
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	return int(CalculateWorkingCarsPerHour(productionRate, successRate)) / int(60)
}

// CalculateCost works out the cost of producing the given number of cars.
// One car is $10,000 but 10 cars is $95,000 saving $5,000
func CalculateCost(carsCount int) uint {
	return ((uint(carsCount) / uint(10)) * uint((95_000))) + ((uint(carsCount) % uint(10)) * uint(10_000))
}
