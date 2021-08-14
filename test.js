
const persons = [
    {
        id: 0,
        firstName: "Juerg",
        lastName: "Paulison",
        details: { age: 5 }
    },
    {
        id: 1,
        firstName: "Peter",
        lastName: "Mueller",
        details: { age: 5 }
    },
    {
        id: 2,
        firstName: "Manfred",
        lastName: "Schneider",
        details: { age: 17 }
    },
    {
        id: 3,
        firstName: "Hans",
        lastName: "Mettmann",
        details: { age: 3 }
    },
    {
        id: 4,
        firstName: "Dieter",
        lastName: "Schmitt"
    },
    {
        id: 5,
        firstName: "Klaudia",
        lastName: "Meier",
        details: { age: 23 }
    }
]



var result = $.grep(persons, function(e){ return e.id == id; });


console.log(result)