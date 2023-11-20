// Only change code below this line
var a;
var b;
var c;
// Only change code above this line

a = 5;
b = 10;
c = "I am a";

a = a + 1;
b = b + 5;
c = c + " String!";


// Variable declarations
var studlyCapVar;
var properCamelCase;
var titleCaseOver;

// Variable assignments
studlyCapVar = 10;
properCamelCase = "A String";
titleCaseOver = 9000;



//USING SWITCH

function caseInSwitch(val) {
  let answer = "";
  // Only change code below this line
  switch (val) {
    case 1:
    answer = "alpha";
    break;
    case 2: 
    answer = "beta";
    break;
    case 3:
    answer = "gamma";
    break;
    case 4:
    answer = "delta";
    break;
  }



  // Only change code above this line
  return answer;
}

caseInSwitch(1);




// USING SWITCH WITH A DEFAULT VALUE
function switchOfStuff(val) {
  let answer = "";
  // Only change code below this line
  switch (val) {
    case "a":
    answer = "apple";
    break;
    case "b":
    answer = "bird";
    break;
    case "c":
    answer = "cat"
    break;
    default:
    answer = "stuff";
    break;
  }



  // Only change code above this line
  return answer;
}

switchOfStuff(1);

// Multiple Identical Options in Switch Statements
function sequentialSizes(val) {
  let answer = "";
  // Only change code below this line
  switch (val) {
    case 1:
    case 2:
    case 3:
      answer = "Low";
      break;
    case 4:
    case 5:
    case 6:
      answer = "Mid";
      break;
    case 7:
    case 8:
    case 9:
      answer = "High";
      break;
    
  }



  // Only change code above this line
  return answer;
}

sequentialSizes(1);

// Build JavaScript Objects
const myDog = {
  // Only change code below this line
  "name": "Alfie",
  "legs": 4,
  "tails": 1,
  "friends": ["bob", "zoe"]


  // Only change code above this line
};

// Accessing Object Properties with Dot Notation
// Setup
const testObj = {
  "hat": "ballcap",
  "shirt": "jersey",
  "shoes": "cleats"
};

// Only change code below this line
const hatValue = testObj.hat;      // Change this line
const shirtValue = testObj.shirt;    // Change this line

// Accessing Object Properties with Variables
// Setup
const testObj = {
  12: "Namath",
  16: "Montana",
  19: "Unitas"
};

// Only change code below this line
const playerNumber = 16;  // Change this line
const player = testObj[playerNumber];   // Change this line


// Add New Properties to a JavaScript Object
const myDog = {
  "name": "Happy Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"]
};

myDog.bark = "woof";


// Delete Properties from a JavaScript Object
// Setup
const myDog = {
  "name": "Happy Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"],
  "bark": "woof"
};

// Only change code below this line
delete myDog.tails;



// Using Objects for Lookups
// Setup
function phoneticLookup(val) {
  let result = "";

  // Only change code below this line

  const lookup = {
    "alpha": "Adams",
    "bravo": "Boston",
    "charlie": "Chicago",
    "delta": "Denver",
    "echo": "Easy",
    "foxtrot": "Frank"
  }; 
  result = lookup[val];

  // Only change code above this line
  return result;
}

phoneticLookup("charlie");


// Testing Objects for Properties

/*Modify the function checkObj to test if the object passed to the function 
parameter obj contains the specific property passed to the function parameter checkProp. 
If the property passed to checkProp is found on obj, return that property's value. If not, return Not Found.*/

function checkObj(obj, checkProp) {
  // Only change code below this line
  if (obj.hasOwnProperty(checkProp)) {
    // If the property is found, return its value
    return obj[checkProp];
  } else {
    // If the property is not found, return "Not Found"
    return "Not Found";
  }
  // Only change code above this line
}

// Manipulating Complex Objects
/*Add a new album to the myMusic array. Add artist and title strings, 
release_year number, and a formats array of strings.*/
const myMusic = [
  {
    "artist": "Billy Joel",
    "title": "Piano Man",
    "release_year": 1973,
    "formats": [
      "CD",
      "8T",
      "LP"
    ],
    "gold": true
  }
, {
    "artist": "Billy Joel",
    "title": "Piano Man",
    "release_year": 1973,
    "formats": [
      "CD",
      "8T",
      "LP"
    ],
    "gold": true
  }];




// Accessing Nested Objects

/*Access the myStorage object and assign the contents of the glove box property to the gloveBoxContents variable. 
Use dot notation for all properties where possible, otherwise use bracket notation.*/
const myStorage = {
  "car": {
    "inside": {
      "glove box": "maps",
      "passenger seat": "crumbs"
     },
    "outside": {
      "trunk": "jack"
    }
  }
};

const gloveBoxContents = myStorage.car.inside["glove box"];


// Record Collection
// Setup
const recordCollection = {
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
  },
  1245: {
    artist: 'Robert Palmer',
    tracks: []
  },
  5439: {
    albumTitle: 'ABBA Gold'
  }
};

// Only change code below this line
function updateRecords(records, id, prop, value) {
   const updatedRecords = { ...records };

  // If value is an empty string, delete the given prop property from the album
  if (value === "") {
    delete updatedRecords[id][prop];
  } else if (prop !== "tracks") {
    // If prop isn't tracks and value isn't an empty string, assign the value to that album's prop
    updatedRecords[id][prop] = value;
  } else {
    // If prop is tracks and value isn't an empty string
    if (!updatedRecords[id].hasOwnProperty("tracks")) {
      // If the album does not have a tracks property, assign it an empty array
      updatedRecords[id].tracks = [];
    }
    // Add the value as the last item in the album's tracks array
    updatedRecords[id].tracks.push(value);
  }

  // Return the entire updated records object
  return updatedRecords;
}

updateRecords(recordCollection, 5439, 'artist', 'ABBA');


// Add the numbers 5 through 0 (inclusive) in descending order to myArray using a while loop.
// Setup
const myArray = [];

// Only change code below this line
let i = 5;

while (i >= 0) {
  myArray.push(i);
  i--;
}



// Modify function multiplyAll so that it returns the product of all the numbers in the sub-arrays of arr.
function multiplyAll(arr) {
  let product = 1;
  // Only change code below this line
  for (let i = 0; i < arr.length; i++) {
    // Iterate through the sub-array
    for (let j = 0; j < arr[i].length; j++) {
      // Multiply each element with the product
      product *= arr[i][j];
    }
  }

  // Only change code above this line
  return product;
}

multiplyAll([[1, 2], [3, 4], [5, 6, 7]]);
