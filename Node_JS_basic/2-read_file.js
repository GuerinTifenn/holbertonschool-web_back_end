const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8').trim();
        const lines = data.split('\n').filter(line => line);
        const students = lines.slice(1);
        const fields = {};

        students.forEach((student) => {
            const [firstname, lastname, age, field] = student.split(',');
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstname);
        });

        console.log(`Number of students: ${students.length}`);
        for (const field in fields) {
            console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
