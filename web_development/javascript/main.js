function lifeInWeeks (age) {
    var yearsRemaining = 90 - age;
    var days = yearsRemaining * 365;
    var weeks = yearsRemaining * 52;
    var months = yearsRemaining * 12;

    console.log ("You have " + days + "days " + weeks + "weeks, and " + months + "months left.");
}

function bmiCalculator(weight, height) {
    var bmi = weight / (height * height);
    return Math.round(bmi);
}

var bmi = bmiCalculator(65, 1.8);
