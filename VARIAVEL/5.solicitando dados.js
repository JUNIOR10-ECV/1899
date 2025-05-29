// Instalar: npm install readline.sync

const radline = require('readline-sync')

const idade = readline.questionInt('Digite sua idade: ')

if (idade < 18) {
    console.log('Menor de idae.')
} else {
    console.log('Maior de idade.')          
}