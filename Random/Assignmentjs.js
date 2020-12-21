// Make a function “Person” which you will be using as a class,
// This must have the basic properties:
// 1. First Name
// 2. Last Name
// 3. Email
// 4. Password
// 5. getFullName, a function which returns full name
// 6. Add a prototype getFullName

function Person(fname, lname, email, password){
    this.firstName = fname;
    this.lastName = lname;
    this.email = email;
    this.password = password;
}

Person.prototype.getFullName = function(){
  return `${this.firstName} ${this.lastName}` ;
}

var person = new Person("Akshay", "Sahu", "akx@gmail.com", "Akx12345");

console.log(person.firstName)
console.log(person.lastName)
console.log(person.email)
console.log(person.password)

console.log(person.getFullName())