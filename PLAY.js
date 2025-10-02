//let a = 10;
//let b = 5;
//let c = a/b;
//console.log(c)

try {
    let a = 10;
    let b = "Isaac";

    if (b === 0) throw new Error("You cannot divide by zero");
    if (typeof b === "string") throw new Error("Entry is not a number");

    let c = a / b;
    console.log(c);
} 
catch (error) {
    console.log(error.message);
} 
finally {
    console.log("Attend to divide operation");
}

//method 1: object literal
const student1 = {
    fullname: "Isaac Newton",
    yob: 1643,
    gender: "male",
    accessnumber: "A12345",
    course: "bsit", 
};

const student2 = {
    fullname: "Jenkins Kasibantte",
    yob: 2006,
    gender: "male",
    accessnumber: "A12347",
    course: "bsit",
};

console.log(student1.fullname,student2.fullname);
//method 2: object constructor
class Student {
    constructor(fullname, yob, accessnumber, course, gender) 
    {
        this.fullname = fullname,
        this.yob = yob,
        this.accessnumber = accessnumber,
        this.course = course,
        this.gender = gender;
    }
}
const Student1 = new Student("Isaac Newton", 1643, "A12345", "bsit", "male");
const Student2 = new Student("Jenkins Kasibantte", 2006, "A12347", "bsit", "male");

console.log(Student1);
console.log(Student2);
console.log(student1)
//creating a function that generates student age
studentage = function()
{
    //AGE = CURRENT YEAR - YEAR OF BIRTH
    let currentyear = new Date().getFullYear();
    let age = currentyear - this.yob;
    return age;
    
}
console.log(`This student is ${studentage.call(student1)} years old`);
console.log(`This student is ${studentage.call(student2)} years old`);
